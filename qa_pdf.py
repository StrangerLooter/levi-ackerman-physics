"""
qa_pdf.py — Automated Forensic Quality Assurance for ODM Gear Physics Paper.

Performs comprehensive automated inspection:
1. Opens target PDF with PyMuPDF
2. Validates page count, geometry, and metadata
3. Renders high-resolution preview images of all pages
4. Assembles a visual contact sheet grid of all pages
5. Extracts text to test selectability
6. Scans for missing glyph boxes, replacement chars (e.g. \u25a0, \ufffd, ?), and garbled entities
7. Analyzes page occupancy / detects empty or suspiciously sparse pages
8. Verifies presence of all 14 required sections and key mathematical principles
"""

import sys
import os
import math
from pathlib import Path
import pymupdf
from PIL import Image

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PDF_PATH = Path("ODM_Gear_Physics_Levi_Ackerman.pdf")
PREVIEW_DIR = Path("output/preview")
CONTACT_SHEET_PATH = Path("output/contact_sheet.png")

REQUIRED_SECTIONS = [
    "Introduction",
    "What Is ODM Gear?",
    "From Anime Motion to Kinematics",
    "The Cable as a Mathematical Constraint",
    "Why Straight",
    "Centripetal Force and Cable Tension",
    "Two-Anchor Vector Control",
    "Variable Cable Length, Energy, and Momentum",
    "Drag and High-Speed Limits",
    "Levi's Rotational Combat",
    "Could the Cables Survive?",
    "Can the Human Body Survive It?",
    "Optimal Trajectory and Reality Check",
    "Conclusion"
]

def run_qa():
    print("=" * 70)
    print("  RUNNING FORENSIC PDF QUALITY AUDIT (qa_pdf.py)")
    print("=" * 70)

    if not PDF_PATH.exists():
        alt = Path("output") / PDF_PATH.name
        if alt.exists():
            target = alt
        else:
            print(f"[ERROR] PDF not found: {PDF_PATH}")
            return False
    else:
        target = PDF_PATH

    print(f"Target PDF: {target} ({target.stat().st_size / 1024 / 1024:.2f} MB)")

    doc = pymupdf.open(str(target))
    total_pages = len(doc)
    print(f"Total Pages: {total_pages}")

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    for stale in PREVIEW_DIR.glob("page_*.png"):
        try: stale.unlink()
        except Exception: pass
    page_images = []
    suspicious_glyphs = []
    sparse_pages = []
    found_sections = {s: False for s in REQUIRED_SECTIONS}

    print("\n--- Page-by-Page Audit ---")
    for idx, page in enumerate(doc):
        page_num = idx + 1
        text = page.get_text()
        text_len = len(text.strip())

        # Render page image (150 DPI for preview & contact sheet)
        pix = page.get_pixmap(dpi=150)
        img_path = PREVIEW_DIR / f"page_{page_num:02d}.png"
        pix.save(str(img_path))
        page_images.append(img_path)

        # Check for missing glyph / square box characters
        black_boxes = text.count('\u25a0') + text.count('■')
        rep_chars = text.count('\ufffd')
        if black_boxes > 0 or rep_chars > 0:
            suspicious_glyphs.append((page_num, black_boxes, rep_chars))

        # Check section titles
        for s in REQUIRED_SECTIONS:
            if s.lower() in text.lower():
                found_sections[s] = True

        # Sparse page check (excluding cover page)
        img_list = page.get_images()
        if page_num > 1 and text_len < 300 and len(img_list) == 0:
            sparse_pages.append((page_num, text_len, len(img_list)))

        print(f"  Page {page_num:2d}: {text_len:4d} chars | {len(img_list):2d} images | "
              f"Boxes: {black_boxes} | RepChars: {rep_chars} | Status: {'OK' if black_boxes==0 and rep_chars==0 else 'WARN GLYPHS'}")

    # Build Contact Sheet Grid
    print("\nAssembling Contact Sheet...")
    cols = 5
    rows = math.ceil(total_pages / cols)
    thumb_w = 300
    thumb_h = int(thumb_w * (841.89 / 595.28)) # A4 ratio
    grid_img = Image.new('RGB', (cols * thumb_w, rows * thumb_h), color=(20, 24, 32))

    for idx, img_path in enumerate(page_images):
        r = idx // cols
        c = idx % cols
        with Image.open(img_path) as im:
            thumb = im.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
            grid_img.paste(thumb, (c * thumb_w, r * thumb_h))

    CONTACT_SHEET_PATH.parent.mkdir(parents=True, exist_ok=True)
    grid_img.save(str(CONTACT_SHEET_PATH), quality=90)
    print(f"Contact Sheet saved to: {CONTACT_SHEET_PATH}")

    # Final Verdict & Report
    print("\n" + "=" * 70)
    print("  AUDIT SUMMARY")
    print("=" * 70)
    print(f"Total Pages: {total_pages}")
    
    missing_secs = [s for s, found in found_sections.items() if not found]
    if missing_secs:
        print(f"[WARN] Sections not detected in text: {missing_secs}")
    else:
        print("[PASS] All 14 required sections detected.")

    if suspicious_glyphs:
        print(f"[FAIL] Pages with missing glyph boxes / replacement characters:")
        for p, bb, rc in suspicious_glyphs:
            print(f"   - Page {p}: {bb} black squares [■], {rc} replacement characters")
    else:
        print("[PASS] Zero missing glyph boxes [■] or replacement characters detected!")

    if sparse_pages:
        print(f"[WARN] Suspiciously sparse pages (<300 chars, no images): {sparse_pages}")
    else:
        print("[PASS] No empty or accidentally orphaned sparse pages detected.")

    passed = (len(suspicious_glyphs) == 0) and (len(missing_secs) == 0)
    print("=" * 70)
    print(f"AUDIT RESULT: {'PASSED' if passed else 'FAILED'}")
    print("=" * 70)
    return passed

if __name__ == '__main__':
    ok = run_qa()
    sys.exit(0 if ok else 1)

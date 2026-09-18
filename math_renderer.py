"""
math_renderer.py — High-Fidelity Scientific Equation Renderer for ReportLab
Using Matplotlib's LaTeX-compatible MathText Engine with STIX Fonts.

This module converts LaTeX math strings into high-resolution (600 DPI) vector-sharp
images with transparent backgrounds and wraps them into ReportLab Flowables.
"""

import os
import io
import hashlib
from pathlib import Path
from PIL import Image as PILImage
import matplotlib as mpl
import matplotlib.mathtext as mathtext
from reportlab.platypus.flowables import Flowable

# Configure Matplotlib MathText for publication-quality STIX fontset
mpl.rcParams['mathtext.fontset'] = 'stix'
mpl.rcParams['mathtext.default'] = 'regular'

# Cache directory for rendered equation images
CACHE_DIR = Path(__file__).resolve().parent / "rendered_equations"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

import re

def sanitize_latex(s: str) -> str:
    """Normalize LaTeX math string for Matplotlib MathText parser."""
    text = s.strip()
    # Strip enclosing $ if provided
    if text.startswith('$$') and text.endswith('$$'):
        text = text[2:-2].strip()
    elif text.startswith('$') and text.endswith('$'):
        text = text[1:-1].strip()
    
    # Strip \displaystyle if present
    if text.startswith(r'\displaystyle'):
        text = text[len(r'\displaystyle'):].strip()

    # Exact token replacements with word boundaries
    text = re.sub(r'\\implies\b', r'\\Longrightarrow', text)
    text = re.sub(r'\\impliedby\b', r'\\Longleftarrow', text)
    text = re.sub(r'\\iff\b', r'\\Longleftrightarrow', text)
    text = re.sub(r'\\to\b', r'\\rightarrow', text)
    text = re.sub(r'\\le\b', r'\\leq', text)
    text = re.sub(r'\\ge\b', r'\\geq', text)
    text = re.sub(r'\\bm\{', r'\\mathbf{', text)
    text = re.sub(r'\\boldsymbol\{', r'\\mathbf{', text)

    return text


class EquationFlowable(Flowable):
    """
    A ReportLab Flowable that renders LaTeX mathematics using Matplotlib's
    MathText engine at 600 DPI, centered with proper vertical padding.
    """
    def __init__(self, latex_str: str, fontsize: float = 12.0, color: str = '#111111',
                 space_before: float = 6.0, space_after: float = 6.0, scale: float = 1.05):
        super().__init__()
        self.raw_latex = latex_str
        self.latex_str = sanitize_latex(latex_str)
        self.fontsize = fontsize
        self.color = color
        self.space_before = space_before
        self.space_after = space_after
        self.scale = scale

        # Cache key based on content, font properties, and scale
        h = hashlib.sha256(f"{self.latex_str}_{fontsize}_{color}_{scale}".encode('utf-8')).hexdigest()[:16]
        self.img_path = CACHE_DIR / f"eq_{h}.png"

        self._render_if_needed()

        # Read dimensions
        with PILImage.open(self.img_path) as im:
            px_w, px_h = im.size

        # Convert to points (72 points = 1 inch, 600 DPI)
        self.img_w = (px_w / 600.0) * 72.0 * self.scale
        self.img_h = (px_h / 600.0) * 72.0 * self.scale

    def _render_if_needed(self):
        if not self.img_path.exists():
            math_expr = f"${self.latex_str}$"
            prop = mpl.font_manager.FontProperties(size=self.fontsize)
            try:
                mathtext.math_to_image(
                    math_expr,
                    str(self.img_path),
                    dpi=600,
                    format='png',
                    prop=prop,
                    color=self.color
                )
            except Exception as e:
                # Fallback: if formula failed, log and render fallback error text
                print(f"[math_renderer ERROR] Failed to parse: {self.latex_str!r} -> {e}")
                # Create a simple fallback image
                prop_plain = mpl.font_manager.FontProperties(size=10)
                mathtext.math_to_image(
                    r"$\text{[Equation Parse Error]}$",
                    str(self.img_path),
                    dpi=600,
                    format='png',
                    prop=prop_plain,
                    color='#CC0000'
                )

    def wrap(self, availWidth, availHeight):
        self.avail_width = availWidth
        # Ensure equation does not exceed available width
        draw_w = self.img_w
        draw_h = self.img_h
        if draw_w > availWidth and availWidth > 0:
            scale_down = availWidth / draw_w
            draw_w = availWidth
            draw_h = draw_h * scale_down

        self.draw_w = draw_w
        self.draw_h = draw_h
        return availWidth, self.draw_h + self.space_before + self.space_after

    def draw(self):
        c = self.canv
        # Center horizontally within available width
        x = (self.avail_width - self.draw_w) / 2.0
        y = self.space_after
        c.drawImage(str(self.img_path), x, y, width=self.draw_w, height=self.draw_h, mask='auto')


def render_equation(latex_str: str, fontsize: float = 12.0, color: str = '#111111',
                    space_before: float = 6.0, space_after: float = 6.0, scale: float = 1.05) -> EquationFlowable:
    """Helper function returning an EquationFlowable for ReportLab story."""
    return EquationFlowable(
        latex_str,
        fontsize=fontsize,
        color=color,
        space_before=space_before,
        space_after=space_after,
        scale=scale
    )

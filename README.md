<div align="center">

<img src="diagrams/fig03_3d_trajectory.png" width="700" alt="ODM 3D Trajectory — Levi Ackerman"/>

# The Mathematics and Physics of ODM Gear
### A Physical Model of Levi Ackerman's Three-Dimensional Movement

[![PDF Download](https://img.shields.io/badge/📄_Download_PDF-6.6_MB-C8A96E?style=for-the-badge&logoColor=white)](ODM_Gear_Physics_Levi_Ackerman.pdf)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![ReportLab](https://img.shields.io/badge/ReportLab-PDF_Engine-red?style=for-the-badge)](https://www.reportlab.com/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Diagrams-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

*Physics · Vector Mechanics · Aerodynamics · Material Science · 2026*

</div>

---

## 🎯 What Is This?

This repository contains a **29-page, publication-quality academic physics essay** that applies serious Newtonian mechanics, vector dynamics, aerodynamics, material science, and human physiology to the ODM (Omni-Directional Mobility) gear used by Levi Ackerman in *Attack on Titan*.

This is **not** a casual "anime science" article. It is a mathematically structured essay modelled on competition-level academic physics writing — with rigorous equations, numbered theorems, proper uncertainty analysis, engineering data tables, and a comprehensive citation list of **real published sources** (no fabricated DOIs, no fan-wiki authority).

### The Central Mathematical Question

> *Can Levi Ackerman's three-dimensional ODM movement be represented as a physically meaningful constrained dynamical system, and what do mathematics and Newtonian mechanics predict about speed, acceleration, cable tension, energy, trajectory geometry, and human survivability?*

The answer hinges on a single constraint equation:

$$\|\mathbf{r}_L(t) - \mathbf{r}_A(t)\| = L(t)$$

— where $\mathbf{r}_L(t)$ is Levi's position, $\mathbf{r}_A(t)$ is the anchor position, and $L(t)$ is the instantaneous cable length. From this one equation, the entire mechanical model cascades outward.

---

## 📐 Paper Structure (14 Sections)

| Section | Title | Key Mathematics |
|---------|-------|-----------------|
| — | **Abstract** | Central question, roadmap |
| 1 | **Introduction** | Opening hook (Ep. 22), central constraint |
| 2 | **What Is ODM Gear?** | Component table, dual-cable architecture |
| 3 | **Kinematics** | $\mathbf{r}(t)$, $\mathbf{v}(t)$, $\mathbf{a}(t)$ in 3D; Levi's physical parameters |
| 4 | **The Cable as a Mathematical Constraint** | $\|\mathbf{r}_L - \mathbf{r}_A\| = L(t)$; velocity constraint derivation |
| 5 | **Why Straight-Line Kinematics Fails** | Tangential–normal decomposition; $a_n = v^2/\rho$ |
| 6 | **Centripetal Force and Cable Tension** | $\mathbf{F}_c = mv^2/\rho$; full force balance $m\mathbf{a} = \mathbf{T} + \mathbf{F}_g + \mathbf{F}_\text{gas} + \mathbf{F}_D$ |
| 7 | **Two-Anchor Vector Control** | $\mathbf{T}_\text{res} = \mathbf{T}_1 + \mathbf{T}_2$; manoeuvre capability table |
| 8 | **Variable Cable Length, Energy & Momentum** | $K = \frac{1}{2}mv^2$; impulse $\Delta\mathbf{p} = \int F\,dt$ |
| 9 | **Drag and High-Speed Limits** | $F_D = \frac{1}{2}C_D\rho A v^2$; power $P_D = F_D \cdot v$ |
| 10 | **Levi's Rotational Combat** | $\mathbf{L} = \mathbf{r} \times m\mathbf{v}$; angular momentum conservation |
| 11 | **Could the Cables Survive?** | $\sigma = T/A_c$; material stress table; 4 mm cable analysis |
| 12 | **Can the Human Body Survive It?** | $n = v^2/(rg) + 1$; G-force table vs NASA/Stapp limits |
| 13 | **Optimal Trajectory** | Constrained optimisation $\min \int P\,dt$; reality check table |
| 14 | **Conclusion** | What physics explains; what requires fictional technology |
| — | **References** | 12 real published sources; research audit statement |

---

## 🖼️ Scientific Diagrams

All 12 figures are original — computed from physics equations and rendered with Matplotlib. No figures are borrowed from external sources.

| Figure | Description |
|--------|-------------|
| `fig03_3d_trajectory.png` | Two-anchor ODM trajectory in 3D space |
| `fig03_odm_schematic.png` | ODM gear component schematic |
| `fig05_cable_constraint.png` | Cable constraint geometry — sphere of radius L(t) |
| `fig06_tangential_normal.png` | Tangential–normal acceleration decomposition |
| `fig07_free_body.png` | Free-body diagram: **T**, **F**_g, **F**_gas, **F**_D |
| `fig08_two_anchor.png` | Two-anchor vector resultant **T**_res |
| `fig09_energy_momentum.png` | Kinetic energy vs speed; impulsive force vs time |
| `fig10_drag_force.png` | Drag force and drag power vs speed |
| `fig11_rotational.png` | Simple pendulum vs rotational attack trajectory |
| `fig12_cable_stress.png` | Stress–strain curve; cable tension vs breaking load |
| `fig13_gforce.png` | G-force comparison (ODM vs real-world references) |
| `fig14_optimization.png` | Candidate trajectories; power budget ∫P dt |

<div align="center">

| Diagram Gallery |
|---|
| <img src="diagrams/fig06_tangential_normal.png" width="380" alt="Tangential-Normal Decomposition"/> <img src="diagrams/fig07_free_body.png" width="380" alt="Free Body Diagram"/> |
| <img src="diagrams/fig12_cable_stress.png" width="380" alt="Cable Stress"/> <img src="diagrams/fig13_gforce.png" width="380" alt="G-Force Comparison"/> |

</div>

---

## 🏷️ Epistemic Labelling System

Every factual claim in the paper is tagged inline with one of the following markers — this is the most important design decision of the essay:

| Tag | Meaning |
|-----|---------|
| `[CANON]` | Established by the *Attack on Titan* series or official guidebooks |
| `[PHYSICS]` | Standard textbook result, independently verified |
| `[MODEL]` | Physical interpretation introduced by this paper |
| `[ASSUMPTION]` | Engineering input with explicit value, units, and sensitivity note |
| `[ESTIMATE]` | Order-of-magnitude derivation from canonical geometry |
| `[FICTIONAL LIMIT]` | Point where real physics breaks down; fictional technology required |

**No canon claim was sourced from fan wikis alone. No assumption was presented as measured fact.**

---

## 📊 Key Numerical Results

| Calculation | Formula | Result |
|-------------|---------|--------|
| Speed at bottom of 15 m swing (60° release) | $v = \sqrt{2gL(1-\cos\theta_0)}$ | **≈ 12.1 m/s** |
| Cable tension (v = 15 m/s, r = 12 m, m = 80 kg) | $T = m(v^2/r + g)$ | **≈ 2.3 kN** |
| Cable tension (v = 20 m/s, r = 8 m) | Same formula | **≈ 4.8 kN** |
| Normal acceleration (v = 15 m/s, ρ = 12 m) | $a_n = v^2/\rho$ | **≈ 18.75 m/s²** |
| Kinetic energy at v = 20 m/s | $K = \frac{1}{2}mv^2$ | **16 kJ** |
| Drag force (v = 20 m/s, horizontal) | $F_D = \frac{1}{2}C_D\rho A v^2$ | **≈ 69 N** |
| Spin speed-up (r₁ = 4 m → r₂ = 2 m) | Angular momentum conservation | **v: 10 → 20 m/s** |
| Required cable diameter (SF = 5) | $d = \sqrt{4A_c/\pi}$ | **≈ 3.9 mm** |
| G-force (v = 20 m/s, r = 10 m) | $n = v^2/(rg) + 1$ | **≈ 5.1 Gz** |
| G-force (v = 30 m/s, r = 5 m) | Same formula | **≈ 19.4 Gz ⚠️** |

---

## 🚀 Reproducing the PDF

### 1. Clone the repository

```bash
git clone https://github.com/StrangerLooter/levi-ackerman-physics.git
cd levi-ackerman-physics
```

### 2. Install dependencies

```bash
pip install matplotlib numpy scipy reportlab pymupdf
```

> **Python ≥ 3.10** required. Tested on Python 3.13.

### 3. Generate the scientific diagrams

```bash
python generate_diagrams.py
```

This creates all 12 PNG figures in `diagrams/`.

### 4. Generate the PDF

```bash
python generate_pdf.py
```

This produces `output/ODM_Gear_Physics_Levi_Ackerman.pdf` (≈ 6.6 MB, 29 pages).

### 5. (Optional) Render page previews

```bash
python -c "
import pymupdf, os
doc = pymupdf.open('output/ODM_Gear_Physics_Levi_Ackerman.pdf')
os.makedirs('output/preview', exist_ok=True)
for i in range(doc.page_count):
    pix = doc[i].get_pixmap(matrix=pymupdf.Matrix(2,2))
    pix.save(f'output/preview/page_{i+1:02d}.png')
print(f'Rendered {doc.page_count} pages')
"
```

---

## 📁 Repository Structure

```
levi-ackerman-physics/
│
├── ODM_Gear_Physics_Levi_Ackerman.pdf   ← Final output (29 pages, 6.6 MB)
│
├── generate_diagrams.py                 ← Matplotlib script — 12 scientific figures
├── generate_pdf.py                      ← ReportLab script — full PDF assembly
│
├── diagrams/                            ← Generated PNG assets
│   ├── fig03_3d_trajectory.png
│   ├── fig03_odm_schematic.png
│   ├── fig05_cable_constraint.png
│   ├── fig06_tangential_normal.png
│   ├── fig07_free_body.png
│   ├── fig08_two_anchor.png
│   ├── fig09_energy_momentum.png
│   ├── fig10_drag_force.png
│   ├── fig11_rotational.png
│   ├── fig12_cable_stress.png
│   ├── fig13_gforce.png
│   └── fig14_optimization.png
│
└── README.md                            ← This file
```

---

## 📚 References

The paper cites 12 real, published sources:

1. Young & Freedman — *University Physics with Modern Physics*, 14th ed., Pearson, 2016
2. OpenStax — *University Physics, Volume 1*, 2016 [CC-BY 4.0]
3. Meriam & Kraige — *Engineering Mechanics: Dynamics*, 8th ed., Wiley, 2016
4. Hajime Isayama — *Attack on Titan*, Vols. 1–34, Kodansha, 2009–2021 *(primary canon source)*
5. *Attack on Titan Official Guidebook / Inside*, Kodansha, 2014 *(Levi's stats: 160 cm, 65 kg)*
6. Wire Rope Technical Board — *Wire Rope Users Manual*, 4th ed., 2005
7. Sheldahl & Klimas — *Aerodynamic Characteristics of Seven Symmetrical Airfoil Sections*, SAND80-2114, Sandia NL, 1981
8. **NASA-STD-3001** — *NASA Space Flight Human-System Standard, Vol. 1: Crew Health*, 2014
9. J.P. Stapp — "Human Tolerance to Deceleration," *Journal of Aviation Medicine*, vol. 22, 1951
10. F.E. Guignard — "Human Tolerance to Whole-Body Acceleration," *Human Factors in Aviation*, Academic Press, 1988
11. Koei Tecmo / Omega Force — *Attack on Titan: Wings of Freedom*, 2016
12. Attack on Titan Wiki — Secondary cross-reference only; not used as primary source for any physics claim

---

## 🧠 Design Philosophy

This paper was designed around five principles drawn from serious academic physics writing:

1. **Progressive escalation** — Each mathematical framework is introduced precisely when the previous one fails. The paper never introduces complexity for its own sake.

2. **Honest modelling** — Every unknown is stated explicitly. No engineering value was invented and presented as measured canon data.

3. **Epistemic rigour** — The `[CANON] / [MODEL] / [ASSUMPTION] / [ESTIMATE] / [FICTIONAL LIMIT]` tagging system ensures the reader always knows exactly what is being claimed and on what authority.

4. **Accessible depth** — The mathematics starts at A-level / first-year university physics and escalates to graduate-level constrained optimisation. Each step is legible independently.

5. **Visual quality** — All figures are purpose-built from the physics equations. No stock imagery, no copied diagrams.

---

## ⚠️ Disclaimer

This is a **fan-made, non-commercial academic exercise**. *Attack on Titan* and all related characters, gear, and lore are the intellectual property of Hajime Isayama and Kodansha. This project is not affiliated with or endorsed by any rights holder.

The physical model developed here is an original engineering interpretation, not an official description of how ODM gear is intended to work within the fictional universe.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

The PDF essay and all generated figures are released under the same license. Attribution appreciated but not required.

---

<div align="center">

*"The only time a soldier should retreat is when they can't win."*
— **Levi Ackerman**

*The mathematics agrees: at n ≈ 9 Gz, retreat is the physically correct choice.*

</div>

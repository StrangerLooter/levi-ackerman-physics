"""
Scientific Diagram Generator
The Mathematics and Physics of ODM Gear
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, Arc, Circle, FancyBboxPatch
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec
import matplotlib.patheffects as pe
import warnings
warnings.filterwarnings('ignore')

# ── Color palette (dark military aesthetic) ──────────────────────────────────
BG       = '#0D0D0D'    # near-black page
DARK     = '#111520'    # panel background
PANEL    = '#1A1F30'    # card
ACCENT   = '#C8A96E'    # gold / Survey Corps
ACCENT2  = '#6E9AC8'    # steel blue
ACCENT3  = '#C86E6E'    # blood red / danger
GREEN    = '#6EC88A'    # success / safe
WHITE    = '#E8E8E8'
GREY     = '#888888'
TEXTGREY = '#BBBBBB'

def style_ax(ax, title='', xlabel='', ylabel='', bg=DARK):
    ax.set_facecolor(bg)
    ax.tick_params(colors=TEXTGREY, labelsize=9)
    ax.spines['bottom'].set_color(GREY)
    ax.spines['left'].set_color(GREY)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    if title:
        ax.set_title(title, color=WHITE, fontsize=11, fontweight='bold', pad=8)
    if xlabel:
        ax.set_xlabel(xlabel, color=TEXTGREY, fontsize=9)
    if ylabel:
        ax.set_ylabel(ylabel, color=TEXTGREY, fontsize=9)

def save_fig(fig, name, dpi=300):
    fig.savefig(f'diagrams/{name}', dpi=dpi, bbox_inches='tight',
                facecolor=BG, edgecolor='none')
    plt.close(fig)
    print(f'  OK: {name} (dpi={dpi})')

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 1 — 3D trajectory in coordinate space
# ═══════════════════════════════════════════════════════════════════════════
def diagram_3d_trajectory():
    fig = plt.figure(figsize=(7, 6), facecolor=BG)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor(DARK)

    # Parametric swing path
    t = np.linspace(0, 2*np.pi, 300)
    # Two connected swings
    t1 = np.linspace(0, np.pi, 150)
    t2 = np.linspace(0, np.pi, 150)

    # Swing 1: arc around anchor A1
    cx1, cy1, cz1 = 10, 0, 15
    R1 = 12
    x1 = cx1 + R1*np.sin(t1)*np.cos(0.3)
    y1 = cy1 + R1*np.sin(t1)*np.sin(0.3)
    z1 = cz1 - R1*np.cos(t1) + R1

    # Swing 2: arc around anchor A2
    cx2, cy2, cz2 = 20, 12, 18
    R2 = 10
    x2 = cx2 + R2*np.sin(t2)*np.cos(-0.5) + (x1[-1]-cx2-R2*np.sin(0)*np.cos(-0.5))
    y2 = cy2 + R2*np.sin(t2)*np.sin(-0.5) + (y1[-1]-cy2-R2*np.sin(0)*np.sin(-0.5))
    z2 = cz2 - R2*np.cos(t2) + R2

    # Stitch
    xs = np.concatenate([x1, x2])
    ys = np.concatenate([y1, y2])
    zs = np.concatenate([z1, z2])

    # Grid lines (floor)
    for xg in np.linspace(0, 30, 7):
        ax.plot([xg, xg], [0, 25], [0, 0], color='#2A2A3A', lw=0.5)
    for yg in np.linspace(0, 25, 6):
        ax.plot([0, 30], [yg, yg], [0, 0], color='#2A2A3A', lw=0.5)

    # Trajectory
    ax.plot(xs, ys, zs, color=ACCENT2, lw=2.5, zorder=5, label='ODM trajectory')

    # Start / end markers
    ax.scatter([xs[0]], [ys[0]], [zs[0]], color=GREEN, s=80, zorder=6)
    ax.scatter([xs[-1]], [ys[-1]], [zs[-1]], color=ACCENT3, s=80, zorder=6)

    # Anchor points
    A1 = np.array([cx1, cy1, cz1])
    A2 = np.array([cx2, cy2, cz2])
    ax.scatter(*A1, color=ACCENT, s=120, marker='^', zorder=7)
    ax.scatter(*A2, color=ACCENT, s=120, marker='^', zorder=7)

    # Cable lines at midpoint
    mid1 = len(t1)//2
    mid2 = len(t2)//2
    ax.plot([x1[mid1], cx1], [y1[mid1], cy1], [z1[mid1], cz1],
            color=ACCENT, lw=1, ls='--', alpha=0.7)
    ax.plot([x2[mid2], cx2], [y2[mid2], cy2], [z2[mid2], cz2],
            color=ACCENT, lw=1, ls='--', alpha=0.7)

    # Labels
    ax.text(cx1+1, cy1, cz1+1, r'$\mathbf{r}_{A_1}$', color=ACCENT, fontsize=10)
    ax.text(cx2+1, cy2, cz2+1, r'$\mathbf{r}_{A_2}$', color=ACCENT, fontsize=10)
    ax.text(xs[0]+1, ys[0], zs[0]+1, r'$\mathbf{r}_L(0)$', color=GREEN, fontsize=9)
    ax.text(xs[-1]+1, ys[-1], zs[-1]+1, r'$\mathbf{r}_L(t_f)$', color=ACCENT3, fontsize=9)

    # Axis labels
    ax.set_xlabel('x (m)', color=TEXTGREY, fontsize=9, labelpad=5)
    ax.set_ylabel('y (m)', color=TEXTGREY, fontsize=9, labelpad=5)
    ax.set_zlabel('z (m)', color=TEXTGREY, fontsize=9, labelpad=5)
    ax.tick_params(colors=TEXTGREY, labelsize=7)

    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#2A2A3A')
    ax.yaxis.pane.set_edgecolor('#2A2A3A')
    ax.zaxis.pane.set_edgecolor('#2A2A3A')

    ax.set_title('Figure 3: ODM Trajectory in 3D Space\n'
                 r'$\mathbf{r}_L(t) = [x(t),\, y(t),\, z(t)]$',
                 color=WHITE, fontsize=10, pad=10)
    ax.view_init(elev=25, azim=-50)

    fig.tight_layout()
    save_fig(fig, 'fig03_3d_trajectory.png')

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 2 — Cable constraint geometry (2D)
# ═══════════════════════════════════════════════════════════════════════════
def diagram_cable_constraint():
    fig, ax = plt.subplots(figsize=(7, 5), facecolor=BG)
    style_ax(ax, bg=DARK)
    ax.set_aspect('equal')
    ax.set_xlim(-1, 14)
    ax.set_ylim(-1, 12)

    # Anchor
    Ax, Ay = 8, 10
    # Levi at two positions
    Lx1, Ly1 = 2, 3
    Lx2, Ly2 = 5, 1

    # Cable vectors
    ax.annotate('', xy=(Ax, Ay), xytext=(Lx1, Ly1),
                arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2))
    ax.annotate('', xy=(Ax, Ay), xytext=(Lx2, Ly2),
                arrowprops=dict(arrowstyle='->', color=ACCENT2, lw=2))

    # Arc showing angle
    theta1 = np.degrees(np.arctan2(Ay-Ly1, Ax-Lx1))
    theta2 = np.degrees(np.arctan2(Ay-Ly2, Ax-Lx2))
    arc = Arc((Ax, Ay), 3, 3, angle=0, theta1=min(theta1,theta2)-180,
              theta2=max(theta1,theta2)-180, color=GREEN, lw=1.5)
    ax.add_patch(arc)

    # Levi points
    ax.plot(Lx1, Ly1, 'o', color=ACCENT2, markersize=14, zorder=5)
    ax.plot(Lx2, Ly2, 'o', color=ACCENT3, markersize=14, zorder=5)
    ax.text(Lx1-1.2, Ly1, r'$\mathbf{r}_L(t_1)$', color=ACCENT2, fontsize=10, va='center')
    ax.text(Lx2-1.2, Ly2, r'$\mathbf{r}_L(t_2)$', color=ACCENT3, fontsize=10, va='center')

    # Anchor
    ax.plot(Ax, Ay, '^', color=ACCENT, markersize=14, zorder=5)
    ax.text(Ax+0.3, Ay+0.3, r'$\mathbf{r}_A$', color=ACCENT, fontsize=11)

    # L labels
    L1 = np.sqrt((Ax-Lx1)**2+(Ay-Ly1)**2)
    L2 = np.sqrt((Ax-Lx2)**2+(Ay-Ly2)**2)
    mx1, my1 = (Ax+Lx1)/2, (Ay+Ly1)/2
    mx2, my2 = (Ax+Lx2)/2, (Ay+Ly2)/2
    ax.text(mx1-1.5, my1+0.3, rf'$L(t_1)={L1:.1f}$ m', color=ACCENT, fontsize=9, style='italic')
    ax.text(mx2+0.2, my2, rf'$L(t_2)={L2:.1f}$ m', color=ACCENT2, fontsize=9, style='italic')

    # Equation box
    eq_text = (r'Constraint: $\|\mathbf{r}_L(t) - \mathbf{r}_A\| = L(t)$')
    ax.text(0.5, 11, eq_text, color=WHITE, fontsize=10,
            ha='left', va='top',
            bbox=dict(facecolor=PANEL, edgecolor=ACCENT, alpha=0.9, boxstyle='round,pad=0.5'))

    # Grid floor
    for xg in range(0, 14, 2):
        ax.axvline(xg, color='#2A2A3A', lw=0.5, zorder=0)
    for yg in range(0, 12, 2):
        ax.axhline(yg, color='#2A2A3A', lw=0.5, zorder=0)

    ax.set_title('Figure 5: Cable Constraint Geometry — Variable Length $L(t)$',
                 color=WHITE, fontsize=10, pad=8)
    ax.set_xlabel('x (m)', color=TEXTGREY, fontsize=9)
    ax.set_ylabel('z (m)', color=TEXTGREY, fontsize=9)
    ax.set_facecolor(DARK)

    save_fig(fig, 'fig05_cable_constraint.png')

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 3 — Tangential + Normal acceleration decomposition
# ═══════════════════════════════════════════════════════════════════════════
def diagram_tangential_normal():
    fig, ax = plt.subplots(figsize=(7, 5.5), facecolor=BG)
    style_ax(ax, bg=DARK)
    ax.set_aspect('equal')
    ax.set_xlim(-3, 11)
    ax.set_ylim(-2, 9)

    # Curved path
    t = np.linspace(0, np.pi, 200)
    R = 5
    cx, cy = 5, 0
    xs = cx + R*np.cos(t)
    ys = cy + R*np.sin(t)
    ax.plot(xs, ys, color=ACCENT2, lw=2.5, zorder=3, label='ODM path')

    # Point on curve
    t0 = np.pi*0.55
    Px = cx + R*np.cos(t0)
    Py = cy + R*np.sin(t0)

    # Tangent direction
    Tx = -np.sin(t0)
    Ty = np.cos(t0)
    # Normal direction (inward = centripetal)
    Nx = np.cos(t0 + np.pi)
    Ny = np.sin(t0 + np.pi)

    scale = 2.5
    # Draw vectors
    ax.annotate('', xy=(Px+scale*Tx, Py+scale*Ty), xytext=(Px, Py),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
    ax.annotate('', xy=(Px+scale*Nx, Py+scale*Ny), xytext=(Px, Py),
                arrowprops=dict(arrowstyle='->', color=ACCENT3, lw=2.5))
    # Total acceleration (diagonal)
    at_s = 1.2; an_s = 2.5
    ax.annotate('', xy=(Px+at_s*Tx+an_s*Nx, Py+at_s*Ty+an_s*Ny), xytext=(Px, Py),
                arrowprops=dict(arrowstyle='->', color=WHITE, lw=2, ls='--'))

    ax.plot(Px, Py, 'o', color=ACCENT, markersize=12, zorder=5)

    # Labels
    ax.text(Px+scale*Tx+0.2, Py+scale*Ty+0.1, r'$\hat{\mathbf{T}}$' + '\n(tangential)', color=GREEN, fontsize=10)
    ax.text(Px+scale*Nx-2.5, Py+scale*Ny-0.5, r'$\hat{\mathbf{N}}$' + '\n(normal/centripetal)', color=ACCENT3, fontsize=10)
    ax.text(Px+at_s*Tx+an_s*Nx+0.1, Py+at_s*Ty+an_s*Ny-0.4,
            r'$\mathbf{a}$', color=WHITE, fontsize=12)

    # Equations box
    eq = (r'$\mathbf{a} = a_t\hat{\mathbf{T}} + a_n\hat{\mathbf{N}}$'
          '\n'
          r'$a_t = \frac{dv}{dt}$,   $a_n = \frac{v^2}{\rho}$')
    ax.text(-2.5, 8.5, eq, color=WHITE, fontsize=10,
            bbox=dict(facecolor=PANEL, edgecolor=ACCENT, alpha=0.9, boxstyle='round,pad=0.6'))

    # Center of curvature
    ax.plot(cx, cy, 'x', color=ACCENT, markersize=10, mew=2, zorder=4)
    ax.text(cx+0.2, cy+0.2, r'Centre of curvature $C$', color=ACCENT, fontsize=9)
    # Dashed radius
    ax.plot([cx, Px], [cy, Py], color=ACCENT, lw=1, ls=':', alpha=0.5)
    ax.text((cx+Px)/2-1, (cy+Py)/2+0.3, r'$\rho$', color=ACCENT, fontsize=10)

    ax.set_title('Figure 6: Tangential and Normal Acceleration Decomposition',
                 color=WHITE, fontsize=10, pad=8)
    ax.set_xlabel('x (m)', color=TEXTGREY, fontsize=9)
    ax.set_ylabel('z (m)', color=TEXTGREY, fontsize=9)

    save_fig(fig, 'fig06_tangential_normal.png')

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 4 — Free-body diagram (centripetal, cable tension, gravity, gas)
# ═══════════════════════════════════════════════════════════════════════════
def diagram_free_body():
    fig, ax = plt.subplots(figsize=(6, 7), facecolor=BG)
    style_ax(ax, bg=DARK)
    ax.set_aspect('equal')
    ax.set_xlim(-5, 10)
    ax.set_ylim(-7, 11)

    # Levi body
    body = Circle((0, 0), 0.7, color=ACCENT2, zorder=5)
    ax.add_patch(body)
    ax.text(0, 0, 'L', color=WHITE, ha='center', va='center', fontsize=12, fontweight='bold', zorder=6)

    # Anchor above-right
    Ax, Ay = 5, 8
    ax.plot(Ax, Ay, '^', color=ACCENT, markersize=14, zorder=5)
    ax.text(Ax+0.3, Ay+0.3, r'$A$', color=ACCENT, fontsize=11)

    # Tension vector (toward anchor)
    Tmag = 3.5
    Tdir = np.array([Ax, Ay]) / np.linalg.norm([Ax, Ay])
    ax.annotate('', xy=(Tmag*Tdir[0], Tmag*Tdir[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=ACCENT, lw=3))
    ax.text(Tmag*Tdir[0]+0.2, Tmag*Tdir[1]-0.3,
            r'$\mathbf{T}$' + '\n(cable tension)', color=ACCENT, fontsize=10)

    # Gravity vector (downward)
    Gmag = 2.5
    ax.annotate('', xy=(0, -Gmag), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=ACCENT3, lw=3))
    ax.text(0.2, -Gmag-0.2, r'$\mathbf{F}_g = m\mathbf{g}$', color=ACCENT3, fontsize=10)

    # Gas thrust (horizontal / forward)
    Fmag = 2.0
    ax.annotate('', xy=(-Fmag, 0.5), xytext=(0, 0.5),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
    ax.text(-Fmag-2.5, 0.5, r'$\mathbf{F}_{gas}$' + '\n(thrust)', color=GREEN, fontsize=10, va='center')

    # Velocity vector (tangential to swing arc, moving up-left)
    vx, vy = -3.0, 2.5
    v_norm = np.hypot(vx, vy)
    v_dir = np.array([vx, vy]) / v_norm
    ax.annotate('', xy=(vx, vy), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=ACCENT2, lw=2.5, linestyle='dashed'))
    ax.text(vx - 0.4, vy + 0.3, r'$\mathbf{v}$ (velocity)', color=ACCENT2, fontsize=11, fontweight='bold')

    # Drag (strictly opposes velocity: antiparallel to v)
    Dmag = 1.6
    Ddir = -v_dir
    ax.annotate('', xy=(Dmag * Ddir[0], Dmag * Ddir[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color='#FF9F40', lw=2.5))
    ax.text(Dmag * Ddir[0] + 0.3, Dmag * Ddir[1] - 0.3,
            r'$\mathbf{F}_D$' + '\n(aerodynamic drag,\nopposes ' + r'$\mathbf{v}$)', color='#FF9F40', fontsize=10, va='top')

    # Net force equation
    eq = (r'$m\mathbf{a} = \mathbf{T} + m\mathbf{g} + \mathbf{F}_{\mathrm{gas}} + \mathbf{F}_D$'
          '\n' + r'Note: $F_c = m v^2/\rho$ is the net radial component, not an independent force.')
    ax.text(-4.5, 10, eq, color=WHITE, fontsize=9.5,
            bbox=dict(facecolor=PANEL, edgecolor=ACCENT, alpha=0.9, boxstyle='round,pad=0.6'))

    ax.set_title('Figure 7: Free-Body Diagram — Forces on Levi During ODM Swing',
                 color=WHITE, fontsize=10, pad=8)
    ax.set_xlabel('x (m)', color=TEXTGREY, fontsize=9)
    ax.set_ylabel('z (m)', color=TEXTGREY, fontsize=9)
    # Light grid
    for i in range(-5, 11, 2):
        ax.axvline(i, color='#2A2A3A', lw=0.4, zorder=0)
    for i in range(-7, 12, 2):
        ax.axhline(i, color='#2A2A3A', lw=0.4, zorder=0)

    save_fig(fig, 'fig07_free_body.png')

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 5 — Two-anchor vector diagram (3D perspective)
# ═══════════════════════════════════════════════════════════════════════════
def diagram_two_anchor():
    fig = plt.figure(figsize=(8, 6.5), facecolor=BG)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor(DARK)

    # Levi position
    Lx, Ly, Lz = 5, 5, 3

    # Two anchors
    A1 = np.array([0, 0, 10])
    A2 = np.array([12, 2, 9])
    L  = np.array([Lx, Ly, Lz])

    # Cable vectors
    C1 = A1 - L
    C2 = A2 - L
    T1_hat = C1 / np.linalg.norm(C1)
    T2_hat = C2 / np.linalg.norm(C2)

    T1_mag = 2.5
    T2_mag = 2.0
    T_res  = T1_mag*T1_hat + T2_mag*T2_hat

    def arr(ax, start, vec, color, lw=2.5, label=''):
        end = start + vec
        ax.quiver(*start, *vec, color=color, lw=lw, arrow_length_ratio=0.15)
        if label:
            ax.text(*(end + 0.3), label, color=color, fontsize=10)

    # Cables (dashed)
    for A in [A1, A2]:
        ax.plot([L[0], A[0]], [L[1], A[1]], [L[2], A[2]],
                color=ACCENT, lw=1.5, ls='--', alpha=0.8)

    # Tension vectors
    arr(ax, L, T1_mag*T1_hat, ACCENT, label=r'$\mathbf{T}_1$')
    arr(ax, L, T2_mag*T2_hat, ACCENT2, label=r'$\mathbf{T}_2$')

    # Resultant
    arr(ax, L, T_res, WHITE, lw=3, label=r'$\mathbf{T}_{res}$')

    # Gravity
    arr(ax, L, np.array([0, 0, -2.0]), ACCENT3, label=r'$\mathbf{F}_g$')

    # Levi and anchors
    ax.scatter(*L, color=ACCENT2, s=150, zorder=7)
    ax.scatter(*A1, color=ACCENT, s=150, marker='^', zorder=7)
    ax.scatter(*A2, color=ACCENT, s=150, marker='^', zorder=7)
    ax.text(A1[0]-0.5, A1[1], A1[2]+0.5, r'$A_1$', color=ACCENT, fontsize=11)
    ax.text(A2[0]+0.5, A2[1], A2[2]+0.5, r'$A_2$', color=ACCENT, fontsize=11)
    ax.text(Lx-0.5, Ly-0.5, Lz+0.5, r'Levi', color=ACCENT2, fontsize=11)

    # Parallelogram dashes for resultant
    P1 = L + T1_mag*T1_hat
    P2 = L + T2_mag*T2_hat
    Pr = L + T_res
    ax.plot([P1[0], Pr[0]], [P1[1], Pr[1]], [P1[2], Pr[2]],
            color=GREY, lw=1, ls=':', alpha=0.5)
    ax.plot([P2[0], Pr[0]], [P2[1], Pr[1]], [P2[2], Pr[2]],
            color=GREY, lw=1, ls=':', alpha=0.5)

    ax.set_xlabel('x (m)', color=TEXTGREY, fontsize=9)
    ax.set_ylabel('y (m)', color=TEXTGREY, fontsize=9)
    ax.set_zlabel('z (m)', color=TEXTGREY, fontsize=9)
    ax.tick_params(colors=TEXTGREY, labelsize=7)
    ax.xaxis.pane.fill = False; ax.yaxis.pane.fill = False; ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('#2A2A3A')
    ax.yaxis.pane.set_edgecolor('#2A2A3A')
    ax.zaxis.pane.set_edgecolor('#2A2A3A')

    ax.set_title('Figure 8: Two-Anchor Vector Control\n'
                 r'$\mathbf{T}_{res} = \mathbf{T}_1 + \mathbf{T}_2$',
                 color=WHITE, fontsize=10)
    ax.view_init(elev=20, azim=35)

    fig.tight_layout()
    save_fig(fig, 'fig08_two_anchor.png')

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 6 — Drag force vs velocity
# ═══════════════════════════════════════════════════════════════════════════
def diagram_drag_force():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), facecolor=BG)

    v = np.linspace(0, 40, 400)
    rho = 1.225       # kg/m^3 air density
    Cd1 = 1.0         # upright/open body
    Cd2 = 0.6         # streamlined position
    A1  = 0.7         # m^2 frontal area, upright
    A2  = 0.4         # m^2 streamlined

    FD1 = 0.5 * Cd1 * rho * A1 * v**2
    FD2 = 0.5 * Cd2 * rho * A2 * v**2

    ax = axes[0]
    style_ax(ax, bg=DARK, xlabel='Speed $v$ (m/s)', ylabel='Drag Force $F_D$ (N)')
    ax.plot(v, FD1, color=ACCENT3, lw=2.5, label=r'Upright ($C_DA=0.70$ m²)')
    ax.plot(v, FD2, color=GREEN,   lw=2.5, label=r'Streamlined ($C_DA=0.24$ m²)')
    ax.axvline(10, color=ACCENT, lw=1, ls='--', alpha=0.6)
    ax.axvline(25, color=ACCENT, lw=1, ls='--', alpha=0.6)
    ax.text(10.3, max(FD1)*0.7, '10 m/s', color=ACCENT, fontsize=8)
    ax.text(25.3, max(FD1)*0.7, '25 m/s', color=ACCENT, fontsize=8)

    # Shade combat range
    ax.fill_betweenx([0, max(FD1)*1.05], 10, 25, alpha=0.1, color=ACCENT)
    ax.text(17, max(FD1)*0.85, 'combat\nrange', color=ACCENT, fontsize=8, ha='center')

    ax.legend(fontsize=8, facecolor=PANEL, edgecolor=GREY, labelcolor=WHITE)
    ax.set_title('Drag Force vs Speed', color=WHITE, fontsize=10)
    ax.set_ylim(0, max(FD1)*1.1)

    # Right panel: fraction of gas thrust spent on drag
    # Assume gas thrust = 500 N (assumption)
    ax2 = axes[1]
    style_ax(ax2, bg=DARK, xlabel='Speed $v$ (m/s)', ylabel='Power consumed by drag (W)')
    Pd1 = FD1 * v
    Pd2 = FD2 * v
    ax2.plot(v, Pd1, color=ACCENT3, lw=2.5, label='Upright')
    ax2.plot(v, Pd2, color=GREEN,   lw=2.5, label='Streamlined')
    ax2.set_title('Drag Power $P_D = F_D \\cdot v$', color=WHITE, fontsize=10)
    ax2.legend(fontsize=8, facecolor=PANEL, edgecolor=GREY, labelcolor=WHITE)

    fig.suptitle('Figure 10: Aerodynamic Drag Analysis\n'
                 r'$F_D = \frac{1}{2} C_D \rho A v^2$',
                 color=WHITE, fontsize=11, y=1.01)
    fig.tight_layout()
    save_fig(fig, 'fig10_drag_force.png', dpi=300)

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 7 — Rotational combat / angular momentum
# ═══════════════════════════════════════════════════════════════════════════
def diagram_rotational():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), facecolor=BG)

    # Left: simple pendulum swing
    ax1 = axes[0]
    style_ax(ax1, bg=DARK)
    ax1.set_aspect('equal')
    ax1.set_xlim(-6, 6)
    ax1.set_ylim(-7, 5)

    t = np.linspace(-np.pi*0.7, np.pi*0.7, 200)
    R = 6
    xs = R*np.sin(t)
    ys = -R*np.cos(t)
    ax1.plot(xs, ys, color=ACCENT2, lw=2.5)
    ax1.plot(0, 0, '^', color=ACCENT, markersize=14)
    ax1.text(0.3, 0.3, r'$A$', color=ACCENT, fontsize=11)

    # Levi at bottom
    ax1.plot(0, -R, 'o', color=ACCENT2, markersize=14)
    ax1.plot([0, 0], [0, -R], '--', color=ACCENT, lw=1, alpha=0.6)
    ax1.text(0.2, -R-0.4, r'$v = \sqrt{gL}$', color=WHITE, fontsize=9)

    # Velocity vector
    ax1.annotate('', xy=(2, -R+1.5), xytext=(0, -R),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=2.5))
    ax1.text(2.2, -R+1.8, r'$\mathbf{v}$', color=GREEN, fontsize=11)

    ax1.set_title('Simple Pendulum Swing\n(single anchor)', color=WHITE, fontsize=10)
    ax1.set_xlabel('x (m)', color=TEXTGREY, fontsize=9)
    ax1.set_ylabel('z (m)', color=TEXTGREY, fontsize=9)

    # Right: rotational attack
    ax2 = axes[1]
    style_ax(ax2, bg=DARK)
    ax2.set_aspect('equal')
    ax2.set_xlim(-7, 7)
    ax2.set_ylim(-7, 7)

    # Spiral (decreasing radius = pulling cable in)
    t2 = np.linspace(0, 3*np.pi, 500)
    R_spiral = 5.0 - 1.3*(t2/(3*np.pi))
    xs2 = R_spiral * np.cos(t2)
    ys2 = R_spiral * np.sin(t2)
    ax2.plot(xs2, ys2, color=ACCENT3, lw=2.5)

    # Center
    ax2.plot(0, 0, '+', color=ACCENT, markersize=16, mew=2)
    ax2.text(0.3, 0.3, r'$A$', color=ACCENT, fontsize=11)

    # Angular momentum arrow (out of page)
    ax2.annotate('', xy=(0, 2.5), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=GREEN, lw=3))
    ax2.text(0.3, 2.8, r'$\mathbf{L} = \mathbf{r}\times\mathbf{p}$', color=GREEN, fontsize=10)

    # Blade path segments
    for i in range(0, len(t2)-10, 40):
        bx = xs2[i]; by = ys2[i]
        tang = np.array([-np.sin(t2[i]), np.cos(t2[i])])
        blen = 0.7
        ax2.annotate('', xy=(bx+blen*tang[0], by+blen*tang[1]), xytext=(bx, by),
                    arrowprops=dict(arrowstyle='->', color=WHITE, lw=1.5))

    ax2.set_title("Levi's Rotational Attack\n(decreasing radius → angular speed ↑)", color=WHITE, fontsize=10)
    ax2.set_xlabel('x (m)', color=TEXTGREY, fontsize=9)
    ax2.set_ylabel('y (m)', color=TEXTGREY, fontsize=9)

    # Annotation
    ax2.text(-6.5, -6, r'$r \downarrow \Rightarrow \omega \uparrow$ (conservation of $\mathbf{L}$)',
             color=ACCENT, fontsize=9,
             bbox=dict(facecolor=PANEL, edgecolor=ACCENT, alpha=0.8, boxstyle='round,pad=0.4'))

    fig.suptitle('Figure 11: Angular Momentum and Rotational Combat\n'
                 r'$\boldsymbol{\tau} = \frac{d\mathbf{L}}{dt}$, $\mathbf{L} = \mathbf{r} \times \mathbf{p}$',
                 color=WHITE, fontsize=11, y=1.01)
    fig.tight_layout()
    save_fig(fig, 'fig11_rotational.png', dpi=300)

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 8 — Cable stress diagram
# ═══════════════════════════════════════════════════════════════════════════
def diagram_cable_stress():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), facecolor=BG)

    # Left: stress-strain curve
    ax1 = axes[0]
    style_ax(ax1, bg=DARK, xlabel=r'Strain $\varepsilon = \Delta L / L_0$',
             ylabel=r'Stress $\sigma$ (MPa)')

    eps = np.linspace(0, 0.025, 500)
    E   = 200e3  # MPa (steel Young's modulus)
    sig_y = 1960  # MPa (EIPS yield ~ UTS for wire)
    sig_u = 2160  # MPa (EEIPS)

    # Linear elastic region
    eps_y = sig_y / E
    sig_linear = E * eps
    sig_linear[eps > eps_y] = np.nan

    # Plastic + fracture
    eps_plastic = np.linspace(eps_y, 0.022, 200)
    sig_plastic = sig_y + (sig_u - sig_y) * (1 - np.exp(-200*(eps_plastic - eps_y)))

    ax1.plot(eps*100, sig_linear, color=GREEN, lw=2.5, label='Elastic (steel)')
    ax1.plot(eps_plastic*100, sig_plastic, color=ACCENT3, lw=2.5, label='Plastic / failure')
    ax1.axhline(sig_y, color=ACCENT, lw=1.5, ls='--', alpha=0.7)
    ax1.axhline(sig_u, color=WHITE,  lw=1,   ls=':', alpha=0.6)
    ax1.text(0.1, sig_y+30, f'$\\sigma_{{EIPS}}$ = {sig_y:.0f} MPa', color=ACCENT, fontsize=9)
    ax1.text(0.1, sig_u+30, f'$\\sigma_{{EEIPS}}$ = {sig_u:.0f} MPa', color=WHITE, fontsize=9)
    ax1.legend(fontsize=8, facecolor=PANEL, edgecolor=GREY, labelcolor=WHITE)
    ax1.set_title('Stress-Strain: High-Tensile Steel', color=WHITE, fontsize=10)

    # Right: required tension vs speed for circular swing
    ax2 = axes[1]
    style_ax(ax2, bg=DARK, xlabel='Speed $v$ (m/s)',
             ylabel='Cable Tension $T$ (kN)')

    v2  = np.linspace(0, 40, 400)
    m   = 80    # kg (Levi + gear)
    r   = 10    # m swing radius
    T_centripetal = m * v2**2 / r / 1000   # kN

    # Add gravity component (worst case: bottom of swing)
    T_total = T_centripetal + m*9.81/1000  # kN

    # Failure threshold for 3mm cable (approx breaking load)
    A_c_3mm = np.pi*(1.5e-3)**2  # m^2
    T_break_3mm = 1960e6 * A_c_3mm / 1000  # kN
    A_c_5mm = np.pi*(2.5e-3)**2
    T_break_5mm = 1960e6 * A_c_5mm / 1000

    ax2.plot(v2, T_total, color=ACCENT2, lw=2.5, label=r'Required $T$ ($r=10$ m, $m=80$ kg)')
    ax2.axhline(T_break_3mm, color=ACCENT3, lw=1.5, ls='--',
                label=f'3 mm cable break ({T_break_3mm:.1f} kN)')
    ax2.axhline(T_break_5mm, color=GREEN, lw=1.5, ls='--',
                label=f'5 mm cable break ({T_break_5mm:.1f} kN)')
    ax2.fill_between(v2, T_break_3mm, T_break_5mm, alpha=0.1, color=ACCENT)

    ax2.set_ylim(0, max(T_break_5mm*1.2, max(T_total)*1.1))
    ax2.legend(fontsize=8, facecolor=PANEL, edgecolor=GREY, labelcolor=WHITE)
    ax2.set_title('Required Tension vs Speed\n[ASSUMPTION: $r=10$ m, $m=80$ kg]',
                  color=WHITE, fontsize=10)

    fig.suptitle('Figure 12: Cable Stress Analysis\n'
                 r'$\sigma = T / A_c$',
                 color=WHITE, fontsize=11, y=1.01)
    fig.tight_layout()
    save_fig(fig, 'fig12_cable_stress.png', dpi=300)

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 9 — G-force comparison chart
# ═══════════════════════════════════════════════════════════════════════════
def diagram_gforce():
    fig, ax = plt.subplots(figsize=(9, 6), facecolor=BG)
    style_ax(ax, bg=DARK)

    categories = [
        'Normal standing\n(1 g)',
        'Roller coaster\npeak (3–4 g)',
        'Fighter pilot\n(sustained, 9 g)',
        'ODM swing\n(10 m radius, 15 m/s)',
        'ODM sprint\n(5 m radius, 20 m/s)',
        'Stapp\nrocket sled\n(46.2 g, brief)',
    ]
    values     = [1.0, 3.5, 9.0, 15.81/9.81 + 1, 20**2/(5*9.81)+1, 46.2]
    colors     = [GREEN, GREEN, ACCENT, ACCENT2, ACCENT3, ACCENT3]
    labels     = ['Safe', 'Safe', 'Trained pilot limit', '[MODEL] ODM 15 m/s', '[MODEL] ODM 20 m/s', 'Brief (experimental)']

    # Sort by value
    idx = np.argsort(values)
    cats   = [categories[i] for i in idx]
    vals   = [values[i] for i in idx]
    cols   = [colors[i] for i in idx]
    labs   = [labels[i] for i in idx]

    bars = ax.barh(cats, vals, color=cols, edgecolor=DARK, height=0.6)

    # Threshold lines
    ax.axvline(9.0,  color=ACCENT, lw=1.5, ls='--', alpha=0.7)
    ax.text(9.2, -0.5, 'Pilot limit\n(anti-G suit)', color=ACCENT, fontsize=8, va='center')
    ax.axvline(4.5,  color=GREEN, lw=1.5, ls=':', alpha=0.5)
    ax.text(4.7, -0.5, 'Sustained\nlimit (no suit)', color=GREEN, fontsize=8, va='center')

    for bar, val, lab in zip(bars, vals, labs):
        ax.text(val+0.3, bar.get_y()+bar.get_height()/2,
                f'{val:.1f} g  ({lab})', color=TEXTGREY, fontsize=8, va='center')

    ax.set_xlabel('Load Factor $n = a/g$', color=TEXTGREY, fontsize=10)
    ax.set_title('Figure 13: G-Force Comparison — ODM vs Real Human Limits\n'
                 r'[ASSUMPTION] values derived from $n = v^2/(rg) + 1$ at swing bottom',
                 color=WHITE, fontsize=10, pad=8)
    ax.set_xlim(0, 55)
    ax.tick_params(colors=TEXTGREY)

    save_fig(fig, 'fig13_gforce.png', dpi=300)

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 10 — Trajectory optimization (conceptual)
# ═══════════════════════════════════════════════════════════════════════════
def diagram_optimization():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), facecolor=BG)

    # Left: three candidate trajectories
    ax1 = axes[0]
    style_ax(ax1, bg=DARK)
    ax1.set_xlim(0, 20)
    ax1.set_ylim(0, 15)
    ax1.set_aspect('equal')

    # Start and end
    sx, sy = 1, 2
    ex, ey = 18, 2

    # Obstacles (rectangles = buildings)
    obs = [(7, 0, 3, 12), (13, 0, 2, 8)]
    for (ox, oy, ow, oh) in obs:
        rect = patches.Rectangle((ox, oy), ow, oh, linewidth=1,
                                  edgecolor=GREY, facecolor='#1A1A2A', zorder=2)
        ax1.add_patch(rect)
        ax1.text(ox+ow/2, oh+0.4, 'bldg', color=GREY, fontsize=7, ha='center')

    # Path A (direct / impossible)
    ax1.annotate('', xy=(ex, ey), xytext=(sx, sy),
                arrowprops=dict(arrowstyle='->', color=ACCENT3, lw=1.5, ls='--'))
    ax1.text(10, 1, 'Blocked', color=ACCENT3, fontsize=8, ha='center')

    # Path B (high arc — longer but safe)
    t = np.linspace(0, np.pi, 100)
    xb = sx + (ex-sx)*t/np.pi
    yb = sy + 10*np.sin(t)
    ax1.plot(xb, yb, color=ACCENT2, lw=2, label='Path B (safe arc)')

    # Path C (optimized — minimum energy swing)
    xc = np.array([sx, 6, 9, 12, 15.5, ex])
    yc = np.array([sy, 10, 13, 12, 8, ey])
    from numpy.polynomial import polynomial as P
    coeffs = np.polyfit([0, 1, 2, 3, 4, 5], yc, 4)
    xfine = np.linspace(0, 5, 200)
    yfine = np.polyval(coeffs, xfine)
    xfine_real = np.interp(xfine, [0, 5], [sx, ex])
    ax1.plot(xfine_real, yfine, color=GREEN, lw=2.5, label='Path C (optimised)')

    # Anchors for path C
    anc = [(8, 14), (15, 10)]
    for (axp, ayp) in anc:
        ax1.plot(axp, ayp, '^', color=ACCENT, markersize=10)
        ax1.plot([axp, axp], [0, ayp], ':', color=ACCENT, lw=0.8, alpha=0.5)

    ax1.plot(sx, sy, 'o', color=GREEN, markersize=10, zorder=5)
    ax1.plot(ex, ey, 's', color=ACCENT, markersize=10, zorder=5)
    ax1.text(sx-0.5, sy+0.4, 'Start', color=GREEN, fontsize=8)
    ax1.text(ex+0.2, ey+0.4, 'Target', color=ACCENT, fontsize=8)

    ax1.legend(fontsize=8, facecolor=PANEL, edgecolor=GREY, labelcolor=WHITE, loc='upper right')
    ax1.set_title('Trajectory Options in Urban Environment', color=WHITE, fontsize=10)
    ax1.set_xlabel('x (m)', color=TEXTGREY, fontsize=9)
    ax1.set_ylabel('z (m)', color=TEXTGREY, fontsize=9)

    # Right: cost functional visualization
    ax2 = axes[1]
    style_ax(ax2, bg=DARK, xlabel='Time $t$ (s)', ylabel='Power $P(t)$ (W)')
    t_sim = np.linspace(0, 4, 200)
    # Path B power (high, constant arc)
    PB = 400 + 150*np.sin(np.pi*t_sim/4) + 30*np.random.randn(200)
    PB = np.maximum(PB, 0)
    # Path C power (optimized)
    PC = 300*np.exp(-0.3*t_sim) + 80 + 20*np.sin(2*t_sim)
    PC = np.maximum(PC, 0)

    ax2.plot(t_sim, PB, color=ACCENT2, lw=2, label=f'Path B  (J = {np.trapezoid(PB,t_sim):.0f} J)')
    ax2.plot(t_sim, PC, color=GREEN,   lw=2, label=f'Path C  (J = {np.trapezoid(PC,t_sim):.0f} J)')
    ax2.fill_between(t_sim, PB, alpha=0.15, color=ACCENT2)
    ax2.fill_between(t_sim, PC, alpha=0.15, color=GREEN)
    ax2.legend(fontsize=8, facecolor=PANEL, edgecolor=GREY, labelcolor=WHITE)
    ax2.set_title(r'Cost Functional $J = \int P(t)\,dt$', color=WHITE, fontsize=10)

    fig.suptitle('Figure 14: Trajectory Optimisation\n'
                 r'$\min J = \int_0^{t_f} P(t)\,dt$ subject to cable and body constraints',
                 color=WHITE, fontsize=11, y=1.01)
    fig.tight_layout()
    save_fig(fig, 'fig14_optimization.png', dpi=300)

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 11 — Energy and momentum (impulse)
# ═══════════════════════════════════════════════════════════════════════════
def diagram_energy_momentum():
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), facecolor=BG)

    # Left: KE vs speed
    ax1 = axes[0]
    style_ax(ax1, bg=DARK, xlabel='Speed $v$ (m/s)', ylabel='Kinetic Energy $K$ (kJ)')
    v = np.linspace(0, 40, 400)
    m = 80   # kg
    K = 0.5 * m * v**2 / 1000   # kJ
    ax1.plot(v, K, color=ACCENT2, lw=2.5)
    for speed, label in [(10, '10 m/s'), (20, '20 m/s'), (30, '30 m/s')]:
        Kval = 0.5*m*speed**2/1000
        ax1.scatter([speed], [Kval], color=ACCENT, s=60, zorder=5)
        ax1.text(speed+0.5, Kval+0.2, f'{Kval:.1f} kJ\n({label})', color=ACCENT, fontsize=8)
    ax1.set_title(r'Kinetic Energy $K = \frac{1}{2}mv^2$' + '\n[ASSUMPTION: $m=80$ kg]',
                  color=WHITE, fontsize=10)

    # Right: Impulse / redirection
    ax2 = axes[1]
    style_ax(ax2, bg=DARK, xlabel=r'Time $\Delta t$ (s)', ylabel='Peak Force (kN)')

    dt = np.linspace(0.05, 2.0, 400)
    dp_magnitudes = [m*15, m*20, m*25]   # Δp = m Δv
    labs = ['$\\Delta v = 15$ m/s', '$\\Delta v = 20$ m/s', '$\\Delta v = 25$ m/s']
    cols2 = [GREEN, ACCENT2, ACCENT3]
    for dp, lab, col in zip(dp_magnitudes, labs, cols2):
        F_peak = dp / dt / 1000   # kN
        ax2.plot(dt, F_peak, color=col, lw=2, label=lab)

    ax2.axhline(9.81*m/1000, color=ACCENT, lw=1, ls='--', alpha=0.6)
    ax2.text(0.05, 9.81*m/1000+0.2, 'Body weight', color=ACCENT, fontsize=8)
    ax2.set_ylim(0, 60)
    ax2.legend(fontsize=8, facecolor=PANEL, edgecolor=GREY, labelcolor=WHITE)
    ax2.set_title(r'Impulse: $F_{avg} = \Delta p / \Delta t$' + '\n[ASSUMPTION: $m=80$ kg]',
                  color=WHITE, fontsize=10)

    fig.suptitle('Figure 9: Energy and Momentum\n'
                 r'$K = \frac{1}{2}mv^2$,  $\mathbf{p} = m\mathbf{v}$,  $\mathbf{F} = d\mathbf{p}/dt$',
                 color=WHITE, fontsize=11, y=1.01)
    fig.tight_layout()
    save_fig(fig, 'fig09_energy_momentum.png', dpi=300)

# ═══════════════════════════════════════════════════════════════════════════
# DIAGRAM 12 — ODM gear schematic (component labels)
# ═══════════════════════════════════════════════════════════════════════════
def diagram_odm_schematic():
    fig, ax = plt.subplots(figsize=(8, 7), facecolor=BG)
    style_ax(ax, bg=DARK)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis('off')

    # Body silhouette (simplified)
    body_x = [4.5, 5.5, 5.5, 6.2, 6.0, 5.5, 5.3, 4.7, 4.5, 3.8, 4.0, 4.5, 4.5]
    body_y = [9.0, 9.0, 7.5, 7.0, 6.5, 6.0, 5.0, 5.0, 6.0, 6.5, 7.0, 7.5, 9.0]
    ax.fill(body_x, body_y, color='#2A2F45', edgecolor=ACCENT2, lw=1.5, zorder=3)

    # Head
    head = Circle((5, 9.5), 0.55, color='#2A2F45', edgecolor=ACCENT2, lw=1.5, zorder=3)
    ax.add_patch(head)

    # Gas canisters (hips)
    for cx, cy in [(3.4, 6.2), (6.6, 6.2)]:
        rect = patches.Rectangle((cx-0.4, cy-0.8), 0.8, 1.6, linewidth=1.5,
                                  edgecolor=ACCENT3, facecolor='#1A0808', zorder=4)
        ax.add_patch(rect)

    # Wire reel housings (sides)
    for cx, cy in [(2.8, 5.5), (7.2, 5.5)]:
        rect = patches.Rectangle((cx-0.5, cy-0.5), 1.0, 1.0, linewidth=1.5,
                                  edgecolor=ACCENT, facecolor='#1A1500', zorder=4)
        ax.add_patch(rect)

    # Cables shooting out
    ax.annotate('', xy=(1.0, 8.5), xytext=(2.8, 5.5),
                arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2))
    ax.annotate('', xy=(9.2, 8.5), xytext=(7.2, 5.5),
                arrowprops=dict(arrowstyle='->', color=ACCENT, lw=2))

    # Blades (lower)
    for bx, by in [(3.2, 4.5), (6.8, 4.5)]:
        rect = patches.Rectangle((bx-0.15, by-0.6), 0.3, 1.2, linewidth=1,
                                  edgecolor=WHITE, facecolor='#333', angle=10, zorder=4)
        ax.add_patch(rect)

    # Harness lines
    for (x1, y1, x2, y2) in [
        (4.5, 7.5, 3.4, 6.2), (5.5, 7.5, 6.6, 6.2),
        (4.5, 7.5, 3.4, 5.5), (5.5, 7.5, 6.6, 5.5),
        (4.7, 5.0, 4.0, 4.5), (5.3, 5.0, 6.0, 4.5),
    ]:
        ax.plot([x1, x2], [y1, y2], color=TEXTGREY, lw=1, alpha=0.7, zorder=2)

    # Labels with arrows
    label_data = [
        (3.4, 7.0, 1.5, 7.5, 'Body Harness\n(load distribution)'),
        (3.4, 5.5, 1.2, 5.5, 'Wire Reel Housing\n(anchor launcher)'),
        (3.4, 6.2, 1.2, 6.2, 'Gas Canister\n(Iceburst Stone)'),
        (4.7, 4.5, 1.5, 4.2, 'Blade + Hilt\n(trigger controls)'),
        (1.2, 8.5, 0.5, 8.8, 'Steel Wire Cable\n(anchor deployed)'),
        (6.6, 6.2, 8.2, 6.8, 'Gas Canister\n(other side)'),
        (7.2, 5.5, 8.5, 5.5, 'Wire Reel Housing\n(other side)'),
    ]
    for (ox, oy, lx, ly, txt) in label_data:
        ax.annotate(txt, xy=(ox, oy), xytext=(lx, ly),
                   fontsize=7.5, color=TEXTGREY, ha='center', va='center',
                   arrowprops=dict(arrowstyle='->', color=GREY, lw=0.8),
                   bbox=dict(facecolor=PANEL, edgecolor=GREY, alpha=0.8, boxstyle='round,pad=0.2'))

    ax.set_title('Figure 3: ODM Gear — Canonical Component Diagram\n'
                 '[CANON] based on official Attack on Titan descriptions',
                 color=WHITE, fontsize=10, y=0.98)

    save_fig(fig, 'fig03_odm_schematic.png', dpi=300)

# ═══════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print('Generating diagrams...')
    diagram_3d_trajectory()
    diagram_cable_constraint()
    diagram_tangential_normal()
    diagram_free_body()
    diagram_two_anchor()
    diagram_drag_force()
    diagram_rotational()
    diagram_cable_stress()
    diagram_gforce()
    diagram_optimization()
    diagram_energy_momentum()
    diagram_odm_schematic()
    print('\nAll diagrams generated successfully.')

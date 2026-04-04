"""
PWE validation: gap-width sweep confirms r_c = sqrt(mu/pi) * a.

Plane-wave expansion computes TM band gap as a function of r/a for
the square lattice of dielectric rods in air (ε = 8.9). The gap-midgap
ratio is the sole input to the fold-measure prediction.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.special import j1


# --- PWE core ---

def reciprocal_lattice_square(n_max):
    ns = np.arange(-n_max, n_max + 1)
    n1, n2 = np.meshgrid(ns, ns, indexing='ij')
    Gx = 2 * np.pi * n1.ravel()
    Gy = 2 * np.pi * n2.ravel()
    return Gx, Gy


def epsilon_fourier(Gx, Gy, eps_rod, eps_bg, r_over_a):
    """Fourier coefficients of ε(r) for circular rods in square cell."""
    n_G = len(Gx)
    f = np.pi * r_over_a**2  # filling fraction (cell area = a² = 1)
    eps = np.zeros((n_G, n_G), dtype=complex)
    for i in range(n_G):
        for j in range(n_G):
            dG = np.sqrt((Gx[i]-Gx[j])**2 + (Gy[i]-Gy[j])**2)
            if dG < 1e-10:
                eps[i, j] = eps_bg + (eps_rod - eps_bg) * f
            else:
                GR = dG * r_over_a
                eps[i, j] = (eps_rod - eps_bg) * f * 2 * j1(GR) / GR
    return eps


def solve_tm(kx, ky, Gx, Gy, eps_mat, n_bands=6):
    """TM eigenfrequencies: (ωa/2πc) from generalized eigenproblem."""
    kG2 = (kx + Gx)**2 + (ky + Gy)**2
    D = np.diag(kG2)
    eigvals = eigh(D, eps_mat, eigvals_only=True,
                   subset_by_index=[0, n_bands - 1])
    return np.sqrt(np.maximum(eigvals, 0)) / (2 * np.pi)


def band_structure(eps_rod, eps_bg, r_over_a, n_max=7, n_bands=6, n_pts=80):
    """Full TM band structure along Γ-X-M-Γ."""
    Gx, Gy = reciprocal_lattice_square(n_max)
    eps_mat = epsilon_fourier(Gx, Gy, eps_rod, eps_bg, r_over_a)

    # k-path: Γ(0,0) → X(π,0) → M(π,π) → Γ(0,0)
    segs = [
        (np.linspace(0, np.pi, n_pts), np.zeros(n_pts)),
        (np.full(n_pts, np.pi), np.linspace(0, np.pi, n_pts)),
        (np.linspace(np.pi, 0, n_pts), np.linspace(np.pi, 0, n_pts)),
    ]
    kx = np.concatenate([s[0] for s in segs])
    ky = np.concatenate([s[1] for s in segs])

    bands = np.zeros((len(kx), n_bands))
    for i in range(len(kx)):
        bands[i] = solve_tm(kx[i], ky[i], Gx, Gy, eps_mat, n_bands)

    labels = ['Γ', 'X', 'M', 'Γ']
    ticks = [0, n_pts, 2*n_pts, 3*n_pts - 1]
    return bands, labels, ticks


def gap_midgap(eps_rod, eps_bg, r_over_a, n_max=7, n_pts=80):
    """Compute gap-midgap ratio between TM bands 0 and 1."""
    bands, _, _ = band_structure(eps_rod, eps_bg, r_over_a, n_max, 4, n_pts)
    top0 = np.max(bands[:, 0])
    bot1 = np.min(bands[:, 1])
    if bot1 <= top0:
        return 0.0
    return (bot1 - top0) / ((bot1 + top0) / 2)


# --- Main ---

def run():
    EPS_ROD = 8.9
    EPS_BG = 1.0
    N_MAX = 7

    print("PWE gap-width sweep: ε=8.9 rods in air, square lattice, TM")
    print("=" * 60)

    # 1. Band structure at canonical r/a = 0.2
    print("\nBand structure at r/a = 0.2...")
    bands_02, labels, ticks = band_structure(EPS_ROD, EPS_BG, 0.2, N_MAX)
    g02 = gap_midgap(EPS_ROD, EPS_BG, 0.2, N_MAX)
    print(f"  Δω/ω_mid = {g02:.4f}  (Joannopoulos: 0.281)")

    # 2. Sweep r/a
    print("\nSweeping r/a...")
    r_values = np.linspace(0.05, 0.48, 44)
    gaps = np.array([gap_midgap(EPS_ROD, EPS_BG, r, N_MAX, 60)
                     for r in r_values])

    for r, g in zip(r_values, gaps):
        if g > 0:
            print(f"  r/a={r:.3f}  Δω/ω={g:.4f}  "
                  f"r_c={np.sqrt(g/np.pi):.4f} a")

    # 3. Figure
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(
        "PWE Validation: TM gap width → $r_c = \\sqrt{\\mu/\\pi}\\,a$",
        fontsize=13, y=1.02)

    # (a) Band structure
    ax = axes[0]
    for b in range(min(6, bands_02.shape[1])):
        ax.plot(bands_02[:, b], 'k-', lw=0.8)
    top0 = np.max(bands_02[:, 0])
    bot1 = np.min(bands_02[:, 1])
    if bot1 > top0:
        ax.axhspan(top0, bot1, alpha=0.2, color='#8b0000')
        ax.text(len(bands_02)//2, (top0+bot1)/2,
                f"$\\Delta\\omega/\\omega = {g02:.3f}$",
                ha='center', fontsize=9, color='#8b0000')
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels)
    ax.set_ylabel('$\\omega a / 2\\pi c$')
    ax.set_title('(a) TM band structure, $r/a = 0.2$')
    ax.set_xlim(0, len(bands_02)-1)
    ax.set_ylim(0, 0.8)

    # (b) Gap-midgap vs r/a
    ax = axes[1]
    ax.plot(r_values, gaps, 'k-', lw=2)
    ax.axhline(0, color='gray', ls=':', lw=0.5)
    ax.plot(0.2, g02, 'o', ms=8, color='#8b0000', zorder=5,
            label=f'$r/a = 0.2$: $\\Delta\\omega/\\omega = {g02:.3f}$')
    ax.set_xlabel('$r / a$')
    ax.set_ylabel('$\\Delta\\omega / \\omega_{\\rm mid}$')
    ax.set_title('(b) TM gap width vs rod radius')
    ax.legend(fontsize=8)
    ax.set_xlim(0.05, 0.48)

    # (c) Predicted r_c from gap width
    ax = axes[2]
    mask = gaps > 0.001
    r_c_pred = np.sqrt(gaps / np.pi)
    ax.plot(r_values[mask], r_c_pred[mask], '-', lw=2, color='#8b0000',
            label='$r_c = \\sqrt{\\Delta\\omega/(\\omega\\,\\pi)}\\;a$')
    # Mark canonical point
    rc_02 = np.sqrt(g02 / np.pi)
    ax.plot(0.2, rc_02, 'o', ms=8, color='#8b0000', zorder=5)
    ax.annotate(f'{rc_02:.3f} a', (0.2, rc_02),
                textcoords='offset points', xytext=(8, -12), fontsize=9)
    # Shade the observation range from Pryamikov
    ax.axhspan(0.25, 0.35, alpha=0.15, color='#2a5caa',
               label='Observed reversed flow (Pryamikov)')
    ax.set_xlabel('$r / a$')
    ax.set_ylabel('Reversed-flow radius $r_c / a$')
    ax.set_title('(c) Predicted $r_c$ vs rod radius')
    ax.legend(fontsize=8)
    ax.set_xlim(0.05, 0.48)
    ax.set_ylim(0, 0.45)

    plt.tight_layout()
    plt.savefig("notebooks/pwe_validation.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: notebooks/pwe_validation.png")

    # Summary
    print(f"\nAt r/a = 0.2: gap = {g02:.4f}, predicted r_c = {rc_02:.4f} a")
    print(f"Pryamikov observed extent: 0.25–0.35 a")
    in_range = 0.25 <= rc_02 <= 0.35
    print(f"{'Within' if in_range else 'Outside'} observed range")


if __name__ == "__main__":
    run()

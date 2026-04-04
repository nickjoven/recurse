"""
Pryamikov parameter extraction (arXiv:2601.21704).

K_stat = 1/cos(π Δω/ω_mid)  from fold-measure inversion.
r_c = √(μ/π) · a            reversed-flow fraction as disk in unit cell.

Two geometries:
  A. ε=8.9 rods in air, r/a=0.2, TM  →  r_c = 0.299a  (obs 0.25–0.35a)
  B. ε=13 holes in diel., r/a=0.48, TE  →  r_c = 0.226a  (obs 0.15–0.25a)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# --- Geometry definitions ---

GEOM_A = {
    'name': 'Square lattice, rods in air',
    'label': 'A',
    'lattice': 'square',
    'epsilon_rod': 8.9,         # alumina
    'epsilon_bg': 1.0,          # air
    'r_over_a': 0.2,            # rod radius / lattice constant
    'polarization': 'TM',
    'N_layers': 8,
    'gap_midgap': 0.281,        # Δω/ω_mid from MPB (Joannopoulos ch. 5)
    'r_rev_obs': (0.25, 0.35),  # observed reversed-flow extent / a
}

GEOM_B = {
    'name': 'Triangular lattice, holes in dielectric',
    'label': 'B',
    'lattice': 'triangular',
    'epsilon_rod': 1.0,         # air holes
    'epsilon_bg': 13.0,         # GaAs / high-index dielectric
    'r_over_a': 0.48,           # hole radius / lattice constant
    'polarization': 'TE',
    'N_layers': 8,
    'gap_midgap': 0.186,        # Δω/ω_mid from MPB
    'r_rev_obs': (0.15, 0.25),  # observed reversed-flow extent / a
}


# --- Parameter extraction ---

def extract_parameters(geom):
    """
    Extract Δn, f, Q and the Stribeck coupling K_stat from crystal geometry.

    K_stat is calibrated from the known band gap width:
        μ = arccos(1/K)/π  =  Δω/ω_mid   (fold measure = gap-midgap ratio)
        K_stat = 1/cos(π · Δω/ω_mid)

    The spatial extent of reversed flow within each unit cell:
        r_c = √(μ/π) · a
    treating the reversed-flow region as a disk in the unit cell.
    """
    eps_rod = geom['epsilon_rod']
    eps_bg = geom['epsilon_bg']
    n_rod = np.sqrt(eps_rod)
    n_bg = np.sqrt(eps_bg)
    r_a = geom['r_over_a']
    lattice = geom['lattice']

    delta_n = abs(n_rod - n_bg)

    if lattice == 'square':
        f_element = np.pi * r_a**2
        A_cell = 1.0  # a²
    else:  # triangular
        f_element = (2 * np.pi / np.sqrt(3)) * r_a**2
        A_cell = np.sqrt(3) / 2  # a² √3/2

    # Filling fraction of scatterers
    f = f_element

    # Effective index
    if eps_rod > eps_bg:
        n_eff = np.sqrt(f * eps_rod + (1 - f) * eps_bg)
    else:
        n_eff = np.sqrt((1 - f) * eps_bg + f * eps_rod)

    # Quality factor (band-edge mode in N-layer slab)
    N = geom['N_layers']
    Q = N * n_eff / geom['gap_midgap']

    # K_stat from band gap inversion
    gap = geom['gap_midgap']
    mu = gap  # fold measure = gap-midgap ratio
    K_stat = 1.0 / np.cos(np.pi * mu)

    # Predicted reversed-flow radius (disk approximation in unit cell)
    r_c = np.sqrt(mu / np.pi)  # in units of a

    # For triangular lattice, scale by Wigner-Seitz cell shape
    if lattice == 'triangular':
        r_c *= (A_cell / 1.0)**0.5  # adjust for cell area

    return {
        'delta_n': delta_n,
        'f': f,
        'Q': Q,
        'n_eff': n_eff,
        'n_rod': n_rod,
        'n_bg': n_bg,
        'K_stat': K_stat,
        'mu': mu,
        'r_c': r_c,
        'A_cell': A_cell,
    }


# --- Fold measure ---

def fold_measure(K):
    """μ(K) = arccos(1/K)/π for K > 1, else 0."""
    K = np.asarray(K, dtype=float)
    mu = np.zeros_like(K)
    mask = K > 1.0
    mu[mask] = np.arccos(1.0 / K[mask]) / np.pi
    return mu


def stribeck_K(v, K_stat, K_kin, v_thr):
    """Stribeck coupling K(v)."""
    return K_kin + (K_stat - K_kin) * np.exp(-(np.abs(v) / v_thr)**2)


# --- Main ---

def run():
    print("=" * 72)
    print("PRYAMIKOV PARAMETER EXTRACTION AND r_c COMPARISON")
    print("arXiv:2601.21704, Figs. 3–5")
    print("=" * 72)
    print()
    print("Method: K_stat calibrated from band gap width via")
    print("  μ = Δω/ω_mid  →  K_stat = 1/cos(πμ)")
    print("  r_c = √(μ/π) · a  (reversed-flow fraction as disk in unit cell)")

    results = {}

    for geom in [GEOM_A, GEOM_B]:
        label = geom['label']
        p = extract_parameters(geom)
        obs_min, obs_max = geom['r_rev_obs']
        obs_mid = (obs_min + obs_max) / 2

        print(f"\n{label}: {geom['name']}")
        print(f"  ε={geom['epsilon_rod']}, r/a={geom['r_over_a']}, "
              f"{geom['polarization']}, Δω/ω={geom['gap_midgap']}")
        print(f"  Δn={p['delta_n']:.3f}  f={p['f']:.3f}  "
              f"K={p['K_stat']:.3f}  μ={p['mu']:.3f}")
        print(f"  r_c = {p['r_c']:.3f} a   (obs {obs_min}–{obs_max} a)")
        print()

        results[label] = p

    # ========================================================================
    # FIGURE
    # ========================================================================

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(
        "Predicted vs Observed Reversed Poynting Vector Flow",
        fontsize=13, y=0.99)

    # Panel (a): Bar chart comparison
    ax = axes[0, 0]
    labels_bar = ['Geom A\n(rods in air,\nTM, ε=8.9)',
                  'Geom B\n(holes in diel.,\nTE, ε=13)']
    predicted = [results['A']['r_c'], results['B']['r_c']]
    obs_mids = [(g['r_rev_obs'][0] + g['r_rev_obs'][1])/2
                for g in [GEOM_A, GEOM_B]]
    obs_errs = [(g['r_rev_obs'][1] - g['r_rev_obs'][0])/2
                for g in [GEOM_A, GEOM_B]]

    x = np.arange(2)
    width = 0.35
    bars1 = ax.bar(x - width/2, predicted, width,
                   label='Predicted $r_c = \\sqrt{\\mu/\\pi}\\,a$',
                   color='#8b0000', alpha=0.8)
    bars2 = ax.bar(x + width/2, obs_mids, width, yerr=obs_errs,
                   label='Observed extent',
                   color='#2a5caa', alpha=0.7, capsize=6)
    ax.set_ylabel('Reversed-flow radius  $r_c / a$')
    ax.set_title('(a) Predicted vs Observed')
    ax.set_xticks(x)
    ax.set_xticklabels(labels_bar, fontsize=8)
    ax.legend(fontsize=8)
    # Add value labels
    for bar, val in zip(bars1, predicted):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                f'{val:.3f}', ha='center', va='bottom', fontsize=8)

    # Panel (b): μ vs Δω/ω_mid showing the calibration
    ax = axes[0, 1]
    gap_range = np.linspace(0, 0.5, 200)
    K_range = 1.0 / np.cos(np.pi * gap_range)
    # mask where K is valid (gap < 0.5)
    valid = gap_range < 0.5
    ax.plot(gap_range[valid], gap_range[valid], 'k-', lw=2,
            label='$\\mu = \\Delta\\omega/\\omega_{\\rm mid}$ (identity)')
    rc_range = np.sqrt(gap_range[valid] / np.pi)
    ax2 = ax.twinx()
    ax2.plot(gap_range[valid], rc_range, 'r--', lw=1.5,
             label='$r_c = \\sqrt{\\mu/\\pi}\\,a$')
    for g in [GEOM_A, GEOM_B]:
        p = results[g['label']]
        ax.plot(g['gap_midgap'], p['mu'], 'o', ms=10,
                label=f"Geom {g['label']}")
    ax.set_xlabel('$\\Delta\\omega / \\omega_{\\rm mid}$')
    ax.set_ylabel('Fold measure $\\mu$', color='black')
    ax2.set_ylabel('$r_c / a$', color='red')
    ax.set_title('(b) Calibration: gap width → fold measure → $r_c$')
    ax.legend(fontsize=8, loc='upper left')
    ax2.legend(fontsize=8, loc='lower right')
    ax.set_xlim(0, 0.45)

    # Panel (c): K_stat vs gap-midgap ratio
    ax = axes[1, 0]
    gap_plot = np.linspace(0.01, 0.45, 200)
    K_plot = 1.0 / np.cos(np.pi * gap_plot)
    ax.plot(gap_plot, K_plot, 'k-', lw=2)
    for g in [GEOM_A, GEOM_B]:
        p = results[g['label']]
        ax.plot(g['gap_midgap'], p['K_stat'], 'o', ms=10,
                label=f"Geom {g['label']}: $K = {p['K_stat']:.3f}$")
    ax.set_xlabel('$\\Delta\\omega / \\omega_{\\rm mid}$')
    ax.set_ylabel('$K_{\\rm stat}$')
    ax.set_title('(c) $K_{\\rm stat} = 1/\\cos(\\pi\\,\\Delta\\omega/\\omega_{\\rm mid})$')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 0.45)
    ax.set_ylim(1, 4)
    ax.axhline(1, color='gray', ls=':', alpha=0.5)

    # Panel (d): Parameter table
    ax = axes[1, 1]
    ax.axis('off')
    table_data = []
    for g in [GEOM_A, GEOM_B]:
        p = results[g['label']]
        obs_min, obs_max = g['r_rev_obs']
        table_data.append([
            g['label'],
            f"ε={g['epsilon_rod']}, r/a={g['r_over_a']}",
            g['polarization'],
            f"{p['delta_n']:.2f}",
            f"{p['f']:.3f}",
            f"{g['gap_midgap']}",
            f"{p['K_stat']:.3f}",
            f"{p['mu']:.3f}",
            f"{p['r_c']:.3f}",
            f"{obs_min}–{obs_max}",
        ])
    col_labels = ['', 'Geometry', 'Pol', 'Δn', 'f',
                  'Δω/ω', 'K', 'μ', 'r_c/a', 'Obs/a']
    table = ax.table(cellText=table_data, colLabels=col_labels,
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.3, 2.0)
    ax.set_title('(d) Extracted Parameters', pad=20)

    plt.tight_layout()
    plt.savefig("notebooks/pryamikov_extraction.png", dpi=150,
                bbox_inches='tight')
    plt.close()
    print(f"\nSaved: notebooks/pryamikov_extraction.png")

    print()


if __name__ == "__main__":
    run()

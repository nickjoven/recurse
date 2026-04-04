"""
2D FDTD: Poynting vector field in a finite photonic crystal slab.

TM polarization, 8-layer slab of ε=8.9 rods in air (square lattice,
r/a = 0.2). Plane wave incident at band-edge frequency. Measures the
time-averaged reversed-flow area and compares to r_c = sqrt(mu/pi) * a.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# --- Grid parameters ---
A = 40          # grid points per lattice constant
N_LAYERS = 8    # crystal layers in x
PML = 30        # PML thickness (grid points)
NY = A          # one period in y (periodic BC)
BUFFER = 3 * A  # buffer on each side of crystal

NX = 2 * PML + 2 * BUFFER + N_LAYERS * A
DX = 1.0 / A    # grid spacing in units of a
DT = DX / (2.0)  # Courant factor = 0.5 (stable for 2D)
C = 1.0          # speed of light

# Crystal
EPS_ROD = 8.9
R_OVER_A = 0.2
R_GRID = R_OVER_A * A  # rod radius in grid points

# Crystal slab x-extent
X_START = PML + BUFFER  # first rod center
X_END = X_START + N_LAYERS * A


def build_epsilon(nx, ny):
    """Build epsilon grid for the photonic crystal slab."""
    eps = np.ones((nx, ny))
    for layer in range(N_LAYERS):
        cx = X_START + layer * A + A // 2  # rod center x
        cy = ny // 2                        # rod center y (one per cell)
        for ix in range(nx):
            for iy in range(ny):
                dx = ix - cx
                # periodic in y
                dy = min(abs(iy - cy), ny - abs(iy - cy))
                if dx**2 + dy**2 < R_GRID**2:
                    eps[ix, iy] = EPS_ROD
    return eps


def build_pml_sigma(nx, pml_width):
    """PML conductivity profile (polynomial grading)."""
    sigma = np.zeros(nx)
    sigma_max = 3.0  # tuned for absorption
    for i in range(pml_width):
        grade = ((pml_width - i) / pml_width) ** 3
        sigma[i] = sigma_max * grade
        sigma[nx - 1 - i] = sigma_max * grade
    return sigma


def find_band_edge_freq():
    """Get band-edge frequency from PWE (import from 04 or recompute)."""
    # From PWE computation: gap between 0.3224 and 0.4426 (ωa/2πc)
    # Band edge (top of band 0) ≈ 0.322
    # Use frequency just below gap
    return 0.322


def run_fdtd(freq=None, label=""):
    if freq is None:
        freq = find_band_edge_freq()
    print(f"\n{'='*50}")
    print(f"FDTD run: ωa/2πc = {freq:.4f} {label}")
    print(f"{'='*50}")
    print("Building grid...")
    eps = build_epsilon(NX, NY)
    sigma_x = build_pml_sigma(NX, PML)

    # PML auxiliary fields
    sigma_2d = sigma_x[:, np.newaxis] * np.ones((1, NY))

    # Fields (TM: E_z, H_x, H_y)
    Ez = np.zeros((NX, NY))
    Hx = np.zeros((NX, NY))
    Hy = np.zeros((NX, NY))

    # PML split fields
    Ez_x = np.zeros((NX, NY))
    Ez_y = np.zeros((NX, NY))

    # Source: CW plane wave at band-edge frequency
    omega = 2 * np.pi * freq
    src_x = PML + A  # source plane (before crystal)
    print(f"Frequency: ωa/2πc = {freq:.4f}")
    print(f"Grid: {NX} x {NY}, dx = {DX:.4f} a")
    print(f"Crystal: x = [{X_START*DX:.1f}, {X_END*DX:.1f}] a")

    # Time-averaged Poynting vector accumulators
    N_STEPS = 3000
    N_AVG_START = 2000  # start averaging after transients
    Sx_avg = np.zeros((NX, NY))
    Sy_avg = np.zeros((NX, NY))
    n_avg = 0

    print(f"Running {N_STEPS} time steps...")
    for n in range(N_STEPS):
        t = n * DT

        # --- Update H (half step) ---
        # dE_z/dy
        dEz_dy = np.roll(Ez, -1, axis=1) - Ez
        # dE_z/dx
        dEz_dx = np.roll(Ez, -1, axis=0) - Ez

        Hx -= (DT / DX) * dEz_dy
        Hy += (DT / DX) * dEz_dx

        # --- Update E ---
        dHy_dx = Hy - np.roll(Hy, 1, axis=0)
        dHx_dy = Hx - np.roll(Hx, 1, axis=1)
        curl_H = (dHy_dx - dHx_dy) / DX

        # PML: split-field update
        Ez_x = (1 - sigma_2d * DT) * Ez_x + (DT / eps) * dHy_dx / DX
        Ez_y = (1 - sigma_2d * DT) * Ez_y - (DT / eps) * dHx_dy / DX
        Ez = Ez_x + Ez_y

        # Add source (soft source: additive plane wave)
        src_val = np.sin(omega * t) * (1 - np.exp(-(t / (20 * DT))**2))
        Ez[src_x, :] += src_val

        # Accumulate Poynting vector after transients
        if n >= N_AVG_START:
            # S_x = E_z * H_y (instantaneous, accumulate for time avg)
            Sx_avg += Ez * Hy
            # S_y = -E_z * H_x
            Sy_avg -= Ez * Hx
            n_avg += 1

        if n % 500 == 0:
            print(f"  step {n}/{N_STEPS}, max|Ez| = {np.max(np.abs(Ez)):.4f}")

    Sx_avg /= n_avg
    Sy_avg /= n_avg

    # --- Measure reversed flow in crystal region ---
    # Extract Poynting vector inside the crystal
    x_lo, x_hi = X_START, X_END
    Sx_crystal = Sx_avg[x_lo:x_hi, :]
    Sy_crystal = Sy_avg[x_lo:x_hi, :]

    # Forward direction is +x (incident wave direction)
    total_cells = Sx_crystal.size
    reversed_cells = np.sum(Sx_crystal < 0)
    frac_reversed = reversed_cells / total_cells
    r_rev = np.sqrt(frac_reversed / np.pi)

    print(f"\n{'='*50}")
    print(f"RESULTS (inside crystal, {N_LAYERS} layers)")
    print(f"{'='*50}")
    print(f"Reversed-flow fraction: {frac_reversed:.4f}")
    print(f"Effective radius: r_rev = {r_rev:.4f} a")
    print(f"Predicted:        r_c  = {np.sqrt(0.314/np.pi):.4f} a")
    print(f"Observed range:         0.25–0.35 a")

    # --- Figure ---
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.5))
    fig.suptitle(
        "FDTD: Poynting Vector in 8-Layer Photonic Crystal Slab "
        "($\\varepsilon = 8.9$, $r/a = 0.2$, TM)",
        fontsize=12, y=1.02)

    # (a) Sx in the crystal (2 unit cells)
    ax = axes[0]
    x_show = slice(X_START + 3*A, X_START + 5*A)
    Sx_show = Sx_avg[x_show, :]
    x_coords = np.arange(Sx_show.shape[0]) * DX
    y_coords = np.arange(NY) * DX
    vmax = np.percentile(np.abs(Sx_show), 95)
    if vmax > 0:
        im = ax.pcolormesh(x_coords, y_coords, Sx_show.T,
                           cmap='RdBu_r', vmin=-vmax, vmax=vmax,
                           shading='auto')
        plt.colorbar(im, ax=ax, shrink=0.8, label='$S_x$')
    # Draw rod outlines
    for layer in [3, 4]:
        cx = (layer * A + A//2) * DX
        cy = 0.5  # in units of a
        circle = plt.Circle((cx, cy), R_OVER_A, fill=False,
                            ec='black', lw=0.8, ls='--')
        ax.add_patch(circle)
    ax.set_xlabel('$x / a$')
    ax.set_ylabel('$y / a$')
    ax.set_title('(a) $S_x$ (red = forward, blue = reversed)')
    ax.set_aspect('equal')

    # (b) Full slab Sx cross-section
    ax = axes[1]
    x_full = np.arange(NX) * DX
    Sx_line = np.mean(Sx_avg, axis=1)
    ax.plot(x_full, Sx_line, 'k-', lw=0.8)
    ax.axvspan(X_START*DX, X_END*DX, alpha=0.1, color='gray',
               label='Crystal slab')
    ax.axvline(src_x*DX, color='green', ls=':', label='Source')
    ax.set_xlabel('$x / a$')
    ax.set_ylabel('$\\langle S_x \\rangle_y$')
    ax.set_title('(b) $y$-averaged Poynting flux')
    ax.legend(fontsize=8)
    ax.set_xlim(0, NX*DX)

    # (c) Comparison bar chart
    ax = axes[2]
    labels = ['FDTD\nreversed', 'Fold\nprediction', 'Pryamikov\nobserved']
    values = [r_rev, np.sqrt(0.314/np.pi), 0.30]
    errs = [0, 0, 0.05]
    colors = ['#2a5caa', '#8b0000', '#444444']
    bars = ax.bar(labels, values, yerr=errs, color=colors, alpha=0.8,
                  capsize=5, width=0.6)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{val:.3f}', ha='center', va='bottom', fontsize=9)
    ax.set_ylabel('$r_c / a$')
    ax.set_title('(c) Reversed-flow radius')
    ax.set_ylim(0, 0.5)

    plt.tight_layout()
    plt.savefig("notebooks/fdtd_poynting.png", dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: notebooks/fdtd_poynting.png")
    return frac_reversed, r_rev


def run_frequency_scan():
    """Run FDTD at several frequencies to show convergence."""
    freqs = [0.25, 0.28, 0.30, 0.315, 0.322]
    results = []

    for f in freqs:
        label = "(band edge)" if f == 0.322 else "(mid-band)" if f == 0.28 else ""
        r = run_fdtd(freq=f, label=label)
        if r is not None:
            results.append((f, r))

    if results:
        print(f"\n{'='*50}")
        print("FREQUENCY SCAN SUMMARY")
        print(f"{'='*50}")
        print(f"{'freq':>8}  {'frac_rev':>10}  {'r_rev':>8}")
        for f, (frac, r_rev) in results:
            print(f"  {f:.3f}    {frac:.4f}     {r_rev:.4f}")
        print(f"  Prediction (μ=0.314):   {np.sqrt(0.314/np.pi):.4f}")
        print(f"  Observed:               0.25–0.35")


if __name__ == "__main__":
    run_fdtd(freq=0.322, label="(band edge)")

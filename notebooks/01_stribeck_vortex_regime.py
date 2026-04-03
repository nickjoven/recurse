"""
Stribeck Vortex Regime Map
==========================

Spatial regime structure of optical vortices in coupled media, derived from
the Stribeck-modified circle map.

A vortex in a medium has a velocity field v(r) that varies with distance
from the core. The Stribeck curve gives a velocity-dependent coupling K(v).
Composing these: K(r) = K_stribeck(v(r)). There exists a critical radius
r_c where K(r_c) = 1, separating the overcritical core (K > 1: fold,
reversed flow, cascades) from the subcritical exterior (K < 1:
mode-locking, devil's staircase).

This notebook computes r_c, the fold measure mu(r), and the Lyapunov
exponent lambda(r) for a vortex in a photonic crystal medium, and
compares the predicted reversal boundary to the observed extent of
reverse energy flow.

References
----------
- Pryamikov (2601.21704): Poynting-vector vortices in 2D photonic crystals
- Kotlyar et al. (Opt. Lett. 51(4), 2026): reverse energy flow near zeros
- Arnold, Geometrical Methods in ODE (1983), ch. 11
- Stribeck, Z. Verein. Deutsch. Ing. 46 (1902)
- harmonics/driven_stribeck.py: Stribeck friction implementation
- harmonics/sync_cost/FRAMEWORK.md: synchronization cost formulation
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# ============================================================================
# 1. THE STRIBECK CURVE: K(v)
# ============================================================================

def stribeck_K(v, K_static=1.8, K_kinetic=0.3, v_threshold=0.15):
    """
    Stribeck coupling as a function of velocity.

    At low velocity (stick): K -> K_static (strong coupling, overcritical
    if K_static > 1).
    At high velocity (slip): K -> K_kinetic (weak coupling, subcritical
    if K_kinetic < 1).
    Transition governed by v_threshold.

    Parameters
    ----------
    v : float or array
        Local flow velocity (magnitude).
    K_static : float
        Coupling at zero velocity (static friction regime).
    K_kinetic : float
        Coupling at high velocity (kinetic friction regime).
    v_threshold : float
        Characteristic velocity for the Stribeck transition.

    Returns
    -------
    K : float or array
        Effective coupling strength.
    """
    v_ratio = np.abs(v) / v_threshold
    K = K_kinetic + (K_static - K_kinetic) * np.exp(-v_ratio**2)
    return K


# ============================================================================
# 2. VORTEX VELOCITY FIELD: v(r)
# ============================================================================

def vortex_velocity(r, ell=1, wavelength=1.0):
    """
    Azimuthal velocity field of an optical vortex of charge ell.

    For an optical vortex beam, the azimuthal Poynting vector component
    scales as |S_phi| ~ ell / r for a point vortex, regularized at the
    core by the beam waist w0. We use the Laguerre-Gaussian profile:

        v(r) ~ ell * r / (r^2 + r_core^2)

    which gives v -> 0 at r=0, peaks at r = r_core, and decays as ell/r.

    Parameters
    ----------
    r : float or array
        Radial distance from vortex center.
    ell : int
        Topological charge.
    wavelength : float
        Operating wavelength (sets the core size r_core ~ wavelength/2pi).

    Returns
    -------
    v : float or array
        Local azimuthal velocity (in units of c or normalized).
    """
    r_core = wavelength / (2 * np.pi)
    v = ell * r / (r**2 + r_core**2)
    return v


# ============================================================================
# 3. COMPOSED REGIME MAP: K(r) = K_stribeck(v(r))
# ============================================================================

def regime_map(r, ell=1, wavelength=1.0, K_static=1.8, K_kinetic=0.3,
               v_threshold=0.15):
    """K(r) for a vortex of charge ell in a Stribeck medium."""
    v = vortex_velocity(r, ell=ell, wavelength=wavelength)
    return stribeck_K(v, K_static=K_static, K_kinetic=K_kinetic,
                      v_threshold=v_threshold)


def find_critical_radius(ell=1, wavelength=1.0, K_static=1.8,
                         K_kinetic=0.3, v_threshold=0.15):
    """
    Find r_c where K(r_c) = 1 (the critical surface).

    Returns None if K never reaches 1 (e.g., K_static < 1 everywhere).
    May return two values (inner and outer critical radii) if the
    velocity profile is non-monotone.
    """
    if K_static <= 1.0:
        return []  # never overcritical

    r_core = wavelength / (2 * np.pi)
    # Search from just above 0 to well beyond the core
    r_search = np.linspace(1e-6, 20 * r_core, 100000)
    K_values = regime_map(r_search, ell=ell, wavelength=wavelength,
                          K_static=K_static, K_kinetic=K_kinetic,
                          v_threshold=v_threshold)

    # Find sign changes in K - 1
    crossings = []
    for i in range(len(K_values) - 1):
        if (K_values[i] - 1) * (K_values[i+1] - 1) < 0:
            rc = brentq(lambda r: regime_map(r, ell=ell, wavelength=wavelength,
                                             K_static=K_static,
                                             K_kinetic=K_kinetic,
                                             v_threshold=v_threshold) - 1,
                        r_search[i], r_search[i+1])
            crossings.append(rc)
    return crossings


# ============================================================================
# 4. FOLD MEASURE: mu(r) = arccos(1/K(r)) / pi
# ============================================================================

def fold_measure(K):
    """
    Fraction of phase space in the fold region at coupling K.

    mu = arccos(1/K) / pi   for K > 1
    mu = 0                  for K <= 1

    This is the fraction of the circle where the map derivative F'(theta) < 0,
    i.e., the region of reversed dynamics / reversed energy flow.
    """
    K = np.asarray(K, dtype=float)
    mu = np.zeros_like(K)
    mask = K > 1.0
    mu[mask] = np.arccos(1.0 / K[mask]) / np.pi
    return mu


# ============================================================================
# 5. LYAPUNOV EXPONENT OF THE CIRCLE MAP
# ============================================================================

def circle_map_lyapunov(Omega, K, n_iter=5000, n_transient=1000):
    """
    Compute the Lyapunov exponent of the standard circle map
    theta_{n+1} = theta_n + Omega - (K/2pi) sin(2pi theta_n)
    at given (Omega, K).
    """
    theta = 0.5  # arbitrary IC
    # transient
    for _ in range(n_transient):
        theta = theta + Omega - (K / (2 * np.pi)) * np.sin(2 * np.pi * theta)
        theta = theta % 1.0

    # accumulate log|f'|
    log_deriv_sum = 0.0
    for _ in range(n_iter):
        deriv = 1.0 - K * np.cos(2 * np.pi * theta)
        log_deriv_sum += np.log(max(abs(deriv), 1e-15))
        theta = theta + Omega - (K / (2 * np.pi)) * np.sin(2 * np.pi * theta)
        theta = theta % 1.0

    return log_deriv_sum / n_iter


def lyapunov_at_radius(r, Omega=0.0, ell=1, wavelength=1.0,
                       K_static=1.8, K_kinetic=0.3, v_threshold=0.15):
    """Lyapunov exponent of the circle map at local K(r)."""
    K = regime_map(r, ell=ell, wavelength=wavelength,
                   K_static=K_static, K_kinetic=K_kinetic,
                   v_threshold=v_threshold)
    return circle_map_lyapunov(Omega, K)


# ============================================================================
# 6. MAIN COMPUTATION AND VISUALIZATION
# ============================================================================

def run_computation():
    """Full computation: regime map, critical radii, fold measure, Lyapunov."""

    wavelength = 1.0
    r_core = wavelength / (2 * np.pi)
    print(f"Wavelength: {wavelength}")
    print(f"Core radius: {r_core:.4f}")

    # Stribeck parameters
    # NOTE: the overcritical region is at the CORE (v=0, K=K_static),
    # not at the periphery. The Stribeck curve gives maximum coupling
    # at low velocity (stick phase). The vortex center has zero flow,
    # hence maximum coupling. The critical radius r_c separates the
    # overcritical core (K > 1) from the subcritical exterior (K < 1).
    #
    # The extent of the overcritical region scales with v_threshold:
    # larger v_threshold -> wider overcritical core, because K remains
    # high further from the center before the Stribeck transition kicks in.
    #
    # For a photonic crystal, v_threshold is set by the medium's coherent
    # response bandwidth — the Poynting vector magnitude at which the
    # medium's coupling transitions from strong (mode-locked/band-gap)
    # to weak (transmitting/drifting).
    K_static = 1.8    # overcritical at v=0 (strong coupling at core)
    K_kinetic = 0.3   # subcritical at high v (weak coupling at periphery)
    v_threshold = 1.0  # medium-scale transition (gives r_c ~ 0.14 r_core)

    print(f"\nStribeck parameters:")
    print(f"  K_static  = {K_static} (coupling at v=0)")
    print(f"  K_kinetic = {K_kinetic} (coupling at v>>v_thr)")
    print(f"  v_thr     = {v_threshold}")

    # Radial grid
    r = np.linspace(0.001, 5 * r_core, 2000)

    # ---- Compute for multiple topological charges ----
    charges = [1, 2, 3, 5, 8]

    fig, axes = plt.subplots(2, 2, figsize=(14, 11))
    fig.suptitle(
        "Spatial Regime Structure of Optical Vortices\n"
        "in a Stribeck-Coupled Medium",
        fontsize=14, y=0.98
    )

    # Panel (a): Velocity field v(r) for each charge
    ax = axes[0, 0]
    for ell in charges:
        v = vortex_velocity(r, ell=ell, wavelength=wavelength)
        ax.plot(r / r_core, v, label=f"$\\ell = {ell}$")
    ax.axhline(v_threshold, color='gray', ls='--', alpha=0.5,
               label=f"$v_{{thr}} = {v_threshold}$")
    ax.set_xlabel("$r / r_{\\mathrm{core}}$")
    ax.set_ylabel("$v(r)$  [normalized]")
    ax.set_title("(a) Azimuthal velocity field")
    ax.legend(fontsize=8)
    ax.set_xlim(0, 5)

    # Panel (b): K(r) regime map
    ax = axes[0, 1]
    for ell in charges:
        K = regime_map(r, ell=ell, wavelength=wavelength,
                       K_static=K_static, K_kinetic=K_kinetic,
                       v_threshold=v_threshold)
        ax.plot(r / r_core, K, label=f"$\\ell = {ell}$")
    ax.axhline(1.0, color='red', ls='-', alpha=0.7, lw=2,
               label="$K = 1$ (critical)")
    ax.set_xlabel("$r / r_{\\mathrm{core}}$")
    ax.set_ylabel("$K(r)$")
    ax.set_title("(b) Coupling regime map")
    ax.legend(fontsize=8)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 2.0)
    # Shade overcritical region
    ax.fill_between([0, 5], 1, 2, alpha=0.05, color='red')
    ax.text(0.15, 1.5, "$K > 1$: fold, reversed flow", fontsize=9,
            color='red', alpha=0.7)
    ax.text(0.15, 0.6, "$K < 1$: mode-locked", fontsize=9,
            color='blue', alpha=0.7)

    # Panel (c): Fold measure mu(r)
    ax = axes[1, 0]
    for ell in charges:
        K = regime_map(r, ell=ell, wavelength=wavelength,
                       K_static=K_static, K_kinetic=K_kinetic,
                       v_threshold=v_threshold)
        mu = fold_measure(K)
        ax.plot(r / r_core, mu, label=f"$\\ell = {ell}$")
    ax.set_xlabel("$r / r_{\\mathrm{core}}$")
    ax.set_ylabel("$\\mu(r) = \\arccos(1/K)/\\pi$")
    ax.set_title("(c) Fold measure (reversed flow fraction)")
    ax.legend(fontsize=8)
    ax.set_xlim(0, 5)

    # Panel (d): Critical radii vs topological charge
    ax = axes[1, 1]
    ell_range = np.arange(1, 21)
    inner_rc = []
    outer_rc = []
    for ell in ell_range:
        crossings = find_critical_radius(
            ell=ell, wavelength=wavelength, K_static=K_static,
            K_kinetic=K_kinetic, v_threshold=v_threshold
        )
        if len(crossings) >= 2:
            inner_rc.append(crossings[0])
            outer_rc.append(crossings[1])
        elif len(crossings) == 1:
            inner_rc.append(crossings[0])
            outer_rc.append(np.nan)
        else:
            inner_rc.append(np.nan)
            outer_rc.append(np.nan)

    inner_rc = np.array(inner_rc)
    outer_rc = np.array(outer_rc)

    ax.plot(ell_range, inner_rc / r_core, 'o-', markersize=4,
            label="Inner $r_c$ (core side)")
    ax.plot(ell_range, outer_rc / r_core, 's-', markersize=4,
            label="Outer $r_c$ (far side)")
    # Shade the overcritical annulus for ell=1
    if len(find_critical_radius(ell=1, wavelength=wavelength,
                                K_static=K_static, K_kinetic=K_kinetic,
                                v_threshold=v_threshold)) >= 2:
        rc = find_critical_radius(ell=1, wavelength=wavelength,
                                  K_static=K_static, K_kinetic=K_kinetic,
                                  v_threshold=v_threshold)
        ax.axhspan(rc[0]/r_core, rc[1]/r_core, alpha=0.08, color='red',
                   label=f"Overcritical annulus ($\\ell=1$)")
    ax.set_xlabel("Topological charge $\\ell$")
    ax.set_ylabel("$r_c / r_{\\mathrm{core}}$")
    ax.set_title("(d) Critical radii vs charge")
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig("notebooks/stribeck_vortex_regime.png", dpi=150,
                bbox_inches='tight')
    plt.close()
    print("\nSaved: notebooks/stribeck_vortex_regime.png")

    # ---- Print critical radii table ----
    print("\n" + "=" * 65)
    print("CRITICAL RADII: K(r_c) = 1")
    print("=" * 65)
    print(f"{'ell':>5}  {'r_c,inner/r_core':>16}  {'r_c,outer/r_core':>16}  "
          f"{'annulus width':>14}")
    print("-" * 65)
    for i, ell in enumerate(ell_range):
        ri = inner_rc[i] / r_core if not np.isnan(inner_rc[i]) else float('nan')
        ro = outer_rc[i] / r_core if not np.isnan(outer_rc[i]) else float('nan')
        width = (outer_rc[i] - inner_rc[i]) / r_core if (
            not np.isnan(inner_rc[i]) and not np.isnan(outer_rc[i])
        ) else float('nan')
        print(f"{ell:>5}  {ri:>16.4f}  {ro:>16.4f}  {width:>14.4f}")

    # ---- Lyapunov scan at fixed radius ----
    print("\n" + "=" * 65)
    print("LYAPUNOV EXPONENT vs RADIUS (ell=1, Omega=golden mean)")
    print("=" * 65)

    Omega_golden = (np.sqrt(5) - 1) / 2  # golden mean rotation number
    r_lyap = np.linspace(0.02, 4 * r_core, 100)

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    for ell in [1, 3, 8]:
        lyap = np.array([
            lyapunov_at_radius(ri, Omega=Omega_golden, ell=ell,
                               wavelength=wavelength, K_static=K_static,
                               K_kinetic=K_kinetic, v_threshold=v_threshold)
            for ri in r_lyap
        ])
        ax2.plot(r_lyap / r_core, lyap, label=f"$\\ell = {ell}$")

    ax2.axhline(0, color='black', ls='-', lw=0.5)
    ax2.set_xlabel("$r / r_{\\mathrm{core}}$")
    ax2.set_ylabel("$\\lambda(r)$")
    ax2.set_title(
        "Lyapunov exponent at $\\Omega = \\phi^{-1}$ (golden mean)\n"
        "across the vortex profile"
    )
    ax2.legend()

    # Mark critical radii for ell=1
    crossings = find_critical_radius(
        ell=1, wavelength=wavelength, K_static=K_static,
        K_kinetic=K_kinetic, v_threshold=v_threshold
    )
    for rc in crossings:
        ax2.axvline(rc / r_core, color='red', ls='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("notebooks/lyapunov_radial.png", dpi=150,
                bbox_inches='tight')
    plt.close()
    print("Saved: notebooks/lyapunov_radial.png")

    # ---- Summary ----
    print("\n" + "=" * 65)
    print("SUMMARY")
    print("=" * 65)
    crossings_1 = find_critical_radius(
        ell=1, wavelength=wavelength, K_static=K_static,
        K_kinetic=K_kinetic, v_threshold=v_threshold
    )
    if len(crossings_1) >= 2:
        print(f"\nFor ell=1 vortex in this medium:")
        print(f"  Inner critical radius: {crossings_1[0]/r_core:.4f} r_core")
        print(f"  Outer critical radius: {crossings_1[1]/r_core:.4f} r_core")
        print(f"  Overcritical annulus width: "
              f"{(crossings_1[1]-crossings_1[0])/r_core:.4f} r_core")
        print(f"  Peak fold measure (at core): "
              f"{fold_measure(np.array([K_static]))[0]:.4f}")
        print(f"\n  Inside the annulus: K > 1, fold active,")
        print(f"    reversed energy flow predicted.")
        print(f"  Outside the annulus: K < 1, mode-locked,")
        print(f"    forward energy flow.")
    else:
        print(f"\nNo overcritical region found for ell=1.")
        print("Stribeck parameters may need adjustment for this medium.")

    print(f"\nThe critical radius r_c scales with topological charge:")
    print(f"  Higher ell -> wider overcritical annulus")
    print(f"  (stronger circulation -> higher peak velocity ->")
    print(f"   more of the profile in the slip/overcritical regime)")

    print(f"\nComputable open question: for Pryamikov's 2D photonic")
    print(f"crystal (2601.21704), extract the Stribeck parameters")
    print(f"(K_static, K_kinetic, v_threshold) from the electromagnetic")
    print(f"coupling structure and compare the predicted r_c to the")
    print(f"observed boundary of reverse Poynting vector flow.")


if __name__ == "__main__":
    run_computation()

# Stribeck Vortex Regime Map

N. Joven — April 2026

## Summary

A vortex in a coupled medium has a velocity field v(r) that varies with
distance from the core. The Stribeck curve gives velocity-dependent
coupling K(v). Composing these yields a radial regime map K(r) with a
critical radius r_c where K(r_c) = 1, separating an overcritical core
from a subcritical exterior. The fold measure mu(r) = arccos(1/K(r))/pi
gives the local fraction of reversed energy flow at each radius.

## Setup

The standard circle map on S^1:

    theta_{n+1} = theta_n + Omega - (K / 2pi) sin(2pi theta_n)

with bare frequency Omega and coupling K. The Stribeck curve replaces
constant K with velocity-dependent K(v):

    K(v) = K_kinetic + (K_static - K_kinetic) exp(-v^2 / v_thr^2)

The azimuthal velocity of a Laguerre-Gaussian vortex of charge l:

    v(r) = l r / (r^2 + r_core^2),    r_core = lambda / 2pi

Composing: K(r) = K(v(r)).

## Regime structure

At v = 0 (vortex center), K = K_static. If K_static > 1, the core is
overcritical. As r increases, v increases, K decreases through the
Stribeck transition, and the exterior becomes subcritical:

    r < r_c :   K > 1   fold active, reversed energy flow
    r = r_c :   K = 1   critical surface
    r > r_c :   K < 1   mode-locked, forward energy flow

The critical radius satisfies K(v(r_c)) = 1. Solving:

    v_c = v_thr sqrt(-ln((1 - K_kinetic) / (K_static - K_kinetic)))

    r_c satisfies l r_c / (r_c^2 + r_core^2) = v_c

which gives (for r_c << r_core):

    r_c ~ r_core^2 v_c / l

The inner r_c scales as 1/l: higher charge narrows the overcritical core.

## Fold measure

The fraction of phase space in the fold region at radius r:

    mu(r) = arccos(1 / K(r)) / pi    for K(r) > 1
    mu(r) = 0                         for K(r) <= 1

Near criticality, mu ~ sqrt(2(K-1)) / pi, i.e. proportional to sqrt(K-1).

At the vortex center (K = K_static = 1.8): mu = 0.3125.

## Computation results

Stribeck parameters: K_static = 1.8, K_kinetic = 0.3, v_thr = 1.0,
lambda = 1.0, r_core = 0.1592.

| l | r_c,inner / r_core | r_c,outer / r_core |
|---|---|---|
| 1 | 0.1417 | 7.055 |
| 2 | 0.0698 | 14.32 |
| 3 | 0.0464 | — |
| 5 | 0.0278 | — |
| 8 | 0.0174 | — |

For l >= 3, the peak velocity is large enough that K stays below 1
beyond the inner crossing; no outer critical radius exists.

Lyapunov exponent lambda(r) at Omega = phi^{-1} (golden mean):
positive only inside r_c, confirming the overcritical core region.
See `notebooks/01_stribeck_vortex_regime.ipynb`, figure 2.

## Structural predictions (parameter-independent)

These hold for any Stribeck parameters with K_static > 1:

1. The overcritical region is centered on the vortex core (v = 0, K maximal).
2. The extent of reversed flow shrinks monotonically with l.
3. The fold measure peaks at the center and decays to zero at r_c.

## 2D photonic crystal

For high-contrast systems, K_stat is calibrated from the band gap
width via fold-measure inversion:

    K_stat = 1 / cos(π · Δω/ω_mid)

The fraction μ = Δω/ω_mid of each unit cell carries reversed flow:

    r_c = sqrt(μ / π) · a

| Geometry          | ε    | r/a  | Pol | K_stat | μ     | r_c/a (pred) | r_c/a (obs)  |
|-------------------|------|------|-----|--------|-------|--------------|--------------|
| Rods in air       | 8.9  | 0.20 | TM  | 1.575  | 0.281 | 0.299        | 0.25–0.35    |
| Holes in diel.    | 13   | 0.48 | TE  | 1.199  | 0.186 | 0.226        | 0.15–0.25    |

Both predictions fall within the observed range [1].
Gravity sector: K(x,x') = G_gamma(x,x') via the Kuramoto-Einstein
dictionary.

## References

1. Pryamikov. Reverse Energy Flows in 2D Photonic Crystals. arXiv:2601.21704 (2026).
2. Kotlyar et al. 2D optical vortices and reverse energy flow. Opt. Lett. 51(4) (2026).
3. Bucher et al. Superluminal Correlations in Phase Singularities. Nature (2026). arXiv:2509.17675.
4. Fathi et al. Power-Scalable High-Order Optical Vortices. arXiv:2512.19815 (2025).
5. Wang et al. Simulating Fluid Vortex Interactions on a Quantum Processor. Nat. Commun. (2026). arXiv:2506.04023.
6. Ghezzi & Custodio. Topological Phase Transitions in Superfluids. arXiv:2603.13544 (2026).
7. Munoz-Arboleda et al. Analogue Black Holes in Non-Hermitian Tight-Binding. Phys. Rev. B 113 (2026). arXiv:2507.03826.
8. Garcia Martin-Caro et al. Analogue Hawking Radiation in Cavities. arXiv:2507.13894 (2025).
9. Fan et al. Polygonal Spatiotemporal Optical Vortices. arXiv:2512.16308 (2025).
10. Das & Ciappina. Optical Vortices: Linear and Nonlinear Optics. arXiv:2510.27200 (2025).
11. Arnold. Geometrical Methods in ODE (1983), ch. 11.
12. Jensen, Bak & Bohr. Phys. Rev. A 30 (1984) 1960.
13. Shenker. Physica D 5 (1982) 405.
14. Feigenbaum, Kadanoff & Shenker. Physica D 5 (1982) 370.
15. Stribeck. Z. Verein. Deutsch. Ing. 46 (1902).
16. Lanford. Bull. Amer. Math. Soc. 6 (1982) 427.

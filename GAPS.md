# Open Questions in the Overcritical Regime

Four open problems in the vortex and analogue-gravity literature where the
K > 1 circle-map grammar may apply. Each gap is sourced from published
papers. Computation results are stated as findings.

---

## 1. Singularity Velocity Divergence Before Annihilation

**The problem:**

Bucher et al. (2509.17675, Nature 2026) directly measured that optical
phase singularities accelerate to unbounded velocities before
vortex-antivortex annihilation in hexagonal boron nitride. The kinematic
explanation — continuity of spacetime paths forces divergence at the
annihilation point — does not predict the **rate** of divergence or explain
why slow group-velocity media amplify the effect.

**Circle-map structure:**

As a vortex-antivortex pair approaches annihilation, mutual coupling
increases (shorter range → stronger interaction). In the circle-map
grammar, this corresponds to K increasing through the overcritical regime.
The Lyapunov exponent at the tongue boundary scales as:

```
    λ ~ (K - K_c)^γ
```

Computation at the golden-mean winding number gives **γ ≈ 1.19 ± 0.08**.
If the effective coupling scales as K_eff ~ 1/r² (from Biot-Savart
point-vortex dynamics) and the approach law is r ~ Δt^α, the velocity
divergence exponent is **β = 2αγ**:

- Dissipative regime (α = 1/2): β ≈ 1.19
- Linear approach (α = 1): β ≈ 2.38

**Open:** The mapping K_eff ~ 1/r² is structural analogy, not derivation.
The identification of singularity velocity with the Lyapunov exponent
requires justification. Measuring β from Bucher et al.'s data would
determine whether the circle-map exponent γ is relevant.

---

## 2. Photonic Band Gap Criterion

**The problem:**

Pryamikov (2601.21704) establishes that Poynting-vector vortices in 2D
photonic crystals determine band gap formation, but provides no predictive
criterion for which vortex configurations produce band gaps.

**Circle-map structure:**

The fold region of the overcritical circle map — where F'(θ) < 0 — is the
region of reversed energy flow. The exact fold measure is:

```
    μ(K) = arccos(1/K) / π
```

This is zero for K ≤ 1 and grows monotonically for K > 1. Near the
critical point:

```
    μ(K) ~ √(2(K-1)) / π       (square root, not linear)
```

The band gap opens when the effective coupling exceeds the critical value
K = 1, and its width is proportional to **√(K-1)**, not (K-1).

**Resolved (1D):** For a 1D Bragg stack, K = 1 + 2(Δn)². This follows
from the Fresnel reflection coefficient |r| = Δn/(2 + Δn) and the
requirement that the fold measure μ = arccos(1/K)/π match the known
Bragg gap width Δω/ω = (4/π)arcsin(|r|) in the small-contrast limit.
The fold measure reproduces the Bragg gap to within 1% for Δn < 0.2.

**Resolved (2D):** For high-contrast systems, K_stat = 1/cos(π · Δω/ω_mid)
by fold-measure inversion. The reversed-flow radius r_c = √(μ/π) · a
falls within the observed range for both of Pryamikov's geometries
(0.299a vs 0.25–0.35a; 0.226a vs 0.15–0.25a).
See `notebooks/03_pryamikov_extraction.py`.

---

## 3. Classical Simulation Cost and Stern-Brocot Depth

**The problem:**

Quantum algorithms for Navier-Stokes show potential exponential speedup
for turbulent flows (arXiv 2303.16550), and Wang et al. (2506.04023)
demonstrate quantum simulation of multi-vortex dynamics. There is no
criterion for which vortex configurations benefit from quantum simulation
versus which are efficiently classical.

**Circle-map structure (confirmed by computation):**

At K = 1.5, the self-similar descent organizes periodic windows within
chaotic bands by Stern-Brocot depth:

- **Window widths decay exponentially:** width ~ 0.458^depth (R² = 0.78).
  Each additional depth level shrinks the mode-locked window by ~2.2×.
- **Tongue width scaling steepens:** q^{-3.2} at K = 1.5, versus the
  universal q^{-2} at K = 1. The self-similar descent makes windows
  narrower faster in the overcritical regime.
- **Dynamical convergence is polynomial:** N ~ q^{1.15} iterates to
  determine the rotation number. The exponential cost is in **parameter
  resolution** (targeting a specific deep-SB-depth rotation number), not
  in time-stepping.
- **Noble numbers are hardest:** confirmed. Irrational rotation numbers
  (infinite SB depth, zero window width) require infinite classical
  precision.

**Resolved:** The quantum advantage is specific to frequency resolution,
not to Hamiltonian simulation. Iterative QPE (Kitaev) resolves SB depth
d in O(d) circuit depth versus O(2^d) classically — an exponential
advantage in depth. Standard QPE requires O(2^d) controlled-U operations
(no advantage over classical). For Hamiltonian simulation of N point
vortices to time T, the gate count is O(N² T polylog(T/ε)) and does not
depend on rotation-number structure. The SB-depth-dependent advantage
applies only to the problem of identifying which mode-locked window a
trajectory occupies.

---

## 4. OAM Multistability and Switching Thresholds

**The problem:**

Experiments on vortex fiber lasers demonstrate switching between OAM
states (e.g., ℓ = 2 and ℓ = 20), and optical bistability in graphene
quantum dot systems is sensitive to the orbital angular momentum of the
coupling vortex beam. No framework predicts which OAM states coexist at
given parameters or what determines switching thresholds.

**Circle-map structure (confirmed by computation):**

At K > 1, Arnold tongue overlap produces multistability with a clean
Stern-Brocot hierarchy:

- Multistability first appears at K ~ 1.2, between Farey-adjacent tongues.
- **All** overlapping pairs are SB-adjacent (tree distance = 1) up to
  K ~ 4.0. Distant pairs require much higher coupling.
- Overlap threshold K_c depends on SB distance: SB-adjacent pairs overlap
  at K ~ 1.5–1.75; SB-distance ≥ 2 requires K > 4.0.

**Open:** The ℓ-to-rotation-number mapping is the critical gap. The 1D
circle map cannot produce coexistence between ℓ = 2 and ℓ = 20 (too
SB-distant). Explaining distant-mode switching requires either coupled
circle maps on a torus (higher-dimensional), a nonlinear compression
of the OAM spectrum, or a fundamentally different identification of
ℓ with the dynamical variable.

---

## Computation Findings

| Gap | Grammar computation | Physical bridge status |
|---|---|---|
| 1 (velocity) | γ ≈ 1.19; β = 2αγ | Theoretical values fixed; awaits data |
| 2 (band gap) | μ = arccos(1/K)/π; K = 1/cos(πμ) | Resolved for 1D and 2D (Pryamikov) |
| 3 (quantum cost) | Width ~ 0.458^depth; iterative QPE O(d) | Resolved: advantage is in frequency resolution |
| 4 (OAM) | SB-adjacent tongues overlap first at K~1.5 | Open: 1D map insufficient for distant charges |

Resolved: §2 (band gap, 1D and 2D), §3 (quantum cost).
Theoretical: §1 (velocity exponent, awaits data).
Open: §4 (OAM, requires higher-dimensional maps).

Gravity sector: K(x,x') = G_γ(x,x') via Kuramoto-Einstein dictionary.

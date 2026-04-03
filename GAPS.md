# Open Questions in the Overcritical Regime

Four open problems in the vortex and analogue-gravity literature where the
K > 1 circle-map grammar provides structural predictions. Each gap is
sourced from published papers. Computation results are stated as findings.

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

## 2. Predictive Criterion for Photonic Band Gaps

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

**Open:** The mapping K ↔ Δn (refractive index contrast) is not derived.
Known photonic band gap scaling is linear in Δn. If the identification
holds, it implies K - 1 ∝ (Δn)², but this requires derivation from the
specific system's coupling structure.

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

**Open:** The quantum half of the prediction — that quantum phase
estimation resolves rotation numbers with polynomial overhead in precision
bits — is plausible but not yet computed.

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

| Gap | Grammar result | K-mapping status |
|---|---|---|
| 1 (velocity) | γ ≈ 1.19; β = 2αγ | K_eff ~ 1/r² is structural, not derived |
| 2 (band gap) | μ = arccos(1/K)/π; scales as √(K-1) | K ↔ Δn mapping open |
| 3 (quantum cost) | Width ~ 0.458^depth (R²=0.78); q^{-3.2} | Quantum cost comparison open |
| 4 (OAM) | SB-adjacent tongues overlap first at K~1.5 | ℓ-to-ρ mapping fails for distant charges |

The grammar's internal computations produce clean, reproducible results
in every case. The open problem in each gap is the mapping from the
physical system's parameters to the circle map's coupling K.

For the gravity sector, this mapping is derived: K(x,x') = G_γ(x,x')
(the Green's function of the spatial Laplacian), via the Kuramoto-Einstein
dictionary (`proslambenomenos/kuramoto_einstein_mapping.md`). For the
vortex systems above, the analogous derivation has not been performed.

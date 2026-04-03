# Admitted Gaps and K > 1 Resolutions

Six open problems identified in the literature, with precise statements of
what the overcritical circle-map framework would predict for each. Each gap
is sourced from the papers or from review articles that flag the question.

---

## Gap 1: The Trans-Planckian Problem in Analogue Horizons

**What the literature admits:**

Hawking radiation derivations require tracing modes back through the horizon
to arbitrarily high frequencies. In analogue systems (lattices, BECs, optical
media), there is a physical UV cutoff — the lattice spacing, the healing
length, the molecular scale. When the horizon is sharp (changes within one
lattice site), the Hawking temperature becomes ill-defined and "an instability
in the form of an exponential burst of charge and phase quantum fluctuations"
replaces regular thermal emission (arXiv 2204.06583). Garcia Martin-Caro et al.
(2507.13894) find that thermal signatures are "highly dependent on frequency
bands and acceleration parameters" — some configurations produce genuine
thermal spectra, others produce spurious non-thermal artifacts, and they lack
a criterion to predict which.

**What K > 1 provides:**

The tongue-internal cascade gives a **natural hierarchy of scales** between
the tongue boundary (the horizon) and the Feigenbaum accumulation point
(the onset of chaos within the tongue). The cascade produces scales at
ratios converging to δ = 4.669...:

```
    tongue edge → period q → 2q → 4q → ... → chaos
    scale:         Λ₀       Λ₀/δ   Λ₀/δ²     Λ₀/δⁿ
```

The Feigenbaum accumulation point is a **natural UV cutoff** — it is where
the cascade terminates and chaotic fluctuations replace periodic orbits.
The "exponential burst" that the lattice models observe when the horizon is
sharp corresponds to the system being pushed past the accumulation point
into fully developed chaos within the tongue.

**Testable prediction:** The gray-body factors measured by Garcia Martin-Caro
et al. should exhibit oscillatory structure with period ratios converging to
1/δ. The frequency bands where thermal signatures emerge correspond to modes
within the cascade; the bands where they fail correspond to modes beyond the
accumulation point.

---

## Gap 2: Why Singularity Velocities Diverge Before Annihilation

**What the literature admits:**

Bucher et al. (2509.17675, published in Nature 2026) directly measured
superluminal phase-singularity velocities before vortex-antivortex
annihilation. Their explanation: "as opposite-charged singularities approach
each other, their paths in spacetime must form a continuous curve at the
annihilation point, forcing their acceleration to unbounded velocities."
This is kinematic (continuity forces it) but not dynamical — it does not
explain the **rate** of divergence or why slow group velocity media
"paradoxically amplify" the effect.

**What K > 1 provides:**

As a vortex-antivortex pair approaches annihilation, the effective coupling
between them increases (stronger mutual influence at shorter range). This
drives the system deeper into the overcritical regime: K grows through the
interaction. The Lyapunov exponent at the tongue boundary diverges as:

```
    λ ~ (K - K_c)^γ    as K → K_c from above
```

where K_c is the critical coupling for the specific tongue and γ is a
critical exponent. The singularity velocity v_s should scale with the
Lyapunov exponent: faster divergence of nearby orbits = faster motion of
the phase singularity through the field.

**Why slow media amplify:** In a medium with slow group velocity v_g, the
effective coupling K_eff ~ 1/v_g (slower propagation means longer
interaction time). The hexagonal boron nitride in Bucher et al. has
exceptionally slow phonon polaritons, pushing K_eff deep into the
overcritical regime. The "paradox" resolves: slow media don't amplify
velocity directly — they amplify the effective coupling, which drives
the Lyapunov divergence harder.

**Testable prediction:** The velocity divergence exponent (v_s ~ Δt^{-β}
as annihilation time Δt → 0) should be related to the Lyapunov critical
exponent γ. Measuring β in Bucher et al.'s data and comparing to γ from
the circle map at the relevant tongue would test this.

---

## Gap 3: Predictive Criterion for Photonic Band Gaps

**What the literature admits:**

Pryamikov (2601.21704) establishes that Poynting-vector vortices determine
whether photonic crystals produce band gaps or transmission, but states only
that "the geometry and dynamics of the Poynting-vector vortices determine
whether the incident electromagnetic energy is impeded." A 2025 study on
micro-structured optical fibers confirms that "differences in the level of
leakage losses arise from the vortex structure of the Poynting vector of
the fundamental core mode." Neither provides a **predictive criterion** for
which vortex configurations produce band gaps.

**What K > 1 provides:**

The fold region of the overcritical circle map — the interval where
F'(θ) < 0 — is precisely the region of reversed energy flow. The band gap
corresponds to parameter configurations where the fold captures a
significant fraction of the phase space:

```
    Band gap width ∝ measure{θ : F'(θ) < 0} ∝ (K - 1)
```

For K ≤ 1, the fold has zero width — no band gap. For K > 1, the fold
width grows linearly in K - 1. This gives a quantitative prediction:

**The band gap opens when the effective coupling exceeds the critical value
K = 1, and its width is proportional to K - 1.**

**Testable prediction:** In Pryamikov's 2D photonic crystals, the coupling
K depends on the refractive index contrast and the crystal geometry.
Plotting band gap width vs. (n₁/n₂ - 1) (a proxy for K - 1) should give
a linear relationship for small overcriticality. The slope encodes the
local phase-space structure.

---

## ~~Gap 4: BKT Critical Temperature on Curved Spacetime~~ [RETRACTED]

**What the literature admits:**

Ghezzi & Custodio (2603.13544) find vortex-antivortex pair proliferation
near black hole horizons using the 2D XY model on Schwarzschild-de Sitter
spacetime. They identify the phenomenon but do not derive the **critical
temperature** T_BKT as a function of the black hole parameters.

**Original prediction — FALSIFIED BY COMPUTATION:**

The original claim was T_BKT / T_Hawking = (δ-1)/δ ≈ 0.786. This is wrong
on two independent grounds:

1. **(δ-1)/δ is not the correct cascade ratio.** The actual logistic map
   ratio (r_∞ - r_1)/(r_max - r_1) = 0.570, not 0.786. The formula
   conflated the geometric series ratio with the parameter-space ratio.

2. **BKT and Feigenbaum are different universality classes.** BKT is a
   topological transition (vortex-antivortex unbinding), governed by the
   Kosterlitz RG flow. Feigenbaum is a metric transition (period-doubling
   → chaos). They are not the same transition and one does not predict
   the other. The known BKT temperature T_BKT/J ≈ 0.893 for flat 2D XY
   is derived from the Kosterlitz flow equations, not from any cascade.

**What the cascade DOES predict (revised, narrower claim):**

For a **driven** XY model near a black hole horizon (not the equilibrium
model Ghezzi & Custodio study), the topologically ordered phase (T < T_BKT,
bound vortex pairs) can undergo period-doubling under external driving.
The chaos onset within the ordered phase would occur at:

```
    T_chaos / T_BKT ≈ (r_∞ - r_1) / (r_max - r_1) ≈ 0.570
```

This is testable but requires a different system than the one in the paper.

**For the actual Ghezzi & Custodio system:** The BKT transition on curved
spacetime is governed by the position-dependent effective coupling
J_eff(r) = J · √g_rr(r). The critical temperature is where
T_local(r) = T_BKT(J_eff(r)). This is a well-posed GR + XY calculation,
not a circle-map question. The K > 1 framework has nothing to add here.

---

## Gap 5: Which Vortex Flows Have Quantum Advantage

**What the literature admits:**

Quantum algorithms for Navier-Stokes show "a potential quantum exponential
speedup" for turbulent flows (arXiv 2303.16550), and Wang et al. (2506.04023)
demonstrate quantum simulation of multi-vortex dynamics. But there is no
criterion for **which** vortex configurations benefit from quantum simulation
vs. which are efficiently classical. The literature identifies speedup for
"rough/non-smooth flows" without specifying what roughness means in terms
of the flow's dynamical structure.

**What K > 1 provides:**

The self-similar descent gives the criterion. Classical simulation difficulty
tracks the depth of the Stern-Brocot tree required to resolve the flow's
periodic windows within chaos:

- **Efficiently classical:** flows whose dynamics are mode-locked in
  low-order tongues (small q, shallow SB depth). These are regular,
  periodic, and classically simulable in polynomial time.
- **Quantum-advantaged:** flows near noble rotation numbers (deep SB depth,
  long continued fractions). These have self-similar structure at every
  scale — the periodic windows within chaos recapitulate the SB hierarchy
  — and resolving this requires exponential classical resources but maps
  naturally to quantum superposition over the hierarchy levels.

**Testable prediction:** Run Wang et al.'s 8-qubit simulation for vortex
configurations at different effective rotation numbers. Measure classical
simulation cost (e.g., matrix product state bond dimension) vs. quantum
circuit depth. The classical cost should grow exponentially with SB depth;
the quantum cost should grow polynomially.

---

## Gap 6: OAM Multistability and Switching Thresholds

**What the literature admits:**

Experiments on graphene quantum dots show that "the optical bistability
intensity threshold is sensitive to the orbital angular momentum and
azimuthal phase of the coupling vortex beam." A 2025 vortex fiber laser
demonstrates "rapid switching between OAM beams of topological charge
ℓ = 2 and ℓ = 20." But there is no framework predicting **which** OAM
states coexist at given parameters, or what determines the switching
threshold between them.

**What K > 1 provides:**

Tongue overlap at K > 1 predicts exactly this. Two OAM states with
topological charges ℓ₁ and ℓ₂ coexist when their Arnold tongues overlap
at the operating point (Ω, K). The overlap condition depends on tongue
widths: wider tongues (smaller q in the SB tree) overlap first. The
switching threshold corresponds to the **basin boundary** between the
two coexisting attractors — the unstable periodic orbit that separates
their basins of attraction.

**Testable prediction:** For the ℓ = 2 / ℓ = 20 switching laser, the
tongue-overlap model predicts that:
- Coexistence requires K > K_c(ℓ₁, ℓ₂) where K_c depends on the SB
  distance between ℓ₁ and ℓ₂
- The switching threshold (pump power at transition) scales with the
  basin boundary width, which narrows as tongues overlap more deeply
- Intermediate OAM states (ℓ = 3, 5, 8, 13...) should exhibit transient
  population during switching — the system traverses the SB tree between
  ℓ₁ and ℓ₂

---

## Summary: Gap Resolution Scorecard

| Gap | Source | K > 1 resolution | Testable? |
|---|---|---|---|
| Trans-Planckian cutoff | 2507.13894, 2204.06583 | Feigenbaum cascade = natural UV hierarchy | Yes: gray-body oscillation periods → 1/δ |
| Velocity divergence rate | 2509.17675 (Nature) | Lyapunov critical exponent at tongue boundary | Yes: measure β in v_s ~ Δt^{-β}, compare to γ |
| Band gap criterion | 2601.21704 | Fold width F'(θ)<0 ∝ (K-1) | Yes: band gap width vs. index contrast |
| ~~BKT critical temperature~~ | ~~2603.13544~~ | ~~RETRACTED: BKT ≠ Feigenbaum (different universality class)~~ | ~~No~~ |
| Quantum advantage criterion | 2303.16550, 2506.04023 | SB depth of rotation number | Yes: classical cost vs. quantum cost at different ρ |
| OAM switching thresholds | fiber laser experiments | Tongue overlap + basin boundaries | Yes: intermediate ℓ transients during switching |

Five of six resolutions survive. Gap 4 (BKT temperature) was retracted
after computation showed BKT and Feigenbaum are different universality
classes. Three surviving gaps (1, 2, 6) yield specific numerical targets.
Two (3, 5) yield scaling laws. None require new mathematics beyond the
standard K > 1 circle-map phenomenology posed in FRAMEWORK.md §9.

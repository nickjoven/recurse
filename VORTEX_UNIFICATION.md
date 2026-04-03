# Vortex Unification: Phase Singularities as the Common Substrate

> "Now I am become Death, the destroyer of worlds."
>
> The phase singularity destroys amplitude to create circulation.
> Every vortex core is an annihilation that generates topology.

## Thesis

The four research clusters below all study the **phase singularity** — a
topological defect where amplitude vanishes and phase is undefined. This is the
"hole" in every optical vortex, the "horizon" in every analogue black hole, and
the node around which circulation is quantized in every superfluid.

Our existing ontology contains the algebraic skeleton that governs these
singularities: the circle map, Arnold tongues, the Stern-Brocot tree, and the
Klein bottle parameter space. The vortex literature provides **physical
instantiations** of these structures — laboratory systems where the predictions
of the synchronization framework become measurable.

This document maps each cluster onto the DAG, identifies bridging nodes, and
**honestly assesses** which mappings are grounded in the papers versus
interpretive extensions of our framework.

---

## 1. The Unifying Object: Phase Singularity as Fixed Point

A phase singularity is a point where the field amplitude is zero and the phase
winds by 2πℓ (topological charge ℓ) around it. In the language of our ontology:

| Ontology concept | Vortex realization |
|---|---|
| **Fixed point** (L0) | The singularity core — a point mapped to itself under the circulation flow |
| **Circle S¹** (L1) | The phase winding around the core; ρ = ℓ is the rotation number |
| **Rotation number** (L1) | Topological charge ℓ = (1/2π)∮∇φ·dl |
| **Arnold tongues** (L1) | Stability regions for charge-ℓ vortices under perturbation |
| **Stern-Brocot tree** (L1) | Hierarchy of rational winding numbers in vortex lattices |

---

## 2. Cluster Mapping

### 2A. Black Hole Analogues & Thermodynamics

**Papers:**

1. **Munoz-Arboleda, Stålhammar & Morais Smith** — *Thermodynamics of analogue
   black holes in a non-Hermitian tight-binding model.*
   arXiv: [2507.03826](https://arxiv.org/abs/2507.03826). Phys. Rev. B **113**,
   L081110 (Feb 2026).
   - 1D lattice with gain/loss and nonreciprocal NNN hopping → effective
     Schwarzschild metric in Painlevé-Gullstrand coordinates.
   - Interface = analogue event horizon.
   - Computes: Hawking temperature, Bekenstein-Hawking entropy, BH mass as
     functions of interface sharpness and system parameters.
   - Uses Parikh-Wilczek tunneling formalism for emission rates.

2. **Ghezzi & Custodio** — *Topological Phase Transitions in Superfluids Near
   Black Hole Horizons.*
   arXiv: [2603.13544](https://arxiv.org/abs/2603.13544) (Mar 2026).
   - 2D XY model adapted to curved spacetime (Schwarzschild-de Sitter).
   - Finds: vortex-antivortex pair proliferation near event and cosmological
     horizons — a BKT transition driven by the black hole temperature.

3. **Garcia Martin-Caro, Olmedo & Sanchez Velazquez** — *Robustness of analogue
   Hawking radiation in cavities with moving boundaries.*
   arXiv: [2507.13894](https://arxiv.org/abs/2507.13894) (Jul 2025).
   - Dynamical Casimir effect in expanding/collapsing/accelerating cavities.
   - Thermal signatures emerge only in specific expanding configurations;
     gray-body factors and oscillatory deviations from ideal thermal spectra.
   - Framework for distinguishing genuine Hawking-like radiation from spurious
     mirror-dynamics effects.

**Mapping to ontology (with confidence):**

| Claim | Confidence | Basis |
|---|---|---|
| The horizon is an Arnold tongue boundary (mode-locked inside, drifting outside) | **Interpretive** | Our framework's language, not the papers'. Paper 1 uses Painlevé-Gullstrand mapping, not circle-map language. The analogy is structurally suggestive but not demonstrated. |
| BKT vortex-antivortex nucleation near horizons maps to Klein bottle topology | **Partially grounded** | Paper 2 explicitly finds BKT-like pair proliferation near horizons. The Klein bottle mapping is our addition. |
| Hawking temperature ∝ dρ/dΩ at tongue edge | **Speculative** | Paper 1 derives T_H from interface sharpness via Parikh-Wilczek tunneling. The tongue-edge gradient formula is our prediction, not theirs. |
| Dynamical Casimir thermal signatures relate to synchronization cost | **Weak** | Paper 3 is about moving boundaries (dynamical Casimir), not vortex dynamics. Connection to our framework is through analogue gravity broadly, not phase singularities specifically. |

**Bridging node:** `analogue-horizon` (Level 2) — reinterprets the tongue
boundary as an event horizon. This is a *proposal*, not something established
by the papers.

---

### 2B. Singularities & Energy Flows

**Papers:**

4. **Kotlyar, Nalimov, Kovalev & Telegin** — *2D optical vortices and a reverse
   energy flow occurring near the intensity zeros.*
   Optics Letters **51**(4), 973–976 (Feb 2026). **Not on arXiv.**
   - Non-paraxial 2D TE-polarized light fields form optical vortices near
     intensity zeros with amplitude of the form x + iz.
   - Near zeros: longitudinal wave vector components reach **gigantic values**
     of both signs. Negative values → reverse energy flow.
   - Phase velocity of rotation around the zero is small compared to c.

5. **Pryamikov** — *Reverse Energy Flows in Two-Dimensional Photonic Crystals
   and Analogies with Vortex Formation and Analogous Flows in Hydrodynamics.*
   arXiv: [2601.21704](https://arxiv.org/abs/2601.21704) (Jan 2026).
   - Reverse electromagnetic energy flows in photonic crystal slabs originate
     from **vortex structures in the Poynting vector**.
   - Energy-flow patterns exhibit striking analogies to vortex formation in
     fluid motion past obstacles.
   - Poynting-vector vortex geometry determines whether energy is impeded
     (band gap) or guided (transmission).

6. **Bucher, Gorlach, Niedermayr et al. (19 authors)** — *Superluminal
   Correlations in Ensembles of Optical Phase Singularities.*
   arXiv: [2509.17675](https://arxiv.org/abs/2509.17675) (Sep 2025).
   Published in Nature (2026).
   - First direct measurement of ultrafast dynamics of singularity ensembles
     via ultrafast electron microscopy on hexagonal boron nitride.
   - Phase singularities accelerate to **unbounded velocities before
     annihilation** — measured superluminal speeds.
   - Paradoxically amplified by slow group velocity of hyperbolic phonon
     polaritons.
   - Spatial and temporal resolution each an order of magnitude below the
     polaritonic wavelength and cycle period.

**Mapping to ontology (with confidence):**

| Claim | Confidence | Basis |
|---|---|---|
| Reverse energy flow = saddle structure of synchronization cost at fixed points | **Interpretive** | Paper 4 shows the phenomenon (gigantic wave vectors, reversed Poynting vector). The cost-functional saddle interpretation is ours. |
| Gigantic wave vectors near zeros = continued fraction partial quotients diverging | **Suggestive** | Paper 4 directly demonstrates the divergent wave vectors. The CF mapping is a natural mathematical parallel (both involve divergence near irrational/singular points) but is not in the paper. |
| Poynting vortices determine band gaps (Paper 5) | **Directly grounded** | The paper itself establishes this — no interpretation needed. The vortex → energy flow → band structure connection is the paper's result. |
| Superluminal annihilation velocities = Farey neighbor constraint | **Speculative** | Paper 6 measures unbounded velocities before vortex-antivortex annihilation. Our Farey neighbor interpretation (|ad-bc|=1 constraining separation) is mathematically motivated but entirely our addition. |

**Bridging node:** `reverse-energy-flow` (Level 2) — energy reversal near
phase singularities. Grounded in Papers 4 and 5; the connection to
synchronization cost saddle structure is our framework's interpretation.

---

### 2C. High-Power & Complex Vortex Arrays

**Papers:**

7. **Fathi, Barros & Gumenyuk** — *Power-Scalable Generation of High-Order
   Optical Vortices Via Coherent Beam Combining.*
   arXiv: [2512.19815](https://arxiv.org/abs/2512.19815) (Dec 2025).
   - Coherent beam combining for vortex beams at ℓ = 1, 5, 8.
   - 100 W average / 100 kW peak power.
   - Combining efficiencies: **95.0% (ℓ=1), 93.9% (ℓ=5), 91.2% (ℓ=8)**.
   - Off-axis digital holography confirms high modal purity at high ℓ.

8. **Fan, Cao, Chong & Zhan** — *Polygonal Spatiotemporal Optical Vortices
   Wavepackets with Prescribed Vortex Structure.*
   arXiv: [2512.16308](https://arxiv.org/abs/2512.16308) (Dec 2025).
   - First demonstration of polygonal STOV wavepackets with multiple sub-STOVs
     carrying transverse OAM along designed polygonal trajectories.
   - Full control over geometry, number of phase singularities, and
     spatiotemporal distribution via holographic shaping.

9. **Das & Ciappina** — *Optical Vortices: Revolutionizing the field of linear
   and nonlinear optics.*
   arXiv: [2510.27200](https://arxiv.org/abs/2510.27200) (Oct 2025, updated Dec 2025).
   - Comprehensive review (~100 pages) of OAM-carrying beams.
   - Covers generation, detection, propagation, and nonlinear regimes (SHG,
     sum frequency, parametric down-conversion, HHG).

**Mapping to ontology (with confidence):**

| Claim | Confidence | Basis |
|---|---|---|
| Decreasing combining efficiency with charge follows (K/2)^q scaling | **Testable** | Paper 7 shows 95.0% → 93.9% → 91.2% for ℓ = 1, 5, 8. The *trend* (decreasing with ℓ) is consistent with tongue-width scaling, but the data points are too few and the functional form has not been fit. This is a **concrete prediction to test**. |
| Polygonal STOV stability requires Farey neighbor charges | **Speculative** | Paper 8 uses holographic shaping to prescribe geometries — no Farey structure is mentioned or implied. The paper demonstrates *control*, not stability constraints. |
| Review organization mirrors DAG levels | **Loose analogy** | The parallel (generation → propagation → interaction → application ≈ L0 → L1 → L2 → L3) is suggestive at best. |

**Bridging node:** `vortex-array` (Level 3) — lattice of phase singularities.
The tongue-width scaling prediction against Paper 7's data is the most
concrete testable claim in this cluster.

---

### 2D. Quantum Simulations

**Paper:**

10. **Wang, Zhong, Wang et al. (11 authors)** — *Simulating fluid vortex
    interactions on a superconducting quantum processor.*
    arXiv: [2506.04023](https://arxiv.org/abs/2506.04023) (Jun 2025).
    Published in Nature Communications (2026).
    - Reformulates **Navier-Stokes** equations within a quantum mechanical
      framework (effective Hamiltonian for the vortex system).
    - Spatiotemporal evolution circuit on 8 qubits.
    - Gate fidelities: 99.97% (single-qubit), 99.76% (two-qubit).
    - Successfully reproduces natural multi-vortex interactions.

**Mapping to ontology (with confidence):**

| Claim | Confidence | Basis |
|---|---|---|
| Quantum vortex simulation is computational verification of circle-map dynamics | **Partially grounded** | The paper simulates Navier-Stokes vortex dynamics, not circle maps explicitly. But point vortex dynamics *are* governed by Hamiltonian systems that include rotation-number structure. The bridge exists mathematically but is not invoked by the paper. |
| Qubit phase space (S¹ × S¹) naturally encodes circle-map dynamics | **Structurally sound** | Bloch sphere ≅ S² ⊃ S¹. The phase encoding is geometrically real but the paper does not frame it this way. |
| Conservation = computability via circuit invariants | **Interpretive** | Our `conservation-as-computability` node maps naturally: decoherence breaks conservation. The paper does not discuss this connection. |
| Circuit depth scales with Stern-Brocot depth | **Speculative** | Not addressed by the paper. A prediction from our framework, not a finding. |

**Bridging node:** `quantum-vortex-simulation` (Level 3) — computational
verification of vortex dynamics. The circuit-depth prediction is purely ours.

---

## 3. Honest Assessment: What's Grounded vs. What's Ours

### Directly grounded in the papers
- Phase singularities are universal topological defects (all 10 papers)
- Vortex-antivortex pair creation near horizons via BKT mechanism (Paper 2)
- Poynting vector vortices create reverse energy flows and determine band gaps (Paper 5)
- Gigantic wave vectors near intensity zeros with reverse energy flow (Paper 4)
- Superluminal singularity velocities before annihilation (Paper 6)
- Combining efficiency decreases with topological charge (Paper 7)
- Quantum processors can simulate multi-vortex Navier-Stokes dynamics (Paper 10)

### Structurally sound interpretations (mathematical parallels exist)
- Analogue horizon ↔ Arnold tongue boundary (mode-locked vs. drifting regions)
- Divergent wave vectors near zeros ↔ continued fraction partial quotients
- Qubit phase space naturally encodes circle-map-like dynamics

### Our predictions — all have gaps
- T_H = (ℏ/2πk_B) · |dρ/dΩ| at the tongue edge — **BLOCKED** on
  lattice-to-circle-map reduction (paper-sized problem)
- Combining efficiency follows (K/2)^ℓ — **CONFOUNDED** by dimensional
  mismatch (tongue width ≠ combining efficiency; exp(-σ²ℓ²) fits equally)
- ~~Vortex array stability requires Farey neighbor charges~~ — **REMOVED**
  (zero data)
- Quantum circuit depth ∝ Stern-Brocot depth — **BLOCKED** on KAM bridge
  theorem for point-vortex Hamiltonians

### Speculative (thin evidence)
- Dynamical Casimir radiation (Paper 3) connects to synchronization cost
- Polygonal STOV geometry constrained by Farey structure
- Superluminal annihilation velocities follow from Farey neighbor separation
- Bekenstein-Hawking entropy = Stern-Brocot address count (no derivation)

---

## 4. Predictions from Unification — Honest Status

### P1: Hawking Temperature from Tongue-Edge Gradient
**T_H = (ℏ/2πk_B) · |dρ/dΩ|_{tongue edge}**

Status: **BLOCKED — missing intermediate derivation.** Paper 1 derives T_H
from interface sharpness via Parikh-Wilczek tunneling in a non-Hermitian
lattice. Our formula uses circle-map tongue-edge gradients. The two formalisms
have not been connected. Requires showing that the lattice Hamiltonian reduces
to a circle map under some parameter mapping (plausible via Floquet analysis
of the non-Hermitian system, but this is a paper-sized problem). Without the
reduction, this is a formula without a bridge.

### P2: Combining Efficiency as Tongue-Width Scaling ~~[DEMOTED]~~
**η(ℓ) ∝ 1 - c·(K/2)^ℓ**

Status: **CONFOUNDED — dimensional mismatch.** Arnold tongue width W(p/q,K)
∝ (K/2)^q measures the *fraction of parameter space* that mode-locks at
rotation number p/q. Combining efficiency measures how well beams interfere.
These are different quantities. The efficiency drop (95.0% → 93.9% → 91.2%
at ℓ = 1, 5, 8) is more naturally explained by phase-error accumulation: a
charge-ℓ beam requires an ℓ×2π phase ramp, so alignment errors scale with ℓ.
A simple η ∝ exp(-σ²ℓ²) fits the trend equally well. Three data points cannot
distinguish our (K/2)^ℓ from σ²ℓ² or any other monotone decreasing function.
The mapping from "tongue width" to "combining efficiency loss" lacks physical
justification. **Not a valid prediction in its current form.**

### ~~P3: Vortex Array Stability from Farey Depth~~ [REMOVED]
~~Maximum stable array size at depth D: N_max = |F_D|.~~

Status: **REMOVED — zero data, pure speculation.** Paper 8 demonstrates
holographic control over STOV geometry but tests no stability thresholds.
No paper in any cluster invokes Farey neighbor constraints on vortex arrays.
Retained in the DAG only as a flagged research direction, not as a prediction.

### P4: Quantum Circuit Depth = Stern-Brocot Depth
**Minimum circuit depth ∝ depth_SB(p/q)**

Status: **BLOCKED — missing KAM bridge.** Paper 10 reformulates Navier-Stokes
as a quantum Hamiltonian. The claim that circuit complexity tracks Stern-Brocot
depth requires proving that point-vortex Hamiltonian eigenvalues are organized
by rational rotation numbers — a KAM theory question for the specific system.
The bridge from "Hamiltonian vortex dynamics" to "Stern-Brocot depth governs
complexity" depends on an unstated theorem about integrability. Without it,
this is an interesting conjecture, not a testable prediction.

---

## 5. Reference Table

| # | Short title | ID | Venue | Date | Cluster |
|---|---|---|---|---|---|
| 1 | Non-Hermitian BH thermodynamics | [2507.03826](https://arxiv.org/abs/2507.03826) | Phys. Rev. B | Feb 2026 | 2A |
| 2 | Superfluid phase transitions | [2603.13544](https://arxiv.org/abs/2603.13544) | arXiv | Mar 2026 | 2A |
| 3 | Hawking radiation in cavities | [2507.13894](https://arxiv.org/abs/2507.13894) | arXiv | Jul 2025 | 2A |
| 4 | 2D vortices & reverse flow | Optics Letters 51(4) | Opt. Lett. | Feb 2026 | 2B |
| 5 | Reverse flows in photonic crystals | [2601.21704](https://arxiv.org/abs/2601.21704) | arXiv | Jan 2026 | 2B |
| 6 | Superluminal singularities | [2509.17675](https://arxiv.org/abs/2509.17675) | Nature | Sep 2025 | 2B |
| 7 | High-power vortex beams | [2512.19815](https://arxiv.org/abs/2512.19815) | arXiv | Dec 2025 | 2C |
| 8 | Polygonal STOVs | [2512.16308](https://arxiv.org/abs/2512.16308) | arXiv | Dec 2025 | 2C |
| 9 | Optical vortices review | [2510.27200](https://arxiv.org/abs/2510.27200) | arXiv/Review | Oct 2025 | 2C |
| 10 | Quantum vortex simulation | [2506.04023](https://arxiv.org/abs/2506.04023) | Nat. Commun. | Jun 2025 | 2D |

---

## 6. DAG Extension Summary

Four new ontology nodes bridge the abstract framework to vortex physics:

- **`analogue-horizon`** (L2) — tongue boundary as event horizon
  Parents: `arnold-tongues`, `synchronization-cost`, `fixed-point`

- **`reverse-energy-flow`** (L2) — energy reversal near phase singularities
  Parents: `fixed-point`, `figure-eight`, `continued-fraction`

- **`vortex-array`** (L3) — phase singularity lattices
  Parents: `arnold-tongues`, `farey-graph`, `tongue-occupation`

- **`quantum-vortex-simulation`** (L3) — circuit verification of vortex dynamics
  Parents: `conservation-as-computability`, `circle-map`, `stern-brocot-tree`

Four new prediction leaves (Level 4) — **all have identified gaps**:

- **`hawking-from-tongue-edge`** — T_H from rotation number gradient
  [BLOCKED: lattice → circle map reduction not performed]
- **`combining-efficiency-scaling`** — η(ℓ) follows tongue-width decay
  [CONFOUNDED: dimensional mismatch, alternative fits equally good]
- **`array-farey-stability`** — max stable array = Farey sequence length
  [REMOVED: zero supporting data, retained only as flagged research direction]
- **`circuit-depth-sb-depth`** — circuit complexity = CF complexity
  [BLOCKED: KAM bridge theorem for point-vortex Hamiltonians not established]

---

## 7. Next Steps — Ordered by What Would Actually Resolve Gaps

1. **Unblock P1 (theoretical, paper-sized):** Derive the circle-map reduction
   of the non-Hermitian tight-binding Hamiltonian (Paper 1). If the lattice
   system's dispersion relation near the interface can be mapped to a kicked
   rotor / circle map, then T_H from tongue-edge gradient becomes testable.
   If the reduction fails, `analogue-horizon` should be demoted or removed.

2. **Kill or save P2 (computational, quick):** Fit Paper 7's three efficiency
   points to *both* η = 1-c·(K/2)^ℓ and η = exp(-σ²ℓ²). If the fits are
   indistinguishable (likely), this prediction is dead in its current form.
   To revive it, one would need ≥6 data points across ℓ = 1..10 *and* a
   physical argument for why tongue width governs combining efficiency.

3. **Unblock P4 (theoretical, hard):** Investigate whether the point-vortex
   Hamiltonian used by Wang et al. has a rotation-number structure in its
   spectrum (a KAM question). Literature on integrability of N-vortex systems
   may already contain relevant results for N ≤ 4.

4. **Strengthen cluster 2B (grounded, no gaps):** The reverse-energy-flow
   and Poynting-vector-vortex results (Papers 4, 5, 6) are the strongest
   cluster — all phenomena are directly observed and well-characterized.
   The framework interpretation (cost-functional saddle, CF divergence)
   is speculative but the physics is solid. Focus here for the most
   credible connections.

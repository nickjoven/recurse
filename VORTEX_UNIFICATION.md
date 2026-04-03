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

### Our predictions (testable but not in the papers)
- T_H = (ℏ/2πk_B) · |dρ/dΩ| at the tongue edge
- Combining efficiency follows (K/2)^ℓ (fit against Paper 7 data)
- Vortex array stability requires Farey neighbor charges
- Quantum circuit depth ∝ Stern-Brocot depth of target rotation number

### Speculative (thin evidence)
- Dynamical Casimir radiation (Paper 3) connects to synchronization cost
- Polygonal STOV geometry constrained by Farey structure
- Superluminal annihilation velocities follow from Farey neighbor separation

---

## 4. Predictions from Unification

### P1: Hawking Temperature from Tongue-Edge Gradient
**T_H = (ℏ/2πk_B) · |dρ/dΩ|_{tongue edge}**

Status: **Our prediction.** Paper 1 derives T_H from interface sharpness.
Testing: Compute tongue-edge slopes in a circle map parameterized to match
Paper 1's lattice parameters. If they give the same T_H, the mapping holds.

### P2: Combining Efficiency as Tongue-Width Scaling
**η(ℓ) ∝ 1 - c·(K/2)^ℓ** for some coupling K and constant c.

Status: **Testable now.** Paper 7 gives three data points (ℓ=1,5,8 →
95.0%, 93.9%, 91.2%). Fit K and c. If the fit is good, predict η for
ℓ = 2, 3, 4 and propose the experiment.

### P3: Vortex Array Stability from Farey Depth
Maximum stable array size at depth D: **N_max = |F_D|**.

Status: **Speculative.** No paper addresses this. Would require systematic
stability measurements across array configurations.

### P4: Quantum Circuit Depth = Stern-Brocot Depth
Minimum circuit depth to precision ε scales as **depth_SB(p/q)** where
|ρ - p/q| < ε.

Status: **Our prediction.** Paper 10 does not report circuit depth vs.
rotation number precision. Benchmarking their 8-qubit setup against
continued-fraction depth would test this directly.

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

Four new predictions (Level 4 leaves):

- **`hawking-from-tongue-edge`** — T_H from rotation number gradient
- **`combining-efficiency-scaling`** — η(ℓ) follows tongue-width decay
- **`array-farey-stability`** — max stable array = Farey sequence length
- **`circuit-depth-sb-depth`** — circuit complexity = CF complexity

---

## 7. Next Steps

1. **Immediate (computational):** Fit Paper 7's efficiency data (95.0%, 93.9%,
   91.2% at ℓ = 1, 5, 8) to η(ℓ) = 1 - c·(K/2)^ℓ. If the fit works, we
   have a quantitative prediction for untested charges.

2. **Near-term (theoretical):** Map Paper 1's lattice parameters to circle-map
   parameters. Compute T_H both ways. Agreement would validate the
   horizon ↔ tongue boundary identification.

3. **Medium-term (observational):** Propose to Paper 10's group (Wang et al.)
   a benchmark: measure circuit depth vs. rotation-number precision for their
   8-qubit vortex simulation. Compare against Stern-Brocot depth.

4. **Long-term (experimental):** Design a vortex array stability experiment
   that systematically varies nearest-neighbor charge pairs to test the
   Farey neighbor condition.

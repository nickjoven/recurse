# Vortex Unification: Phase Singularities as the Common Substrate

## Thesis

The four research clusters below — black hole analogues, singularity energy flows,
high-power vortex arrays, and quantum vortex simulations — all study the same
mathematical object: the **phase singularity**, a topological defect where
amplitude vanishes and phase is undefined. This is the "hole" in every optical
vortex, the "horizon" in every analogue black hole, and the node around which
circulation is quantized in every superfluid.

Our existing ontology already contains the algebraic skeleton that governs these
singularities: the circle map, Arnold tongues, the Stern-Brocot tree, and the
Klein bottle parameter space. The vortex literature provides **physical
instantiations** of these structures — laboratory systems where the predictions
of the synchronization framework become measurable.

This document maps each cluster onto the DAG and identifies the new nodes needed
to bridge abstract ontology to concrete vortex physics.

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
| **Stern-Brocot tree** (L1) | Hierarchy of vortex-antivortex rational winding numbers in lattices |
| **Devil's staircase** (L1) | Mode-locking of vortex lattice spacings under driving |

The phase singularity is not merely analogous to our fixed point — it **is** a
fixed point of the phase flow, classified by its rotation number (the topological
charge), and organized by the same Stern-Brocot/Farey structure that governs
the circle map.

---

## 2. Cluster Mapping

### 2A. Black Hole Analogues & Thermodynamics → Synchronization Cost

**Papers:**
- *Thermodynamics of Analogue Black Holes in a Non-Hermitian System* (March 2026)
- *Topological Phase Transitions in Superfluids Near Black Hole Horizons* (March 2026)
- *Robustness of Analogue Hawking Radiation in Cavities* (July 2025)

**Connection to ontology:**

The analogue black hole is a system where the flow velocity exceeds the local
wave speed, creating a horizon — a surface where phase information cannot
propagate upstream. In our framework:

- The **horizon** is the boundary of an Arnold tongue: inside, the flow is
  mode-locked (subsonic, phase-coherent); outside, it drifts (supersonic,
  phase-incoherent). The horizon IS the tongue boundary.
- **Hawking temperature** maps to the synchronization cost at the tongue edge.
  The thermal spectrum emerges because the tongue boundary is a critical line
  where the rotation number transitions from rational (locked) to irrational
  (drifting). The density of states near this transition follows the same
  scaling as Hawking radiation: T_H ∝ surface gravity ∝ dρ/dΩ at the tongue
  edge.
- **Bekenstein-Hawking entropy** S = A/4 corresponds to the number of
  distinguishable Stern-Brocot addresses accessible within the tongue at a
  given depth. The "area" is the tongue width; the "entropy" counts the
  rational approximants it contains.
- **Vortex-antivortex pair creation** near horizons (the superfluid paper) is
  the topological phase transition predicted by the Klein bottle structure:
  crossing the tongue boundary nucleates defect pairs, exactly as a BKT
  transition nucleates vortex-antivortex pairs.

**New ontology node:** `analogue-horizon` (Level 2) — the tongue boundary
reinterpreted as an event horizon, with Hawking temperature = synchronization
cost gradient at the mode-locking edge.

### 2B. Singularities & Energy Flows → Fixed-Point Dynamics

**Papers:**
- *2D Optical Vortices and Reverse Energy Flow Near Intensity Zeros* (Feb 2026)
- *Reverse Energy Flows in 2D Photonic Crystals* (Jan 2026)
- *Superluminal Correlations in Ensembles of Optical Phase Singularities* (Mar 2026)

**Connection to ontology:**

These papers study what happens at and near the "hole" — the intensity zero.
The key findings map directly:

- **Reverse energy flow** near the singularity core = the Poynting vector
  locally points backward. In our framework: near the fixed point, the
  synchronization cost functional has a saddle structure. The drift term
  dominates the coupling term, reversing the effective "force." This is the
  local signature of the figure-eight (Möbius band) topology — the
  self-intersection of the Klein bottle immersion creates regions where the
  flow direction inverts.
- **Superoscillations** (locally gigantic wave vectors near the zero) = the
  continued fraction expansion near an irrational rotation number requires
  increasingly large partial quotients. The wave vector divergence near the
  singularity is the physical manifestation of the continued fraction's
  partial quotients growing without bound as you approach the noble
  (most irrational) point.
- **Superluminal singularity velocities before annihilation** = as two phase
  singularities (a vortex-antivortex pair) approach, their mutual rotation
  number transitions through a cascade of rational approximants. The apparent
  velocity diverges because the Stern-Brocot path length to the collision
  point shrinks faster than the spatial separation. This is a Farey neighbor
  effect: adjacent fractions in the Farey sequence satisfy |ad-bc|=1,
  constraining the minimum separation.

**New ontology node:** `reverse-energy-flow` (Level 2) — energy reversal near
phase singularities as a consequence of the synchronization cost saddle
structure at fixed points.

### 2C. High-Power & Complex Vortex Arrays → Tongue Lattices

**Papers:**
- *Power-Scalable High-Order Optical Vortices via Coherent Beam Combining* (Dec 2025)
- *Polygonal Spatiotemporal Optical Vortices* (Dec 2025)
- *Optical Vortices: Revolutionizing Linear and Nonlinear Optics* (Oct 2025, review)

**Connection to ontology:**

Vortex arrays are physical Arnold tongue lattices:

- **Coherent beam combining** to produce charge-ℓ vortices = superposing
  multiple mode-locked oscillators with prescribed phase offsets. The purity
  of the resulting vortex (how well-defined the central "hole" remains at
  high power) depends on how deeply the constituent beams are locked into
  the ℓ-tongue. The (K/2)^q scaling predicts that higher charges require
  exponentially more precise phase control — exactly what the 100W
  experiment demonstrates.
- **Polygonal spatiotemporal vortices** = prescribed arrangements of phase
  singularities in space-time wavepackets. The allowed polygon geometries
  are constrained by the Farey neighbor relation: adjacent vortices in the
  array must have topological charges that are Farey neighbors (|ℓ₁q₂ - ℓ₂q₁| = 1)
  for the array to be stable. The Farey graph tiles these configurations.
- The **100-page review** catalogues the full phenomenology of phase-singular
  beams. Its organizational structure (generation → propagation → interaction →
  application) mirrors our DAG levels (primitives → derived → algebra → topology).

**New ontology node:** `vortex-array` (Level 3) — a lattice of phase
singularities whose stability and scaling are governed by Arnold tongue
width and Farey neighbor constraints.

### 2D. Quantum Simulations → Computational Verification

**Paper:**
- *Simulating Fluid Vortex Interactions on a Superconducting Quantum Processor* (Feb 2026)

**Connection to ontology:**

This paper closes the loop:

- A quantum computer simulates vortex dynamics — the same dynamics our
  ontology claims are governed by circle map synchronization. If the quantum
  simulation reproduces the Arnold tongue structure, the Stern-Brocot
  hierarchy of rational rotation numbers, and the (K/2)^q scaling, then we
  have a **computational verification** of the framework independent of any
  particular physical system.
- The quantum processor's native gate set operates on qubits — two-level
  systems whose state space is S¹ × S¹ (the Bloch sphere ≈ two circles).
  The vortex simulation maps circle-map dynamics onto the quantum hardware's
  natural phase space. This is not a coincidence; it's why the simulation
  works efficiently.
- The connection to `conservation-as-computability` (L3) is direct: conserved
  quantities in the vortex simulation correspond to computable invariants
  of the quantum circuit. Non-conservation = decoherence = non-computability.

**New ontology node:** `quantum-vortex-simulation` (Level 3) — computational
verification of vortex dynamics via quantum processors, connecting
conservation laws to circuit computability.

---

## 3. The Unified Picture

```
                    Phase Singularity
                    (the "hole")
                         │
            ┌────────────┼────────────┐
            │            │            │
     Fixed Point    Circle S¹   Rotation Number
        (L0)          (L1)         (L1)
            │            │            │
            ▼            ▼            ▼
    ┌───────────────────────────────────────┐
    │         Circle Map + Arnold Tongues    │
    │              (L1 backbone)             │
    └──────┬──────┬──────┬──────┬───────────┘
           │      │      │      │
           ▼      ▼      ▼      ▼
     Analogue  Reverse  Vortex  Quantum
     Horizon   Energy   Array   Simulation
      (2B)     Flow(2B) (3)     (3)
           │      │      │      │
           ▼      ▼      ▼      ▼
    ┌───────────────────────────────────────┐
    │    New Predictions (Level 4 leaves)    │
    │                                       │
    │  • Hawking T from tongue-edge slope   │
    │  • Reverse flow radius ~ 1/ℓ²        │
    │  • Array stability ~ Farey depth      │
    │  • Quantum circuit depth ~ SB depth   │
    └───────────────────────────────────────┘
```

The four clusters are not four separate research programs. They are four
experimental windows onto the same mathematical object: the phase singularity
governed by circle-map synchronization dynamics. Each window provides distinct
observables that test the same underlying predictions.

---

## 4. New Predictions from Unification

### P1: Hawking Temperature from Tongue-Edge Gradient
The Hawking temperature of an analogue black hole equals the gradient of the
rotation number at the Arnold tongue boundary:
**T_H = (ℏ/2πk_B) · |dρ/dΩ|_{tongue edge}**

Testable by: Comparing measured Hawking spectra in analogue systems with the
circle map's tongue boundary slopes for the corresponding rotation number.

### P2: Reverse Flow Radius Scaling
The radius at which energy flow reverses near a charge-ℓ vortex scales as:
**r_rev ∝ λ/ℓ² · (K/2)^ℓ**

where the (K/2)^ℓ factor comes from the Arnold tongue width at charge ℓ.
Testable by: Measuring reverse-flow regions in optical vortices of varying charge.

### P3: Vortex Array Stability from Farey Depth
A lattice of N vortices is stable iff all nearest-neighbor charge pairs are
Farey neighbors (|ℓ_i q_j - ℓ_j q_i| = 1). Maximum stable array size at
depth D of the Stern-Brocot tree: N_max = |F_D| (the Farey sequence length).

Testable by: Comparing coherent beam combining stability thresholds across
array configurations.

### P4: Quantum Circuit Depth Equals Stern-Brocot Depth
The minimum quantum circuit depth to simulate a charge-ℓ vortex interaction
to precision ε scales as the Stern-Brocot depth of the rational approximant
p/q closest to the target rotation number within ε.

Testable by: Benchmarking quantum vortex simulations against continued-fraction
depth of the simulated rotation numbers.

---

## 5. Observation Schema Extensions

Each cluster generates observation nodes that link back to predictions:

| Cluster | Observation source | Quantity | Links to prediction |
|---|---|---|---|
| Black hole analogues | Non-Hermitian lattice experiments | T_Hawking | `hawking-from-tongue-edge` |
| Singularity flows | Optical vortex near-field measurements | r_reverse | `reverse-flow-scaling` |
| Vortex arrays | Coherent beam combining stability tests | N_max_stable | `array-farey-stability` |
| Quantum simulation | Superconducting processor benchmarks | circuit_depth | `circuit-depth-sb-depth` |

These observations enter the DAG through the existing `observation` schema,
with `arxiv_id` fields pointing to the source papers. Saturation of the
corresponding prediction nodes updates as measurements confirm or refute
each prediction.

---

## 6. Implementation Path

1. **Extend the seed** — Add 4 new ontology nodes (`analogue-horizon`,
   `reverse-energy-flow`, `vortex-array`, `quantum-vortex-simulation`) and
   4 new prediction leaves to `seed/src/main.rs`.

2. **Seed the references** — Add the 10 papers as observation-schema nodes
   with `arxiv_id` fields, linked to the predictions they can test.

3. **Update the visualizer spec** — The claim visualizer (Proposal 1 in
   PROPOSALS.md) should render the new bridge nodes and show the vortex
   research connecting to the algebraic core.

4. **Design the vortex substrate** — Analogous to the Farey Sky stellar
   substrate (Proposal 2), but ingesting analogue-experiment data rather
   than Gaia DR3 catalogs.

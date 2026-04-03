# Vortex Unification: Phase Singularities as the Common Substrate

## Thesis

The four research clusters below all study the phase singularity — a
topological defect where amplitude vanishes and phase is undefined. Such
singularities appear in optical vortices, analogue black holes, and
superfluids, in each case as the locus where circulation is quantized.

The synchronization cost framework (harmonics/sync_cost/) provides the
algebraic grammar that classifies these singularities: the circle map,
Arnold tongues, the Stern-Brocot tree, the Feigenbaum cascade, and the
Klein bottle parameter space. For the gravity sector, the Kuramoto-Einstein
dictionary (proslambenomenos/kuramoto_einstein_mapping.md) derives the
coupling K explicitly. For the vortex systems below, the K-mapping remains
to be derived — each is a candidate instantiation.

---

## 1. The Unifying Object: Phase Singularity as Fixed Point

A phase singularity is a point where the field amplitude is zero and the phase
winds by 2πℓ (topological charge ℓ) around it. In the grammar:

| Grammar concept | Vortex realization |
|---|---|
| **Fixed point** (L0) | The singularity core — a point mapped to itself under the circulation flow |
| **Circle S¹** (L1) | The phase winding around the core; ρ = ℓ is the rotation number |
| **Rotation number** (L1) | Topological charge ℓ = (1/2π)∮∇φ·dl |
| **Arnold tongues** (L1) | Stability regions for charge-ℓ vortices under perturbation |
| **Lyapunov exponent** (L1) | Diagnostic at K > 1: λ < 0 (locked), λ > 0 (chaotic) |

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
   - Computes Hawking temperature, Bekenstein-Hawking entropy, BH mass
     via Parikh-Wilczek tunneling.

2. **Ghezzi & Custodio** — *Topological Phase Transitions in Superfluids Near
   Black Hole Horizons.*
   arXiv: [2603.13544](https://arxiv.org/abs/2603.13544) (Mar 2026).
   - 2D XY model on Schwarzschild-de Sitter: vortex-antivortex pair
     proliferation near event and cosmological horizons (BKT transition).

3. **Garcia Martin-Caro, Olmedo & Sanchez Velazquez** — *Robustness of analogue
   Hawking radiation in cavities with moving boundaries.*
   arXiv: [2507.13894](https://arxiv.org/abs/2507.13894) (Jul 2025).
   - Dynamical Casimir effect; gray-body factors and oscillatory deviations.

**Grammar connection:** In the gravity sector, the Kuramoto-Einstein dictionary
provides the K-mapping: r(x,t) = N (coherence = lapse function), so the
event horizon is r = 0 = N = 0, and K(x,x') = G_γ(x,x') is the Green's
function of the spatial Laplacian. For Paper 1's non-Hermitian lattice, the
analogous mapping K(hopping asymmetry, gain/loss) has not been derived.
The BKT transition (Paper 2) is a topological phase transition distinct from
the Feigenbaum period-doubling cascade — they are different universality classes.

### 2B. Singularities & Energy Flows

**Papers:**

4. **Kotlyar, Nalimov, Kovalev & Telegin** — *2D optical vortices and a reverse
   energy flow occurring near the intensity zeros.*
   Optics Letters **51**(4), 973–976 (Feb 2026). **Not on arXiv.**
   - Non-paraxial TE fields form vortices near intensity zeros with
     gigantic wave vector components of both signs; reverse energy flow.

5. **Pryamikov** — *Reverse Energy Flows in Two-Dimensional Photonic Crystals
   and Analogies with Vortex Formation and Analogous Flows in Hydrodynamics.*
   arXiv: [2601.21704](https://arxiv.org/abs/2601.21704) (Jan 2026).
   - Poynting-vector vortices determine band gap formation; energy-flow
     patterns analogous to fluid vortices past obstacles.

6. **Bucher, Gorlach, Niedermayr et al.** — *Superluminal Correlations in
   Ensembles of Optical Phase Singularities.*
   arXiv: [2509.17675](https://arxiv.org/abs/2509.17675) (Sep 2025). Nature 2026.
   - First direct measurement of singularity ensemble dynamics via
     ultrafast electron microscopy; superluminal velocities before annihilation.

**Grammar connection:** The fold region of the overcritical circle map
({θ : F'(θ) < 0}) corresponds to reversed energy flow. The exact fold
measure is μ(K) = arccos(1/K)/π, scaling as √(K-1) near criticality.
For photonic crystals, the mapping K ↔ index contrast Δn is open; the
√(K-1) scaling implies K-1 ∝ (Δn)² if the identification holds.
The Lyapunov exponent γ ≈ 1.19 at the tongue boundary provides a
candidate exponent for the velocity divergence before annihilation.

### 2C. High-Power & Complex Vortex Arrays

**Papers:**

7. **Fathi, Barros & Gumenyuk** — *Power-Scalable Generation of High-Order
   Optical Vortices Via Coherent Beam Combining.*
   arXiv: [2512.19815](https://arxiv.org/abs/2512.19815) (Dec 2025).
   - 100 W / 100 kW at ℓ = 1, 5, 8; efficiencies 95.0%, 93.9%, 91.2%.

8. **Fan, Cao, Chong & Zhan** — *Polygonal Spatiotemporal Optical Vortices
   Wavepackets with Prescribed Vortex Structure.*
   arXiv: [2512.16308](https://arxiv.org/abs/2512.16308) (Dec 2025).
   - First polygonal STOV wavepackets with prescribed sub-STOV geometry.

9. **Das & Ciappina** — *Optical Vortices: Revolutionizing the field of linear
   and nonlinear optics.*
   arXiv: [2510.27200](https://arxiv.org/abs/2510.27200) (Oct 2025).
   - Comprehensive review of OAM beams across linear and nonlinear regimes.

**Grammar connection:** At K > 1, the grammar implies multistability
(coexisting OAM states from tongue overlap) and tongue-internal cascades.
Computation shows SB-adjacent tongues overlap first (K ~ 1.5), with all
observed overlaps at SB-distance 1 up to K ~ 4. The l-to-rotation-number
mapping for OAM states has not been established; for distant charges
(e.g., l = 2 and l = 20), the 1D circle map is insufficient and
higher-dimensional maps may be needed.

### 2D. Quantum Simulations

**Paper:**

10. **Wang, Zhong, Wang et al.** — *Simulating fluid vortex interactions on a
    superconducting quantum processor.*
    arXiv: [2506.04023](https://arxiv.org/abs/2506.04023) (Jun 2025).
    Nature Communications 2026.
    - Navier-Stokes reformulated as quantum Hamiltonian; 8 qubits,
      99.97%/99.76% gate fidelities; reproduces multi-vortex interactions.

**Grammar connection:** Classical simulation cost grows exponentially with
Stern-Brocot depth of the target rotation number (window width ~ 0.458^depth
at K = 1.5, confirmed by computation). The cost is in parameter resolution,
not dynamical time-stepping. Whether quantum phase estimation achieves
polynomial overhead remains to be computed. K(Gamma, r, N) for interacting
point vortices has not been derived.

---

## 3. Status Classification

### Observed
- Phase singularities are universal topological defects (all 10 papers)
- Vortex-antivortex pair creation near horizons via BKT mechanism (Paper 2)
- Poynting-vector vortices create reverse energy flows and determine band gaps (Paper 5)
- Large wave vectors near intensity zeros with reverse energy flow (Paper 4)
- Superluminal singularity velocities before annihilation (Paper 6, Nature)
- Combining efficiency decreases with topological charge (Paper 7)
- Quantum processors simulate multi-vortex Navier-Stokes dynamics (Paper 10)

### Derived (gravity sector)
- Horizon = r = 0 = N = 0 (coherence = lapse, from Kuramoto-Einstein dictionary)
- K(x,x') = G_gamma(x,x') — coupling is the spatial Green's function, not a free parameter
- Synchronization cost functional as variational principle leading to Einstein equations
  at K = 1 in the continuum limit (Derivation 13, Proof Chain A)

### Open (K-mapping not derived for vortex systems)
- Hawking temperature from tongue-edge gradient: requires lattice-to-circle-map
  reduction for Paper 1's non-Hermitian system
- Quantum circuit depth proportional to Stern-Brocot depth: requires KAM bridge theorem for
  point-vortex Hamiltonians
- Photonic band gap width proportional to sqrt(K-1): requires K-to-index-contrast derivation
- OAM coexistence from tongue overlap: requires l-to-rotation-number mapping;
  1D circle map insufficient for distant charges

---

## 4. Computable Open Questions

### Q1: Hawking Temperature from Tongue-Edge Gradient

Open question: does Paper 1's non-Hermitian lattice Hamiltonian reduce to a
circle map under Floquet analysis? If so, the tongue-edge gradient yields
T_H = (hbar/2pi k_B) |d rho/d Omega| at the tongue edge, which can be
compared to the Parikh-Wilczek tunneling result. In the gravity sector, the
Kuramoto-Einstein dictionary already provides the horizon identification;
the question is whether Paper 1's specific system admits the same mapping.

### Q2: Quantum Circuit Depth and Stern-Brocot Depth

Open question: does the point-vortex Hamiltonian spectrum exhibit
rotation-number structure (as KAM theory would suggest)? If so, minimum
circuit depth should scale with depth_SB(p/q). Classical cost scaling has
been confirmed computationally (width ~ 0.458^depth); the quantum half
(polynomial overhead via phase estimation) remains to be computed.

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
| 9 | Optical vortices review | [2510.27200](https://arxiv.org/abs/2510.27200) | arXiv | Oct 2025 | 2C |
| 10 | Quantum vortex simulation | [2506.04023](https://arxiv.org/abs/2506.04023) | Nat. Commun. | Jun 2025 | 2D |

---

## 6. DAG Extension

Four ontology nodes bridge the grammar to vortex physics as candidate
instantiations (K-mapping open for each):

- **`analogue-horizon`** (L2) — horizon as λ < 0 → λ > 0 boundary.
  Gravity-sector K derived via Kuramoto-Einstein dictionary.
  Non-Hermitian lattice K: open.

- **`reverse-energy-flow`** (L2) — fold region F'(θ) < 0.
  Fold measure μ = arccos(1/K)/π exact. K ↔ Δn: open.

- **`vortex-array`** (L3) — multistability from tongue overlap at K > 1.
  K(phase noise, beams, ℓ): open.

- **`quantum-vortex-simulation`** (L3) — self-similar descent governs
  classical cost. K(Γ, r, N) for point vortices: open.

Two open questions (Level 4):

- `hawking-from-tongue-edge` — lattice reduction needed
- `circuit-depth-sb-depth` — KAM bridge needed

---

## 7. Next Steps

1. **Floquet reduction of Paper 1's lattice.** Apply Floquet analysis to
   the non-Hermitian tight-binding Hamiltonian of Munoz-Arboleda et al.
   (2507.03826) and determine whether a circle-map reduction exists. If
   it does, extract K(hopping asymmetry, gain/loss) and compare the
   resulting T_H to their Parikh-Wilczek result.

2. **K-derivation for photonic crystals.** Starting from the electromagnetic
   coupling structure in Pryamikov's 2D photonic crystal (2601.21704),
   compute K(Δn, geometry). Compare the fold measure sqrt(K-1) to observed
   band gap widths as a function of index contrast.

3. **Quantum phase estimation benchmark.** Using the confirmed classical
   cost scaling (window width ~ 0.458^depth at K = 1.5), compute the
   circuit depth required for quantum phase estimation to resolve rotation
   numbers at each SB depth. Benchmark against Wang et al.'s 8-qubit
   system (2506.04023).

4. **Coupled circle maps for distant OAM states.** Construct coupled
   circle maps on a torus to model OAM switching between distant charges
   (e.g., l = 2 and l = 20). Determine the minimum coupling topology
   that produces coexistence between SB-distant tongues.

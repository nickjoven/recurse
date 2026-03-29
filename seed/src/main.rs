mod schemas;

use canon_d::Canon;
use ket_cas::{Cid, Store as CasStore};
use ket_dag::{DagNode, NodeKind};
use serde_json::json;
use std::collections::HashMap;
use std::path::PathBuf;

fn ket_home() -> PathBuf {
    std::env::var("KET_HOME")
        .map(PathBuf::from)
        .unwrap_or_else(|_| PathBuf::from(".ket"))
}

/// Create a DAG node and store it in CAS, return the node CID.
fn create_dag_node(
    cas: &CasStore,
    kind: NodeKind,
    output_cid: Cid,
    agent: &str,
    schema_cid: Cid,
    saturation: f32,
    parents: Vec<Cid>,
    meta: Vec<(&str, &str)>,
) -> Cid {
    let mut node = DagNode::new(kind, parents, output_cid, agent)
        .with_schema(schema_cid)
        .with_saturation(saturation);
    for (k, v) in meta {
        node = node.with_meta(k, v);
    }
    let node_bytes = serde_json::to_vec(&node).expect("node serialization failed");
    cas.put(&node_bytes).expect("CAS write failed")
}

// ─── Node descriptor for batch creation ─────────────────────────────────────

struct OntologyEntry {
    level: u8,
    slug: &'static str,
    name: &'static str,
    description: &'static str,
    symbol: Option<&'static str>,
    tags: &'static [&'static str],
    /// Parent slugs — resolved after all content CIDs are created.
    parent_slugs: &'static [&'static str],
}

struct PredictionEntry {
    slug: &'static str,
    name: &'static str,
    description: &'static str,
    quantity: &'static str,
    predicted_value: &'static str,
    source_derivation: &'static str,
    testable_by: &'static str,
    /// Parent slugs in the ontology.
    parent_slugs: &'static [&'static str],
}

fn main() {
    let home = ket_home();
    let cas_path = home.join("cas");

    // Init or open CAS
    let cas = if cas_path.exists() {
        CasStore::open(cas_path).expect("failed to open CAS")
    } else {
        CasStore::init(&cas_path).expect("failed to init CAS")
    };

    // ── Store schemas ───────────────────────────────────────────────────
    let onto_schema = schemas::ontology_node_schema();
    let pred_schema = schemas::prediction_schema();
    let _obs_schema = schemas::observation_schema(); // stored for Phase 2

    let onto_schema_cid = cas
        .put(&onto_schema.to_canonical_bytes())
        .expect("schema write failed");
    let pred_schema_cid = cas
        .put(&pred_schema.to_canonical_bytes())
        .expect("schema write failed");
    let obs_schema_cid = cas
        .put(&_obs_schema.to_canonical_bytes())
        .expect("schema write failed");

    println!("ontology_node schema CID: {}", onto_schema_cid.as_str());
    println!("prediction schema CID:    {}", pred_schema_cid.as_str());
    println!("observation schema CID:   {}", obs_schema_cid.as_str());

    let onto_canon = Canon::new(&onto_schema);
    let pred_canon = Canon::new(&pred_schema);

    // ── Level 0 — the four primitives ───────────────────────────────────
    // These are roots. No parents. Same content → same CID as harmonics.
    //
    // ── Level 1 — derived structures ────────────────────────────────────
    // Each parents one or more Level 0 nodes.
    //
    // ── Level 2 — the algebra ───────────────────────────────────────────
    // Groups and equations that emerge from Level 1 structure.
    //
    // ── Level 3 — topology and cosmology ────────────────────────────────
    // Global structure: Klein bottle, modes, partitions.
    //
    // ── Level 4 — predictions (separate schema) ─────────────────────────
    // The leaves. What observations test.

    let ontology: Vec<OntologyEntry> = vec![
        // ── Level 0: Primitives ─────────────────────────────────────────
        OntologyEntry {
            level: 0,
            slug: "integers",
            name: "Integers",
            description: "The discrete substrate. Z as the free group on one generator. Counting precedes measuring.",
            symbol: Some("Z"),
            tags: &["primitive", "discrete", "group"],
            parent_slugs: &[],
        },
        OntologyEntry {
            level: 0,
            slug: "mediant",
            name: "Mediant operation",
            description: "Given a/b and c/d, the mediant (a+c)/(b+d). The operation that generates the Stern-Brocot tree from 0/1 and 1/0. Not averaging — concatenation of numerators and denominators.",
            symbol: Some("⊕"),
            tags: &["primitive", "operation", "farey"],
            parent_slugs: &[],
        },
        OntologyEntry {
            level: 0,
            slug: "fixed-point",
            name: "Fixed point",
            description: "A state that maps to itself under iteration. The golden ratio φ is the fixed point of x ↦ 1+1/x. Fixed points organize the dynamics: attractors, repellers, and the boundaries between basins.",
            symbol: Some("x*"),
            tags: &["primitive", "dynamics", "attractor"],
            parent_slugs: &[],
        },
        OntologyEntry {
            level: 0,
            slug: "parabola",
            name: "Parabola",
            description: "The quadratic map x ↦ x² + c. Simplest nonlinear iterated system. Contains the Feigenbaum cascade, period-doubling, and the route to chaos. The logistic map is conjugate.",
            symbol: Some("x² + c"),
            tags: &["primitive", "nonlinear", "iteration", "feigenbaum"],
            parent_slugs: &[],
        },

        // ── Level 0.5: Immediate consequences of primitives ────────────
        OntologyEntry {
            level: 0,
            slug: "continued-fraction",
            name: "Continued fraction expansion",
            description: "Every real number has a unique continued fraction [a₀; a₁, a₂, ...]. The partial convergents ARE the Stern-Brocot path. Rational numbers terminate; irrationals don't. The golden ratio φ = [1;1,1,...] is the 'most irrational' — slowest to converge.",
            symbol: Some("[a₀; a₁, a₂, ...]"),
            tags: &["primitive", "expansion", "convergent"],
            parent_slugs: &["integers", "mediant"],
        },
        OntologyEntry {
            level: 0,
            slug: "golden-ratio",
            name: "Golden ratio φ",
            description: "φ = (1+√5)/2 ≈ 1.618. The fixed point of x ↦ 1+1/x. Continued fraction [1;1,1,...] — all 1s. The noble number: hardest to mode-lock, last to synchronize. The rotation number that organizes the devil's staircase.",
            symbol: Some("φ"),
            tags: &["primitive", "irrational", "noble", "fixed-point"],
            parent_slugs: &["fixed-point", "mediant"],
        },
        OntologyEntry {
            level: 0,
            slug: "feigenbaum-constants",
            name: "Feigenbaum constants",
            description: "δ = 4.6692... (period-doubling rate) and α = 2.5029... (orbit scaling). Universal constants of the parabola's route to chaos. Every unimodal map shares them. They encode how the quadratic fixed point destabilizes.",
            symbol: Some("δ = 4.669..., α = 2.502..."),
            tags: &["primitive", "universal", "chaos", "period-doubling"],
            parent_slugs: &["parabola", "fixed-point"],
        },

        // ── Level 1: Derived structures ─────────────────────────────────
        OntologyEntry {
            level: 1,
            slug: "circle-s1",
            name: "Circle S¹",
            description: "R/Z — the reals modulo 1. Phase lives here. The circle is where fixed points become rotation numbers, and where rational vs irrational dynamics diverge.",
            symbol: Some("S¹"),
            tags: &["derived", "topology", "phase"],
            parent_slugs: &["integers", "fixed-point"],
        },
        OntologyEntry {
            level: 1,
            slug: "stern-brocot-tree",
            name: "Stern-Brocot tree",
            description: "The complete binary tree of positive rationals generated by iterated mediants from 0/1 and 1/0. Every positive rational appears exactly once. Depth in the tree = continued fraction length. The tree IS the rationals, ordered.",
            symbol: None,
            tags: &["derived", "rationals", "tree", "continued-fraction"],
            parent_slugs: &["integers", "mediant"],
        },
        OntologyEntry {
            level: 1,
            slug: "circle-map",
            name: "Circle map",
            description: "θ ↦ θ + Ω - (K/2π)sin(2πθ). The standard map on S¹ parameterized by bare frequency Ω and coupling K. At K=0, free rotation. At K=1, the critical line where mode-locking tongues touch.",
            symbol: Some("θ_{n+1} = θ_n + Ω - (K/2π)sin(2πθ_n)"),
            tags: &["derived", "dynamics", "circle", "mode-locking"],
            parent_slugs: &["circle-s1", "parabola"],
        },
        OntologyEntry {
            level: 1,
            slug: "devils-staircase",
            name: "Devil's staircase",
            description: "The rotation number ρ(Ω) as a function of the bare frequency at K=1. A continuous, monotone, singular function: constant on every mode-locking plateau (rational ρ), yet maps [0,1] onto [0,1]. The measure of the plateaus is 1 — almost every Ω is locked.",
            symbol: Some("ρ(Ω)"),
            tags: &["derived", "fractal", "singular", "measure"],
            parent_slugs: &["circle-map", "stern-brocot-tree"],
        },
        OntologyEntry {
            level: 1,
            slug: "arnold-tongues",
            name: "Arnold tongues",
            description: "In the (Ω, K) parameter plane, the set of parameters giving rotation number p/q forms a tongue-shaped region rooted at (p/q, 0). Width at height K scales as (K/2)^q for small K. The tongue structure is the Stern-Brocot tree made visible in parameter space.",
            symbol: None,
            tags: &["derived", "parameter-space", "mode-locking", "tongue"],
            parent_slugs: &["circle-map", "stern-brocot-tree"],
        },
        OntologyEntry {
            level: 1,
            slug: "rotation-number",
            name: "Rotation number",
            description: "ρ = lim_{n→∞} θ_n/n. The asymptotic average advance per iterate. Rational ρ = p/q means period-q orbit (mode-locked). Irrational ρ means quasiperiodic (drifting). The rotation number is the observable that the Stern-Brocot tree enumerates.",
            symbol: Some("ρ"),
            tags: &["derived", "dynamics", "observable", "rational-irrational"],
            parent_slugs: &["circle-map", "continued-fraction"],
        },
        OntologyEntry {
            level: 1,
            slug: "farey-graph",
            name: "Farey graph",
            description: "Two fractions a/b and c/d are Farey neighbors iff |ad-bc|=1. The Farey graph is the adjacency graph of the Stern-Brocot tree — connecting each fraction to its mediants. It tiles the hyperbolic plane with ideal triangles. SL(2,Z) is its automorphism group.",
            symbol: None,
            tags: &["derived", "graph", "adjacency", "hyperbolic"],
            parent_slugs: &["stern-brocot-tree", "mediant"],
        },
        OntologyEntry {
            level: 1,
            slug: "stribeck-curve",
            name: "Stribeck curve",
            description: "The friction-velocity relationship: static friction → Stribeck minimum → viscous rise. In the synchronization framework, the coupling function K(v) replaces the constant K in the circle map. Setting the Stribeck parameter δ=1/2 reproduces the MOND interpolation function.",
            symbol: Some("K(v)"),
            tags: &["derived", "friction", "coupling", "interpolation"],
            parent_slugs: &["circle-map", "parabola"],
        },
        OntologyEntry {
            level: 1,
            slug: "period-doubling-cascade",
            name: "Period-doubling cascade",
            description: "As the parabola parameter c increases, stable fixed points bifurcate: period 1→2→4→8→... The ratio of successive bifurcation intervals converges to Feigenbaum's δ. At the accumulation point: chaos. The cascade is universal for all unimodal maps.",
            symbol: Some("2^n → chaos"),
            tags: &["derived", "bifurcation", "universal", "route-to-chaos"],
            parent_slugs: &["parabola", "feigenbaum-constants"],
        },

        // ── Level 2: The algebra ────────────────────────────────────────
        OntologyEntry {
            level: 2,
            slug: "field-equation",
            name: "Field equation",
            description: "The synchronization cost functional whose Euler-Lagrange equation gives the field equation. Coupling cost + drift cost, extremized. The dark-matter dual variable emerges as the KKT multiplier of the Hamiltonian constraint.",
            symbol: Some("δS/δg = 0"),
            tags: &["algebra", "variational", "field-equation"],
            parent_slugs: &["circle-map", "fixed-point"],
        },
        OntologyEntry {
            level: 2,
            slug: "sl2z",
            name: "SL(2,Z)",
            description: "The modular group. 2×2 integer matrices with determinant 1. Acts on the Stern-Brocot tree by Möbius transformations. The automorphism group of the Farey graph. Encodes how rational approximations transform.",
            symbol: Some("SL(2,Z)"),
            tags: &["algebra", "group", "modular", "discrete"],
            parent_slugs: &["stern-brocot-tree", "integers"],
        },
        OntologyEntry {
            level: 2,
            slug: "sl2r",
            name: "SL(2,R)",
            description: "The continuous completion of SL(2,Z). Real 2×2 matrices with determinant 1. The isometry group of the hyperbolic plane. Stern-Brocot paths are geodesics in the Poincaré upper half-plane under this group.",
            symbol: Some("SL(2,R)"),
            tags: &["algebra", "group", "continuous", "hyperbolic"],
            parent_slugs: &["sl2z", "circle-s1"],
        },
        OntologyEntry {
            level: 2,
            slug: "d-equals-3",
            name: "Spatial dimension d=3",
            description: "Three spatial dimensions emerge from the Stern-Brocot tree structure: the tree has branching number 2, and 2+1=3 independent directions are needed to embed it without crossings. Equivalently: SL(2,R) acts on R³ via the adjoint representation.",
            symbol: Some("d=3"),
            tags: &["algebra", "dimension", "emergent"],
            parent_slugs: &["sl2r", "stern-brocot-tree"],
        },
        OntologyEntry {
            level: 2,
            slug: "lorentz-group",
            name: "Lorentz group",
            description: "SO(3,1) — the isometry group of Minkowski spacetime. Isomorphic to SL(2,C)/Z₂. Emerges when SL(2,R) is complexified to accommodate both spatial rotations and hyperbolic boosts.",
            symbol: Some("SO(3,1)"),
            tags: &["algebra", "group", "spacetime", "lorentz"],
            parent_slugs: &["sl2r", "d-equals-3"],
        },
        OntologyEntry {
            level: 2,
            slug: "signature-3-1",
            name: "(3,1) signature",
            description: "Three space dimensions, one time dimension. The signature follows from the Lorentz group structure: 3 rotation generators (compact, spatial) and 3 boost generators (non-compact, temporal mixing). Time is the non-compact direction.",
            symbol: Some("(3,1)"),
            tags: &["algebra", "spacetime", "signature"],
            parent_slugs: &["lorentz-group", "d-equals-3"],
        },
        OntologyEntry {
            level: 2,
            slug: "hyperbolic-plane",
            name: "Hyperbolic plane H²",
            description: "The Poincaré upper half-plane with metric ds² = (dx²+dy²)/y². SL(2,R) acts by isometries. The Farey graph embeds as the ideal triangulation. Stern-Brocot paths are geodesics. Hyperbolic distance between fractions encodes continued-fraction complexity.",
            symbol: Some("H²"),
            tags: &["algebra", "geometry", "hyperbolic", "poincare"],
            parent_slugs: &["sl2r", "farey-graph"],
        },
        OntologyEntry {
            level: 2,
            slug: "synchronization-cost",
            name: "Synchronization cost functional",
            description: "S[g, θ] = ∫(coupling cost + drift cost). The action whose extremization gives the field equation. Coupling cost ~ K·(1-cos Δθ) penalizes phase mismatch. Drift cost ~ (dθ/dt - Ω)² penalizes deviation from natural frequency. The balance determines dynamics.",
            symbol: Some("S[g, θ]"),
            tags: &["algebra", "variational", "action", "cost"],
            parent_slugs: &["field-equation", "circle-map", "stribeck-curve"],
        },
        OntologyEntry {
            level: 2,
            slug: "mobius-transformation",
            name: "Möbius transformation",
            description: "z ↦ (az+b)/(cz+d) with ad-bc=1. The action of SL(2,Z) on rationals and SL(2,R) on the upper half-plane. Preserves the Farey neighbor relation. Maps circles to circles. The group of 'rational rearrangements' — how one Stern-Brocot address transforms to another.",
            symbol: Some("z ↦ (az+b)/(cz+d)"),
            tags: &["algebra", "transformation", "conformal", "projective"],
            parent_slugs: &["sl2z", "sl2r"],
        },

        // ── Level 3: Topology and cosmology ─────────────────────────────
        OntologyEntry {
            level: 3,
            slug: "klein-bottle",
            name: "Klein bottle",
            description: "The non-orientable surface formed by identifying opposite edges of a square with one pair reversed. In the circle map context: identifying θ with -θ (time-reversal) while identifying Ω with Ω+1 (periodicity). The Klein bottle is the natural parameter space for the circle map with symmetry.",
            symbol: Some("K²"),
            tags: &["topology", "non-orientable", "parameter-space"],
            parent_slugs: &["circle-s1", "arnold-tongues"],
        },
        OntologyEntry {
            level: 3,
            slug: "four-modes",
            name: "Four modes",
            description: "The Klein bottle's fundamental domain under the circle map symmetry group has four distinguished regions: locked/drifting × orientation-preserving/reversing. These four modes map to the four forces in the synchronization framework: gravity, electromagnetism, weak, strong.",
            symbol: Some("4"),
            tags: &["topology", "modes", "forces", "symmetry-breaking"],
            parent_slugs: &["klein-bottle", "field-equation"],
        },
        OntologyEntry {
            level: 3,
            slug: "farey-partition",
            name: "Farey partition F₆ (13/19)",
            description: "The Farey sequence of order 6 contains 13 fractions. The Klein bottle's fundamental domain, triangulated by Farey fractions up to order 6, has 13 vertices and 19 edges. This (13,19) pair fixes the Farey order and determines the partition of parameter space into tongue regions.",
            symbol: Some("F₆ → (13, 19)"),
            tags: &["topology", "farey", "partition", "combinatorial"],
            parent_slugs: &["klein-bottle", "stern-brocot-tree", "sl2z"],
        },
        OntologyEntry {
            level: 3,
            slug: "figure-eight",
            name: "Figure-eight (Möbius band)",
            description: "The immersion of the Klein bottle in R³ produces a figure-eight cross-section. The self-intersection curve is the Möbius band — the complement of every consolidation. Every convergence generates its residual through this topological structure.",
            symbol: Some("∞"),
            tags: &["topology", "mobius", "complement", "residual"],
            parent_slugs: &["klein-bottle", "lorentz-group"],
        },
        OntologyEntry {
            level: 3,
            slug: "conservation-as-computability",
            name: "Conservation as computability",
            description: "Conservation laws (energy, momentum, charge) correspond to computable invariants of the DAG. A quantity is conserved iff its value can be verified by tracing the Merkle proof chain from leaves to roots. Non-conservation = non-computability of the invariant.",
            symbol: None,
            tags: &["topology", "conservation", "computability", "invariant"],
            parent_slugs: &["figure-eight", "four-modes", "signature-3-1"],
        },
        OntologyEntry {
            level: 3,
            slug: "cosmological-constant",
            name: "Cosmological constant Λ",
            description: "The vacuum energy density. In the synchronization framework: Λ is the residual drift cost when all modes are maximally locked. The fraction of parameter space NOT covered by Arnold tongues at the critical coupling. Related to a₀ via a₀ = c√(Λ/3)/2π.",
            symbol: Some("Λ"),
            tags: &["topology", "cosmology", "vacuum", "residual"],
            parent_slugs: &["farey-partition", "synchronization-cost"],
        },
        OntologyEntry {
            level: 3,
            slug: "stern-brocot-address",
            name: "Stern-Brocot address system",
            description: "Every positive rational has a unique address in the Stern-Brocot tree: a binary string of L(eft) and R(ight) turns. This address IS the continued fraction read differently. Stars get addresses by converting T_eff/T_CMB to a continued fraction. The address places each star on the Farey graph.",
            symbol: Some("LRLRL..."),
            tags: &["topology", "address", "encoding", "stellar"],
            parent_slugs: &["stern-brocot-tree", "farey-graph", "hyperbolic-plane"],
        },
        OntologyEntry {
            level: 3,
            slug: "tongue-occupation",
            name: "Arnold tongue occupation distribution",
            description: "The empirical question: how many stars land at each Farey fraction? The population N(p/q) at fraction p/q should scale as (K/2)^q if the stellar population follows the circle map dynamics. This is the bridge between algebraic prediction and stellar observation.",
            symbol: Some("N(p/q) ∝ (K/2)^q"),
            tags: &["topology", "distribution", "empirical", "bridge"],
            parent_slugs: &["arnold-tongues", "stern-brocot-address", "devils-staircase"],
        },
    ];

    let predictions: Vec<PredictionEntry> = vec![
        PredictionEntry {
            slug: "spectral-tilt",
            name: "Spectral tilt n_s",
            description: "The CMB spectral index. Predicted from the devil's staircase self-similarity at the golden ratio fixed point: n_s = 1 - 1/φ⁴ where φ = (1+√5)/2. The deviation from scale-invariance IS the fixed-point correction.",
            quantity: "n_s",
            predicted_value: "1 - 1/phi^4 ≈ 0.8541 (or from mode-locking: ≈ 0.9649)",
            source_derivation: "sync_cost/derivations/04_spectral_tilt_reframed.md",
            testable_by: "Planck 2018: n_s = 0.9649 ± 0.0042",
            parent_slugs: &["devils-staircase", "fixed-point", "farey-partition"],
        },
        PredictionEntry {
            slug: "mond-scale",
            name: "MOND acceleration scale a₀",
            description: "The acceleration below which galactic dynamics deviates from Newtonian gravity. Predicted as a₀ = cH₀/2π — the acceleration at which synchronization coupling cost equals drift cost. Not a free parameter: determined by the Hubble rate.",
            quantity: "a_0",
            predicted_value: "cH_0 / (2 pi) ≈ 1.2e-10 m/s²",
            source_derivation: "sync_cost/derivations/03_a0_threshold.md",
            testable_by: "Galaxy rotation curves (SPARC): a₀ ≈ 1.2e-10 m/s²",
            parent_slugs: &["field-equation", "circle-map", "conservation-as-computability"],
        },
        PredictionEntry {
            slug: "dark-energy-fraction",
            name: "Dark energy fraction Ω_Λ",
            description: "The fraction of the universe's energy density in dark energy. Predicted from the Farey partition: Ω_Λ ∈ [13/19, 11/16]. The 13/19 lower bound is the Klein bottle's Farey-6 vertex/edge ratio. The 11/16 upper bound comes from the next Farey order correction.",
            quantity: "Omega_Lambda",
            predicted_value: "13/19 ≈ 0.6842 to 11/16 = 0.6875",
            source_derivation: "farey_partition → klein_bottle → (13,19)",
            testable_by: "Planck 2018 + BAO: Ω_Λ = 0.6847 ± 0.0073",
            parent_slugs: &["farey-partition", "klein-bottle", "fixed-point"],
        },
        PredictionEntry {
            slug: "hierarchy-ratio",
            name: "Hierarchy ratio (gravity/electroweak)",
            description: "The enormous ratio between the gravitational and electroweak scales. In the synchronization framework: the ratio of coupling constants across the four modes maps to the Stern-Brocot depth separation between the gravitational tongue (deepest, widest) and the electroweak tongue.",
            quantity: "M_Planck / v_EW",
            predicted_value: "~10^17 (from Stern-Brocot depth ratio)",
            source_derivation: "sync_cost/derivations/06_planck_scale.md",
            testable_by: "M_Planck ≈ 1.22e19 GeV, v_EW ≈ 246 GeV",
            parent_slugs: &["arnold-tongues", "four-modes", "sl2z"],
        },
        PredictionEntry {
            slug: "coupling-ratio",
            name: "Strong/electroweak coupling ratio",
            description: "The ratio α_s/α₂ at unification. Predicted from the Klein bottle mode structure: the four modes assign coupling strengths in ratio 27/8, emerging from the Stern-Brocot addresses of each mode's tongue.",
            quantity: "alpha_s / alpha_2",
            predicted_value: "27/8 = 3.375",
            source_derivation: "sync_cost/derivations/05_two_forces.md",
            testable_by: "PDG 2024: α_s(M_Z) = 0.1179, α₂(M_Z) ≈ 0.0338 → ratio ≈ 3.49",
            parent_slugs: &["four-modes", "arnold-tongues", "stern-brocot-tree"],
        },
        PredictionEntry {
            slug: "weinberg-angle",
            name: "Weinberg angle sin²θ_W",
            description: "The electroweak mixing angle. Predicted from the mode partition on the Klein bottle: sin²θ_W = 8/35, the fraction of the electroweak tongue area assigned to hypercharge vs isospin.",
            quantity: "sin2_theta_W",
            predicted_value: "8/35 ≈ 0.2286",
            source_derivation: "klein_bottle → four_modes → tongue_areas",
            testable_by: "PDG 2024: sin²θ_W = 0.23121 ± 0.00004",
            parent_slugs: &["four-modes", "klein-bottle", "farey-partition"],
        },
        PredictionEntry {
            slug: "three-generations",
            name: "Three fermion generations",
            description: "Exactly three generations of fermions. Predicted from the Klein bottle topology: π₁(K²) = Z ⋊ Z, and the fundamental domain under the modular group has exactly 3 inequivalent cusps. Each cusp is a generation.",
            quantity: "N_gen",
            predicted_value: "3",
            source_derivation: "klein_bottle → modular_cusps",
            testable_by: "LEP: N_ν = 2.984 ± 0.008 (from Z width)",
            parent_slugs: &["klein-bottle", "sl2z", "four-modes"],
        },
        PredictionEntry {
            slug: "spatial-dimension",
            name: "Spatial dimension d=3",
            description: "Three macroscopic spatial dimensions. Not an input — derived from the Stern-Brocot branching structure requiring 3 independent directions for consistent embedding.",
            quantity: "d",
            predicted_value: "3",
            source_derivation: "stern_brocot_tree → sl2r → adjoint_rep",
            testable_by: "Direct observation: we point in three directions",
            parent_slugs: &["d-equals-3"],
        },
        PredictionEntry {
            slug: "tongue-width-scaling",
            name: "Arnold tongue width scaling exponent",
            description: "The width of the p/q tongue at coupling K scales as (K/2)^q. This is exact for the standard circle map and predicted to hold for the stellar population distribution. The exponent q is the Stern-Brocot depth — the continued fraction length.",
            quantity: "W(p/q, K)",
            predicted_value: "(K/2)^q",
            source_derivation: "circle_map → arnold_tongues → stern_brocot_depth",
            testable_by: "Stellar population counts at each Farey fraction from Gaia DR3",
            parent_slugs: &["tongue-occupation", "arnold-tongues"],
        },
        PredictionEntry {
            slug: "a0-lambda-relation",
            name: "MOND-Λ relationship",
            description: "The MOND acceleration scale is not independent of the cosmological constant: a₀ = c√(Λ/3)/2π. Both emerge from the synchronization cost at different scales. This relation is a prediction, not an input.",
            quantity: "a_0 / c * sqrt(3/Lambda)",
            predicted_value: "2 pi",
            source_derivation: "sync_cost/derivations/03_a0_threshold.md",
            testable_by: "Planck Λ + SPARC a₀: ratio ≈ 2π within 10%",
            parent_slugs: &["mond-scale", "cosmological-constant"],
        },
    ];

    // ── Phase 1: Seed ontology nodes ────────────────────────────────────
    // Two passes: first create all content CIDs, then create DAG nodes with parents.

    // Pass 1: content CIDs (no parents needed)
    let mut slug_to_content_cid: HashMap<String, Cid> = HashMap::new();

    for entry in &ontology {
        let tags_json: Vec<serde_json::Value> = entry
            .tags
            .iter()
            .map(|t| serde_json::Value::String(t.to_string()))
            .collect();

        let mut value = json!({
            "level": entry.level.to_string(),
            "slug": entry.slug,
            "name": entry.name,
            "description": entry.description,
        });

        if let Some(sym) = entry.symbol {
            value["symbol"] = json!(sym);
        }
        if !entry.tags.is_empty() {
            value["tags"] = json!(tags_json);
        }

        let canonical = onto_canon.encode(&value).expect("canonical encoding failed");
        let content_cid = cas.put(&canonical).expect("CAS write failed");
        slug_to_content_cid.insert(entry.slug.to_string(), content_cid);
    }

    // Pass 2: DAG nodes with parent edges
    let mut slug_to_node_cid: HashMap<String, Cid> = HashMap::new();

    println!("\n── Seeding {} ontology nodes ──", ontology.len());

    for entry in &ontology {
        let content_cid = slug_to_content_cid[entry.slug].clone();

        let parents: Vec<Cid> = entry
            .parent_slugs
            .iter()
            .filter_map(|s| slug_to_node_cid.get(*s).cloned())
            .collect();

        let node_cid = create_dag_node(
            &cas,
            NodeKind::Reasoning,
            content_cid,
            "recurse-seed",
            onto_schema_cid.clone(),
            // Level 0 primitives are axiomatic (saturation 1.0)
            // Higher levels have saturation proportional to their derivation completeness
            match entry.level {
                0 => 1.0,
                1 => 0.9,
                2 => 0.8,
                3 => 0.7,
                _ => 0.5,
            },
            parents,
            vec![
                ("level", &entry.level.to_string()),
                ("slug", entry.slug),
                ("name", entry.name),
            ],
        );

        slug_to_node_cid.insert(entry.slug.to_string(), node_cid.clone());

        let depth_marker = match entry.level {
            0 => "●",
            1 => "├",
            2 => "│├",
            3 => "││├",
            _ => "│││├",
        };

        println!(
            "  L{} {} {} → {}",
            entry.level,
            depth_marker,
            entry.slug,
            &node_cid.as_str()[..16]
        );
    }

    // ── Seed prediction leaves (Level 4) ────────────────────────────────
    println!("\n── Seeding {} prediction leaves ──", predictions.len());

    for pred in &predictions {
        let value = json!({
            "slug": pred.slug,
            "predicted_value": pred.predicted_value,
            "name": pred.name,
            "description": pred.description,
            "quantity": pred.quantity,
            "source_derivation": pred.source_derivation,
            "testable_by": pred.testable_by,
        });

        let canonical = pred_canon.encode(&value).expect("prediction encoding failed");
        let content_cid = cas.put(&canonical).expect("CAS write failed");

        let parents: Vec<Cid> = pred
            .parent_slugs
            .iter()
            .filter_map(|s| slug_to_node_cid.get(*s).cloned())
            .collect();

        let node_cid = create_dag_node(
            &cas,
            NodeKind::Reasoning,
            content_cid,
            "recurse-seed",
            pred_schema_cid.clone(),
            0.0, // predictions start at 0 saturation — observations must confirm them
            parents,
            vec![
                ("slug", pred.slug),
                ("quantity", pred.quantity),
                ("predicted_value", pred.predicted_value),
            ],
        );

        slug_to_node_cid.insert(pred.slug.to_string(), node_cid.clone());

        println!(
            "  L4 │││├ {} ({} = {}) → {}",
            pred.slug,
            pred.quantity,
            pred.predicted_value,
            &node_cid.as_str()[..16]
        );
    }

    // ── Summary ─────────────────────────────────────────────────────────
    let mut level_counts = [0u32; 5];
    for entry in &ontology {
        level_counts[entry.level as usize] += 1;
    }
    let pred_count = predictions.len();

    println!("\n── Summary ──");
    println!("  Level 0 (primitives):      {}", level_counts[0]);
    println!("  Level 1 (derived):         {}", level_counts[1]);
    println!("  Level 2 (algebra):         {}", level_counts[2]);
    println!("  Level 3 (topology):        {}", level_counts[3]);
    println!("  Level 4 (predictions):     {}", pred_count);
    println!(
        "  Total nodes:               {}",
        ontology.len() + pred_count
    );
    println!("  Schemas stored:");
    println!("    ontology_node: {}", onto_schema_cid.as_str());
    println!("    prediction:    {}", pred_schema_cid.as_str());
    println!("    observation:   {}", obs_schema_cid.as_str());
    println!("\n  Ready for Phase 2: stellar observations via Gaia DR3 TAP queries.");
    println!("  Each star → normalize → hash → embed → link. Idempotent.");
    println!("  Same star sown twice produces same CID.");
}

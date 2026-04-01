# Proposals: Claim Visualizer & Universe Substrate

## 1. Claim / Concept Visualizer

### Problem

The DAG in ket CAS is machine-readable (CIDs, canonical bytes, parent edges) but
human-opaque. You can't currently see *why* a prediction like `Omega_Lambda = 13/19`
traces back through `farey-partition → klein-bottle → circle-s1 → integers`.
The console output is a flat list. The structure IS the argument — so the
visualizer is not decoration, it's the primary interface for evaluating claims.

### Proposal: DAG Provenance Explorer

A local-first web UI (single HTML + JS, no framework) that reads the ket CAS
directly and renders the 5-level ontology as an interactive provenance graph.

**Core view: derivation trace**

```
[prediction leaf]  ←  click any prediction
       │
   ┌───┴───┐
   │       │        ← parent edges become visible paths
 [L3]    [L2]
   │    ┌──┴──┐
 [L1] [L1]  [L0]   ← you see the full argument chain
```

Each node shows:
- **Name + symbol** (e.g., "Klein bottle K²")
- **Saturation bar** — 0.0 (untested prediction) to 1.0 (axiom). Color gradient
  from red (0.0) through amber to green (1.0). This is the trust signal.
- **Description** on hover/click (the "why this concept exists" text already in CAS)
- **Testable_by** for predictions (the empirical anchor)

**Concrete interaction model:**

1. **Start at leaves.** Default view shows 10 prediction nodes as cards:
   `n_s ≈ 0.9649`, `a₀ ≈ 1.2e-10`, `Ω_Λ ∈ [13/19, 11/16]`, etc.
   Each card shows predicted value vs. observed value side by side.

2. **Pull the thread.** Click a prediction → the DAG unfolds upward, showing
   every concept in its derivation chain. Nodes animate in from the bottom.
   You can see: "this prediction depends on 7 concepts across 4 levels."

3. **Highlight shared structure.** When two predictions share parent nodes,
   those nodes glow. This makes the theory's parsimony visible: 10 predictions
   trace back to 4 primitives. The bottleneck nodes (like `circle-map` or
   `stern-brocot-tree`, which appear in many derivation chains) are visually
   larger.

4. **Saturation as trust.** Level 0 primitives glow solid green (saturation 1.0).
   As you move up the tree toward predictions, saturation decreases — the color
   shifts. Predictions start at 0.0 (red). When observations confirm them
   (Phase 2+), saturation rises and the node visually "fills in."

**Why this beats a static diagram:**

- The DAG is *content-addressed*. Rerunning the seed produces identical CIDs.
  The visualizer can diff two runs and show what changed.
- Observations (Phase 2) will add nodes. The visualizer shows new evidence
  flowing into the graph, updating saturation in real time.
- The provenance chain is *verifiable* — each edge is a Merkle proof.
  The visualizer can verify integrity, not just display structure.

**Implementation:**

| Component | Tech | Why |
|-----------|------|-----|
| Layout | d3-force or dagre | DAG-native layout, handles 53 nodes easily |
| Rendering | SVG (not canvas) | Nodes need to be individually interactive |
| Data source | Read `.ket/cas/` directly via Rust CLI that dumps JSON | Keep CAS as source of truth |
| Hosting | `file://` or `python -m http.server` | No deploy needed |

New binary: `recurse-viz` in the workspace. Reads CAS, emits a single
`index.html` with embedded JSON + d3. No server, no build step, no npm.

```
seed/          ← existing
viz/
  Cargo.toml
  src/main.rs  ← reads CAS, emits index.html
  template.html ← d3 visualization template
```

The `viz` binary walks the CAS, reconstructs the DAG, serializes it to JSON,
and injects it into the HTML template. Output: one self-contained file you
open in a browser.

---

## 2. Universe Substrate

### The honest question first

> "Only if this is more intuitive than existing public offerings for understanding
> the cosmos"

Existing tools:
- **Stellarium / WorldWide Telescope**: 3D star catalogs. Beautiful, comprehensive,
  but they show *where* things are, not *why* they're there.
- **Gaia Sky**: Gaia data rendered in 3D. Excellent for spatial exploration.
  No theoretical structure overlaid.
- **Cosmological simulations (Illustris, FIRE)**: N-body/hydro. Show structure
  formation. No connection to number theory or dynamical systems.

None of these answer: "Given a star's temperature, where does it land in
the number-theoretic structure of the Stern-Brocot tree, and does the
population distribution follow the predicted (K/2)^q scaling?"

That is a question no existing tool addresses. The universe substrate is
worth building **only for that specific question** — not as a general-purpose
sky viewer.

### Proposal: Farey Sky

A substrate that places real stars on the Stern-Brocot tree / Farey graph
according to their temperature ratio T_eff / T_CMB, then tests whether the
population statistics match the circle map predictions.

**The pipeline:**

```
Gaia DR3 TAP query
  → T_eff for ~1.5M stars (those with astrophysical parameters)
  → T_eff / T_CMB (= T_eff / 2.7255 K)
  → continued fraction expansion [a₀; a₁, a₂, ...]
  → truncate at depth D (e.g., D=6 to match F₆)
  → rational approximation p/q
  → Stern-Brocot address (L/R string)
  → place on Farey graph
  → store as observation node in ket CAS
```

Each star becomes a CAS node with schema `observation`:
```json
{
  "source": "Gaia DR3 <source_id>",
  "quantity": "T_eff",
  "value": "5778",
  "uncertainty": "50",
  "catalog": "gaiadr3.astrophysical_parameters",
  "stern_brocot_path": "LRLRL",
  "farey_address": "8/5"
}
```

**The visualization that matters:**

Not a sky map. A **tongue occupation histogram**:

```
N(p/q)
  │
  │ ██████████  1/1    ← most stars near T_eff/T_CMB ≈ 1? No —
  │ ████████    2/1       most stars are much hotter
  │ ██████      3/2
  │ ████        5/3
  │ ███         8/5    ← Sun lands here (5778/2.7255 ≈ 2120 → CF → p/q)
  │ ██          ...
  │ █
  └──────────────────── q (Stern-Brocot depth)
                        predicted: log N ∝ q·log(K/2)
```

**The test:** Plot log N(p/q) vs. q. If the slope matches log(K/2) for
some consistent K, the circle map prediction holds. If it doesn't, the
prediction is falsified. Either outcome is informative.

**Second view: Poincare disk**

The Farey graph tiles the hyperbolic plane. Render it in the Poincare disk
model (which already has well-known d3 implementations). Each Farey triangle
is colored by star count. Hotter regions of the disk = more occupied tongues.
The golden ratio φ sits at the boundary — the "most irrational" point, the
last to mode-lock, predicted to have the fewest stars nearby.

This view is genuinely novel. No public tool renders stellar populations
on the Farey tessellation of the hyperbolic plane.

**What this is NOT:**

- Not a planetarium replacement (use Stellarium for that)
- Not a general-purpose Gaia browser (use TOPCAT or Gaia Sky)
- Not a cosmological simulation

It is a **single hypothesis tester**: does the stellar temperature distribution
follow the Arnold tongue occupation scaling predicted by the circle map
framework?

### Implementation

```
substrate/
  Cargo.toml
  src/
    main.rs          ← orchestrator
    gaia.rs          ← TAP query client (async, reqwest)
    continued_fraction.rs  ← T_eff/T_CMB → [a₀;a₁,...] → p/q
    ingest.rs        ← observation → CAS node
  templates/
    histogram.html   ← tongue occupation plot (d3)
    poincare.html    ← Farey graph on hyperbolic disk (d3)
```

**Phase 2a** (data): Query Gaia DR3 TAP endpoint for stars with `teff_gspphot`.
~1.5M rows. Store locally as observations in ket CAS. Idempotent — same star
same CID.

**Phase 2b** (analysis): Compute continued fractions, bin by Farey address,
fit log N vs q. Emit the histogram and Poincare views.

**Phase 2c** (connection): Link observation nodes back to the prediction nodes
(`tongue-width-scaling`, `tongue-occupation`). Update saturation based on
fit quality. The claim visualizer (Proposal 1) then shows predictions
transitioning from red (0.0) to green as data confirms or denies them.

---

## How They Connect

```
┌─────────────────────┐     ┌─────────────────────┐
│  Claim Visualizer   │     │  Universe Substrate  │
│  (Proposal 1)       │     │  (Proposal 2)        │
│                     │     │                      │
│  Shows the DAG:     │     │  Adds to the DAG:    │
│  concepts →         │◄────│  stars →             │
│  predictions →      │     │  observations →      │
│  saturation         │     │  saturation updates  │
│                     │     │                      │
│  "Why do we predict │     │  "Here's what Gaia   │
│   Ω_Λ = 13/19?"    │     │   actually shows"    │
└─────────────────────┘     └─────────────────────┘
         │                           │
         └───────────┬───────────────┘
                     │
              ┌──────┴──────┐
              │  ket CAS    │
              │  (shared)   │
              │  BLAKE3 CIDs│
              └─────────────┘
```

The visualizer is the **reading** interface. The substrate is the **writing**
interface. Both operate on the same content-addressed store. The CIDs are the
glue — an observation node's parent edges point to the prediction nodes it
tests, and the visualizer renders that link as a visible connection between
"what we claimed" and "what we found."

---

## Recommended build order

1. **Claim Visualizer first.** The ontology DAG already exists in CAS. The
   visualizer makes the existing 53 nodes navigable today. No external
   dependencies, no API keys, no data downloads.

2. **Universe Substrate second.** Depends on Gaia TAP (external API), needs
   the continued-fraction pipeline, and produces results that only become
   meaningful when viewed through the claim visualizer.

3. **Saturation feedback loop third.** Wire observation fit quality back into
   prediction node saturation. This is the moment the system becomes
   self-updating: new data changes what you see in the visualizer.

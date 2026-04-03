# Framework: From Counting to Coupling

A guide to the mental model, written for skeptics.

---

## 0. What this document does

The ontology DAG contains 37 nodes across 4 levels. The nodes are terse.
A reader encountering them would see names — *mediant*, *Arnold tongues*,
*devil's staircase* — without understanding **why** these specific concepts
connect or what physical content the connections carry.

This document builds the chain from the ground up. Each step follows from
the previous one by a single move. No step requires physics beyond what a
second-year undergraduate knows. The physics emerges at the end, not the
beginning.

---

## 1. Integers and the Mediant

Start with two fractions: 0/1 and 1/0.

The first is zero. The second is a formal symbol meaning "infinity" — the
endpoint. Between any two fractions a/b and c/d, define the **mediant**:

```
    a/b ⊕ c/d  =  (a+c)/(b+d)
```

This is not averaging. It concatenates numerators and denominators separately.

Apply the mediant once to our two endpoints:

```
    0/1 ⊕ 1/0  =  1/1
```

Now we have three points: 0/1, 1/1, 1/0. Apply the mediant to each
adjacent pair:

```
    0/1 ⊕ 1/1  =  1/2
    1/1 ⊕ 1/0  =  2/1
```

Continue. At the next level:

```
    0/1 ⊕ 1/2  =  1/3       1/2 ⊕ 1/1  =  2/3
    1/1 ⊕ 2/1  =  3/2       2/1 ⊕ 1/0  =  3/1
```

This process generates the **Stern-Brocot tree**: a binary tree in which
every positive rational number appears **exactly once**, in lowest terms,
in its natural order. The integers and the mediant operation are sufficient
to enumerate all rationals. Nothing else is needed.

The Stern-Brocot tree is not an arbitrary enumeration.
It is the unique binary tree of rationals with the property that every
fraction's ancestors are its best rational approximants. The tree encodes
the structure of rational approximation.

Reference: Graham, Knuth & Patashnik, *Concrete Mathematics* (1994), §4.5.

---

## 2. Continued Fractions Are the Same Structure

Every real number x has a continued fraction expansion:

```
    x = a₀ + 1/(a₁ + 1/(a₂ + 1/(a₃ + ...)))
```

written [a₀; a₁, a₂, a₃, ...]. The partial quotients a₀, a₁, a₂, ...
are positive integers (except a₀ which may be 0 or negative).

Truncating the continued fraction at depth n gives the
convergent pₙ/qₙ, and the sequence of convergents p₀/q₀, p₁/q₁, p₂/q₂, ...
traces a path down the Stern-Brocot tree. The continued fraction expansion
and the Stern-Brocot address are two notations for the same object.

- **Rationals** have finite continued fractions. They terminate. They are
  nodes at finite depth in the tree.
- **Irrationals** have infinite continued fractions. They never terminate.
  They are infinite paths through the tree — limits of sequences of rationals,
  never reached exactly.

The golden ratio φ = [1; 1, 1, 1, ...] has all partial quotients equal
to 1. This makes its convergents (1/1, 2/1, 3/2, 5/3, 8/5, 13/8, ...)
the slowest to converge of any continued fraction. In a precise sense,
φ is the most poorly approximable irrational: the hardest to approximate
by rationals, the deepest path through the tree that avoids settling near
any rational.

A rational number p/q represents a pattern that repeats after q steps.
An irrational represents a pattern that never repeats, but the continued
fraction tells you how close it comes to repeating at each depth. The
partial quotients measure the degree of near-repetition. Small partial
quotients mean "almost periodic"; large ones mean "far from any period."

Reference: Hardy & Wright, *An Introduction to the Theory of Numbers*
(6th ed., 2008), Chapters 10–11.

---

## 3. The Circle: Where Rationals Become Periods

Now add a single geometric object: the circle S¹ = R/Z (the real line
modulo 1). A point on the circle is an angle θ ∈ [0, 1).

Define the simplest possible dynamical system on the circle — pure rotation:

```
    θ_{n+1} = θ_n + Ω    (mod 1)
```

The parameter Ω is the **bare frequency**: how far the point advances per
step. This is the **K = 0** case.

The **rotation number** ρ is the long-run average advance:

```
    ρ = lim_{n→∞} (θ_n - θ_0) / n
```

At K = 0, the rotation number is exactly Ω. Nothing happens to it. But the
nature of the orbit depends entirely on whether Ω is rational or irrational:

- **Ω = p/q (rational):** the orbit is periodic with period q. After q
  steps, the point returns to where it started. The orbit visits exactly
  q distinct points on the circle, evenly spaced.

- **Ω irrational:** the orbit is **quasiperiodic**. It never repeats. It
  visits infinitely many distinct points. By Weyl's equidistribution theorem,
  these points become uniformly dense on the circle as n → ∞.

So at K = 0, the Stern-Brocot tree classifies all possible orbit types:
each rational p/q in the tree corresponds to a distinct periodic orbit,
and the irrationals (infinite paths) correspond to quasiperiodic orbits.

At K = 0, one observes periodic and quasiperiodic motion: clocks,
planetary orbits (approximately), uncoupled oscillators. The Stern-Brocot
tree is a catalog of all possible periods and near-periods.

At this stage there is no coupling, so the tree classifies orbits without affecting them.

Reference: Katok & Hasselblatt, *Introduction to the Modern Theory of
Dynamical Systems* (1995), §4.1.

---

## 4. The Circle Map: Coupling as Interference

Now introduce coupling. The **standard circle map** is:

```
    θ_{n+1} = θ_n + Ω - (K/2π) sin(2πθ_n)    (mod 1)
```

Two parameters:
- **Ω** — the bare frequency (what the oscillator *wants* to do)
- **K** — the coupling strength (how strongly the oscillator is pulled
  toward or away from certain phases)

The sin term is the simplest periodic function that can couple the phase
back to itself. It represents **interference** in the most literal sense:
the current phase θ_n affects the next phase θ_{n+1}, creating a feedback
loop between where you are and where you go.

The rotation number ρ(Ω, K) now depends on both parameters. It is no longer
simply equal to Ω — the coupling can **shift** the effective frequency.

Concretely, consider an oscillator with natural frequency Ω coupled to
a periodic forcing (or to another oscillator, or to a lattice). The
coupling K measures how strongly the external signal interferes with the
natural oscillation. The rotation number ρ measures what the oscillator
actually does under the combined influence of its own frequency and the
coupling.

This is the setting for:
- A pendulum driven by a periodic force
- A Josephson junction in a microwave field
- A neuron receiving periodic synaptic input
- A laser in a ring cavity with feedback
- Two coupled metronomes on a shared platform
- A charge-density wave driven by an electric field

The circle map is the normal form for any periodically forced oscillator
near a resonance. Every system listed above reduces to the circle map (or
its generalization) in the appropriate limit.

Reference: Arnold, *Geometrical Methods in the Theory of Ordinary
Differential Equations* (1983), §11; Jensen, Bak & Bohr, "Transition to
chaos by interaction of resonances in dissipative systems", Phys. Rev. A
**30** (1984) 1960.

---

## 5. K = 0: Free Rotation

At K = 0, as described above:

```
    θ_{n+1} = θ_n + Ω
```

- Rotation number ρ = Ω exactly
- Rational Ω → period-q orbit
- Irrational Ω → quasiperiodic dense orbit
- The graph of ρ(Ω) is the identity line: ρ = Ω

This is the baseline. Every oscillator evolves independently. There is
no synchronization and no frequency-locking. The Stern-Brocot tree
classifies orbits but has no dynamical effect — it serves only as a
classification scheme.

---

## 6. 0 < K < 1: Mode-Locking (The Subcritical Regime)

When coupling is introduced, the dynamics change qualitatively.

For each rational p/q in the Stern-Brocot tree, there is now a **range**
of bare frequencies Ω that all produce the *same* rotation number ρ = p/q.
The oscillator is **pulled** into the nearby rational frequency and locked
there. This range is called an **Arnold tongue**.

The tongue for the rational p/q:
- Is rooted at (Ω, K) = (p/q, 0) — a single point at K = 0
- Opens into a tongue-shaped region as K increases
- Has width proportional to **(K/2)^q** for small K

That last fact is critical. The width depends on q — the **denominator** of
the rational, which is the **depth** in the Stern-Brocot tree. Fractions
with small denominators (1/1, 1/2, 2/3) have wide tongues — they lock
easily. Fractions with large denominators (8/13, 13/21) have narrow
tongues — they barely lock at all.

The **devil's staircase** is the graph of ρ(Ω) at a fixed K < 1. It is:
- A continuous function (no jumps)
- Non-decreasing (Ω goes up, ρ never goes down)
- Constant on every mode-locking plateau (the tongues)
- Yet maps [0,1] onto [0,1] (it reaches every value)

At 0 < K < 1, the set of mode-locked frequencies has **positive but less
than full measure**. There are still gaps — irrational rotation numbers
that are not locked. These correspond to quasiperiodic orbits that survive
the coupling.

At 0 < K < 1, the irrationals correspond to quasiperiodic orbits that
resist synchronization. The golden ratio φ, being the most poorly
approximable, is the last rotation number to be captured by a tongue.
The noble numbers (those whose continued fraction tails are all 1s,
like φ = [1;1,1,...]) form a hierarchy of resistance to mode-locking,
organized by the Stern-Brocot tree.

Experimental manifestations include frequency-locking in driven oscillators,
phase-locked loops in electronics, synchronization of cardiac pacemaker
cells, mode-locking in lasers, and resonance capture in celestial mechanics
(e.g., Pluto:Neptune = 2:3, Moon's spin:orbit = 1:1). The devil's staircase
has been directly measured in Josephson junctions and charge-density wave
systems.

The rotation number ρ is determined self-consistently. It cannot be
computed from Ω and K by a closed-form formula; one must iterate the map
and take a limit. The system finds its own effective frequency through the
interplay of its natural frequency and its coupling: the output (ρ)
depends on the dynamics, which depend on the output.

References:

- Arnold, "Small denominators. I: Mappings of the circumference onto
  itself", Izv. Akad. Nauk SSSR Ser. Mat. **25** (1961) 21–86.
  [The original paper defining the tongues.]
- Bak, "The devil's staircase", Physics Today **39**(12) (1986) 38–45.
  [Accessible introduction to mode-locking.]
- Jensen, Bak & Bohr, Phys. Rev. A **30** (1984) 1960.
  [Tongue width scaling, devil's staircase measurement.]
- Bohr, Bak & Jensen, "Transition to chaos by interaction of resonances
  in dissipative systems. II. Josephson junctions, charge-density waves,
  and standard maps", Phys. Rev. A **30** (1984) 1970.
  [Experimental devil's staircase in physical systems.]

---

## 7. K = 1: The Critical Line

At K = 1, the circle map reaches a critical transition.

```
    θ_{n+1} = θ_n + Ω - (1/2π) sin(2πθ_n)
```

The derivative of the map with respect to θ touches zero at one point
(θ = 0). The map is still continuous but is **no longer invertible** at
this point — it has a cubic inflection. This is the edge of a fold.

At K = 1:
- The Arnold tongues have grown to **fill the entire parameter line**.
  The total measure of mode-locked frequencies is 1.
- The devil's staircase is **complete**: it is constant almost everywhere
  (on a set of measure 1), yet still continuous and surjective.
- The irrational rotation numbers survive only on a set of **measure zero**
  — they are dense but infinitely rare.
- The staircase is a **singular function**: continuous everywhere,
  differentiable almost everywhere (with derivative 0), yet non-constant.
  It increases without ever having a positive derivative — it rises only
  on the measure-zero set of irrationals.

K = 1 is the boundary between two qualitatively different regimes. Below
K = 1, irrational rotation numbers have positive measure — quasiperiodic
orbits occupy a finite fraction of phase space. At K = 1, they are
squeezed to measure zero but still exist as topological limits. Above
K = 1, the map folds, and the devil's staircase framework breaks.

The approach to the critical point at the golden ratio rotation number
exhibits universal scaling exponents.
The sequence of mode-locked intervals converging on φ from above and below
scales with ratios related to the Feigenbaum constants and to the
continued fraction structure. Specifically, at the golden-mean fixed
point of the renormalization operator, there are two critical exponents:

- σ = −1.2886... (the eigenvalue governing the relevant direction)
- The scaling of tongue widths near the golden ratio follows from the
  renormalization group fixed point.

This universality means that the critical behavior does not depend on the
details of the sin coupling — any smooth circle map with the same
inflection type gives the same exponents. The universality class is
determined by the topology (the circle), the order of the inflection
(cubic), and the number-theoretic properties of the rotation number
(continued fraction structure).

The critical transition at K = 1 has been measured in Josephson junction
arrays, where the voltage steps (Shapiro steps) are the physical
manifestation of Arnold tongues, and the transition from incomplete to
complete mode-locking corresponds to the junction reaching its critical
current.

References:

- Shenker, "Scaling behavior in a map of a circle onto itself: empirical
  results", Physica D **5** (1982) 405–411.
  [First identification of the critical exponents.]
- Feigenbaum, Kadanoff & Shenker, "Quasiperiodicity in dissipative systems:
  a renormalization group analysis", Physica D **5** (1982) 370–386.
  [Renormalization group analysis at the golden-mean fixed point.]
- Ostlund, Rand, Sethna & Siggia, "Universal properties of the transition
  from quasi-periodicity to chaos in dissipative systems", Physica D **8**
  (1983) 303–342.
  [Comprehensive analysis of the critical line.]
- Cvitanović, Shraiman & Söderberg, "Scaling laws for mode lockings in
  circle maps", Physica Scripta **32** (1985) 263–270.
  [Tongue-width scaling and its relation to thermodynamic formalism.]

---

## 8. Summary of What We Have

```
    K = 0           0 < K < 1            K = 1
    ─────           ─────────            ─────
    Free rotation   Mode-locking         Complete staircase
    ρ = Ω           ρ locked on tongues  Tongues fill measure 1
    No coupling     Weak coupling        Critical coupling
    SB tree is      SB tree governs      SB tree fully realized
     just a catalog  tongue hierarchy      as singular function

    Irrationals:    Irrationals:         Irrationals:
    dense, full     dense, positive      dense, measure zero
    measure         measure (gaps)       (topological limits)

    Physics:        Physics:             Physics:
    free oscillators synchronization     critical current,
    clocks, orbits  PLLs, Josephson      onset of chaos,
                    cardiac sync         Shapiro steps
```

The progression from K = 0 to K = 1 is a single story:

Integers generate the Stern-Brocot tree via the mediant. The tree
classifies all rotation numbers (periods and quasi-periods) of the
simplest dynamical system on the circle. Turning on coupling (the sin
term) causes rational rotation numbers to lock into tongues whose widths
are governed by continued fraction depth. At the critical coupling K = 1,
the tongues fill everything, the devil's staircase is complete, and the
irrationals (the quasiperiodic orbits that resisted locking) are squeezed
to measure zero — but they never vanish, and their structure (the golden
ratio at the top, the noble numbers below) governs the universal scaling
at the critical point.

Every concept in this chain is standard mathematics. Every physical
manifestation listed above has been experimentally verified. The references
are to foundational papers, not to our framework — this is the shared
ground from which any extension must be justified.

---

## 9. The Algebraic Collapse at K > 1

### What breaks

At K ≤ 1, the circle map is a **homeomorphism** — a continuous bijection
with continuous inverse. It preserves the topological structure of S¹.
Every orbit type is classified cleanly by a single rotation number. The
devil's staircase is a well-defined function: one Ω, one ρ.

At K > 1, the map is no longer injective. It has **critical points** — values
of θ where the derivative vanishes and changes sign. The map **folds** the
circle onto itself: two distinct phases can be sent to the same image.

This single failure — loss of injectivity — causes four algebraic
properties that the K ≤ 1 framework depends on to break down:

**1. The staircase ceases to be a function.**

At K ≤ 1, the rotation number ρ(Ω) is monotone non-decreasing: increasing
the bare frequency never decreases the effective frequency. This monotonicity
follows from the fact that the map preserves the circular order of points.

At K > 1, the map can reverse circular order (the fold crosses points over
each other). The rotation number ρ(Ω) is **no longer monotone**. It can
decrease as Ω increases. The devil's staircase develops **overhangs** —
it bends back on itself. A single value of ρ can be achieved at multiple
non-contiguous intervals of Ω.

The graph of ρ(Ω) is no longer the graph of a function. It is a **relation**.

**2. Tongues overlap.**

At K ≤ 1, the Arnold tongues are disjoint: the tongue for p/q and the tongue
for p'/q' do not intersect (they are separated by the gap containing
irrationals between p/q and p'/q' in the Farey sequence). The Farey neighbor
condition |pq' - p'q| = 1 governs adjacency — neighboring tongues touch
only at K = 1, exactly at the boundary.

At K > 1, tongues **cross into each other's territory**. A single parameter
value (Ω, K) can lie inside the tongue for p/q *and* inside the tongue for
p'/q' simultaneously. The Farey neighbor constraint, which enforced
separation, is violated.

Physically: the same oscillator, at the same parameter values, can lock to
*either* of two different frequencies depending on initial conditions. This
is **multistability** — and it has no counterpart in the K ≤ 1 theory.

**3. The conjugacy to rotation breaks.**

The Denjoy theorem guarantees that for K ≤ 1 (smooth enough homeomorphisms),
every irrational rotation number corresponds to a map that is topologically
conjugate to a rigid rotation. The dynamics, however complex they look, are
equivalent to simple rotation by a coordinate change.

At K > 1, this theorem does not apply. The fold creates orbits that are not
conjugate to any rotation. Period-doubling cascades, intermittency, and
chaotic trajectories have no rotational equivalent. The topological
classification scheme (by rotation number alone) is **insufficient** to
describe the dynamics.

**4. Self-consistency becomes multi-valued.**

At K ≤ 1, the self-consistency condition uniquely determines ρ: given
(Ω, K), the system finds one rotation number. The dynamics are
deterministic in parameter space.

At K > 1, the self-consistency condition has **multiple solutions**.
Several rotation numbers are simultaneously consistent with the same
parameters. Which one the system selects depends on its history — the
initial condition, the path through parameter space, hysteresis. The
rotation number is no longer a function of parameters; it is a function
of parameters **and history**.

### The precise algebraic statement

Let F: R → R be the lift of the circle map, satisfying F(x+1) = F(x) + 1.

At K ≤ 1, F is **strictly increasing**: F'(x) > 0 for all x (except at
most one point where F'(x) = 0 at K = 1). This makes f: S¹ → S¹ a
homeomorphism.

At K > 1, F has **local extrema**: there exist x₁ < x₂ such that
F'(x₁) = 0, F''(x₁) < 0 (local max) and F'(x₂) = 0, F''(x₂) > 0
(local min). The map f is a degree-1 endomorphism but not a homeomorphism.

The fold region is the interval [x₁, x₂] where F is decreasing. Its width
grows as K - 1. In this region, two points are mapped to the same image:
F(x₁ - δ) = F(x₂ + δ') for appropriate δ, δ'.

The rotation number ρ = lim_{n→∞} Fⁿ(x)/n still exists for every x
(this is a theorem — the limit exists for degree-1 continuous maps of the
circle). For a given map (fixed Ω, K), this limit is the same for
*almost every* initial condition x. But the critical orbits (those passing
through the fold) can shadow different periodic orbits, creating the
coexistence of attractors that is multistability.

### What survives the collapse

The collapse is not total. Three structures persist through K > 1:

**The Stern-Brocot tree is arithmetic, not dynamic.** It enumerates the
rationals by the mediant operation. This structure exists independently of
any dynamical system. At K > 1, the rationals don't change — what changes
is how the dynamics *uses* them. The tree still classifies which mode-locked
islands exist. It no longer guarantees they are disjoint or uniquely
accessible.

**Continued fractions still govern approximation.** The best rational
approximants to any real number are still the Stern-Brocot convergents.
This remains true at K > 1 because it is a theorem about numbers, not
about maps. What changes is the physical consequence: at K ≤ 1, the best
approximant determines which tongue captures an irrational orbit. At K > 1,
multiple tongues compete, and the "winner" depends on basin geometry.

**The widest tongues persist.** The tongues with small q (1/1, 1/2, 1/3,
2/3) — the shallowest levels of the Stern-Brocot tree — are the widest.
They grow as (K/2)^q, so small-q tongues dominate at any K. Even as
tongues overlap and internal structure develops, the large-scale
organization by q persists. The low-order resonances remain the most
prominent features of the parameter space.

### What emerges

The fold creates new structure that has no K ≤ 1 counterpart:

**Period-doubling within tongues.** Inside the p/q tongue, for K
sufficiently above 1, the period-q attracting orbit loses stability and
bifurcates to period 2q, then 4q, then 8q, ..., accumulating at a
Feigenbaum point where the orbit becomes chaotic. The cascade rate converges
to δ = 4.6692... (the Feigenbaum constant, already in the ontology at
Level 0). Each tongue recapitulates the structure of the logistic map.

**Chaotic bands.** Between the remnant mode-locked islands, and beyond the
Feigenbaum accumulation points within tongues, there are parameter regions
with positive Lyapunov exponent — genuine chaos. The measure of these chaotic
regions grows with K - 1.

**Periodic windows within chaos.** Inside the chaotic bands, there are
narrow windows of periodic behavior — smaller mode-locked islands. These
windows are organized by the **same Stern-Brocot structure** that organized
the original Arnold tongues. The tree recapitulates at every scale: within
each chaotic band, the largest windows have the smallest q, and the window
widths scale with continued-fraction depth.

The Stern-Brocot tree does not vanish at K > 1. It reappears inside each
chaotic region at smaller scales, governing
the hierarchy of periodic windows just as it governed the hierarchy of
Arnold tongues at K < 1. The Feigenbaum renormalization group is the
mechanism of this descent — each period-doubling cascade carries the
tree's structure to a smaller scale.

### The diagnostic that replaces the staircase

At K ≤ 1, the devil's staircase ρ(Ω) is the complete diagnostic: it tells
you everything about the dynamics.

At K > 1, the rotation number alone is insufficient. The replacement is the
**Lyapunov exponent** λ(Ω, K):

```
    λ = lim_{n→∞} (1/n) Σ log|f'(θᵢ)|
```

This measures the average rate of divergence of nearby orbits.

- λ < 0 : mode-locked (attracting periodic orbit) — inside a tongue
- λ = 0 : critical boundary, or quasiperiodic (at K ≤ 1)
- λ > 0 : chaotic — sensitive dependence on initial conditions

The graph of λ(Ω) at K > 1 replaces the devil's staircase as the primary
diagnostic. It is negative on the mode-locked islands, positive in the
chaotic bands, and zero at the transitions. The tongue structure is still
visible (the dips to λ < 0), but the chaotic regions (λ > 0) are new.

### What we need but do not yet have

To extend the framework through K > 1, we need:

1. **The Lyapunov exponent as a DAG-level concept.** It replaces ρ(Ω) as
   the primary observable. The existing node `rotation-number` (L1) needs a
   sibling: `lyapunov-exponent` (L1), parented by `circle-map` and `parabola`.

2. **The period-doubling connection to tongues.** The existing node
   `period-doubling-cascade` (L1) is currently parented only by `parabola`
   and `feigenbaum-constants`. It needs a parent edge to `arnold-tongues` —
   because period-doubling occurs *within* tongues at K > 1.

3. **The self-similar descent.** A new concept: the Stern-Brocot structure
   reappearing at smaller scales within chaotic bands. This connects
   `stern-brocot-tree` to `period-doubling-cascade` in a way the current
   DAG does not represent.

4. **Multistability.** A new concept: the coexistence of multiple
   attractors at the same parameter values. This is the direct consequence
   of tongue overlap and has no K ≤ 1 analogue.

These four additions would make the K > 1 regime representable in the DAG.
The vortex bridge nodes (`analogue-horizon`, `reverse-energy-flow`,
`vortex-array`, `quantum-vortex-simulation`) could then be re-parented
through the K > 1 structure rather than through the K < 1 tongue-width
formulas that the P2 computation showed are inapplicable.

References:

- Glass & Sun, "Bifurcations in flat-topped maps and the control of
  cardiac chaos", Int. J. Bifurcation and Chaos **4** (1994) 1061–1076.
  [Tongue overlap in non-invertible circle maps.]
- MacKay & Tresser, "Transition to topological chaos for circle maps",
  Physica D **19** (1986) 206–237.
  [What happens to rotation numbers when the map folds.]
- Cvitanović, Gunaratne & Vinson, "On the mode-locking universality for
  critical circle maps", Nonlinearity **3** (1990) 873–885.
  [Scaling of tongues and periodic windows through the critical line.]
- Lanford, "A computer-assisted proof of the Feigenbaum conjectures",
  Bull. Amer. Math. Soc. **6** (1982) 427–434.
  [Rigorous proof that the Feigenbaum cascade is universal.]

---

## 10. The Grammar and Its Instantiations

### What the grammar does

The circle map is the normal form for periodically forced oscillators
near resonance (Arnold 1983). The Stern-Brocot tree, Arnold tongues,
Feigenbaum cascades, Lyapunov exponents, tongue overlap, and self-similar
descent constitute the vocabulary of possible behaviors for such systems.

Given the coupling strength K, the grammar classifies dynamics:

- **K = 0:** periodic or quasiperiodic orbits, classified by the
  Stern-Brocot tree.
- **0 < K < 1:** mode-locking with tongue widths (K/2)^q; noble
  numbers resist longest.
- **K = 1:** complete staircase; universal scaling at the golden ratio.
- **K > 1:** tongue overlap (multistability), internal cascades
  (Feigenbaum), chaos between islands, self-similar descent of the
  Stern-Brocot hierarchy into each chaotic region.

### The K-mapping: where the physics lives

The grammar classifies behavior once K is known. Deriving K for a given
physical system is the system-specific physics:

| System | What determines K | Status |
|---|---|---|
| Gravity (continuum Kuramoto) | K(x,x') = G_γ(x,x'), the Green's function of the spatial Laplacian | Derived (see below) |
| Josephson junction | Ratio of drive current to critical current | Classical textbook |
| Cardiac pacemaker | Coupling strength between cells | Classical textbook |
| Non-Hermitian lattice | Hopping asymmetry, gain/loss ratio | Open |
| Photonic crystal | Refractive index contrast, geometry | Open |
| Optical vortex array | Phase noise, beam count, charge | Open |
| Point vortex system | Inter-vortex Hamiltonian, separation | Open |

The methodology: derive K for a given system from first principles, locate
it in the regime map, read off the behavior from the grammar, compare to
observation. For the gravity sector, this program has been completed. For
the vortex systems, it remains open.

### The gravity sector: K derived

The Kuramoto-Einstein dictionary (`proslambenomenos/kuramoto_einstein_mapping.md`)
provides an explicit mapping between continuum Kuramoto synchronization and
the ADM formulation of general relativity:

| Kuramoto field | ADM field | Interpretation |
|---|---|---|
| r(x,t) — local coherence | N — lapse function | Coherence is clock rate. Horizon = r = 0 = N = 0 |
| ∂ᵢψ — mean phase gradient | Nᵢ — shift vector | Phase gradients are coordinate drift |
| Cᵢⱼ — coherence tensor | γᵢⱼ — spatial metric | Synchronization structure is geometry |
| ω(x) — natural frequency | √(4πGρ) — Jeans frequency | Matter sets the natural frequency |
| K(x,x') — coupling kernel | G_γ(x,x') — spatial Green's function | Coupling propagates through geometry |

The self-consistency equation on the Stern-Brocot tree, at K = 1 in the
continuum limit, uniquely produces the Einstein field equations via
Lovelock's theorem (Derivation 13, Proof Chain A in
`harmonics/sync_cost/derivations/`). The synchronization cost functional
(`harmonics/sync_cost/FRAMEWORK.md`) is the variational principle.

If this identification holds, K is not a free parameter in the gravity
sector but is determined by the spatial geometry through the Green's
function. The grammar's outputs for the gravity sector then follow
without additional free parameters.

### The DAG structure

```
L0:  Integers, mediant, fixed point, parabola        [pure math]
      │
L1:  SB tree, circle map, tongues, staircase,        [grammar]
     Feigenbaum, Lyapunov, period-doubling
      │
L2:  Regime classification (K<1, K=1, K>1),          [grammar]
     multistability, tongue-internal cascade,
     self-similar descent, fold measure
      │
L3:  Instantiations                                  [physics]
     ├─ Gravity sector: K derived (Kuramoto-Einstein)
     └─ Candidate systems: K-mapping open
        (analogue-horizon, reverse-energy-flow,
         vortex-array, quantum-vortex-simulation)
      │
L4:  Open questions                                   [testable]
     ├─ Gravity sector (Ω_Λ, a₀, n_s, ...)
     └─ Vortex sector: conditional on K-derivation
```

For the gravity sector, the derivation chain from L0 to L4 is complete
(39 derivations in `harmonics/sync_cost/derivations/`). For the vortex
systems, deriving K is the open problem and the publishable contribution.

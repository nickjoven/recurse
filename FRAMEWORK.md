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

**Why this matters:** the Stern-Brocot tree is not an arbitrary enumeration.
It is the *unique* binary tree of rationals with the property that every
fraction's ancestors are its best rational approximants. The tree IS the
structure of rational approximation.

Reference: Graham, Knuth & Patashnik, *Concrete Mathematics* (1994), §4.5.

---

## 2. Continued Fractions Are the Same Structure

Every real number x has a continued fraction expansion:

```
    x = a₀ + 1/(a₁ + 1/(a₂ + 1/(a₃ + ...)))
```

written [a₀; a₁, a₂, a₃, ...]. The partial quotients a₀, a₁, a₂, ...
are positive integers (except a₀ which may be 0 or negative).

**Key fact:** truncating the continued fraction at depth n gives the
convergent pₙ/qₙ, and the sequence of convergents p₀/q₀, p₁/q₁, p₂/q₂, ...
traces a path down the Stern-Brocot tree. The continued fraction expansion
and the Stern-Brocot address are **two notations for the same object**.

- **Rationals** have finite continued fractions. They terminate. They are
  nodes at finite depth in the tree.
- **Irrationals** have infinite continued fractions. They never terminate.
  They are infinite paths through the tree — limits of sequences of rationals,
  never reached exactly.

The **golden ratio** φ = [1; 1, 1, 1, ...] has all partial quotients equal
to 1. This makes its convergents (1/1, 2/1, 3/2, 5/3, 8/5, 13/8, ...)
the slowest to converge of any continued fraction. In a precise sense,
φ is the **most irrational** number: the hardest to approximate by rationals,
the deepest path through the tree that avoids settling near any rational.

**What irrationals describe:** a rational number p/q represents a pattern
that repeats after q steps. An irrational represents a pattern that never
repeats — but the continued fraction tells you *how close* it comes to
repeating at each depth. The partial quotients measure the degree of
near-repetition. Small partial quotients mean "almost periodic"; large
ones mean "far from any period."

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

**What we can observe at K = 0:** periodic and quasiperiodic motion. Clocks.
Planetary orbits (approximately). Uncoupled oscillators. The Stern-Brocot
tree is a catalog of all possible periods and near-periods.

But nothing interesting has happened yet, because there is no coupling.

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

**The physical picture:** imagine an oscillator with natural frequency Ω.
Now couple it to a periodic forcing (or to another oscillator, or to a
lattice). The coupling K measures how strongly the external signal
interferes with the natural oscillation. The rotation number ρ measures
what the oscillator actually does under the combined influence of its
own frequency and the coupling.

This is the setting for:
- A pendulum driven by a periodic force
- A Josephson junction in a microwave field
- A neuron receiving periodic synaptic input
- A laser in a ring cavity with feedback
- Two coupled metronomes on a shared platform
- A charge-density wave driven by an electric field

The circle map is not a metaphor for these systems. It is the **normal form**
for any periodically forced oscillator near a resonance. Every system listed
above reduces to the circle map (or its generalization) in the appropriate
limit.

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

This is the baseline. Every oscillator does its own thing. No synchronization.
No frequency-locking. The Stern-Brocot tree classifies orbits but doesn't
*do* anything — it's just a filing system.

---

## 6. 0 < K < 1: Mode-Locking (The Subcritical Regime)

Turn on the coupling. Something new happens.

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

**What irrationals describe at 0 < K < 1:** the quasiperiodic orbits that
resist synchronization. The golden ratio φ, being the most irrational,
resists the longest. It is the last rotation number to be captured by a
tongue. The **noble numbers** (those whose continued fraction tails are
all 1s, like φ = [1;1,1,...]) form a hierarchy of resistance to
mode-locking, organized by the Stern-Brocot tree.

**What we can observe:** frequency-locking in driven oscillators. Phase-
locked loops in electronics. Synchronization of cardiac pacemaker cells.
Mode-locking in lasers. Resonance capture in celestial mechanics (e.g.,
Pluto:Neptune = 2:3, Moon's spin:orbit = 1:1). The devil's staircase has
been directly measured in Josephson junctions and charge-density wave
systems.

**Self-consistency:** the rotation number ρ is determined self-consistently.
You cannot compute it from Ω and K by a formula — you must iterate the map
and take a limit. The system finds its own effective frequency through the
interplay of its natural frequency and its coupling. This is what
"self-consistency" means: the output (ρ) depends on the dynamics, which
depend on the output.

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
  It increases without ever having a positive derivative. This is not a
  paradox; it rises only on the measure-zero set of irrationals.

**Why K = 1 matters:** it is the boundary between two qualitatively
different regimes. Below K = 1, irrational rotation numbers have positive
measure — quasiperiodic orbits occupy a finite fraction of phase space.
At K = 1, they are squeezed to measure zero but still exist as
topological limits. Above K = 1, the map folds, and the devil's staircase
framework breaks.

**Universal scaling at K = 1:** the approach to the critical point at
the golden ratio rotation number exhibits universal scaling exponents.
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

**What we can observe:** the critical transition at K = 1 has been measured
in Josephson junction arrays, where the voltage steps (Shapiro steps) are
the physical manifestation of Arnold tongues, and the transition from
incomplete to complete mode-locking corresponds to the junction reaching
its critical current.

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

**Integers** generate the **Stern-Brocot tree** via the **mediant**.
The tree classifies all **rotation numbers** (periods and quasi-periods)
of the simplest dynamical system on the **circle**. Turning on **coupling**
(the sin term) causes rational rotation numbers to **lock** into **tongues**
whose widths are governed by **continued fraction depth**. At the critical
coupling K = 1, the tongues fill everything, the **devil's staircase** is
complete, and the **irrationals** (the quasiperiodic orbits that resisted
locking) are squeezed to measure zero — but they never vanish, and their
structure (the golden ratio at the top, the noble numbers below) governs
the universal scaling at the critical point.

Every concept in this chain is standard mathematics. Every physical
manifestation listed above has been experimentally verified. The references
are to foundational papers, not to our framework — this is the shared
ground from which any extension must be justified.

---

## 9. What This Does Not Yet Cover

**K > 1** — the overcritical regime. The map folds. Tongues overlap.
Chaos appears. Period-doubling cascades emerge (governed by the Feigenbaum
constants, which are already in the ontology as Level 0 primitives). The
devil's staircase framework no longer applies directly, but the underlying
number-theoretic structure (Stern-Brocot tree, continued fractions, Farey
graph) persists in the organization of the remaining mode-locked islands
amid chaos.

This is where the vortex physics lives (P2's kill established K/2 > 1),
and it is where the framework must go next. But it cannot be built on
weak-coupling formulas. It requires the K > 1 phenomenology: Lyapunov
exponents, strange attractors, the measure of chaotic vs. locked regions,
and the Feigenbaum renormalization group.

The building blocks for K > 1 already exist in the ontology (`parabola`,
`feigenbaum-constants`, `period-doubling-cascade`). They are currently
disconnected from the vortex bridge nodes. Connecting them is the next
structural step.

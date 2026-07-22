# Measure Theory & Lebesgue Integration

Classical Riemann integration is sufficient for basic functions, but fails for highly discontinuous functions (such as the Dirichlet function). **Measure Theory** provides the rigorous generalization of length, area, and volume, underpinning modern Probability Theory and integration.

---

## Lecture 6 (Part 2): Outer Measure

To measure the "size" of arbitrary subsets of real numbers, we introduce the concept of **Outer Measure**.

### Definition of Outer Measure
The **Lebesgue outer measure** $\mu^*: \mathcal{P}(\mathbb{R}) \to [0, \infty]$ of a subset $A \subseteq \mathbb{R}$ is the infimum of the sum of lengths of open intervals that cover $A$:

$$\mu^*(A) = \inf \left\{ \sum_{n=1}^\infty (b_n - a_n) \mid A \subseteq \bigcup_{n=1}^\infty (a_n, b_n) \right\}$$

### Properties of Outer Measure
1.  **Empty Set**: $\mu^*(\emptyset) = 0$.
2.  **Monotonicity**: If $A \subseteq B$, then $\mu^*(A) \le \mu^*(B)$.
3.  **Countable Subadditivity**: For any countable collection of sets $\{A_n\}$, the outer measure of their union is bounded by the sum of their individual outer measures:

$$\mu^*\left(\bigcup_{n=1}^\infty A_n\right) \le \sum_{n=1}^\infty \mu^*(A_n)$$

---

## Lecture 7: Sigma Algebras ($\sigma$-algebras)

We cannot define a consistent measure on *all* subsets of $\mathbb{R}$ while preserving translation-invariance and countable additivity (due to Vitali sets). Therefore, we must restrict our measure to a collection of "well-behaved" sets called a $\sigma$-algebra.

### Definition of a $\sigma$-algebra
Let $X$ be a set. A collection $\Sigma$ of subsets of $X$ is a **$\sigma$-algebra** if it satisfies three axioms:
1.  **Contains the Whole Set**: $X \in \Sigma$.
2.  **Closed under Complement**: If $A \in \Sigma$, then $A^c = X \setminus A \in \Sigma$.
3.  **Closed under Countable Unions**: If $\{A_n\}_{n=1}^\infty \subseteq \Sigma$, then:

$$\bigcup_{n=1}^\infty A_n \in \Sigma$$

### The Borel $\sigma$-algebra ($\mathcal{B}(\mathbb{R})$)
The **Borel $\sigma$-algebra** on $\mathbb{R}$ is the smallest $\sigma$-algebra that contains all open intervals $(a, b)$. It includes all open sets, closed sets (as complements of open sets), countable intersections of open sets ($G_\delta$ sets), and countable unions of closed sets ($F_\sigma$ sets).

---

## Lecture 8: Lebesgue Measurable Sets & Measure

### Carathéodory's Condition
To select the well-behaved subsets of $\mathbb{R}$, we use Constantin Carathéodory's slicing condition.

A set $E \subseteq \mathbb{R}$ is **Lebesgue measurable** if it splits any arbitrary "test set" $A \subseteq \mathbb{R}$ additively:

$$\mu^*(A) = \mu^*(A \cap E) + \mu^*(A \cap E^c)$$

The collection of all Lebesgue measurable sets forms a $\sigma$-algebra, denoted by $\mathcal{M}$.

### The Lebesgue Measure ($\mu$)
When we restrict the outer measure $\mu^*$ to the $\sigma$-algebra of measurable sets $\mathcal{M}$, it is called the **Lebesgue measure** $\mu$. Unlike outer measure, the Lebesgue measure is **countably additive**:

If $\{E_n\}_{n=1}^\infty$ is a countable collection of pairwise disjoint measurable sets, then:

$$\mu\left(\bigcup_{n=1}^\infty E_n\right) = \sum_{n=1}^\infty \mu(E_n)$$

*   **Null Sets**: A set $N$ is a null set if $\mu^*(N) = 0$. Every subset of a null set is Lebesgue measurable (with measure 0), making the Lebesgue measure space complete.

---

## Lecture 9: Lebesgue Measurable Functions

In integration, we integrate functions. For a function to be integrable, it must map measurable sets to measurable sets.

### Definition of Measurable Functions
Let $(X, \Sigma)$ be a measurable space. A function $f: X \to \overline{\mathbb{R}}$ (where $\overline{\mathbb{R}} = \mathbb{R} \cup \{-\infty, \infty\}$) is **measurable** if the preimage of every open interval is a measurable set:

$$f^{-1}((a, \infty)) = \{x \in X \mid f(x) > a\} \in \Sigma \quad \text{for all } a \in \mathbb{R}$$

*   **Theorem**: If $\{f_n\}$ is a sequence of measurable functions, then the functions $\inf f_n$, $\sup f_n$, $\liminf f_n$, and $\limsup f_n$ are also measurable. If the pointwise limit $f(x) = \lim_{n \to \infty} f_n(x)$ exists, then $f$ is measurable.

---

## Lecture 10: Simple Functions & The Lebesgue Integral

To construct the Lebesgue integral, we build it from the bottom up, starting with simple step-like functions.

### Simple Functions
A **simple function** $\phi: X \to \mathbb{R}$ is a real-valued function that takes only a finite number of distinct values. It can be written in its **canonical representation**:

$$\phi(x) = \sum_{i=1}^n c_i \chi_{E_i}(x)$$

where:
- $c_i$ are distinct real numbers.
- $E_i = \{x \in X \mid \phi(x) = c_i\}$ are pairwise disjoint measurable sets.
- $\chi_{E_i}$ is the **indicator function** of $E_i$ ($\chi_{E_i}(x) = 1$ if $x \in E_i$, and $0$ otherwise).

### The Lebesgue Integral of Simple Functions
The **Lebesgue integral** of a non-negative simple function $\phi$ over a measurable set $E$ is defined as:

$$\int_{E} \phi \, d\mu = \sum_{i=1}^n c_i \mu(E_i \cap E)$$

*   **Constructing the General Lebesgue Integral**: For any non-negative measurable function $f$, its Lebesgue integral is defined as the supremum of the integrals of all simple functions bounded by $f$:
    $$\int_{E} f \, d\mu = \sup \left\{ \int_{E} \phi \, d\mu \mid 0 \le \phi \le f, \, \phi \text{ is simple} \right\}$$

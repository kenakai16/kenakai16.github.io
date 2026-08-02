# Lebesgue Measurable Functions

This lecture defines measurable functions, establishes their algebraic closure properties, and covers pointwise limit behavior.

---

## 1. Definition and Equivalence

*   **Definition**: Let $E \subseteq \mathbb{R}$ be measurable. A function $f: E \to [-\infty, \infty]$ is **Lebesgue measurable** if for all $\alpha \in \mathbb{R}$:
    
    $$f^{-1}((\alpha, \infty]) = \{x \in E \mid f(x) > \alpha\} \in \mathcal{M}$$

*   **Theorem**: The following conditions are equivalent for a function $f: E \to [-\infty, \infty]$:
    1.  For all $\alpha \in \mathbb{R}$, $f^{-1}((\alpha, \infty]) \in \mathcal{M}$.
    2.  For all $\alpha \in \mathbb{R}$, $f^{-1}([\alpha, \infty]) \in \mathcal{M}$.
    3.  For all $\alpha \in \mathbb{R}$, $f^{-1}([-\infty, \alpha)) \in \mathcal{M}$.
    4.  For all $\alpha \in \mathbb{R}$, $f^{-1}([-\infty, \alpha]) \in \mathcal{M}$.

    **Proof**:
    $(1 \implies 2)$ follows from $[\alpha, \infty] = \bigcap_{n=1}^\infty (\alpha - 1/n, \infty]$, which translates to a countable intersection of preimages.
    
    $(2 \implies 1)$ follows from $(\alpha, \infty] = \bigcup_{n=1}^\infty [\alpha + 1/n, \infty]$, which is a countable union.
    
    $(2 \iff 3)$ follows from complementation: $[-\infty, \alpha) = ([\alpha, \infty])^c$.
    
    $(3 \iff 4)$ is proved similarly.

*   **Theorem**: If $f: E \to \mathbb{R}$ is measurable, then for any Borel set $F \in \mathcal{B}$, $f^{-1}(F) \in \mathcal{M}$.
    
    *   **Corollary**: Every continuous function $f: \mathbb{R} \to \mathbb{R}$ is measurable.
    *   **Corollary**: The indicator function $\chi_F: E \to \mathbb{R}$ is measurable if and only if $F \cap E$ is measurable.

---

## 2. Algebraic Properties of Measurable Functions

*   **Theorem**: If $f, g: E \to \mathbb{R}$ are measurable and $c \in \mathbb{R}$, then $cf$, $f+g$, and $fg$ are measurable.

    **Proof Sketch**:
    For $f+g$, we use the density of the rationals:
    
    $$f(x) + g(x) > \alpha \iff \exists r \in \mathbb{Q} \text{ such that } f(x) > r > \alpha - g(x)$$
    
    Thus:
    
    $$(f+g)^{-1}((\alpha, \infty]) = \bigcup_{r \in \mathbb{Q}} \Big( f^{-1}((r, \infty]) \cap g^{-1}((\alpha - r, \infty]) \Big)$$
    
    Since $\mathbb{Q}$ is countable, this is a countable union of intersections of measurable sets, which is measurable.
    
    For $fg$, we show $f^2$ is measurable by checking preimages, then write $fg = \frac{1}{4} ((f+g)^2 - (f-g)^2)$.

---

## 3. Limit Behavior & "Almost Everywhere" (a.e.)

One of the key advantages of Lebesgue integration theory over Riemann integration is its robust behavior under pointwise limits.

*   **Theorem**: Let $f_n: E \to [-\infty, \infty]$ be a sequence of measurable functions. Then:
    
    $$g_1(x) = \sup_n f_n(x), \quad g_2(x) = \inf_n f_n(x), \quad g_3(x) = \limsup_{n\to\infty} f_n(x), \quad g_4(x) = \liminf_{n\to\infty} f_n(x)$$
    
    are all measurable.

    **Proof**:
    For $g_1$:
    
    $$x \in g_1^{-1}((\alpha, \infty]) \iff \sup_n f_n(x) > \alpha \iff \exists n \text{ such that } f_n(x) > \alpha \iff x \in \bigcup_n f_n^{-1}((\alpha, \infty])$$
    
    Since it is a countable union of measurable sets, $g_1$ is measurable. Similarly, $g_2$ is measurable using intersections.
    
    Since $\limsup f_n = \inf_n (\sup_{k \ge n} f_k)$ and $\liminf f_n = \sup_n (\inf_{k \ge n} f_k)$, $g_3$ and $g_4$ are measurable.

*   **Corollary**: If $f_n \to f$ pointwise, then $f$ is measurable.
    
    *   *Note*: This is false for Riemann integrable functions (e.g., the limit of piecewise continuous indicators of rational sequences converges pointwise to the Dirichlet function, which is not Riemann integrable).

*   **Definition**: A property holds **almost everywhere (a.e.)** on $E$ if the set of points where it does not hold has measure zero.
    
    *   **Theorem**: If $f = g$ a.e. on $E$ and $f$ is measurable, then $g$ is measurable.

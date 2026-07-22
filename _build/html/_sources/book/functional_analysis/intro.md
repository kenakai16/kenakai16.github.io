# Functional Analysis & Operator Theory

Functional Analysis is the branch of mathematics that generalizes linear algebra from finite-dimensional vector spaces to infinite-dimensional spaces. It provides the rigorous mathematical framework for quantum mechanics, differential equations, and advanced machine learning models (such as kernel methods, Support Vector Machines, and Reproducing Kernel Hilbert Spaces).

---

## Lecture 1: Basic Banach Space Theory

### Normed Vector Spaces
Let $X$ be a vector space over a field $K$ (where $K = \mathbb{R}$ or $\mathbb{C}$). A **norm** on $X$ is a function $\|\cdot\|: X \to \mathbb{R}$ satisfying three axioms for all $x, y \in X$ and $\alpha \in K$:
1.  **Positive Definiteness**: $\|x\| \ge 0$, and $\|x\| = 0$ if and only if $x = 0$.
2.  **Absolute Homogeneity**: $\|\alpha x\| = |\alpha| \|x\|$.
3.  **Triangle Inequality**: $\|x + y\| \le \|x\| + \|y\|$.

A vector space equipped with a norm is called a **normed vector space** $(X, \|\cdot\|)$.

### Completeness and Banach Spaces
A sequence $\{x_n\}$ in a normed space $X$ is a **Cauchy sequence** if for every $\epsilon > 0$, there exists an integer $N$ such that:

$$\|x_n - x_m\| < \epsilon \quad \text{for all } n, m \ge N$$

A normed space $X$ is **complete** if every Cauchy sequence in $X$ converges to a limit that also lies within $X$.

*   **Banach Space**: A complete normed vector space is called a **Banach space**.
*   **Examples**:
    - **Finite-Dimensional**: $\mathbb{R}^n$ and $\mathbb{C}^n$ are complete under any norm.
    - **Sequence Spaces**: $l^p$ spaces (the set of sequences whose $p$-th power sums are finite) are Banach spaces under the norm $\|x\|_p = (\sum |x_i|^p)^{1/p}$.
    - **Continuous Functions**: $C([a,b])$, the space of continuous functions on an interval, is a Banach space under the supremum norm $\|f\|_\infty = \sup_{t \in [a,b]} |f(t)|$.

---

## Lecture 2: Bounded Linear Operators

A function $T: X \to Y$ between two normed vector spaces is a **linear operator** if $T(\alpha x + \beta y) = \alpha Tx + \beta Ty$ for all $x, y \in X$ and scalars $\alpha, \beta$.

### Boundedness and Continuity
A linear operator $T: X \to Y$ is **bounded** if there exists a constant $M \ge 0$ such that:

$$\|Tx\|_Y \le M \|x\|_X \quad \text{for all } x \in X$$

*   **Theorem**: For a linear operator $T$, the following statements are equivalent:
    1. $T$ is continuous at $x = 0$.
    2. $T$ is continuous everywhere on $X$.
    3. $T$ is bounded.

### The Operator Norm
For a bounded linear operator $T: X \to Y$, the **operator norm** $\|T\|$ is defined as the supremum of the ratio of the output norm to the input norm:

$$\|T\| = \sup_{x \neq 0} \frac{\|Tx\|_Y}{\|x\|_X} = \sup_{\|x\|_X \le 1} \|Tx\|_Y$$

The set of all bounded linear operators from $X$ to $Y$ is denoted as $B(X, Y)$. If $Y$ is a Banach space, then $B(X, Y)$ is also a Banach space under the operator norm.

---

## Lecture 3: Quotient Spaces & The Baire Category Theorem

### Quotient Spaces
Let $X$ be a normed space and $M \subseteq X$ be a closed subspace. The **quotient space** $X/M$ is the set of equivalence classes (cosets) $[x] = x + M$ under the norm:

$$\|[x]\| = \inf_{m \in M} \|x - m\|$$

*   **Theorem**: If $X$ is a Banach space, then the quotient space $X/M$ is also a Banach space under this quotient norm.

### Baire Category Theorem
The Baire Category Theorem is a foundational topological property of complete metric spaces.

*   **Theorem**: Let $X$ be a complete metric space. If $X$ is written as a countable union of closed subsets $X = \bigcup_{n=1}^\infty F_n$, then at least one of the subsets $F_n$ must have a non-empty interior.
*   **Intuition**: A complete space cannot be constructed by gluing together a countable number of "thin" (nowhere dense) sets.

### Uniform Boundedness Principle (Banach-Steinhaus Theorem)
Using Baire's theorem, we can prove that pointwise boundedness of a family of operators implies uniform boundedness.

*   **Theorem**: Let $X$ be a Banach space and $Y$ be a normed space. Let $\mathcal{F} \subseteq B(X, Y)$ be a family of bounded linear operators. If for each $x \in X$, there exists $C_x \ge 0$ such that:
    $$\|Tx\|_Y \le C_x \quad \text{for all } T \in \mathcal{F}$$
    then the operators are uniformly bounded:
    $$\sup_{T \in \mathcal{F}} \|T\| < \infty$$

---

## Lecture 4: The Open Mapping & Closed Graph Theorems

These theorems describe the properties of linear operators between Banach spaces.

### The Open Mapping Theorem
A mapping $T: X \to Y$ is an **open map** if the image of every open set in $X$ is an open set in $Y$.

*   **Theorem**: Let $X$ and $Y$ be Banach spaces. If $T: X \to Y$ is a bounded linear operator that is surjective (onto), then $T$ is an open mapping.
*   **Bounded Inverse Theorem**: If a bounded linear operator $T: X \to Y$ between Banach spaces is bijective (one-to-one and onto), then its inverse $T^{-1}: Y \to X$ is automatically bounded.

### The Closed Graph Theorem
Let $T: X \to Y$ be an operator. The **graph** of $T$ is the set $\Gamma(T) = \{(x, Tx) \mid x \in X\} \subseteq X \times Y$. We say $T$ has a **closed graph** if $\Gamma(T)$ is a closed subspace of $X \times Y$ under the product norm.

*   **Theorem**: Let $X$ and $Y$ be Banach spaces. A linear operator $T: X \to Y$ is bounded if and only if its graph is closed.
*   **Practical Use**: To prove an operator is continuous, we only need to show that if $x_n \to 0$ and $Tx_n \to y$, then $y = 0$.

---

## Lecture 5: Zorn's Lemma & The Hahn-Banach Theorem

The Hahn-Banach Theorem guarantees that there are "enough" continuous linear functionals on a normed space to separate points.

### Zorn's Lemma
Zorn's Lemma is an axiom equivalent to the Axiom of Choice.
*   **Poset**: A set equipped with a partial order $\le$.
*   **Chain**: A subset of a poset where every pair of elements is comparable.
*   **Theorem**: If every chain in a poset $P$ has an upper bound in $P$, then $P$ contains at least one maximal element.

### The Hahn-Banach Extension Theorem
Let $X$ be a vector space and $p: X \to \mathbb{R}$ be a sublinear functional (satisfying $p(x+y) \le p(x) + p(y)$ and $p(\alpha x) = \alpha p(x)$ for $\alpha \ge 0$).

*   **Theorem (Real Vector Spaces)**: Let $M \subseteq X$ be a subspace, and $f: M \to \mathbb{R}$ be a linear functional bounded by $p$:
    $$f(x) \le p(x) \quad \text{for all } x \in M$$
    Then there exists a linear functional $F: X \to \mathbb{R}$ extending $f$ ($F(x) = f(x)$ for all $x \in M$) such that:
    $$F(x) \le p(x) \quad \text{for all } x \in X$$
*   **Normed Spaces Corollary**: Let $M$ be a subspace of a normed space $X$, and $f \in M^*$. Then $f$ can be extended to a functional $F \in X^*$ such that the norms are preserved:
    $$\|F\|_{X^*} = \|f\|_{M^*}$$

---

## Lecture 6 (Part 1): The Double Dual & Reflexivity

### The Dual Space ($X^*$)
For a normed space $X$, the space of all bounded linear functionals $f: X \to K$ is the **dual space** $X^* = B(X, K)$. Since the field $K$ ($\mathbb{R}$ or $\mathbb{C}$) is complete, $X^*$ is always a Banach space.

### The Double Dual ($X^{**}$)
The **double dual** (or bidual) $X^{**} = (X^*)^*$ is the dual of $X^*$.

There is a natural map called the **canonical injection** $J: X \to X^{**}$ defined by evaluating a functional at a point $x$:

$$J(x)(f) = f(x) \quad \text{for all } f \in X^*$$

*   **Theorem**: The canonical injection $J$ is an isometric isomorphism (it preserves norms: $\|J(x)\|_{X^{**}} = \|x\|_X$).
*   **Reflexive Spaces**: If $J$ is surjective (meaning $J(X) = X^{**}$), the Banach space $X$ is said to be **reflexive**.
*   **Examples**: All Hilbert spaces and $L^p$ spaces for $1 < p < \infty$ are reflexive. The spaces $L^1$ and $C([a,b])$ are not reflexive.

# The Double Dual & Outer Measure

This lecture discusses the canonical injection into the double dual space, defines reflexivity, and introduces the Lebesgue outer measure.

---

## 1. The Double Dual and Reflexivity

*   **Theorem**: Let $V$ be a normed space. For any $v \in V \setminus \{0\}$, there exists $f \in V'$ (the dual space) such that $\|f\| = 1$ and $f(v) = \|v\|$.

    **Proof**:
    Define $u: \mathbb{C}v \to \mathbb{C}$ on the span of $v$ by $u(\lambda v) = \lambda \|v\|$. Clearly, $|u(t)| \le \|t\|$ for all $t \in \mathbb{C}v$ and $u(v) = \|v\|$. By the Hahn-Banach Theorem, there exists an extension $f \in V'$ with $\|f\| \le 1$ and $f(v) = \|v\|$. Since $f(v/\|v\|) = 1$, we have $\|f\| = 1$.

*   **Definition**: The **double dual** $V''$ of a normed space $V$ is the dual space of $V'$. For any $v \in V$, the evaluation map $T_v: V' \to \mathbb{C}$ defined by $T_v(f) = f(v)$ is an element of $V''$.

*   **Theorem**: The canonical map $T: V \to V''$ sending $v \mapsto T_v$ is an isometric isomorphism into $V''$.

    **Proof**:
    Linearity is clear. For boundedness, $|T_v(f)| = |f(v)| \le \|v\| \|f\|$, so $\|T_v\| \le \|v\|$.
    For $v \neq 0$, choose $f \in V'$ with $\|f\| = 1$ and $f(v) = \|v\|$. Then:
    
    $$\|T_v\| \ge |T_v(f)| = |f(v)| = \|v\|$$
    
    Thus, $\|T_v\| = \|v\|$, and the map is isometric.

*   **Definition**: A Banach space $V$ is **reflexive** if the canonical map $T: V \to V''$ is surjective (onto).
    
    *   **Examples**: $\ell^p$ spaces for $1 < p < \infty$ are reflexive. $\ell^1$ and $c_0$ are not reflexive.

---

## 2. The Outer Measure of Real Subsets

To measure the size of arbitrary subsets of $\mathbb{R}$, we define the outer measure.

*   **Definition**: For any interval $I$, let $\ell(I)$ denote its length. The **Lebesgue outer measure** $m^*: \mathcal{P}(\mathbb{R}) \to [0, \infty]$ of a subset $A \subseteq \mathbb{R}$ is defined as:
    
    $$m^*(A) = \inf \left\{ \sum_{n=1}^\infty \ell(I_n) \;\middle|\; A \subseteq \bigcup_{n=1}^\infty I_n, \text{ where } I_n \text{ are open intervals} \right\}$$

*   **Theorem**: If $A \subseteq \mathbb{R}$ is countable, then $m^*(A) = 0$.

    **Proof**:
    Enumerate $A = \{a_1, a_2, \dots\}$. Fix $\epsilon > 0$. For each $n$, define the open interval:
    
    $$I_n = \left( a_n - \frac{\epsilon}{2^{n+1}}, a_n + \frac{\epsilon}{2^{n+1}} \right)$$
    
    Then $A \subseteq \bigcup_{n=1}^\infty I_n$. By definition:
    
    $$m^*(A) \le \sum_{n=1}^\infty \ell(I_n) = \sum_{n=1}^\infty \frac{\epsilon}{2^n} = \epsilon$$
    
    Since this holds for all $\epsilon > 0$, we have $m^*(A) = 0$.

*   **Theorem (Countable Subadditivity)**: Let $\{A_n\}_{n=1}^\infty$ be a countable family of subsets of $\mathbb{R}$. Then:
    
    $$m^*\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty m^*(A_n)$$

    **Proof**:
    If any $m^*(A_n) = \infty$, the inequality is trivial. Assume $m^*(A_n) < \infty$ for all $n$.
    
    Fix $\epsilon > 0$. For each $n$, choose open intervals $\{I_{nk}\}_{k=1}^\infty$ covering $A_n$ such that:
    
    $$\sum_{k=1}^\infty \ell(I_{nk}) < m^*(A_n) + \frac{\epsilon}{2^n}$$
    
    The countable collection $\{I_{nk}\}_{n,k=1}^\infty$ covers $\bigcup_{n=1}^\infty A_n$. Thus:
    
    $$m^*\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty \sum_{k=1}^\infty \ell(I_{nk}) \le \sum_{n=1}^\infty \left( m^*(A_n) + \frac{\epsilon}{2^n} \right) = \sum_{n=1}^\infty m^*(A_n) + \epsilon$$
    
    Taking $\epsilon \to 0$ yields the result.

---

## 3. Connection to ML/DL: Reproducing Kernel Hilbert Spaces (RKHS) & The Representer Theorem

In machine learning, **kernel methods** (such as Support Vector Machines (SVMs), Kernel PCA, and Gaussian Processes) construct non-linear decision boundaries by mapping inputs $x \in \mathcal{X}$ into an infinite-dimensional feature space. A **Reproducing Kernel Hilbert Space (RKHS)** is a complete Hilbert space of functions where evaluation functionals are continuous.

### Riesz Representation Theorem & Evaluation Functionals
Let $\mathcal{H}$ be a Hilbert space of functions $f: \mathcal{X} \to \mathbb{R}$. For a fixed $x \in \mathcal{X}$, the **evaluation functional** $L_x: \mathcal{H} \to \mathbb{R}$ is defined as:

$$L_x(f) = f(x)$$

If $L_x$ is a bounded (continuous) linear functional for all $x \in \mathcal{X}$ (which defines an RKHS), then by the **Riesz Representation Theorem**, there exists a unique function $K_x \in \mathcal{H}$ (denoted as $K(x, \cdot)$) such that:

$$L_x(f) = f(x) = \langle f, K(x, \cdot) \rangle_{\mathcal{H}}$$

This is the **reproducing property**. The symmetric positive-definite reproducing kernel $K: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ is defined as:

$$K(x, y) = \langle K(x, \cdot), K(y, \cdot) \rangle_{\mathcal{H}}$$

This provides the foundation for the **Kernel Trick**: computing inner products in an infinite-dimensional feature space $\mathcal{H}$ can be performed simply by evaluating the closed-form kernel function $K(x, y)$ in the low-dimensional input space.

### The Representer Theorem
Normally, finding a function $f \in \mathcal{H}$ that minimizes a regularized empirical risk function:

$$\min_{f \in \mathcal{H}} \sum_{i=1}^N \mathcal{L}(f(x_i), y_i) + \lambda \Omega(\|f\|_{\mathcal{H}})$$

is an infinite-dimensional optimization problem since $\mathcal{H}$ is infinite-dimensional.

The **Representer Theorem** guarantees that the optimal solution $f^*$ must lie in the finite-dimensional span of the kernels evaluated at the training points:

$$f^*(x) = \sum_{i=1}^N \alpha_i K(x_i, x)$$

**Proof**:
Any function $f \in \mathcal{H}$ can be decomposed orthogonally as $f = f_{\parallel} + f_{\perp}$, where $f_{\parallel}$ lies in the subspace $\mathcal{H}_{\parallel} = \text{span}(\{K(x_i, \cdot)\}_{i=1}^N)$ and $f_{\perp}$ lies in the orthogonal complement $\mathcal{H}_{\perp}$.

For any training point $x_i$:

$$f(x_i) = \langle f, K(x_i, \cdot) \rangle_{\mathcal{H}} = \langle f_{\parallel} + f_{\perp}, K(x_i, \cdot) \rangle_{\mathcal{H}} = \langle f_{\parallel}, K(x_i, \cdot) \rangle_{\mathcal{H}} + 0 = f_{\parallel}(x_i)$$

Thus, the empirical loss term is independent of $f_{\perp}$.

For the regularization term, if $\Omega$ is strictly monotonically increasing:

$$\|f\|_{\mathcal{H}}^2 = \|f_{\parallel}\|_{\mathcal{H}}^2 + \|f_{\perp}\|_{\mathcal{H}}^2 \ge \|f_{\parallel}\|_{\mathcal{H}}^2$$

Thus, setting $f_{\perp} = 0$ minimizes the regularizer without changing the empirical loss. The optimal function must therefore have the form $f^*(x) = \sum_{i=1}^N \alpha_i K(x_i, x)$, reducing the infinite-dimensional optimization problem to finding the finite-dimensional coefficients $\alpha \in \mathbb{R}^N$.


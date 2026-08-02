# Basic Banach Space Theory

This lecture introduces the foundational concepts of normed spaces, convergence, completeness, and infinite-dimensional vector spaces.

---

## 1. Infinite-Dimensional Vector Spaces

Unlike calculus and linear algebra on $\mathbb{R}^n$, which deal with finitely many variables, functional analysis aims to solve equations in spaces of functions, which are infinite-dimensional.

Let $V$ be a vector space over a field $\mathbb{K}$ (either $\mathbb{R}$ or $\mathbb{C}$).

*   **Definition**: A vector space $V$ is **finite-dimensional** if every linearly independent set in $V$ is finite. That is, for all subsets $E \subseteq V$ such that:
    
    $$\sum_{i=1}^N a_i v_i = 0 \implies a_1 = a_2 = \cdots = a_N = 0 \quad \text{for all } v_1, \dots, v_N \in E$$
    
    $E$ must have a finite cardinality. $V$ is **infinite-dimensional** if it is not finite-dimensional.

*   **Example**: The space $C([0, 1])$ of continuous functions from $[0, 1]$ to $\mathbb{C}$ is infinite-dimensional. To see this, consider the set of monomials:
    
    $$E = \{f_n(x) = x^n \mid n \in \mathbb{Z}_{\ge 0}\}$$
    
    This set is linearly independent and contains infinitely many elements.

---

## 2. Norms and Inducing Metrics

To perform analysis on infinite-dimensional spaces, we need a way to measure distance.

*   **Definition**: A **norm** on a vector space $V$ is a function $\|\cdot\|: V \to [0, \infty)$ satisfying:
    1.  **Positive Definiteness**: $\|v\| = 0$ if and only if $v = 0$.
    2.  **Absolute Homogeneity**: $\|\lambda v\| = |\lambda| \|v\|$ for all $v \in V$ and $\lambda \in \mathbb{K}$.
    3.  **Triangle Inequality**: $\|v_1 + v_2\| \le \|v_1\| + \|v_2\|$ for all $v_1, v_2 \in V$.

    A **seminorm** satisfies properties (2) and (3), but not necessarily (1). A vector space equipped with a norm is called a **normed space**.

*   **Proposition**: A norm $\|\cdot\|$ on $V$ induces a metric $d(v, w) = \|v - w\|$ on $V$.
    
    **Proof**:
    1.  Definiteness: $d(v, w) = \|v - w\| = 0 \iff v - w = 0 \iff v = w$.
    2.  Symmetry: $d(v, w) = \|v - w\| = \|(-1)(w - v)\| = |-1| \cdot \|w - v\| = d(w, v)$.
    3.  Triangle Inequality: For all $u, v, w \in V$:
        
        $$d(u, w) = \|u - w\| = \|(u - v) + (v - w)\| \le \|u - v\| + \|v - w\| = d(u, v) + d(v, w)$$

*   **Examples in Finite Dimensions**: On $\mathbb{K}^n$, we define the $l^p$ norm for $1 \le p < \infty$ and the $l^\infty$ norm as:
    
    $$\|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}, \quad \|x\|_\infty = \max_{1 \le i \le n} |x_i|$$
    
    These norms define different geometric unit balls (spherical, diamond, or square), but they are topologically equivalent.

---

## 3. Completeness of $C_\infty(X)$ and Banach Spaces

Completeness ensures that Cauchy sequences converge to a limit inside the space.

*   **Definition**: A normed space is a **Banach space** if it is complete with respect to the metric induced by its norm.

*   **Theorem**: Let $X$ be a metric space. The space $C_\infty(X)$ of all bounded, continuous functions $u: X \to \mathbb{C}$ equipped with the supremum norm:
    
    $$\|u\|_\infty = \sup_{x \in X} |u(x)|$$
    
    is a Banach space.

    **Proof**:
    Let $\{u_n\}$ be a Cauchy sequence in $C_\infty(X)$. We must show it converges to a limit $u \in C_\infty(X)$.
    
    First, the sequence is bounded. Since it is Cauchy, choose $N_0$ such that for all $n, m \ge N_0$, $\|u_n - u_m\|_\infty < 1$. Thus, for all $n \ge N_0$, $\|u_n\|_\infty \le \|u_{N_0}\|_\infty + 1$. The finite set $\{u_1, \dots, u_{N_0-1}\}$ is also bounded. So there exists $B > 0$ such that $\|u_n\|_\infty \le B$ for all $n \in \mathbb{N}$.

    Second, define a pointwise limit. For any fixed $x \in X$:
    
    $$|u_n(x) - u_m(x)| \le \|u_n - u_m\|_\infty$$
    
    Since $\{u_n\}$ is Cauchy, $\{u_n(x)\}$ is a Cauchy sequence of complex numbers. By the completeness of $\mathbb{C}$, the limit exists, allowing us to define:
    
    $$u(x) = \lim_{n \to \infty} u_n(x)$$
    
    This limit function is bounded because $|u(x)| = \lim_{n\to\infty} |u_n(x)| \le B$, hence $\sup_x |u(x)| \le B$.

    Third, show uniform convergence and continuity. Fix $\epsilon > 0$. Since $\{u_n\}$ is Cauchy, choose $N$ such that $\|u_n - u_m\|_\infty < \epsilon / 2$ for all $n, m \ge N$. For any $x \in X$:
    
    $$|u_n(x) - u_m(x)| < \frac{\epsilon}{2} \quad \text{for all } n, m \ge N$$
    
    Taking the limit as $m \to \infty$ yields:
    
    $$|u_n(x) - u(x)| \le \frac{\epsilon}{2} < \epsilon \quad \text{for all } n \ge N$$
    
    Taking the supremum over $x \in X$, we get $\|u_n - u\|_\infty \to 0$, meaning $u_n$ converges to $u$ uniformly. Since the uniform limit of continuous functions is continuous, $u \in C_\infty(X)$, and $C_\infty(X)$ is complete.

---

## 4. Connection to ML/DL: Robustness & Adversarial Training under Banach Norms

In machine learning, the robustness of a model $f_\theta: \mathbb{R}^d \to \mathbb{R}$ against adversarial attacks is analyzed by considering perturbations under different Banach norms.

An adversarial attack seeks to find a perturbation $\delta$ that maximizes the loss:

$$\max_{\|\delta\| \le \epsilon} \mathcal{L}(f_\theta(x + \delta), y)$$

The geometry of the adversarial perturbation depends directly on the chosen norm $\|\cdot\|_p$:

*   **$L^\infty$ Robustness (Supremum Norm)**: Perturbations are bounded such that $\|\delta\|_\infty \le \epsilon$. This means every single input feature (e.g., pixel) can be changed independently by at most $\epsilon$.
*   **$L^2$ Robustness (Euclidean Norm)**: Perturbations satisfy $\|\delta\|_2 \le \epsilon$. This bounds the total energy of the perturbation, allowing larger changes in a few directions but constraining the collective vector length.
*   **$L^1$ Robustness (Sparsity)**: Bounded by $\|\delta\|_1 \le \epsilon$. This encourages sparse perturbations where only a few features are allowed to change, but those changes can be relatively large.

Adversarial training solves a minimax optimization problem:

$$\min_\theta \mathbb{E}_{(x,y)} \left[ \max_{\|\delta\| \le \epsilon} \mathcal{L}(f_\theta(x + \delta), y) \right]$$

The choice of the Banach space norm determines the dual norm needed to calculate the worst-case gradient direction using the linear approximation:

$$\delta^* = \arg\max_{\|\delta\| \le \epsilon} \delta^T \nabla_x \mathcal{L}$$

which is given by the dual norm dual projection (e.g., sign of the gradient for $L^\infty$, normalized gradient for $L^2$, and one-hot direction of the maximum coordinate for $L^1$).


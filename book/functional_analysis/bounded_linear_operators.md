# Bounded Linear Operators

This lecture covers the equivalence of completeness and absolute summability in normed spaces, the properties of bounded linear operators, and the operator norm.

---

## 1. Absolute Summability and Completeness

In real analysis, absolute convergence of a series implies convergence. In general normed spaces, this property characterizes completeness.

*   **Definition**: Let $\{v_n\}_{n=1}^\infty$ be a sequence in a normed space $V$. The series $\sum_{n=1}^\infty v_n$ is:
    - **Summable** if the sequence of partial sums $s_m = \sum_{n=1}^m v_n$ converges in $V$.
    - **Absolutely Summable** if the series of norms $\sum_{n=1}^\infty \|v_n\|$ converges in $\mathbb{R}$.

*   **Theorem**: A normed vector space $V$ is a Banach space if and only if every absolutely summable series is summable.

    **Proof**:
    $(\implies)$ Suppose $V$ is Banach. Let $\sum_{n=1}^\infty v_n$ be absolutely summable, meaning $S = \sum_{n=1}^\infty \|v_n\| < \infty$. For $m > k$, by the triangle inequality:
    
    $$\|s_m - s_k\| = \left\| \sum_{n=k+1}^m v_n \right\| \le \sum_{n=k+1}^m \|v_n\|$$
    
    Since $\sum_{n=1}^\infty \|v_n\|$ converges, the tail sum goes to $0$ as $k \to \infty$. Thus $\{s_m\}$ is Cauchy, and since $V$ is complete, $\{s_m\}$ converges.

    $(\impliedby)$ Suppose every absolutely summable series in $V$ is summable. Let $\{v_n\}$ be a Cauchy sequence in $V$. We construct a subsequence $\{v_{n_k}\}$ that converges. For each $k \in \mathbb{N}$, choose $N_k$ such that $\|v_n - v_m\| < 2^{-k}$ for all $n, m \ge N_k$. Define $n_k = \sum_{j=1}^k N_j$, which forms an increasing sequence with $n_k \ge N_k$.
    
    Then:
    
    $$\|v_{n_{k+1}} - v_{n_k}\| < 2^{-k}$$
    
    The series $\sum_{k=1}^\infty (v_{n_{k+1}} - v_{n_k})$ is absolutely summable because $\sum_{k=1}^\infty 2^{-k} = 1 < \infty$. By assumption, this series converges. Its partial sums are:
    
    $$\sum_{k=1}^{m-1} (v_{n_{k+1}} - v_{n_k}) = v_{n_m} - v_{n_1}$$
    
    Thus, $v_{n_m} \to v$ for some $v \in V$. Since $\{v_n\}$ is Cauchy and has a convergent subsequence, $\{v_n\}$ converges to $v$, showing $V$ is Banach.

---

## 2. Bounded and Continuous Operators

Let $V$ and $W$ be normed vector spaces. A map $T: V \to W$ is a **linear operator** if $T(a x + b y) = a T(x) + b T(y)$ for all $x, y \in V$ and $a, b \in \mathbb{K}$.

*   **Theorem**: A linear operator $T: V \to W$ is continuous if and only if it is **bounded**, meaning there exists $C > 0$ such that:
    
    $$\|Tv\|_W \le C \|v\|_V \quad \text{for all } v \in V$$

    **Proof**:
    $(\implies)$ Suppose $T$ is continuous. The preimage of the open unit ball $B_W(0, 1)$ is open in $V$ and contains $0$ (since $T(0) = 0$). Thus, there exists $r > 0$ such that $B_V(0, r) \subset T^{-1}(B_W(0, 1))$. For any $v \in V \setminus \{0\}$, the scaled vector $v' = \frac{r}{2\|v\|_V} v$ has norm $r/2 < r$, so $v' \in B_V(0, r)$. Thus:
    
    $$\|Tv'\|_W < 1 \implies \left\| T\left(\frac{r}{2\|v\|_V} v\right) \right\|_W < 1 \implies \|Tv\|_W \le \frac{2}{r} \|v\|_V$$
    
    Setting $C = 2/r$ yields the result.

    $(\impliedby)$ Suppose $\|Tv\|_W \le C \|v\|_V$ for all $v$. If $v_n \to v$, then:
    
    $$\|Tv_n - Tv\|_W = \|T(v_n - v)\|_W \le C \|v_n - v\|_V \to 0$$
    
    Thus $Tv_n \to Tv$, proving continuity.

*   **Integral Operator Example**: Let $K: [0, 1] \times [0, 1] \to \mathbb{C}$ be continuous. The operator $T: C([0, 1]) \to C([0, 1])$ defined by:
    
    $$(Tf)(x) = \int_0^1 K(x, y) f(y) \, dy$$
    
    is linear and bounded. Indeed:
    
    $$|(Tf)(x)| \le \int_0^1 |K(x, y)| |f(y)| \, dy \le \|K\|_\infty \|f\|_\infty$$
    
    Thus $\|Tf\|_\infty \le \|K\|_\infty \|f\|_\infty$, showing $T$ is bounded with constant $C = \|K\|_\infty$.

---

## 3. The Operator Norm and B(V, W)

The space of all bounded linear operators from $V$ to $W$ is denoted $B(V, W)$.

*   **Definition**: The **operator norm** of $T \in B(V, W)$ is:
    
    $$\|T\| = \sup_{\|v\|_V = 1} \|Tv\|_W$$

*   **Theorem**: If $W$ is a Banach space, then $B(V, W)$ is a Banach space under the operator norm.

    **Proof**:
    Let $\{T_n\}$ be a sequence in $B(V, W)$ such that $\sum_{n=1}^\infty \|T_n\| < \infty$. For any $v \in V$:
    
    $$\sum_{n=1}^\infty \|T_n v\| \le \sum_{n=1}^\infty \|T_n\| \|v\| = \|v\| \sum_{n=1}^\infty \|T_n\| < \infty$$
    
    Thus the series $\sum_{n=1}^\infty T_n v$ is absolutely summable in $W$. Since $W$ is complete, it converges, defining a pointwise operator $Tv = \sum_{n=1}^\infty T_n v$. One can easily verify $T$ is linear. To see it is bounded:
    
    $$\|Tv\| \le \sum_{n=1}^\infty \|T_n v\| \le \left( \sum_{n=1}^\infty \|T_n\| \right) \|v\|$$
    
    Thus $T \in B(V, W)$. Finally, $\left\| T - \sum_{n=1}^m T_n \right\| \le \sum_{n=m+1}^\infty \|T_n\| \to 0$ as $m \to \infty$, showing convergence in operator norm.

---

## 4. Connection to ML/DL: Operator Learning (DeepONet & FNOs)

In classical deep learning, neural networks learn functions that map vectors to vectors (e.g., $\mathbb{R}^d \to \mathbb{R}^c$). In **Operator Learning**, modern architectures (such as **DeepONets** and **Fourier Neural Operators - FNOs**) are designed to learn mappings between *infinite-dimensional function spaces* (i.e., operators $T: \mathcal{X} \to \mathcal{Y}$).

A classical example is learning the solution operator of a Partial Differential Equation (PDE):

$$T: a(x) \mapsto u(x)$$

where $a(x)$ is the initial condition or coefficient function, and $u(x)$ is the PDE solution.

*   **DeepONet (Deep Operator Network)**: Based on the Chen-Chen universal approximation theorem for operators, a DeepONet approximates an operator $T(a)(y)$ by splitting the architecture into a **Branch net** (which processes the input function $a(x)$ evaluated at sensor locations) and a **Trunk net** (which processes the evaluation coordinate $y$):
    
    $$T(a)(y) \approx \sum_{k=1}^p b_k(a(x_1), \dots, a(x_m)) \cdot t_k(y)$$

*   **Fourier Neural Operator (FNO)**: Parameterizes the operator directly in the Fourier domain. An FNO layer is formulated as:
    
    $$v^{(t+1)}(x) = \sigma \left( W v^{(t)}(x) + \mathcal{F}^{-1} \left( R \cdot \mathcal{F}(v^{(t)}) \right)(x) \right)$$
    
    where $\mathcal{F}$ is the Fourier transform, $R$ is a parameter matrix that filters high-frequency components, and $W$ is a local linear transformation.

*   **Operator Norm and Stability**: In operator learning, the stability of the learned operator network is quantified by its operator norm:
    
    $$\|T\|_{op} = \sup_{a \neq 0} \frac{\|T(a)\|_{\mathcal{Y}}}{\|a\|_{\mathcal{X}}}$$
    
    If the operator norm is bounded, the model is guaranteed to be stable, meaning small perturbations in the input function $a(x)$ (e.g., measurement noise) will result in bounded perturbations in the output function $u(x)$.


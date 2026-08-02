# Quotient Spaces & Baire Category Theorem

This lecture explores closed subspaces, quotient normed spaces, the topological foundations of the Baire Category Theorem, and the Uniform Boundedness Principle.

---

## 1. Closed Subspaces and Quotients

*   **Proposition**: A subspace $W$ of a Banach space $V$ is complete (Banach) under the inherited norm if and only if $W$ is a closed subset of $V$.

*   **Definition**: Let $W \subseteq V$ be a closed subspace. The **quotient space** $V/W$ is the set of cosets $v + W$ equipped with the quotient norm:
    
    $$\|v + W\|_{V/W} = \inf_{w \in W} \|v - w\|$$

*   **Theorem**: If $V$ is a Banach space and $W$ is a closed subspace, then $V/W$ is a Banach space.
    
    If we define a seminorm $\|\cdot\|$ on $V$, the set $E = \{v \in V \mid \|v\| = 0\}$ is a closed subspace of $V$, and the quotient space $V/E$ becomes a normed space under $\|v + E\|_{V/E} = \|v\|$.

---

## 2. Baire Category Theorem

The Baire Category Theorem is a crucial topological property of complete metric spaces.

*   **Theorem**: Let $M$ be a complete metric space. If $M = \bigcup_{n=1}^\infty C_n$, where each $C_n \subseteq M$ is a closed subset, then at least one of the subsets $C_n$ must contain an open ball $B(x, r)$ (i.e., it has a non-empty interior).

    **Proof**:
    Suppose for contradiction that each $C_n$ has empty interior. Then $M \setminus C_1$ is a dense open set. Choose $p_1 \in M \setminus C_1$ and $\epsilon_1 > 0$ such that $\overline{B(p_1, \epsilon_1)} \cap C_1 = \emptyset$.
    
    Inductively, since $C_{k+1}$ has empty interior, the open ball $B(p_k, \epsilon_k/3)$ is not contained in $C_{k+1}$. Choose $p_{k+1} \in B(p_k, \epsilon_k/3) \setminus C_{k+1}$ and choose $\epsilon_{k+1} < \epsilon_k/3$ such that $\overline{B(p_{k+1}, \epsilon_{k+1})} \cap C_{k+1} = \emptyset$.
    
    This yields a sequence $\{p_k\}$ satisfying $d(p_{k+1}, p_k) < \epsilon_k/3$. By the triangle inequality:
    
    $$d(p_k, p_{k+l}) < \sum_{j=k}^{k+l-1} \frac{\epsilon_j}{3} < \epsilon_1 \sum_{j=k}^\infty 3^{-j} = \frac{\epsilon_1}{2} 3^{-k+1}$$
    
    Thus, $\{p_k\}$ is a Cauchy sequence. Since $M$ is complete, $p_k \to p \in M$. For any fixed $k$, since $p_{k+l} \in B(p_k, \epsilon_k)$ for all $l$, the limit $p$ lies in the closed ball $\overline{B(p_k, \epsilon_k/2)} \subset B(p_k, \epsilon_k)$.
    
    By construction, $B(p_k, \epsilon_k) \cap C_k = \emptyset$, so $p \notin C_k$ for all $k$. This contradicts $M = \bigcup_{n=1}^\infty C_n$.

---

## 3. Uniform Boundedness Principle (Banach-Steinhaus)

*   **Theorem**: Let $B$ be a Banach space and $V$ be a normed space. Let $\{T_i\}_{i \in I} \subseteq B(B, V)$ be a family of bounded linear operators. If for each $b \in B$, the set of values is pointwise bounded:
    
    $$\sup_{i \in I} \|T_i b\|_V < \infty$$
    
    then the family is uniformly bounded in the operator norm:
    
    $$\sup_{i \in I} \|T_i\| < \infty$$

    **Proof**:
    For each $k \in \mathbb{N}$, define the subset:
    
    $$C_k = \{b \in B \mid \sup_{i \in I} \|T_i b\|_V \le k\}$$
    
    Each $C_k$ is closed by the continuity of $T_i$ and the norm. Since $\sup_{i \in I} \|T_i b\|_V < \infty$ for all $b$, we have $B = \bigcup_{k=1}^\infty C_k$.
    
    By the Baire Category Theorem, some $C_{k_0}$ contains an open ball $B(b_0, r)$. For any $b \in B$ with $\|b\| < r$, we have $b_0 + b \in B(b_0, r) \subset C_{k_0}$. Thus, for all $i \in I$:
    
    $$\|T_i b\|_V = \|T_i(b_0 + b) - T_i b_0\|_V \le \|T_i(b_0 + b)\|_V + \|T_i b_0\|_V \le k_0 + k_0 = 2k_0$$
    
    For any unit vector $u \in B$ ($\|u\| = 1$), the vector $b = \frac{r}{2} u$ has norm less than $r$, so:
    
    $$\left\| T_i\left(\frac{r}{2} u\right) \right\|_V \le 2k_0 \implies \|T_i u\|_V \le \frac{4k_0}{r}$$
    
    Taking the supremum over $\|u\| = 1$, we get $\|T_i\| \le \frac{4k_0}{r}$ for all $i \in I$.

---

## 4. Connection to ML/DL: Optimization in Function Space

In standard machine learning, optimization occurs in parameter space $\mathbb{R}^d$ (e.g., gradient descent on network weights $\theta$). However, some models—such as **Gradient Boosting** and generative **Diffusion Models**—optimize directly in *function spaces* or *measure spaces*.

To perform calculus on infinite-dimensional Banach spaces, we generalize the derivative:

*   **Gâteaux Derivative**: Generalizes the directional derivative. For a functional $J: V \to \mathbb{R}$ at $u \in V$ in the direction $h \in V$:
    
    $$dJ(u; h) = \lim_{\epsilon \to 0} \frac{J(u + \epsilon h) - J(u)}{\epsilon} = \left. \frac{d}{d\epsilon} J(u + \epsilon h) \right|_{\epsilon=0}$$

*   **Fréchet Derivative**: Generalizes the total derivative. A linear operator $DF(u) \in B(V, W)$ is the Fréchet derivative of $F: V \to W$ at $u$ if:
    
    $$\lim_{h \to 0} \frac{\|F(u + h) - F(u) - DF(u)h\|_W}{\|h\|_V} = 0$$

### ML/DL Applications

*   **Gradient Boosting**: Minimizes an empirical loss $\sum_{i=1}^N \mathcal{L}(y_i, F(x_i))$ by performing gradient descent directly in function space. At step $m$, the model updates:
    
    $$F_m(x) = F_{m-1}(x) - \gamma_m g_m(x)$$
    
    where $g_m(x)$ is a weak learner (like a decision tree) fitted to approximate the negative Gâteaux derivative (pseudo-residuals) of the loss with respect to $F(x_i)$.

*   **Wasserstein Gradient Flows & Diffusion Models**: Generative diffusion models learn to transport a simple noise distribution to a complex data distribution. This is modeled mathematically as a gradient flow of the Kullback-Leibler (KL) divergence or free energy in the Wasserstein space of probability measures $\mathcal{P}(\mathbb{R}^d)$ (equipped with the Wasserstein metric). The optimization of the density path follows the Fokker-Planck equation, which represents a gradient flow optimizing a functional over a space of measures.


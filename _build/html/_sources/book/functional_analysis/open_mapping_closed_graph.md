# Open Mapping & Closed Graph Theorems

This lecture covers the Open Mapping Theorem, its corollaries on bounded inverses, and the Closed Graph Theorem.

---

## 1. The Open Mapping Theorem

An open map maps open sets to open sets.

*   **Theorem**: Let $B_1, B_2$ be Banach spaces. If $T \in B(B_1, B_2)$ is surjective, then $T$ is an open map.

    **Proof**:
    We first show that the image of the open unit ball $B_1(0, 1)$ contains an open ball in $B_2$ centered at $0$.
    
    Since $T$ is surjective and $B_1 = \bigcup_{n=1}^\infty B(0, n)$, we have:
    
    $$B_2 = \bigcup_{n=1}^\infty T(B(0, n)) \implies B_2 = \bigcup_{n=1}^\infty \overline{T(B(0, n))}$$
    
    Since $B_2$ is a Banach space, by the Baire Category Theorem, there exists $n_0$ such that the closed set $\overline{T(B(0, n_0))} = n_0 \overline{T(B(0, 1))}$ contains an open ball. Thus, $\overline{T(B(0, 1))}$ contains an open ball $B_2(v_0, 4r)$ for some $v_0 \in B_2$ and $r > 0$.
    
    Choose $v_1 = Tu_1 \in T(B(0, 1))$ such that $\|v_0 - v_1\| < 2r$. Then $B_2(v_1, 2r) \subset B_2(v_0, 4r) \subset \overline{T(B(0, 1))}$.
    
    We show that $B_2(0, r) \subset \overline{T(B(0, 1))}$. For any $v \in B_2$ with $\|v\| < r$, we have:
    
    $$\frac{1}{2}(2v + v_1) \in B_2\left(\frac{v_1}{2}, r\right) \subset \overline{T\left(B\left(0, \frac{1}{2}\right)\right)}$$
    
    Thus:
    
    $$v \in -T\left(\frac{u_1}{2}\right) + \overline{T\left(B\left(0, \frac{1}{2}\right)\right)} = \overline{T\left(-\frac{u_1}{2} + B\left(0, \frac{1}{2}\right)\right)} \subset \overline{T(B(0, 1))}$$
    
    since $\|u_1\| < 1$. Thus, $B_2(0, r) \subset \overline{T(B(0, 1))}$. By scaling, $B_2(0, 2^{-n}r) \subset \overline{T(B(0, 2^{-n}))}$.
    
    We now show $B_2(0, r/2) \subset T(B(0, 1))$. Let $v \in B_2$ with $\|v\| < r/2$. Since $v \in \overline{T(B(0, 1/2))}$, choose $b_1 \in B_1(0, 1/2)$ such that $\|v - Tb_1\| < r/4$.
    
    Inductively, choose $b_k \in B_1(0, 2^{-k})$ such that:
    
    $$\left\| v - T\left( \sum_{j=1}^k b_j \right) \right\| < 2^{-(k+1)}r$$
    
    The series $\sum_{k=1}^\infty b_k$ is absolutely summable in $B_1$, so it converges to some $b \in B_1$. Furthermore:
    
    $$\|b\| \le \sum_{k=1}^\infty \|b_k\| < \sum_{k=1}^\infty 2^{-k} = 1$$
    
    By the continuity of $T$:
    
    $$Tb = \lim_{k\to\infty} T\left( \sum_{j=1}^k b_j \right) = v$$
    
    Thus, $v \in T(B(0, 1))$, so $B_2(0, r/2) \subset T(B(0, 1))$. Linearity and translation extend this to show that the image of any open set is open.

*   **Bounded Inverse Theorem**: If $B_1, B_2$ are Banach spaces and $T \in B(B_1, B_2)$ is bijective, then $T^{-1} \in B(B_2, B_1)$.

---

## 2. The Closed Graph Theorem

Let $T: B_1 \to B_2$ be a linear operator between Banach spaces. The **graph** of $T$ is the subspace $\Gamma(T) = \{(x, Tx) \mid x \in B_1\} \subset B_1 \times B_2$.

*   **Theorem**: $T$ is bounded if and only if $\Gamma(T)$ is closed in $B_1 \times B_2$ equipped with the product norm $\|(x, y)\| = \|x\| + \|y\|$.

    **Proof**:
    $(\implies)$ If $T$ is continuous, and $(x_n, Tx_n) \to (x, y)$, then $x_n \to x$ and $Tx_n \to y$. By continuity, $Tx_n \to Tx$, so $y = Tx$. Thus $(x, y) \in \Gamma(T)$, and the graph is closed.

    $(\impliedby)$ Suppose $\Gamma(T)$ is closed. Since $B_1 \times B_2$ is Banach, $\Gamma(T)$ is a Banach space. Define the projection maps $\pi_1: \Gamma(T) \to B_1$ and $\pi_2: \Gamma(T) \to B_2$:
    
    $$\pi_1(x, Tx) = x, \quad \pi_2(x, Tx) = Tx$$
    
    Both projections are bounded linear operators because $\|\pi_1(x, Tx)\| = \|x\| \le \|x\| + \|Tx\| = \|(x, Tx)\|$.
    
    $\pi_1$ is bijective. By the Bounded Inverse Theorem, its inverse $S = \pi_1^{-1}: B_1 \to \Gamma(T)$ defined by $Sx = (x, Tx)$ is bounded.
    
    Since $T = \pi_2 \circ S$ is a composition of bounded operators, $T$ is bounded.

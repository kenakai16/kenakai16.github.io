# Simple Functions

This lecture defines complex-valued measurable functions, introduces simple functions, proves the simple function approximation theorem, and defines the Lebesgue integral for non-negative simple functions.

---

## 1. Complex Measurability & Simple Functions

*   **Definition**: A complex-valued function $f: E \to \mathbb{C}$ is **measurable** if its real part $\text{Re}(f)$ and imaginary part $\text{Im}(f)$ are measurable real-valued functions.
    
    All standard algebraic combinations ($\alpha f$, $f+g$, $fg$, $\bar{f}$, $|f|$) and pointwise limits of complex measurable functions remain measurable.

*   **Definition**: A measurable function $\phi: E \to \mathbb{C}$ is **simple** if its range $\phi(E)$ is a finite set.
    
    If the range is $\{a_1, \dots, a_n\}$, we can partition $E$ into disjoint measurable sets $A_i = \phi^{-1}(\{a_i\})$. The function can then be written in its **canonical representation**:
    
    $$\phi(x) = \sum_{i=1}^n a_i \chi_{A_i}(x)$$

---

## 2. Simple Function Approximation

Simple functions act as the fundamental step-like building blocks of Lebesgue integration.

*   **Theorem**: Let $f: E \to [0, \infty]$ be a non-negative measurable function. Then there exists a sequence of simple functions $\{\phi_n\}_{n=1}^\infty$ on $E$ such that:
    1.  **Monotonicity**: $0 \le \phi_1 \le \phi_2 \le \dots \le f$.
    2.  **Pointwise Convergence**: $\lim_{n\to\infty} \phi_n(x) = f(x)$ for all $x \in E$.
    3.  **Uniform Convergence**: $\phi_n \to f$ uniformly on any set where $f$ is bounded.

    **Proof**:
    For each $n \ge 1$ and $0 \le k \le 2^{2n} - 1$, define:
    
    $$E_n^k = \left\{ x \in E \;\middle|\; k 2^{-n} < f(x) \le (k+1) 2^{-n} \right\}, \quad F_n = \left\{ x \in E \;\middle|\; f(x) > 2^n \right\}$$
    
    These sets are measurable since they are preimages of intervals. Define:
    
    $$\phi_n(x) = \sum_{k=0}^{2^{2n}-1} k 2^{-n} \chi_{E_n^k}(x) + 2^n \chi_{F_n}(x)$$
    
    Each $\phi_n$ is a simple function since it takes only finitely many values. By construction, $0 \le \phi_n \le f$.
    
    To show monotonicity, note that the partition for $n+1$ refines the partition for $n$. Specifically, $E_n^k = E_{n+1}^{2k} \cup E_{n+1}^{2k+1}$, and on these sub-intervals the value of $\phi_{n+1}$ is either $2k \cdot 2^{-(n+1)} = k 2^{-n}$ or $(2k+1) \cdot 2^{-(n+1)} > k 2^{-n}$. Thus, $\phi_n \le \phi_{n+1}$.
    
    To show convergence, note that for any $x$ where $f(x) < \infty$, if we choose $n$ large enough so that $f(x) \le 2^n$, then:
    
    $$0 \le f(x) - \phi_n(x) \le 2^{-n}$$
    
    Taking $n \to \infty$ yields pointwise convergence. Uniform convergence on bounded subsets follows because the choice of $n$ to satisfy $f(x) \le 2^n$ can be made uniform.

---

## 3. Lebesgue Integral of Simple Functions

*   **Definition**: Let $\phi \in L^+(E)$ be a non-negative simple function with canonical representation $\phi = \sum_{j=1}^n a_j \chi_{A_j}$ (where $A_j$ are disjoint and partition $E$). The **Lebesgue integral** of $\phi$ over $E$ is defined as:
    
    $$\int_E \phi \, d\mu = \sum_{j=1}^n a_j m(A_j) \in [0, \infty]$$

*   **Theorem**: If $\phi$ and $\psi$ are non-negative simple functions, then:
    1.  $\int_E c \phi \, d\mu = c \int_E \phi \, d\mu$ for any $c \ge 0$.
    2.  $\int_E (\phi + \psi) \, d\mu = \int_E \phi \, d\mu + \int_E \psi \, d\mu$.
    3.  If $\phi \le \psi$ pointwise, then $\int_E \phi \, d\mu \le \int_E \psi \, d\mu$.

    **Proof of (2)**:
    Let $\phi = \sum_{j=1}^n a_j \chi_{A_j}$ and $\psi = \sum_{k=1}^m b_k \chi_{B_k}$. Since $\{A_j\}$ and $\{B_k\}$ partition $E$, we have $A_j = \bigcup_k (A_j \cap B_k)$ and $B_k = \bigcup_j (A_j \cap B_k)$. By the additive property of measure:
    
    $$\int_E \phi \, d\mu + \int_E \psi \, d\mu = \sum_{j=1}^n a_j m(A_j) + \sum_{k=1}^m b_k m(B_k) = \sum_{j,k} (a_j + b_k) m(A_j \cap B_k)$$
    
    Since $\phi + \psi = \sum_{j,k} (a_j + b_k) \chi_{A_j \cap B_k}$ is a representation of the sum as a simple function on disjoint sets, the result follows.

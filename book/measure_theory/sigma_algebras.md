# Sigma Algebras

This lecture covers the outer measure of intervals, open approximations of subsets, and the formal definition of algebras and $\sigma$-algebras.

---

## 1. Outer Measure of Intervals

*   **Proposition**: If $I$ is any interval in $\mathbb{R}$, then $m^*(I) = \ell(I)$.

    **Proof**:
    We prove the case where $I = [a, b]$ is closed and bounded. The inequality $m^*(I) \le b-a$ is clear since for any $\epsilon > 0$, $[a, b] \subset (a-\epsilon, b+\epsilon)$, so $m^*(I) \le b-a+2\epsilon \to b-a$.
    
    For the reverse inequality, let $\{I_n\}$ be open intervals covering $[a, b]$. Since $[a, b]$ is compact, by the Heine-Borel theorem, there exists a finite subcover $\{J_1, \dots, J_N\}$.
    
    Choose $J_1 = (a_1, b_1)$ containing $a$. If $b_1 \le b$, there must exist $J_2 = (a_2, b_2)$ containing $b_1$. Inductively, we construct a chain $J_1, \dots, J_K$ such that $a_{k+1} < b_k < b_{k+1}$ and $b_K > b$. Then:
    
    $$\sum_{n=1}^\infty \ell(I_n) \ge \sum_{k=1}^K \ell(J_k) = (b_K - a_K) + \dots + (b_1 - a_1) \ge b_K - a_1 > b-a$$
    
    Taking the infimum, we obtain $m^*(I) \ge b-a$.
    
    For other finite intervals, the result follows by approximating them with closed intervals: $[a+\epsilon, b-\epsilon] \subset I \subset [a-\epsilon, b+\epsilon]$.

---

## 2. Approximating Sets with Open Sets

*   **Theorem**: For any subset $A \subseteq \mathbb{R}$ and $\epsilon > 0$, there exists an open set $O \supseteq A$ such that:
    
    $$m^*(A) \le m^*(O) \le m^*(A) + \epsilon$$

    **Proof**:
    If $m^*(A) = \infty$, take $O = \mathbb{R}$. Otherwise, choose open intervals $\{I_n\}$ covering $A$ such that $\sum_{n=1}^\infty \ell(I_n) < m^*(A) + \epsilon$. Define $O = \bigcup_{n=1}^\infty I_n$. Then $O$ is open, $A \subseteq O$, and by subadditivity:
    
    $$m^*(O) \le \sum_{n=1}^\infty m^*(I_n) = \sum_{n=1}^\infty \ell(I_n) < m^*(A) + \epsilon$$

---

## 3. Algebras and $\sigma$-algebras

To define a countably additive measure, we restrict our domain to a subset of $\mathcal{P}(\mathbb{R})$ closed under countable operations.

*   **Definition**: A collection $\mathcal{A}$ of subsets of $X$ is an **algebra** if:
    1. $X \in \mathcal{A}$.
    2. $E \in \mathcal{A} \implies E^c \in \mathcal{A}$.
    3. $E_1, \dots, E_n \in \mathcal{A} \implies \bigcup_{i=1}^n E_i \in \mathcal{A}$.

    An algebra is a **$\sigma$-algebra** if it is also closed under countable unions:
    
    $$\{E_n\}_{n=1}^\infty \subseteq \mathcal{A} \implies \bigcup_{n=1}^\infty E_n \in \mathcal{A}$$

*   **Borel $\sigma$-algebra ($\mathcal{B}$)**: The smallest $\sigma$-algebra containing all open sets in $\mathbb{R}$. It is defined as the intersection of all $\sigma$-algebras in $\mathbb{R}$ containing the open sets.

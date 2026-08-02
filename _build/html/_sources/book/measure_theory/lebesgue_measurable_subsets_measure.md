# Lebesgue Measurable Subsets and Measure

This lecture establishes the $\sigma$-algebra of Lebesgue measurable sets, defines the Lebesgue measure, and proves its countable additivity.

---

## 1. Carathéodory's Definition of Measurability

*   **Definition**: A subset $E \subseteq \mathbb{R}$ is **Lebesgue measurable** if for all test sets $A \subseteq \mathbb{R}$:
    
    $$m^*(A) = m^*(A \cap E) + m^*(A \cap E^c)$$

    We denote the collection of all Lebesgue measurable sets as $\mathcal{M}$. By subadditivity, $E$ is measurable if and only if $m^*(A \cap E) + m^*(A \cap E^c) \le m^*(A)$ for all $A$.

*   **Lemma**: If $m^*(E) = 0$, then $E \in \mathcal{M}$.
    
    **Proof**: Since $A \cap E \subseteq E$, we have $m^*(A \cap E) \le m^*(E) = 0$. Thus:
    
    $$m^*(A \cap E) + m^*(A \cap E^c) = 0 + m^*(A \cap E^c) \le m^*(A)$$
    
    since $A \cap E^c \subseteq A$. Thus, $E$ is measurable.

*   **Lemma**: Let $\mathcal{A}$ be an algebra, and let $\{E_n\}_{n=1}^\infty$ be a countable collection of elements in $\mathcal{A}$. Then there exists a disjoint countable collection $\{F_n\}_{n=1}^\infty$ in $\mathcal{A}$ such that $\bigcup_{n=1}^\infty E_n = \bigcup_{n=1}^\infty F_n$.
    
    **Proof**: Define $G_n = \bigcup_{k=1}^n E_k \in \mathcal{A}$. Let $F_1 = G_1$, and $F_{n+1} = G_{n+1} \setminus G_n \in \mathcal{A}$ for all $n \ge 1$. The sets $\{F_n\}$ are pairwise disjoint and satisfy the union property.

*   **Proposition**: Let $E_1, \dots, E_n$ be pairwise disjoint measurable sets. For any test set $A$:
    
    $$m^*\left( A \cap \left[ \bigcup_{k=1}^n E_k \right] \right) = \sum_{k=1}^n m^*(A \cap E_k)$$

---

## 2. Measurable Sets form a $\sigma$-algebra

*   **Theorem**: The collection $\mathcal{M}$ of all Lebesgue measurable sets is a $\sigma$-algebra, and it contains the Borel $\sigma$-algebra $\mathcal{B}$.

    **Proof Sketch**:
    We already know $\mathcal{M}$ is closed under complementation and finite union. To show closure under countable disjoint union, let $E = \bigcup_{n=1}^\infty E_n$ be a disjoint union of measurable sets. For any test set $A$ and any $N \in \mathbb{N}$:
    
    $$m^*(A) = m^*\left( A \cap \left[ \bigcup_{n=1}^N E_n \right] \right) + m^*\left( A \cap \left[ \bigcup_{n=1}^N E_n \right]^c \right) \ge \sum_{n=1}^N m^*(A \cap E_n) + m^*(A \cap E^c)$$
    
    Letting $N \to \infty$ and applying countable subadditivity:
    
    $$m^*(A) \ge \sum_{n=1}^\infty m^*(A \cap E_n) + m^*(A \cap E^c) \ge m^*(A \cap E) + m^*(A \cap E^c)$$
    
    which proves $E \in \mathcal{M}$.
    
    To show $\mathcal{B} \subseteq \mathcal{M}$, we prove $(a, \infty)$ is measurable for all $a \in \mathbb{R}$. This holds because for any test set $A \subseteq \mathbb{R}$ with finite outer measure, we can cover $A$ with open intervals and split them at $a$. Since open intervals can be split additive-lengthwise at $a$, the limit of the sum of lengths yields $m^*(A \cap (a, \infty)) + m^*(A \cap (-\infty, a]) \le m^*(A)$. Since $\mathcal{M}$ is a $\sigma$-algebra containing all $(a, \infty)$, it contains all open intervals and thus all open sets, meaning $\mathcal{B} \subseteq \mathcal{M}$.

---

## 3. Properties of Lebesgue Measure

*   **Definition**: The **Lebesgue measure** $m(E)$ of a measurable set $E \in \mathcal{M}$ is defined as $m(E) = m^*(E)$.

*   **Theorem (Countable Additivity)**: If $\{E_n\}_{n=1}^\infty$ is a countable collection of pairwise disjoint measurable sets, then:
    
    $$m\left( \bigcup_{n=1}^\infty E_n \right) = \sum_{n=1}^\infty m(E_n)$$

*   **Theorem (Continuity of Measure)**: If $\{E_n\}$ is a sequence of measurable sets with $E_1 \subseteq E_2 \subseteq \dots$, then:
    
    $$m\left( \bigcup_{n=1}^\infty E_n \right) = \lim_{n\to\infty} m(E_n)$$

# Zorn's Lemma & Hahn-Banach Theorem

This lecture covers Zorn's Lemma, its application to showing the existence of a Hamel basis, and the proof of the Hahn-Banach Extension Theorem.

---

## 1. Zorn's Lemma and Hamel Bases

*   **Theorem**: Every vector space $V$ has a Hamel basis.

    **Proof**:
    Let $E$ be the set of all linearly independent subsets of $V$. Order $E$ by set inclusion $\subseteq$. Let $C$ be a chain in $E$. We show that $c = \bigcup_{e \in C} e$ is an upper bound in $E$.
    
    To show $c \in E$, let $v_1, \dots, v_n \in c$. There exist $e_1, \dots, e_n \in C$ such that $v_i \in e_i$. Since $C$ is a chain, we can order these subsets by inclusion: $e_{i_1} \subseteq e_{i_2} \subseteq \dots \subseteq e_{i_n}$. Thus, all $v_1, \dots, v_n$ lie in $e_{i_n}$. Since $e_{i_n}$ is linearly independent, $v_1, \dots, v_n$ are linearly independent. Thus, $c \in E$.
    
    Since $e \subseteq c$ for all $e \in C$, $c$ is an upper bound. By Zorn's Lemma, $E$ has a maximal element $H$.
    
    We show $H$ spans $V$. If not, choose $v \in V \setminus \text{span}(H)$. Then $H \cup \{v\}$ is linearly independent, contradicting the maximality of $H$. Thus $H$ is a Hamel basis.

---

## 2. Hahn-Banach Extension Theorem

*   **Theorem**: Let $V$ be a normed space and $M \subseteq V$ be a subspace. If $u: M \to \mathbb{C}$ is a bounded linear functional satisfying $|u(t)| \le C \|t\|$ for all $t \in M$, then there exists a linear extension $U: V \to \mathbb{C}$ such that $U|_M = u$ and $|U(t)| \le C \|t\|$ for all $t \in V$.

    To prove this, we first establish a single-dimension extension lemma.

*   **Lemma**: Let $M \subset V$ be a subspace and $x \notin M$. If $u: M \to \mathbb{C}$ is a linear functional satisfying $|u(t)| \le C \|t\|$ for all $t \in M$, then there exists an extension $u': M \oplus \mathbb{C}x \to \mathbb{C}$ with the same bound $C$.

    **Proof**:
    Without loss of generality, assume $C = 1$. Any $t' \in M \oplus \mathbb{C}x$ is uniquely written as $t' = t + ax$ for $t \in M, a \in \mathbb{C}$. We must choose $\lambda \in \mathbb{C}$ to define $u'(t + ax) = u(t) + a\lambda$ such that:
    
    $$|u(t) + a\lambda| \le \|t + ax\|$$
    
    Dividing by $|a|$, this is equivalent to finding $\lambda$ such that for all $t \in M$:
    
    $$|u(t) - \lambda| \le \|t - x\|$$
    
    We first find the real part $\alpha = \text{Re}(\lambda)$. Let $w(t) = \text{Re}(u(t))$. For any $t_1, t_2 \in M$:
    
    $$w(t_1) - w(t_2) = w(t_1 - t_2) \le \|t_1 - t_2\| \le \|t_1 - x\| + \|t_2 - x\|$$
    
    Rearranging gives:
    
    $$w(t_1) - \|t_1 - x\| \le w(t_2) + \|t_2 - x\|$$
    
    Taking the supremum over $t_1$ and the infimum over $t_2$, we choose a real number $\alpha$ satisfying:
    
    $$\sup_{t \in M} (w(t) - \|t - x\|) \le \alpha \le \inf_{t \in M} (w(t) + \|t - x\|)$$
    
    This ensures $|w(t) - \alpha| \le \|t - x\|$ for all $t$. A symmetric argument using $ix$ instead of $x$ determines the imaginary part of $\lambda$, yielding the desired extension.

*   **Proof of Hahn-Banach Theorem**:
    Let $E$ be the set of all bounded linear extensions $(v, N)$ of $u$ to subspaces $N \supseteq M$ preserving the bound $C$. Order $E$ by $(v_1, N_1) \le (v_2, N_2)$ if $N_1 \subseteq N_2$ and $v_2|_{N_1} = v_1$.
    
    For any chain in $E$, the union of the subspaces and the pointwise limit of the functionals define an upper bound. By Zorn's Lemma, there exists a maximal extension $(U, N)$.
    
    If $N \neq V$, choose $x \in V \setminus N$. By the Lemma, we can extend $U$ to $N \oplus \mathbb{C}x$, contradicting the maximality of $(U, N)$. Thus, $N = V$.

---

## 3. Connection to ML/DL: Universal Approximation Theorem (Hahn-Banach Perspective)

The **Universal Approximation Theorem** (Cybenko, 1989) states that a feedforward neural network with a single hidden layer and a continuous sigmoidal activation function $\sigma$ can approximate any continuous function on a compact subset of $\mathbb{R}^n$ to arbitrary accuracy.

Historically, Cybenko's proof relies directly on the **Hahn-Banach Theorem** (specifically, Riesz-Markov and Hahn-Banach Riesz representations).

Let $K \subset \mathbb{R}^n$ be a compact set, and let $C(K)$ be the Banach space of continuous real-valued functions on $K$ equipped with the supremum norm $\|f\|_\infty = \sup_{x \in K} |f(x)|$. Let $S \subset C(K)$ be the set of functions of the form:

$$G(x) = \sum_{j=1}^N \alpha_j \sigma(w_j^T x + b_j)$$

We want to prove that $S$ is **dense** in $C(K)$ under the supremum norm.

**The Hahn-Banach Riesz Argument**:
By a direct corollary of the Hahn-Banach Theorem, a subspace $S$ is dense in a normed space $V$ if and only if the only bounded linear functional $L \in V^*$ that vanishes on $S$ is the zero functional:

$$L(s) = 0 \quad \text{for all } s \in S \implies L = 0$$

By the Riesz Representation Theorem, any bounded linear functional $L$ on $C(K)$ corresponds to integration against a signed Borel measure $\mu$ on $K$:

$$L(f) = \int_K f(x) \, d\mu(x)$$

Suppose $L(G) = 0$ for all $G \in S$. This implies that for all weights $w \in \mathbb{R}^n$ and biases $b \in \mathbb{R}$:

$$\int_K \sigma(w^T x + b) \, d\mu(x) = 0$$

Cybenko proved that if $\sigma$ is a continuous sigmoidal function, then the family of functions $\sigma(w^T x + b)$ is **discriminatory**, meaning that the above integral vanishing for all $w, b$ forces the signed measure $\mu$ to be the zero measure ($\mu = 0$).

Since $\mu = 0$, the functional $L$ must be the zero functional. By the Hahn-Banach theorem, this implies that the span of the neural network functions $S$ is dense in $C(K)$. Hence, any continuous function $f \in C(K)$ can be approximated to arbitrary precision by a single-hidden-layer neural network.


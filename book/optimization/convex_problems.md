# Convex Optimization Problems

This page covers the mathematical formulation and classification of optimization problems based on Chapter 4 of Stephen Boyd's *Convex Optimization*.

---

## 1. General Optimization Problems (4.1)

A general mathematical optimization problem has the form:

$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 0, \quad i = 1, \dots, m \\
& h_i(x) = 0, \quad i = 1, \dots, p
\end{aligned}$$

Where:
- $x \in \mathbb{R}^n$ is the **optimization variable**.
- $f_0(x)$ is the **objective function**.
- $f_i(x) \leq 0$ are the **inequality constraints**.
- $h_i(x) = 0$ are the **equality constraints**.

The set of points for which the objective and all constraint functions are defined is the **domain** $\mathcal{D}$. A point $x \in \mathcal{D}$ is **feasible** if it satisfies all constraints. The optimal value $p^*$ is defined as:

$$p^* = \inf \{ f_0(x) \mid f_i(x) \leq 0, \, i=1,\dots,m, \, h_i(x)=0, \, i=1,\dots,p \}$$

---

## 2. Convex Optimization Problems (4.2)

A **convex optimization problem** is one of the form:

$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 0, \quad i = 1, \dots, m \\
& a_i^T x = b_i, \quad i = 1, \dots, p
\end{aligned}$$

Where:
- The objective function $f_0$ must be **convex**.
- The inequality constraint functions $f_1, \dots, f_m$ must be **convex**.
- The equality constraints must be **affine** ($A x = b$).

### Key Property: Local Minima are Global
For a convex optimization problem, any local optimal point is also globally optimal.

---

## 3. Linear Optimization Problems - LP (4.3)

When both the objective and constraint functions are affine, the problem is called a **Linear Program (LP)**:

$$\begin{aligned}
\text{minimize} \quad & c^T x + d \\
\text{subject to} \quad & Gx \leq h \\
& Ax = b
\end{aligned}$$

LPs are widely used in operations research, logistics, and resource allocation.

---

## 4. Quadratic Optimization Problems - QP & QCQP (4.4)

A **Quadratic Program (QP)** has a convex quadratic objective and affine constraints:

$$\begin{aligned}
\text{minimize} \quad & \frac{1}{2} x^T P x + q^T x + r \\
\text{subject to} \quad & Gx \leq h \\
& Ax = b
\end{aligned}$$

Where $P$ is symmetric positive semi-definite ($P \succeq 0$).

### Quadratically Constrained Quadratic Program (QCQP)
If the inequality constraints are also quadratic, the problem is a **QCQP**:

$$\begin{aligned}
\text{minimize} \quad & \frac{1}{2} x^T P_0 x + q_0^T x + r_0 \\
\text{subject to} \quad & \frac{1}{2} x^T P_i x + q_i^T x + r_i \leq 0, \quad i=1, \dots, m \\
& Ax = b
\end{aligned}$$

where $P_0, P_1, \dots, P_m \succeq 0$. QCQPs are used in robust design and signal processing.

---

## 5. Second-Order Cone Programming - SOCP

A **Second-Order Cone Program (SOCP)** is a generalization of QPs and QCQPs. It allows constraints that require a vector to lie within a second-order cone (also known as the Lorentz or ice-cream cone):

$$\begin{aligned}
\text{minimize} \quad & f^T x \\
\text{subject to} \quad & \| A_i x + b_i \|_2 \leq c_i^T x + d_i, \quad i=1, \dots, m \\
& F x = g
\end{aligned}$$

where $x \in \mathbb{R}^n$, $A_i \in \mathbb{R}^{n_i \times n}$, $b_i \in \mathbb{R}^{n_i}$, $c_i \in \mathbb{R}^n$, and $d_i \in \mathbb{R}$.

### Second-Order Cone Constraint
The constraint $\| A_i x + b_i \|_2 \leq c_i^T x + d_i$ requires the affine combination $(A_i x + b_i, c_i^T x + d_i)$ to lie in the second-order cone:

$$\mathcal{K}_i = \{ (y, t) \in \mathbb{R}^{n_i} \times \mathbb{R} \mid \|y\|_2 \leq t \}$$

SOCPs are widely applied in portfolio optimization with tracking error constraints, filter design, and robust linear programming under ellipsoidal uncertainty.

---

## 6. Semidefinite Programming - SDP

A **Semidefinite Program (SDP)** is an optimization problem where the variables are symmetric matrices constrained to be positive semidefinite:

$$\begin{aligned}
\text{minimize} \quad & c^T x \\
\text{subject to} \quad & x_1 F_1 + x_2 F_2 + \dots + x_n F_n \preceq F_0 \\
& A x = b
\end{aligned}$$

where $x \in \mathbb{R}^n$, and $F_0, F_1, \dots, F_n$ are symmetric matrices in $\mathbb{S}^k$ (the space of symmetric $k \times k$ matrices).

### Linear Matrix Inequality (LMI)
The constraint $x_1 F_1 + x_2 F_2 + \dots + x_n F_n \preceq F_0$ is called a **Linear Matrix Inequality (LMI)**. The symbol $\preceq$ denotes matrix inequality, meaning:

$$F_0 - \sum_{i=1}^n x_i F_i \succeq 0 \quad (\text{is Positive Semidefinite})$$

SDPs generalize LPs and SOCPs. They are foundational in control theory (Lyapunov stability), structural design, and machine learning (kernel matrix learning and maximum variance unfolding).

---

## 7. Geometric Programming - GP (4.5)

A **Geometric Program (GP)** is an optimization problem involving objective and constraint functions that are posynomials.

### Monomials and Posynomials
*   A **monomial** $f: \mathbb{R}^n \to \mathbb{R}$ is a function of the form:

    $$f(x) = c x_1^{a_1} x_2^{a_2} \dots x_n^{a_n}$$

    where $c > 0$ and $a_i \in \mathbb{R}$.
*   A **posynomial** is a sum of monomials:

    $$f(x) = \sum_{k=1}^K c_k x_1^{a_{1k}} x_2^{a_{2k}} \dots x_n^{a_{nk}}$$

### Standard Geometric Program
A standard GP has the form:

$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 1, \dots, m \\
& h_i(x) = 1, \dots, p
\end{aligned}$$

where $f_0, \dots, f_m$ are posynomials, and $h_1, \dots, h_p$ are monomials.

### Convex Transformation
GPs are non-convex in their original form. However, we can transform them into convex problems by introducing a change of variables $y_i = \ln(x_i)$ and taking the natural logarithm of the objective and constraints. This results in the transformed problem:

$$\begin{aligned}
\text{minimize} \quad & \tilde{f}_0(y) = \ln f_0(e^y) \\
\text{subject to} \quad & \tilde{f}_i(y) = \ln f_i(e^y) \leq 0, \quad i=1, \dots, m \\
& \tilde{h}_i(y) = \ln h_i(e^y) = 0, \quad i=1, \dots, p
\end{aligned}$$

Since $\tilde{f}_i$ are log-sum-exp functions (which are convex), the transformed problem is a convex optimization problem.

---

## 8. Vector Optimization (4.7)

In many practical situations, we want to optimize multiple objectives simultaneously (multicriterion optimization):

$$\text{minimize (with respect to proper cone } K) \quad f_0(x) = (f_1(x), \dots, f_q(x))$$

Since it is usually impossible to minimize all objectives at once, we look for **Pareto optimal** solutions. A feasible point $x$ is Pareto optimal if there is no other feasible point $y$ that performs better or equal in all objectives and strictly better in at least one.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Formulate the following minimization problem as a standard Quadratic Program (QP):

$$\begin{aligned}
\text{minimize} \quad & (x_1 - x_2)^2 + 3(x_2 - 2)^2 \\
\text{subject to} \quad & x_1 + x_2 \geq 1
\end{aligned}$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
To express the problem in the standard QP form:

$$\begin{aligned}
\text{minimize} \quad & \frac{1}{2} x^T P x + q^T x + r \\
\text{subject to} \quad & Gx \leq h
\end{aligned}$$

we follow these mathematical steps:

**Step 1: Expand the Objective Function**
Expand the algebraic terms in the objective function $f(x)$:

$$
\begin{aligned}
f(x) &= (x_1^2 - 2x_1x_2 + x_2^2) + 3(x_2^2 - 4x_2 + 4) \\
&= x_1^2 - 2x_1x_2 + 4x_2^2 - 12x_2 + 12
\end{aligned}

$$

**Step 2: Extract Matrix Parameters**
We match the expanded objective to the quadratic matrix form $\frac{1}{2} x^T P x + q^T x + r$, where $x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$:

*   **Hessian Matrix ($P$)**:

    $$P = \begin{bmatrix} 2 & -2 \\ -2 & 8 \end{bmatrix}$$

    *(Note that $\frac{1}{2} x^T P x = x_1^2 - 2x_1x_2 + 4x_2^2$)*.
*   **Linear Term Vector ($q$)**:

    $$q = \begin{bmatrix} 0 \\ -12 \end{bmatrix}$$

*   **Constant Scalar ($r$)**:

    $$r = 12$$

**Step 3: Verify Convexity**
For a valid QP, $P$ must be positive semidefinite ($P \succeq 0$). The eigenvalues of $P$ are found by solving $\det(P - \lambda I) = 0$:

$$\det \begin{bmatrix} 2-\lambda & -2 \\ -2 & 8-\lambda \end{bmatrix} = \lambda^2 - 10\lambda + 12 = 0 \implies \lambda \approx 8.61, \; 1.39$$

Since both eigenvalues are strictly positive ($\lambda > 0$), $P$ is symmetric positive definite ($P \succ 0$), guaranteeing that the objective function is strictly convex.

**Step 4: Convert Constraints to Standard Form**
The inequality constraint $x_1 + x_2 \geq 1$ must be converted to the standard form $Gx \leq h$:

$$-x_1 - x_2 \leq -1 \implies \begin{bmatrix} -1 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \leq -1$$

Thus, we identify:

$$G = \begin{bmatrix} -1 & -1 \end{bmatrix}, \quad h = -1$$

**Conclusion**
The problem is successfully formulated as a standard convex Quadratic Program (QP).
```

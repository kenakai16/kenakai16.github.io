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

## 4. Quadratic Optimization Problems - QP (4.4)

A **Quadratic Program (QP)** has a convex quadratic objective and affine constraints:

$$\begin{aligned}
\text{minimize} \quad & \frac{1}{2} x^T P x + q^T x + r \\
\text{subject to} \quad & Gx \leq h \\
& Ax = b
\end{aligned}$$

Where $P$ is symmetric positive semi-definite ($P \succeq 0$). If the inequality constraints are also quadratic, it is called a **Quadratically Constrained Quadratic Program (QCQP)**.

---

## 5. Geometric Programming - GP (4.5)

A **Geometric Program (GP)** involves objective and constraint functions that are posynomials (sums of monomials).
A monomial has the form $cx_1^{a_1}x_2^{a_2}\dots x_n^{a_n}$ where $c > 0$.

Although GPs are not convex in their original form, they can be transformed into convex problems using a change of variables $y_i = \ln(x_i)$ and taking the logarithm of the objective and constraints.

---

## 6. Generalized Inequality Constraints (4.6)

We can extend convex optimization to problems with constraints defined by a proper cone $K$:

$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \preceq_K 0, \quad i = 1, \dots, m \\
& A x = b
\end{aligned}$$

Where $f_i(x) \preceq_K 0$ means $-f_i(x) \in K$. This formulation includes **Semidefinite Programming (SDP)** and **Cone Programming**.

---

## 7. Vector Optimization (4.7)

In many practical situations, we want to optimize multiple objectives simultaneously (multicriterion optimization):

$$\text{minimize (with respect to proper cone } K) \quad f_0(x) = (f_1(x), \dots, f_q(x))$$

Since it is usually impossible to minimize all objectives at once, we look for **Pareto optimal** solutions. A feasible point $x$ is Pareto optimal if there is no other feasible point $y$ that performs better or equal in all objectives and strictly better in at least one.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Formulate the following problem as a Quadratic Program (QP):
$$\text{minimize} \quad (x_1 - x_2)^2 + 3(x_2 - 2)^2 \quad \text{subject to} \quad x_1 + x_2 \geq 1$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Expand the objective function:
$$f(x) = x_1^2 - 2x_1x_2 + x_2^2 + 3(x_2^2 - 4x_2 + 4) = x_1^2 - 2x_1x_2 + 4x_2^2 - 12x_2 + 12$$
This can be written in matrix form $\frac{1}{2} x^T P x + q^T x + r$ with:
$$P = \begin{bmatrix} 2 & -2 \\ -2 & 8 \end{bmatrix}, \quad q = \begin{bmatrix} 0 \\ -12 \end{bmatrix}, \quad r = 12$$
Since eigenvalues of $P$ are positive ($P \succeq 0$), the objective is convex.
The constraint $x_1 + x_2 \geq 1$ can be written as $-x_1 - x_2 \leq -1$ (which is $Gx \leq h$ where $G = [-1, -1]$, $h = -1$).
Thus, it is a QP.
```

# Introduction to Optimization

Optimization is the process of finding the best solution from a set of feasible alternatives. A mathematical optimization problem has the general form:

$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq b_i, \quad i = 1, \dots, m
\end{aligned}$$

Where:
- $x = (x_1, \dots, x_n)$ is the **optimization variable**.
- $f_0: \mathbb{R}^n \to \mathbb{R}$ is the **objective function**.
- $f_i(x) \leq b_i$ are the **constraint functions**.

---

## 1. Least-Squares & Linear Programming

Depending on the mathematical properties of $f_0$ and $f_i$, optimization problems are classified into several major families.

### Least-Squares
A least-squares problem has no constraints and an objective function that is a sum of squares:

$$\text{minimize} \quad \|Ax - b\|_2^2 = \sum_{i=1}^k (a_i^T x - b_i)^2$$

This problem can be solved analytically ($x = (A^T A)^{-1} A^T b$). It is the foundation of **Linear Regression** in machine learning.

### Linear Programming (LP)
In Linear Programming, both the objective and constraint functions are linear:

$$\begin{aligned}
\text{minimize} \quad & c^T x \\
\text{subject to} \quad & a_i^T x \leq b_i, \quad i = 1, \dots, m
\end{aligned}$$

LPs do not have analytical solutions but can be solved extremely fast using algorithms like the Simplex method or Interior-point methods.

---

## 2. Convex vs. Non-linear Optimization

The boundary in optimization is not between linearity and non-linearity, but between **convexity** and **non-convexity**.

| Property | Convex Optimization | Non-convex / Nonlinear Optimization |
| :--- | :--- | :--- |
| **Geometry** | objective function is convex, constraint set is convex. | objective or constraints are non-convex (curves bend down). |
| **Minima** | Any local minimum is a **global minimum**. | Many local minima and saddle points exist. |
| **Solvability** | Can be solved efficiently, reliably, and globally. | Hard to solve; algorithms often get stuck in local minima. |

---

## Exercises

```{admonition} Exercise 1
:class: tip
Classify the following optimization problem (find if it is LP, Least-Squares, or Nonlinear):

$$\text{minimize} \quad (3x_1 + x_2 - 5)^2 + (x_1 - 2x_2 + 1)^2$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
This objective is a sum of squared linear terms:

$$f(x) = \|Ax - b\|_2^2$$
Where $A = \begin{bmatrix} 3 & 1 \\ 1 & -2 \end{bmatrix}$ and $b = \begin{bmatrix} 5 \\ -1 \end{bmatrix}$. 
Therefore, this is a **Least-Squares** problem.
```

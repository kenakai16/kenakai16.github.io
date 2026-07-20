# Duality & KKT Conditions

Duality allows us to view an optimization problem from two perspectives: the **Primal** problem (original variables) and the **Dual** problem (constraints coefficients). This page covers Lagrange Duality and the famous Karush-Kuhn-Tucker (KKT) optimality conditions.

---

## 1. The Lagrange Dual Function

For the primal problem:

$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 0, \quad i = 1, \dots, m \\
& h_i(x) = 0, \quad i = 1, \dots, p
\end{aligned}$$

We define the **Lagrangian** $L: \mathbb{R}^n \times \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R}$ by associating Lagrange multipliers $\lambda_i \geq 0$ and $\nu_i$ with the constraints:

$$L(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^p \nu_i h_i(x)$$

The **Lagrange dual function** $g(\lambda, \nu)$ is the minimum value of the Lagrangian over $x$:

$$g(\lambda, \nu) = \inf_{x \in \mathcal{D}} L(x, \lambda, \nu)$$

### The Lower Bound Property
For any $\lambda \geq 0$ and any $\nu$, the dual function gives a lower bound on the optimal value $p^*$ of the primal problem:

$$g(\lambda, \nu) \leq p^*$$

---

## 2. Strong Duality & Weak Duality

The **Lagrange dual problem** is to find the best lower bound:

$$\begin{aligned}
\text{maximize} \quad & g(\lambda, \nu) \\
\text{subject to} \quad & \lambda \succeq 0
\end{aligned}$$

Let $d^*$ be the optimal value of the dual problem.
- **Weak Duality**: $d^* \leq p^*$ always holds (even for non-convex problems).
- **Strong Duality**: $d^* = p^*$ holds (usually for convex problems satisfying Slater's constraint qualification).

---

## 3. Karush-Kuhn-Tucker (KKT) Conditions

For any optimization problem with differentiable objective and constraint functions for which strong duality holds, any primal-optimal $x^*$ and dual-optimal $(\lambda^*, \nu^*)$ must satisfy the **KKT conditions**:

1. **Primal Feasibility**:

   $$f_i(x^*) \leq 0, \quad i=1,\dots,m$$

   $$h_i(x^*) = 0, \quad i=1,\dots,p$$
2. **Dual Feasibility**:

   $$\lambda^* \succeq 0$$
3. **Complementary Slackness**:

   $$\lambda_i^* f_i(x^*) = 0, \quad i=1,\dots,m$$
4. **Lagrangian Stationarity** (Gradient is zero):

   $$\nabla f_0(x^*) + \sum_{i=1}^m \lambda_i^* \nabla f_i(x^*) + \sum_{i=1}^p \nu_i^* \nabla h_i(x^*) = 0$$

If the primal problem is convex, the KKT conditions are not only necessary but also **sufficient** for optimality.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Explain the meaning of **Complementary Slackness** ($\lambda_i^* f_i(x^*) = 0$).
```

```{admonition} Solution — Exercise 1
:class: dropdown
Complementary slackness states that for each inequality constraint $f_i(x) \leq 0$:
- If the constraint is inactive at the optimum ($f_i(x^*) < 0$), then the multiplier must be zero ($\lambda_i^* = 0$).
- If the multiplier is positive ($\lambda_i^* > 0$), then the constraint must be active ($f_i(x^*) = 0$).

This is the mathematical backing for **Support Vectors** in SVMs, where only data points on the boundary (active constraints) have non-zero Lagrange weights.
```

# Numerical Algorithms & Interior-Point Methods

This page covers numerical algorithms for solving constrained optimization problems based on Chapters 9, 10, and 11 of Stephen Boyd's *Convex Optimization*.

---

## 1. Newton's Method with Equality Constraints (Chapter 10)

For unconstrained optimization, Newton's method uses the second-order Taylor expansion to find the search direction. For problems with equality constraints:

$$\begin{aligned}
\text{minimize} \quad & f(x) \\
\text{subject to} \quad & Ax = b
\end{aligned}$$

where $f$ is convex and twice continuously differentiable. We must ensure that the search step keeps the variable feasible ($A(x + \Delta x) = b$).

### Newton Step under Equality Constraints
The Newton step $\Delta x_{nt}$ is obtained by solving the following KKT system of linear equations:

$$\begin{bmatrix} \nabla^2 f(x) & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} \Delta x_{nt} \\ w \end{bmatrix} = \begin{bmatrix} -\nabla f(x) \\ 0 \end{bmatrix}$$

where:
- $\nabla^2 f(x)$ is the Hessian of $f$.
- $\nabla f(x)$ is the gradient of $f$.
- $w$ is the vector of optimal Lagrange multipliers for the equality constraints.

This KKT matrix is invertible if $\nabla^2 f(x)$ is positive definite on the nullspace of $A$.

---

## 2. The Barrier Method (Chapter 11)

The **Barrier Method** (or path-following method) is an interior-point method used to solve convex optimization problems with inequality constraints:

$$\begin{aligned}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 0, \quad i=1, \dots, m \\
& Ax = b
\end{aligned}$$

### Logarithmic Barrier Function
We can approximate the inequality constraints using an indicator function, which we smooth using the **logarithmic barrier function**:

$$\Phi(x) = -\sum_{i=1}^m \ln(-f_i(x))$$

defined on the feasible interior domain $\text{dom } \Phi = \{x \mid f_i(x) < 0, \, i=1, \dots, m\}$.
As $f_i(x) \to 0$, the function $\Phi(x) \to \infty$, preventing the variable from leaving the feasible interior region.

### The Central Path
For a parameter $t > 0$, we define the central path $x^*(t)$ as the solution to:

$$\begin{aligned}
\text{minimize} \quad & t f_0(x) + \Phi(x) \\
\text{subject to} \quad & Ax = b
\end{aligned}$$

As $t \to \infty$, the central path $x^*(t)$ converges to the optimal solution $x^*$ of the original constrained problem.

### The Barrier Algorithm
1.  **Start** with a strictly feasible starting point $x$, $t = t^{(0)} > 0$, tolerance $\epsilon > 0$, and parameter $\mu > 1$.
2.  **Centering Step**: Compute $x^*(t)$ by minimizing $t f_0(x) + \Phi(x)$ subject to $Ax = b$ (typically solved using Newton's method).
3.  **Update**: $x := x^*(t)$.
4.  **Stopping Criterion**: If $m/t < \epsilon$, stop and return $x$.
5.  **Increase $t$**: $t := \mu t$, and repeat from step 2.

---

## 3. Primal-Dual Interior-Point Methods

Unlike the Barrier Method which executes a full centering step (Newton minimization) for each parameter update, **Primal-Dual Interior-Point Methods** update the primal variables $x$, dual variables $\lambda$ (for inequalities), and $nu$ (for equalities) simultaneously at each iteration.

### Perturbed KKT Conditions
We solve the KKT conditions perturbed by a parameter $t$:

$$\begin{aligned}
\nabla f_0(x) + \sum_{i=1}^m \lambda_i \nabla f_i(x) + A^T \nu &= 0 \\
-\lambda_i f_i(x) &= 1/t, \quad i=1, \dots, m \\
Ax - b &= 0
\end{aligned}$$

Applying Newton's method to this non-linear system of equations gives the primal-dual search direction $(\Delta x_{pd}, \Delta \lambda_{pd}, \Delta \nu_{pd})$. These methods often converge much faster than barrier methods because they do not require high accuracy centering steps.

---

## 4. Self-Concordance Analysis

The rate of convergence of Newton's method typically depends on unknown constants (like the Lipschitz constant of the Hessian). However, Stephen Boyd introduces **Self-concordance**, a properties-based analysis that allows bounding the number of Newton iterations without relying on coordinate-dependent constants.

### Definition of Self-Concordant Functions
A convex function $f: \mathbb{R} \to \mathbb{R}$ is self-concordant if:

$$|f'''(x)| \leq 2 f''(x)^{3/2}$$

For multi-dimensional functions $f: \mathbb{R}^n \to \mathbb{R}$, it must be self-concordant along every line.
*   **Example**: The logarithmic barrier $-\sum \ln(x_i)$ is self-concordant.
*   **Significance**: For self-concordant functions, the number of Newton iterations required to reach a specific accuracy is bounded by a constant that depends only on the initial suboptimality, providing rigorous convergence guarantees.

---

## Python Example: Implementing the Barrier Method

Here is a simple Python script implementing the Barrier Method to solve a quadratically constrained problem:

$$\begin{aligned}
\text{minimize} \quad & x^2 \\
\text{subject to} \quad & x \geq 1 \quad (\text{written as } 1 - x \leq 0)
\end{aligned}$$

```python
import numpy as np

def barrier_method(x0, t=1.0, mu=10.0, epsilon=1e-6):
    x = x0
    m = 1 # Number of inequality constraints: f1(x) = 1 - x <= 0
    
    print(f"Starting Barrier Method from feasible x = {x:.4f}\n")
    
    iteration = 0
    while True:
        # Centering step: minimize t * f0(x) - ln(-f1(x))
        # objective: t * x^2 - ln(x - 1)
        # We solve this mini-optimization using Newton's method:
        for _ in range(50):
            # Gradient of centering objective
            grad = 2 * t * x - 1 / (x - 1)
            # Hessian of centering objective
            hess = 2 * t + 1 / ((x - 1) ** 2)
            
            step = -grad / hess
            x += step
            
            # Convergence check for Newton step
            if abs(step) < 1e-8:
                break
                
        duality_gap = m / t
        print(f"Iter {iteration:02d} | t = {t:8.1f} | x = {x:.6f} | Duality Gap = {duality_gap:.8f}")
        
        if duality_gap < epsilon:
            break
            
        t *= mu
        iteration += 1
        
    return x

# Strictly feasible starting point (x > 1)
optimal_x = barrier_method(x0=5.0)
print(f"\nOptimal Solution found: x = {optimal_x:.6f} (Analytical limit = 1.000000)")
```

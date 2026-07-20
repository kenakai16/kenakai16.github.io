# Optimization Algorithms

To solve unconstrained and constrained minimization problems, we rely on iterative numerical methods. This page covers Gradient Descent, Newton's Method, and Interior-point barrier methods.

---

## 1. Unconstrained Minimization

We want to solve:
$$\text{minimize} \quad f(x)$$

Where $f$ is twice differentiable and convex.

### Descent Methods
A descent method produces a sequence of steps $x^{(k+1)} = x^{(k)} + t^{(k)} \Delta x^{(k)}$ where:
- $\Delta x^{(k)}$ is the **step direction** (ensuring $\nabla f(x)^T \Delta x < 0$).
- $t^{(k)} > 0$ is the **step size** (learning rate), often calculated using backtracking line search.

### Gradient Descent Method
The search direction is the negative gradient:
$$\Delta x = -\nabla f(x)$$

### Newton's Method
Newton's method incorporates second-order curvature:
$$\Delta x_{\text{nt}} = -(\nabla^2 f(x))^{-1} \nabla f(x)$$

Newton's method converges much faster than gradient descent (quadratic convergence) because it scales the gradient step using the inverse Hessian.

---

## 2. Equality & Inequality Constraints (Interior-Point Methods)

### Logarithmic Barrier
To solve problems with inequality constraints $f_i(x) \leq 0$, we approximate them using an indicator function, which we smooth using the **logarithmic barrier**:

$$\Phi(x) = -\sum_{i=1}^m \ln(-f_i(x))$$

As $f_i(x) \to 0$, the log barrier $\Phi(x) \to \infty$, preventing the optimization from stepping outside the feasible region.

### The Barrier Method
The Barrier method solves a sequence of unconstrained problems:
$$\text{minimize} \quad t f_0(x) + \Phi(x)$$
for increasing values of $t > 0$, tracing the **central path** directly to the global optimum.

---

## 3. Python Comparison: Gradient Descent vs. Newton's Method

```python
import numpy as np

# Function: f(x) = x^4, f'(x) = 4x^3, f''(x) = 12x^2
# Minimum is at x = 0

# 1. Gradient Descent
x_gd = 2.0
lr = 0.05
for i in range(5):
    grad = 4 * x_gd**3
    x_gd -= lr * grad
    print(f"GD Step {i+1}: x = {x_gd:.4f}")

# 2. Newton's Method
x_newton = 2.0
for i in range(5):
    grad = 4 * x_newton**3
    hessian = 12 * x_newton**2
    x_newton -= grad / hessian  # Newton step: - f'/f''
    print(f"Newton Step {i+1}: x = {x_newton:.4f}")
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Calculate 1 step of Newton's method starting at $x_0 = 2$ for the function $f(x) = x^3 - 2x^2$.
```

```{admonition} Solution — Exercise 1
:class: dropdown
Derivatives:
- $f'(x) = 3x^2 - 4x \implies f'(2) = 3(4) - 4(2) = 4$
- $f''(x) = 6x - 4 \implies f''(2) = 6(2) - 4 = 8$

Newton step:
$$x_1 = x_0 - \frac{f'(x_0)}{f''(x_0)} = 2 - \frac{4}{8} = 1.5$$
```

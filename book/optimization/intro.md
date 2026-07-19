# Introduction

Optimization is the process of finding the maximum or minimum value of a function. In Machine Learning, training a model is essentially an optimization problem: we want to find the parameters (weights and biases) that **minimize** a loss function.

---

## 1. Local Extrema & Second Derivative Test

To find the minimum or maximum of a multivariable function $f(x, y)$, we start by finding the **critical points** where the gradient is zero:

$$\nabla f(x, y) = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Once we find a critical point, we use the **Hessian matrix** $\mathbf{H}$ (which captures the curvature of the function) to determine its nature:

$$\mathbf{H} = \begin{bmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{bmatrix}$$

Using the eigenvalues of the Hessian matrix at the critical point:
- **Local Minimum**: If $\mathbf{H}$ is positive-definite (all eigenvalues $>0$). The curve bends upwards.
- **Local Maximum**: If $\mathbf{H}$ is negative-definite (all eigenvalues $<0$). The curve bends downwards.
- **Saddle Point**: If $\mathbf{H}$ has both positive and negative eigenvalues. The curve bends up in one direction and down in another.

---

## 2. Gradient Descent

When a function is too complex to solve analytically, we use **Gradient Descent**, an iterative optimization algorithm.

Since the gradient $\nabla f$ points in the direction of the steepest increase, updating our variables in the opposite direction ($-\nabla f$) moves us down toward the minimum:

$$\mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla J(\mathbf{w})$$

Where $\alpha$ is the **learning rate** (step size).

### Python Implementation
Let's minimize the function $f(x) = x^2 - 4x + 4$ (which has a minimum at $x=2$, where the gradient is $2x-4$).

```python
x = 10.0          # Starting point
learning_rate = 0.1
epochs = 20

for epoch in range(epochs):
    gradient = 2 * x - 4
    x = x - learning_rate * gradient
    loss = x**2 - 4*x + 4
    print(f"Epoch {epoch+1:02d}: x = {x:.4f}, Loss = {loss:.4f}")
```

---

## 3. Quadratic Optimization with SymPy

We can use SymPy to find the analytical Hessian and determine the nature of critical points:

```python
import sympy as sp

x, y = sp.symbols('x y')
f = x**2 + y**2 - 4*x - 6*y

# 1. Find critical points by solving Gradient = 0
grad_x = sp.diff(f, x)
grad_y = sp.diff(f, y)
critical_points = sp.solve([grad_x, grad_y], (x, y))
print("Critical Point:", critical_points)

# 2. Compute the Hessian matrix
H = sp.hessian(f, (x, y))
print("\nHessian Matrix:")
sp.pprint(H)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Perform 3 iterations of Gradient Descent manually for the function $f(x) = x^2$. Start at $x_0 = 4$ with a learning rate $\alpha = 0.1$.
```

```{admonition} Exercise 2
:class: tip
Given the function:
$$f(x, y) = x^2 + 2y^2 - 4x - 8y$$
1. Find the critical point.
2. Determine if it is a local minimum, maximum, or saddle point using the Hessian matrix.
```

```{admonition} Solution — Exercise 1
:class: dropdown
The derivative is $f'(x) = 2x$.
- **Iteration 1**:
  $$x_1 = x_0 - \alpha \cdot f'(x_0) = 4 - 0.1(2 \cdot 4) = 4 - 0.8 = 3.2$$
- **Iteration 2**:
  $$x_2 = x_1 - \alpha \cdot f'(x_1) = 3.2 - 0.1(2 \cdot 3.2) = 3.2 - 0.64 = 2.56$$
- **Iteration 3**:
  $$x_3 = x_2 - \alpha \cdot f'(x_2) = 2.56 - 0.1(2 \cdot 2.56) = 2.56 - 0.512 = 2.048$$
```

```{admonition} Solution — Exercise 2
:class: dropdown
1. Calculate partial derivatives and set to zero:
   - $\frac{\partial f}{\partial x} = 2x - 4 = 0 \implies x = 2$
   - $\frac{\partial f}{\partial y} = 4y - 8 = 0 \implies y = 2$
   The critical point is $(2, 2)$.

2. Hessian matrix:
   $$\mathbf{H} = \begin{bmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix}$$
   Since all elements on the diagonal (and eigenvalues) are positive ($2 > 0, 4 > 0$), the Hessian is positive-definite. The point $(2, 2)$ is a **local minimum**.
```

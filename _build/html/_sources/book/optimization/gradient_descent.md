# Gradient Descent & Hessian Curvature

In continuous optimization, we find minimum or maximum values of functions using derivatives. This page covers Gradient Descent (first-order optimization) and the Hessian matrix (second-order optimization).

---

## 1. Local Extrema & Second Derivative Test

To find the minimum or maximum of a multivariable function $f(x, y)$, we start by finding the **critical points** where the gradient is zero:

$$\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

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

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

## 2. General Descent & Gradient Descent

### General Descent Method
To minimize a convex function $f$, we use a general iterative descent method. Given a starting point $x \in \text{dom } f$, the algorithm repeats the following steps:

1.  **Determine descent direction**: Find a search direction $\Delta x$ (for gradient descent, $\Delta x = -\nabla f(x)$).
2.  **Line Search**: Choose a step size $t > 0$ using exact or backtracking line search.
3.  **Update**: Set $x := x + t \Delta x$.

This process repeats until a **stopping criterion** is satisfied, usually of the form:

$$\|\nabla f(x)\|_2 \leq \epsilon$$

For strongly convex functions, the convergence satisfies $f(x^{(k)}) - p^* \leq c^k (f(x^{(0)}) - p^*)$, where $c \in (0, 1)$ depends on the minimum/maximum eigenvalues of the Hessian, the starting point, and the line search method.

### Gradient Descent Step
Since the gradient $\nabla f$ points in the direction of the steepest increase, updating our variables in the opposite direction ($-\nabla f$) moves us down toward the minimum:

$$\mathbf{w} \leftarrow \mathbf{w} - \alpha \nabla J(\mathbf{w})$$

Where $\alpha$ is the **learning rate** (step size).

### Convergence Behavior on Ill-Conditioned Functions
When the contour lines of a function are highly elongated (i.e., the Hessian has a very large condition number $\gamma \gg 1$), the gradient does not point directly towards the optimum. As a result, Gradient Descent exhibits a **zig-zagging behavior** and converges very slowly.

For example, minimizing the quadratic function $f(x) = \frac{1}{2}(x_1^2 + \gamma x_2^2)$ starting from $x^{(0)} = (\gamma, 1)$ using exact line search yields the coordinates at step $k$:

$$x_1^{(k)} = \gamma \left( \frac{\gamma - 1}{\gamma + 1} \right)^k, \quad x_2^{(k)} = \left( -\frac{\gamma - 1}{\gamma + 1} \right)^k$$

If $\gamma = 10$, convergence requires many small, zig-zagging steps to reach the optimum:

```{image} ../../images/gradient_descent_zigzag.png
:alt: "Gradient Descent Zig-Zagging in Poorly Conditioned Quadratic Function"
:width: 480px
:align: center
```

### Line Search Strategies (Backtracking vs Exact)
Choosing the correct step size $\alpha$ at each iteration is crucial:
*   **Exact Line Search**: Minimizes the function along the search direction $p_k$. At each step, the next search direction is orthogonal to the previous one ($\nabla f(x_{k+1})^T \nabla f(x_k) = 0$).
*   **Backtracking Line Search**: An inexact line search method that starts with a large step size and decreases it exponentially (scaled by $\beta$) until it satisfies the Armijo condition. It is computationally cheaper and highly effective in practice:

```{image} ../../images/line_search_comparison.png
:alt: "Comparison of Line Search Strategies on a Non-Quadratic Function"
:width: 480px
:align: center
```

### Linear Convergence on Semilog Plots
For strongly convex functions, the error $f(x^{(k)}) - p^*$ decreases exponentially with $k$. This behavior is called **linear convergence**. When plotted on a semilogarithmic scale (where the y-axis is logarithmic and the x-axis is linear), this exponential decay appears as a straight line:

```{image} ../../images/semilog_convergence_plot.png
:alt: "Linear Convergence on Semilog Plot"
:width: 480px
:align: center
```

---

## 3. Steepest Descent Method (General Norms)

The **Steepest Descent Method** generalizes gradient descent by defining the descent step with respect to a general norm $\|\cdot\|$.

### Normalized Steepest Descent Direction
The normalized steepest descent direction $\Delta x_{\text{nsd}}$ is defined as the step of unit norm that minimizes the directional derivative of $f$:

$$\Delta x_{\text{nsd}} = \text{argmin} \{ \nabla f(x)^T v \mid \|v\| = 1 \}$$

The unnormalized steepest descent step is scaled by the dual norm: $\Delta x_{\text{sd}} = \|\nabla f(x)\|_* \Delta x_{\text{nsd}}$, which satisfies $\nabla f(x)^T \Delta x_{\text{sd}} = -\|\nabla f(x)\|_*^2$.

### Steepest Descent Directions for Different Norms
*   **Euclidean Norm ($\|\cdot\|_2$)**: The steepest descent direction is the negative gradient:

    $$\Delta x_{\text{sd}} = -\nabla f(x)$$

*   **Quadratic Norm ($\|x\|_P = (x^T P x)^{1/2}$)**: The steepest descent direction is:

    $$\Delta x_{\text{sd}} = -P^{-1} \nabla f(x)$$

    This is equivalent to performing standard gradient descent after a coordinate transformation (change of variables) $\bar{x} = P^{1/2} x$. By choosing $P \approx \nabla^2 f(x^*)$, we can align the coordinate system to eliminate ill-conditioning and dramatically speed up convergence.
*   **$\ell_1$-Norm ($\|\cdot\|_1$)**: The steepest descent step updates only a single coordinate direction:

    $$\Delta x_{\text{sd}} = -\frac{\partial f(x)}{\partial x_i} e_i$$

    where $i$ is the index corresponding to the largest component of the gradient: $|\partial f(x)/\partial x_i| = \|\nabla f(x)\|_\infty$. This is the basis of coordinate descent methods.

```{image} ../../images/steepest_descent_norms.png
:alt: "Unit Balls and Normalized Steepest Descent Directions"
:width: 500px
:align: center
```

---

## 4. Quadratic Optimization with SymPy

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

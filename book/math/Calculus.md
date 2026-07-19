# Calculus and Derivatives

Calculus is the mathematical study of continuous change. While integration measures the *accumulation* of quantities, differentiation calculates the *rate of change* (the slope) of a function at any given point. 

In machine learning and data science, derivatives and calculus are the foundational tools used for **model optimization**, particularly in training neural networks via backpropagation and optimizing cost functions with gradient descent.

---

## 1. What is a Derivative?

Imagine you are driving a car and want to find your exact speed at a specific split-second. A standard average speed calculation (distance / time) won't work because it requires an interval of time. 

A **derivative** solves this by finding the rate of change over an infinitesimally small interval. Geometrically, the derivative of a function $f(x)$ at a point is the **slope of the tangent line** to the curve at that point.

The formal definition of a derivative using limits is:

$$\frac{d}{dx}f(x) = f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Where $h$ represents a tiny step away from $x$.

---

## 2. Implementing Derivatives in Python

We can approximate derivatives numerically using **finite differences**, or find them exactly using symbolic math.

### Numerical Approximation (Finite Differences)

We can write a simple function that implements the limit definition of a derivative with a very small value for $h$:

```python
def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Let's find the slope of f(x) = x^2 at x = 3
def f(x):
    return x ** 2

approx_slope = derivative(f, 3)
print(f"Approximated slope of x^2 at x=3: {approx_slope:.6f}")
# The exact derivative of x^2 is 2x. At x=3, 2(3) = 6.
```

**Output:**
```
Approximated slope of x^2 at x=3: 6.000010
```

### Symbolic Differentiation with SymPy

In practice, we use `sympy` to compute analytical (exact) derivatives:

```python
import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the function f(x) = x^2
expr = x**2

# Take the derivative with respect to x
deriv = sp.diff(expr, x)

print(f"The derivative of x^2 is: {deriv}")

# Evaluate the derivative at x = 3
slope_at_3 = deriv.subs(x, 3)
print(f"The derivative evaluated at x=3 is: {slope_at_3}")
```

**Output:**
```
The derivative of x^2 is: 2*x
The derivative evaluated at x=3 is: 6
```

---

## 3. Basic Derivative Rules

Here are some essential algebraic rules for taking derivatives:

| Rule Name | Rule Formula | Example |
|-----------|--------------|---------|
| **Power Rule** | $\frac{d}{dx}[x^n] = n x^{n-1}$ | $\frac{d}{dx}[x^3] = 3x^2$ |
| **Constant Rule** | $\frac{d}{dx}[c] = 0$ | $\frac{d}{dx}[10] = 0$ |
| **Product Rule** | $\frac{d}{dx}[u \cdot v] = u'v + uv'$ | $\frac{d}{dx}[x \cdot e^x] = 1 \cdot e^x + x \cdot e^x$ |
| **Exponential Rule**| $\frac{d}{dx}[e^x] = e^x$ | $\frac{d}{dx}[e^x] = e^x$ |

---

## 4. The Chain Rule

The **Chain Rule** is used to find the derivative of composite functions (functions within functions), written as $f(g(x))$. It states:

$$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

Or in Leibniz's notation, if $y = f(u)$ and $u = g(x)$:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

### Why it Matters for Machine Learning
The Chain Rule is the mathematical backbone of **Backpropagation**. In neural networks, the error (Loss) is a composite function of weights across multiple layers. The Chain Rule allows us to propagate the error backward through the network to update the weights.

### Symbolically calculating the Chain Rule with SymPy:

```python
import sympy as sp

x = sp.symbols('x')

# Let y = (x^2 + 1)^3
# Let g(x) = x^2 + 1 (inner function)
# Let f(u) = u^3       (outer function)
y = (x**2 + 1)**3

# SymPy automatically applies the Chain Rule when differentiating
deriv_y = sp.diff(y, x)
print(f"The derivative of (x^2 + 1)^3 is: {deriv_y}")
```

**Output:**
```
The derivative of (x^2 + 1)^3 is: 6*x*(x**2 + 1)**2
```

---

## 5. Partial Derivatives

In multivariable calculus, functions depend on multiple variables (e.g., $f(x, y) = x^2 + 3xy + y^2$). A **partial derivative** is the derivative of the function with respect to *one* variable, keeping all other variables constant.

The notation uses a curly $\partial$:

- $\frac{\partial f}{\partial x}$ means differentiate with respect to $x$, treating $y$ as a constant number.
- $\frac{\partial f}{\partial y}$ means differentiate with respect to $y$, treating $x$ as a constant number.

### SymPy Implementation:

```python
import sympy as sp

x, y = sp.symbols('x y')

# Define multivariable function: f(x,y) = x^2 + 3*x*y + y^2
f = x**2 + 3*x*y + y**2

# Differentiate with respect to x
df_dx = sp.diff(f, x)
print(f"df/dx = {df_dx}")

# Differentiate with respect to y
df_dy = sp.diff(f, y)
print(f"df/dy = {df_dy}")
```

**Output:**
```
df/dx = 2*x + 3*y
df/dy = 3*x + 2*y
```

### The Gradient Vector

The vector of all partial derivatives of a function is called its **Gradient** ($\nabla f$). 

$$\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$

The gradient points in the direction of the steepest ascent of the function. **Gradient Descent** goes in the opposite direction ($-\nabla f$) to find the minimum of a cost function.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Find the derivative of the function $f(x) = 3x^3 + 5x^2 - 7$ at $x = 2$ using both:
1. Pure Python finite differences approximation (with $h = 10^{-5}$).
2. SymPy differentiation.
```

```{admonition} Exercise 2
:class: tip
Use the Chain Rule to calculate the derivative of $f(x) = e^{x^2}$ by hand, and then verify your answer using SymPy.
```

```{admonition} Exercise 3
:class: tip
For the multivariable function $f(x, y) = x^2 y + \sin(x) + e^y$, find the partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ using SymPy.
```

```{admonition} Solution — Exercise 1
:class: dropdown

\`\`\`python
import sympy as sp

# Finite difference
def f(x):
    return 3*x**3 + 5*x**2 - 7

h = 1e-5
x_val = 2
approx = (f(x_val + h) - f(x_val)) / h
print(f"Finite difference: {approx:.6f}")

# SymPy
x = sp.symbols('x')
expr = 3*x**3 + 5*x**2 - 7
deriv = sp.diff(expr, x)
exact = deriv.subs(x, 2)
print(f"SymPy exact: {exact}")
\`\`\`
```
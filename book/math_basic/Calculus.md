# Calculus & Derivatives

Calculus is the mathematical framework that allows us to understand change. In Machine Learning, calculus provides the engine (such as derivatives and the chain rule) that lets models evaluate and update their parameters.

Here we cover the essential calculus tools used to analyze functions of single and multiple variables.

---

## 1. What Is a Derivative?

The **derivative** of a function measures how the output value changes relative to a change in its input. Geometrically, the derivative is the **slope** of the tangent line to the graph of the function at a given point.

For a function $f(x)$, the derivative $f'(x)$ (also written as $\frac{df}{dx}$) is defined using limits:

$$\frac{df}{dx} = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

---

## 2. Basic Rules of Differentiation

Calculating derivatives using limits can be tedious. Instead, we use standard differentiation rules:

- **Power Rule**: $\frac{d}{dx}(x^n) = n x^{n-1}$
- **Constant Rule**: $\frac{d}{dx}(c) = 0$
- **Sum Rule**: $\frac{d}{dx}(f + g) = f' + g'$
- **Product Rule**: $\frac{d}{dx}(f \cdot g) = f'g + fg'$
- **Quotient Rule**: $\frac{d}{dx}(\frac{f}{g}) = \frac{f'g - fg'}{g^2}$

---

## 3. The Chain Rule

The **Chain Rule** is a formula for calculating the derivative of the composition of two or more functions: $f(g(x))$.

If $y = f(u)$ and $u = g(x)$, then:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

### Why it matters in Deep Learning
In neural networks, the loss (error) is a nested composition of functions across layers. The Chain Rule is the mathematical backbone of **Backpropagation**, allowing the network to calculate how changes in early weights affect the final output error.

---

## 4. Partial Derivatives & Gradients

When a function has multiple variables, e.g., $f(x, y)$, we use **partial derivatives**. A partial derivative measures the rate of change with respect to *one* variable while keeping all other variables constant.

- Partial derivative with respect to $x$: $\frac{\partial f}{\partial x}$
- Partial derivative with respect to $y$: $\frac{\partial f}{\partial y}$

### The Gradient Vector
The **gradient** is a vector containing all the partial derivatives of a multivariable function. It is denoted by the symbol $\nabla$ (nabla):

$$\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$

**Geometrical Meaning**: The gradient vector points in the direction of the **steepest ascent** (greatest increase) of the function at that point.

---

## 5. Python Implementation (SymPy)

We can compute exact symbolic derivatives and gradients easily in Python:

```python
import sympy as sp

x, y = sp.symbols('x y')
f = x**2 * y + 3*x * sp.sin(y)

# 1. Single derivative
df_dx = sp.diff(f, x)
print("Partial derivative w.r.t x :", df_dx)

# 2. Derivative w.r.t y
df_dy = sp.diff(f, y)
print("Partial derivative w.r.t y :", df_dy)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Find the derivative of $f(x) = 5x^3 - 2x^2 + 7$.
```

```{admonition} Exercise 2
:class: tip
Apply the Chain Rule to find the derivative of:
$$f(x) = (3x^2 + 1)^4$$
```

```{admonition} Exercise 3
:class: tip
Find the gradient vector $\nabla f(x, y)$ of:
$$f(x, y) = 3x^2y^3 + 2y$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Using the Power and Sum rules:
$$f'(x) = 5(3x^2) - 2(2x) + 0 = 15x^2 - 4x$$
```

```{admonition} Solution — Exercise 2
:class: dropdown
Let $u = 3x^2 + 1$ (inside function) and $y = u^4$ (outside function).
- $\frac{dy}{du} = 4u^3$
- $\frac{du}{dx} = 6x$

Applying the Chain Rule:
$$\frac{dy}{dx} = 4(3x^2 + 1)^3 \cdot 6x = 24x(3x^2 + 1)^3$$
```

```{admonition} Solution — Exercise 3
:class: dropdown
Compute partial derivatives:
- $\frac{\partial f}{\partial x} = 6xy^3$
- $\frac{\partial f}{\partial y} = 9x^2y^2 + 2$

The gradient vector is:
$$\nabla f(x, y) = \begin{bmatrix} 6xy^3 \\ 9x^2y^2 + 2 \end{bmatrix}$$
```

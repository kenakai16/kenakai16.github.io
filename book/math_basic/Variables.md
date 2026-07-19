# Variables

In mathematics and programming, a **variable** is a named placeholder or symbol (such as $x$, $y$, or $w$) used to represent a value that can change or is currently unknown. In Machine Learning, variables represent our data features and model parameters.

---

## 1. Linear Equations

A linear equation is an equation of a straight line, typically written as:

$$ax + b = 0$$

To solve for $x$:

$$x = -\frac{b}{a}$$

### Multi-variable Linear Equations
In Machine Learning, we often map relationships as linear combinations:

$$y = w_1 x_1 + w_2 x_2 + b$$

This represents a plane in 3D space, which is the foundation of Multiple Linear Regression.

---

## 2. Quadratic Equations

A quadratic equation is in the form:

$$ax^2 + bx + c = 0$$

The solutions (roots) can be found using the quadratic formula:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

---

## 3. Symbolic Algebra in Python with SymPy

We can solve algebraic equations exactly using SymPy:

```python
import sympy as sp

x = sp.symbols('x')

# Solve: 2x - 6 = 0
eq1 = sp.Eq(2*x - 6, 0)
sol1 = sp.solve(eq1, x)
print("Solution for 2x - 6 = 0:", sol1)

# Solve quadratic: x^2 - 5x + 6 = 0
eq2 = sp.Eq(x**2 - 5*x + 6, 0)
sol2 = sp.solve(eq2, x)
print("Solutions for x^2 - 5x + 6 = 0:", sol2)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Solve the quadratic equation:
$$x^2 - 4x - 5 = 0$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Using coefficients $a=1, b=-4, c=-5$:
$$x = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(1)(-5)}}{2(1)}$$
$$x = \frac{4 \pm \sqrt{16 + 20}}{2} = \frac{4 \pm \sqrt{36}}{2}$$
$$x_1 = \frac{4 + 6}{2} = 5, \quad x_2 = \frac{4 - 6}{2} = -1$$
```

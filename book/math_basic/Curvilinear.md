# Curvilinear Functions

A **curvilinear function** is a non-linear function whose graph forms a curve rather than a straight line. In Data Science, curvilinear functions model complex patterns, growth rates, activation thresholds (like Sigmoid), and loss curves.

---

## 1. Types of Curvilinear Functions

### Quadratic Functions (Parabolas)
A quadratic function is a second-degree polynomial in the form:

$$y = ax^2 + bx + c$$

Its graph is a parabola. If $a > 0$, the parabola opens upwards (having a minimum). If $a < 0$, it opens downwards (having a maximum). This shape is central to squared loss functions ($MSE = \frac{1}{n} \sum (y_i - \hat{y}_i)^2$).

### Exponential Functions
Exponential functions represent rapid growth or decay, in the form:

$$y = a \cdot b^x \quad \text{or} \quad y = a \cdot e^{kx}$$

Where $e \approx 2.71828$. This is used to model population growth, compounding interest, or decay rates in learning algorithms.

### Logarithmic Functions
The logarithmic function is the inverse of the exponential function:

$$y = \log_b(x)$$

It grows very rapidly at first but levels off. In machine learning, log functions are used in log-transforms to scale heavily skewed features.

---

## 2. Limits and Curvature

Because the slope of a curvilinear function is constantly changing at every point, we cannot define a single slope. 

- **Secant Line**: The average rate of change between two points $(x_1, y_1)$ and $(x_2, y_2)$.
- **Tangent Line**: The instantaneous rate of change at a single point, which we find using **limits** and **calculus**.

---

## 3. Plotting Curvilinear Functions in Python

Let's visualize a quadratic curve and the standard Logistic Sigmoid function ($S(x) = \frac{1}{1 + e^{-x}}$) commonly used in Logistic Regression:

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 200)

# Quadratic function
y_quad = x**2

# Sigmoid function
y_sigmoid = 1 / (1 + np.exp(-x))

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Parabola
ax1.plot(x, y_quad, color='blue', label=r'$y = x^2$')
ax1.set_title("Quadratic Function")
ax1.grid(True)
ax1.legend()

# Sigmoid
ax2.plot(x, y_sigmoid, color='green', label=r'$S(x) = \frac{1}{1 + e^{-x}}$')
ax2.set_title("Sigmoid Activation Function")
ax2.grid(True)
ax2.legend()

plt.savefig('../../images/curvilinear_functions.png', dpi=150)
plt.show()
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Find the vertex (minimum point) of the quadratic function:
$$f(x) = x^2 - 6x + 9$$
*Hint: The x-coordinate of the vertex of $ax^2 + bx + c$ is given by $x = -b / 2a$.*
```

```{admonition} Solution — Exercise 1
:class: dropdown
Using the formula $x = -b / 2a$:
$$x = \frac{-(-6)}{2(1)} = 3$$
Compute $f(3)$:
$$f(3) = 3^2 - 6(3) + 9 = 9 - 18 + 9 = 0$$
The vertex (minimum) is at $(3, 0)$.
```

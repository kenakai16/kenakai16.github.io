# Approximation Theory

In computational mathematics and data science, many functions (like $e^x$, $\ln(x)$, $\sin(x)$, or complex neural network mappings) cannot be calculated exactly. Instead, computers calculate highly accurate **approximations**. 

Here we cover the core methods of function approximation used in numerical computing, calculators, and machine learning.

---

## 1. Taylor Series & Maclaurin Series

A **Taylor Series** represents a smooth function as an infinite sum of terms calculated from the values of the function's derivatives at a single point $a$.

For a function $f(x)$, the Taylor expansion is:

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n$$

When we center the approximation at $a = 0$, it is called a **Maclaurin Series**:

$$f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$$

### Common Maclaurin Series:
- **Exponential**: $e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$
- **Sine**: $\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
- **Cosine**: $\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$

### Python Implementation (Taylor Approximation)
Let's approximate $e^x$ using SymPy:

```python
import sympy as sp

x = sp.symbols('x')
f = sp.exp(x)

# Taylor expansion centered at 0 (Maclaurin) of degree 4
taylor_poly = f.series(x, 0, 5).removeO()
print("Taylor polynomial of e^x (degree 4):")
sp.pprint(taylor_poly)
```

---

## 2. Chebyshev Polynomials (Minimax Approximation)

Taylor series are extremely accurate *near the expansion point $a$*, but the approximation error grows rapidly as you move away from $a$.

To achieve a uniform error over an entire interval $[a, b]$, we use **Chebyshev Polynomials**. They minimize the maximum error (the "minimax" property) over the interval $[-1, 1]$.

The Chebyshev polynomials of the first kind are defined by the recurrence relation:

$$T_0(x) = 1$$
$$T_1(x) = x$$
$$T_{n+1}(x) = 2x T_n(x) - T_{n-1}(x)$$

For example, $T_2(x) = 2x^2 - 1$, $T_3(x) = 4x^3 - 3x$, etc.

These polynomials are the foundation of numerical libraries in calculators and coding environments (like NumPy's `numpy.polynomial.chebyshev`) to calculate trigonometric and exponential functions efficiently.

---

## 3. Exponential & Logarithmic Approximations

In machine learning and statistics, we often approximate exponentiation and logarithms to speed up calculations or prevent numerical overflow/underflow (e.g., in Softmax or Log-Loss).

For instance, when $x$ is very small, we can approximate $\ln(1+x)$ using the first term of its Taylor series:

$$\ln(1 + x) \approx x$$

Similarly:

$$e^x \approx 1 + x \quad (\text{for } x \approx 0)$$

### Python Example (Log Approximation)
```python
import numpy as np

x = 0.05
approx = x
actual = np.log(1 + x)

print(f"Approximation of ln(1 + {x}) : {approx}")
print(f"Actual value                 : {actual:.6f}")
print(f"Absolute Error               : {abs(approx - actual):.6f}")
```

---

## 4. Remez's Algorithm

**Remez's Algorithm** is an iterative minimax approximation algorithm. It finds the polynomial of a given degree $n$ that minimizes the maximum absolute error for a continuous function $f(x)$ on an interval $[a, b]$.

Unlike Taylor series which focus on a single point, Remez's algorithm produces an approximation where the error oscillates between positive and negative bounds of equal magnitude (equioscillation theorem).

---

## 5. The Universal Approximation Theorem (UAT)

In deep learning, neural networks are fundamentally **universal function approximators**.

The **Universal Approximation Theorem** states that a standard feedforward neural network with:
1. A single hidden layer
2. A finite number of neurons
3. A non-linear activation function (such as ReLU, Sigmoid, or Tanh)

can approximate any continuous function on a compact subset of $\mathbb{R}^n$ to any desired degree of accuracy.

This theorem provides the mathematical justification for why deep learning models are capable of learning extremely complex mappings (images to labels, text to text) from data.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Find the Taylor polynomial of degree 3 for the function $f(x) = \ln(1+x)$ centered at $x=0$.
```

```{admonition} Exercise 2
:class: tip
Using the Chebyshev recurrence relation $T_{n+1}(x) = 2x T_n(x) - T_{n-1}(x)$, derive the formula for $T_4(x)$ given:
- $T_2(x) = 2x^2 - 1$
- $T_3(x) = 4x^3 - 3x$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Compute the derivatives of $f(x) = \ln(1+x)$ at $x=0$:
- $f(0) = \ln(1) = 0$
- $f'(x) = \frac{1}{1+x} \implies f'(0) = 1$
- $f''(x) = -\frac{1}{(1+x)^2} \implies f''(0) = -1$
- $f'''(x) = \frac{2}{(1+x)^3} \implies f'''(0) = 2$

Substitute into the Taylor formula:

$$f(x) \approx 0 + 1(x) + \frac{-1}{2!}x^2 + \frac{2}{3!}x^3 = x - \frac{x^2}{2} + \frac{x^3}{3}$$
```

```{admonition} Solution — Exercise 2
:class: dropdown
Using the recurrence relation for $n=3$:

$$T_4(x) = 2x T_3(x) - T_2(x)$$
$$T_4(x) = 2x(4x^3 - 3x) - (2x^2 - 1)$$
$$T_4(x) = 8x^4 - 6x^2 - 2x^2 + 1$$
$$T_4(x) = 8x^4 - 8x^2 + 1$$
```

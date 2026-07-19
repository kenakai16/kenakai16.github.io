# Approximation

Approximation is anything that is intentionally similar but not exactly equal to something else. It is used when an exact value is unknown, difficult to obtain, or computationally expensive to calculate.

In data science and machine learning, approximations are vital for:
- Evaluating complex functions (like $e^x$, $\log(x)$, or $\sin(x)$) on hardware.
- Fitting complex distributions.
- Defining **universal approximations** (the core theorem supporting Neural Networks).

---

## 1. Mathematical Concept of Approximation

Approximation usually occurs when an exact numerical value or mathematical form is difficult to acquire. For instance:
- The irrational number $\pi$ is often approximated to $3.14159$ or $22/7$.
- Physical measurements are rounded to significant digits. For example, $1.5 \times 10^6$ implies a value between $1,450,000$ and $1,550,000$.

Mathematically, if $P(x)$ is an approximation of $f(x)$ on an interval $[a, b]$, the error is defined as:

$$E(x) = |P(x) - f(x)|$$

Our goal is usually to find a polynomial $P(x)$ that minimizes the maximum error on that interval (Minimax approximation).

---

## 2. Optimal Polynomials & Equioscillation

For well-behaved functions, the **Chebyshev Equioscillation Theorem** states that the optimal $N$-th degree polynomial $P(x)$ minimizing the worst-case error has an error curve $P(x) - f(x)$ that oscillates between $+\varepsilon$ and $-\varepsilon$ exactly $N+2$ times.

If another polynomial $Q(x)$ was a better approximation, it would have to cross $P(x)$ more than $N$ times, which is impossible for polynomials of degree $N$.

---

## 3. Chebyshev Approximation

We can get extremely close to the optimal minimax polynomial by expanding a function in terms of **Chebyshev Polynomials** ($T_n(x)$) instead of standard Taylor polynomials. Chebyshev polynomials are defined recursively:

$$T_0(x) = 1$$
$$T_1(x) = x$$
$$T_{n+1}(x) = 2x T_n(x) - T_{n-1}(x)$$

These polynomials oscillate between $-1$ and $+1$ on the interval $[-1, 1]$ in a perfectly balanced ("level") manner.

### Implementing Chebyshev Approximation in Python

Using `numpy.polynomial.chebyshev`, we can approximate functions easily:

```python
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Chebyshev

# Define target function to approximate: f(x) = exp(x) on [-1, 1]
def f(x):
    return np.exp(x)

# Fit Chebyshev polynomial of degree 3
x_nodes = np.linspace(-1, 1, 100)
cheb_poly = Chebyshev.interpolate(f, 3, domain=[-1, 1])

# Generate predictions
x_eval = np.linspace(-1, 1, 300)
y_exact = f(x_eval)
y_approx = cheb_poly(x_eval)
error = y_approx - y_exact

# Plot results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

ax1.plot(x_eval, y_exact, 'r-', label='Exact $e^x$')
ax1.plot(x_eval, y_approx, 'b--', label='Chebyshev Deg 3')
ax1.set_title('Chebyshev Approximation')
ax1.legend()
ax1.grid(True)

ax2.plot(x_eval, error, 'g-', label='Error $P(x) - f(x)$')
ax2.set_title('Approximation Error')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.savefig('../../images/chebyshev_approx.png')
plt.show()
```

---

## 4. Remez's Algorithm

The **Remez Algorithm** is an iterative minimax refinement method used to find the absolute optimal minimax rational or polynomial approximation.

### The Algorithm Steps:
1. Choose $N+2$ initial test points $x_0, x_1, \dots, x_{N+1}$ in the interval.
2. Solve the linear system for the polynomial coefficients $c_i$ and the error $\pm \varepsilon$:
   $$P(x_i) - f(x_i) = (-1)^i \varepsilon$$
3. Find the local extrema points of the error function $P(x) - f(x)$.
4. Replace the old test points with these new extrema points.
5. Repeat steps 2-4 until $\varepsilon$ converges to a constant value.

---

## 5. Taylor Approximation

A **Taylor Series** approximates a function $f(x)$ near a specific point $x = a$ using its derivatives at that point:

$$T_N(x) = \sum_{n=0}^{N} \frac{f^{(n)}(a)}{n!} (x-a)^n$$

### Implementing Taylor Series in SymPy

```python
import sympy as sp

x = sp.symbols('x')
f = sp.exp(x)

# Find Taylor approximation of e^x around x=0 (Maclaurin series) of degree 4
taylor_approx = f.series(x, 0, 5).removeO()
print(f"Taylor polynomial for exp(x) of degree 4: {taylor_approx}")
```

**Output:**
```
Taylor polynomial for exp(x) of degree 4: x**4/24 + x**3/6 + x**2/2 + x + 1
```

---

## 6. Exponential and Logarithmic Series

Computers calculate continuous values using mathematical series expansions.

### Exponential Series ($e^x$)

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$$

```python
# Compute e^x manually using N terms
def approx_exp(x, n_terms=10):
    val = 0.0
    term = 1.0
    for i in range(n_terms):
        val += term
        term *= x / (i + 1)
    return val

print(f"Manual Exp(1.5)  : {approx_exp(1.5, 10):.10f}")
print(f"numpy.exp(1.5)   : {np.exp(1.5):.10f}")
```

### Logarithmic Series ($\ln(1+x)$)

For $-1 < x \le 1$:

$$\ln(1+x) = \sum_{n=1}^{\infty} (-1)^{n-1}\frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots$$

---

## 7. Universal Approximation Theorem

In deep learning, the **Universal Approximation Theorem** states that a feed-forward network with a single hidden layer containing a finite number of non-linear neurons (using activations like Sigmoid, ReLU) can approximate any continuous function on compact subsets of $\mathbb{R}^n$ to any arbitrary precision.

Mathematically, for any continuous function $f(x)$ and any $\epsilon > 0$, there exists a single-hidden-layer neural network $F(x)$ such that:

$$|F(x) - f(x)| < \epsilon \quad \forall x \in [a, b]$$

This theorem justifies why neural networks are so powerful: they are mathematical **universal function approximators**.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Use SymPy to calculate the Taylor expansion of $f(x) = \sin(x)$ around $x=0$ up to the 5th degree.
```

```{admonition} Exercise 2
:class: tip
Write a Python script that calculates $\ln(1.5)$ using the Logarithmic Series up to 10 terms. Compare it with `numpy.log(1.5)`.
```

```{admonition} Solution — Exercise 1
:class: dropdown

\`\`\`python
import sympy as sp
x = sp.symbols('x')
f = sp.sin(x)
print(f.series(x, 0, 6).removeO())
# Expected output: x**5/120 - x**3/6 + x
\`\`\`
```
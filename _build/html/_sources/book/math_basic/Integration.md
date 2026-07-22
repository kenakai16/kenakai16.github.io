# Integration

Integration is one of the two fundamental operations of calculus (alongside differentiation). While a **derivative** tells us the *rate of change* of a function, an **integral** tells us the *accumulated area* under a curve.

In data science, integration is essential for:
- Computing probabilities from probability density functions (PDFs)
- Understanding the Normal Distribution's CDF
- Calculating expected values in statistics

---

## What Is an Integral?

Imagine you are driving a car. Your speedometer shows your *speed* at any given moment (the derivative). If you want to know **how far you've traveled**, you need to *accumulate* that speed over time — that's integration.

Formally, the **definite integral** of a function $f(x)$ from $a$ to $b$ is written as:

$$\int_{a}^{b} f(x)\, dx$$

This represents the **area** between the curve $f(x)$ and the x-axis, from $x = a$ to $x = b$.

```{note}
If $f(x)$ is negative in some region, the area there is counted as **negative**. The integral gives the *net signed area*.
```

---

## Riemann Sums — Approximating the Area

Before computers, mathematicians approximated integrals by slicing the area under a curve into many thin rectangles and summing their areas. This is called a **Riemann Sum**.

### Step 1: Understand the idea

Suppose we want to find the area under $f(x) = x^2$ from $x = 0$ to $x = 1$.

We divide the interval $[0, 1]$ into $n$ equal slices, each of width:

$$\Delta x = \frac{b - a}{n} = \frac{1}{n}$$

For each slice $i$, we pick a point $x_i$ and draw a rectangle of height $f(x_i)$ and width $\Delta x$.

The total approximated area is:

$$\text{Area} \approx \sum_{i=0}^{n-1} f(x_i) \cdot \Delta x$$

As $n \to \infty$, the approximation becomes exact:

$$\int_{a}^{b} f(x)\, dx = \lim_{n \to \infty} \sum_{i=0}^{n-1} f(x_i) \cdot \Delta x$$

### Step 2: Three types of Riemann Sums

| Type | How to pick $x_i$ | Tendency |
|------|-------------------|---------|
| **Left Riemann Sum** | Left edge of each slice | Under-estimates for increasing $f$ |
| **Right Riemann Sum** | Right edge of each slice | Over-estimates for increasing $f$ |
| **Midpoint Riemann Sum** | Center of each slice | Most accurate of the three |

### Step 3: Implement in Python

```python
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^2
def f(x):
    return x ** 2

# Parameters
a = 0       # lower bound
b = 1       # upper bound
n = 10      # number of rectangles

# Width of each rectangle
dx = (b - a) / n

# Generate x positions for each rectangle
x_left = np.linspace(a, b - dx, n)    # left edges
x_right = np.linspace(a + dx, b, n)   # right edges
x_mid = x_left + dx / 2               # midpoints

# Compute Riemann Sums
left_sum  = np.sum(f(x_left)  * dx)
right_sum = np.sum(f(x_right) * dx)
mid_sum   = np.sum(f(x_mid)   * dx)

print(f"Left Riemann Sum  (n={n}): {left_sum:.6f}")
print(f"Right Riemann Sum (n={n}): {right_sum:.6f}")
print(f"Midpoint Sum      (n={n}): {mid_sum:.6f}")
print(f"Exact answer             : {1/3:.6f}")   # ∫x² dx from 0 to 1 = 1/3
```

**Output:**
```
Left Riemann Sum  (n=10): 0.285000
Right Riemann Sum (n=10): 0.385000
Midpoint Sum      (n=10): 0.332500
Exact answer             : 0.333333
```

### Step 4: Visualize the rectangles

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

a, b, n = 0, 1, 10
dx = (b - a) / n
x_left = np.linspace(a, b - dx, n)

# Smooth curve
x_curve = np.linspace(a, b, 300)

fig, ax = plt.subplots(figsize=(8, 5))

# Draw rectangles (Left Riemann Sum)
ax.bar(x_left, f(x_left), width=dx, align='edge',
       alpha=0.4, color='steelblue', edgecolor='black', label='Rectangles (Left Sum)')

# Draw the actual curve
ax.plot(x_curve, f(x_curve), 'r-', linewidth=2.5, label=r'$f(x) = x^2$')

ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('f(x)', fontsize=12)
ax.set_title(f'Left Riemann Sum with n={n} rectangles', fontsize=14)
ax.legend()
plt.tight_layout()
plt.savefig('../../images/riemann_sum.png', dpi=150)
plt.show()
```

### Step 5: Increasing accuracy with more rectangles

```python
import numpy as np

def f(x):
    return x ** 2

a, b = 0, 1
exact = 1 / 3   # true value of ∫x² dx from 0 to 1

print(f"{'n':>8} | {'Left Sum':>12} | {'Right Sum':>12} | {'Midpoint':>12} | {'Error (mid)':>12}")
print("-" * 65)

for n in [5, 10, 50, 100, 1000, 10000]:
    dx = (b - a) / n
    x_left  = np.linspace(a, b - dx, n)
    x_right = np.linspace(a + dx, b, n)
    x_mid   = x_left + dx / 2

    left  = np.sum(f(x_left)  * dx)
    right = np.sum(f(x_right) * dx)
    mid   = np.sum(f(x_mid)   * dx)
    error = abs(mid - exact)

    print(f"{n:>8} | {left:>12.8f} | {right:>12.8f} | {mid:>12.8f} | {error:>12.2e}")
```

**Output:**
```
       n |     Left Sum |    Right Sum |     Midpoint |  Error (mid)
-----------------------------------------------------------------
       5 | 0.24000000   | 0.44000000   | 0.33500000   |  1.67e-03
      10 | 0.28500000   | 0.38500000   | 0.33250000   |  8.33e-04
      50 | 0.32340000   | 0.34340000   | 0.33330000   |  3.33e-05
     100 | 0.32835000   | 0.33835000   | 0.33332500   |  8.33e-06
    1000 | 0.33283350   | 0.33383350   | 0.33333333   |  8.33e-09
   10000 | 0.33328334   | 0.33338334   | 0.33333333   |  8.33e-11
```

The midpoint rule converges the fastest — with $n = 1000$ it's already accurate to 8 decimal places.

---

## Computing Integrals with SciPy

Instead of approximating manually, we can use `scipy.integrate.quad` for accurate numerical integration.

### Step 1: Basic usage of `quad`

```python
from scipy.integrate import quad

# Define the function
def f(x):
    return x ** 2

# Integrate f(x) from 0 to 1
result, error = quad(f, 0, 1)

print(f"Integral result : {result:.10f}")
print(f"Estimated error : {error:.2e}")
print(f"Exact value     : {1/3:.10f}")
```

**Output:**
```
Integral result : 0.3333333333
Estimated error : 3.70e-15
Exact value     : 0.3333333333
```

### Step 2: Integrate more complex functions

```python
from scipy.integrate import quad
import numpy as np

# Example 1: ∫ sin(x) dx from 0 to π
result, _ = quad(np.sin, 0, np.pi)
print(f"∫ sin(x) dx from 0 to π = {result:.6f}")   # Expected: 2.0

# Example 2: ∫ e^(-x²) dx from -∞ to +∞  (Gaussian integral)
result, _ = quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
print(f"∫ e^(-x²) dx from -∞ to +∞ = {result:.6f}")  # Expected: √π ≈ 1.7725
print(f"√π = {np.sqrt(np.pi):.6f}")
```

**Output:**
```
∫ sin(x) dx from 0 to π = 2.000000
∫ e^(-x²) dx from -∞ to +∞ = 1.772454
√π = 1.772454
```

---

## Symbolic Integration with SymPy

SymPy can compute integrals **symbolically** (exact answers, not approximations).

### Step 1: Indefinite integrals (antiderivatives)

```python
from sympy import symbols, integrate, sin, exp, oo, sqrt, pi

x = symbols('x')

# Indefinite integral of x²
expr = x**2
antideriv = integrate(expr, x)
print(f"∫ x² dx = {antideriv} + C")

# Indefinite integral of sin(x)
print(f"∫ sin(x) dx = {integrate(sin(x), x)} + C")
```

**Output:**
```
∫ x² dx = x**3/3 + C
∫ sin(x) dx = -cos(x) + C
```

### Step 2: Definite integrals

```python
from sympy import symbols, integrate, sin, Rational

x = symbols('x')

# Definite integral of x² from 0 to 1
result = integrate(x**2, (x, 0, 1))
print(f"∫₀¹ x² dx = {result}")            # 1/3

# Definite integral of sin(x) from 0 to π
result2 = integrate(sin(x), (x, 0, Rational(355, 113)))   # ≈ π
print(f"∫₀^π sin(x) dx ≈ {float(result2):.6f}")
```

---

## Real-World Application: Probability from a PDF

In statistics, many probability distributions are defined by a **Probability Density Function (PDF)**. The probability that a value falls between $a$ and $b$ is:

$$P(a \leq X \leq b) = \int_{a}^{b} f(x)\, dx$$

### Example: Normal Distribution

The PDF of the standard Normal distribution is:

$$f(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$

Let's compute the probability that a value falls within **1 standard deviation** of the mean (i.e., between $-1$ and $1$):

```python
from scipy.integrate import quad
from scipy.stats import norm
import numpy as np

# Standard normal PDF
def normal_pdf(x, mu=0, sigma=1):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Step 1: Compute P(-1 ≤ X ≤ 1) by integration
prob_1sigma, _ = quad(normal_pdf, -1, 1)
print(f"P(-1 ≤ X ≤ 1) = {prob_1sigma:.4f} ({prob_1sigma*100:.2f}%)")

# Step 2: P(-2 ≤ X ≤ 2)
prob_2sigma, _ = quad(normal_pdf, -2, 2)
print(f"P(-2 ≤ X ≤ 2) = {prob_2sigma:.4f} ({prob_2sigma*100:.2f}%)")

# Step 3: P(-3 ≤ X ≤ 3)
prob_3sigma, _ = quad(normal_pdf, -3, 3)
print(f"P(-3 ≤ X ≤ 3) = {prob_3sigma:.4f} ({prob_3sigma*100:.2f}%)")

# Step 4: Verify using scipy's built-in CDF
print("\n--- Verification using scipy.stats.norm.cdf ---")
print(f"P(-1 ≤ X ≤ 1) = {norm.cdf(1) - norm.cdf(-1):.4f}")
print(f"P(-2 ≤ X ≤ 2) = {norm.cdf(2) - norm.cdf(-2):.4f}")
print(f"P(-3 ≤ X ≤ 3) = {norm.cdf(3) - norm.cdf(-3):.4f}")
```

**Output:**
```
P(-1 ≤ X ≤ 1) = 0.6827 (68.27%)
P(-2 ≤ X ≤ 2) = 0.9545 (95.45%)
P(-3 ≤ X ≤ 3) = 0.9973 (99.73%)

--- Verification using scipy.stats.norm.cdf ---
P(-1 ≤ X ≤ 1) = 0.6827
P(-2 ≤ X ≤ 2) = 0.9545
P(-3 ≤ X ≤ 3) = 0.9973
```

This confirms the famous **68-95-99.7 rule** of the Normal Distribution.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Use a Riemann Sum (with $n = 100$) to approximate:

$$\int_{0}^{2} (3x^2 + 2x + 1)\, dx$$

Then verify your answer using `scipy.integrate.quad`.

*Hint: The exact answer is 14.*
```

```{admonition} Exercise 2
:class: tip
Using `sympy.integrate`, compute the following indefinite integrals:

1. $\int (4x^3 - 2x)\, dx$
2. $\int e^{2x}\, dx$
3. $\int \frac{1}{x}\, dx$
```

```{admonition} Exercise 3
:class: tip
A machine produces parts whose weights follow a Normal distribution with mean $\mu = 100g$ and standard deviation $\sigma = 5g$.

What is the probability that a randomly selected part weighs **between 90g and 110g**?

Use `scipy.integrate.quad` with a normal PDF to answer this.
```

```{admonition} Solution — Exercise 1
:class: dropdown

```python
import numpy as np
from scipy.integrate import quad

def f(x):
    return 3*x**2 + 2*x + 1

# Riemann Sum (Midpoint, n=100)
a, b, n = 0, 2, 100
dx = (b - a) / n
x_mid = np.linspace(a + dx/2, b - dx/2, n)
riemann = np.sum(f(x_mid) * dx)
print(f"Riemann Sum (n=100): {riemann:.6f}")

# Exact via scipy
exact, _ = quad(f, 0, 2)
print(f"scipy.quad result : {exact:.6f}")
print(f"True answer       : 14")
```
```

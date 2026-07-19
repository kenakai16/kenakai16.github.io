# Logarithms

A **logarithm** is the mathematical operation that is the inverse of exponentiation. Logarithms are widely used in Data Science to scale skewed data (log-transform) and calculate errors in classification loss functions.

---

## 1. What Is a Logarithm?

The logarithm answers the question: *To what power must we raise the base to get a certain number?*

If:
$$b^y = x$$

Then:
$$\log_b(x) = y$$

For example:
$$\log_2(8) = 3 \quad \text{because} \quad 2^3 = 8$$

---

## 2. Common Properties of Logarithms

Logarithms possess unique mathematical properties that simplify complex operations:

- **Product Rule**: $\log_b(x \cdot y) = \log_b(x) + \log_b(y)$
- **Quotient Rule**: $\log_b(\frac{x}{y}) = \log_b(x) - \log_b(y)$
- **Power Rule**: $\log_b(x^k) = k \cdot \log_b(x)$

### Two Crucial Bases:
1. **Natural Logarithm ($\ln(x)$)**: Logarithm with base $e \approx 2.71828$.
2. **Common Logarithm ($\log_{10}(x)$)**: Logarithm with base 10.

---

## 3. Python Implementation

We can compute logarithms in Python using the `math` and `numpy` libraries:

```python
import math
import numpy as np

# Natural logarithm: ln(10)
print("ln(10) =", math.log(10)) # math.log defaults to base e

# Base 10 logarithm
print("log10(100) =", math.log10(100))

# NumPy log-transform on an array
data = np.array([1, 10, 100, 1000])
log_data = np.log10(data)
print("Log-transformed data:", log_data)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Solve for $x$:
$$\log_3(x) = 4$$
```

```{admonition} Exercise 2
:class: tip
Expand the expression using logarithm properties:
$$\ln\left(\frac{x^3}{y}\right)$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Convert to exponential form:
$$x = 3^4 = 81$$
```

```{admonition} Solution — Exercise 2
:class: dropdown
Apply the quotient and power rules:
$$\ln\left(\frac{x^3}{y}\right) = \ln(x^3) - \ln(y) = 3\ln(x) - \ln(y)$$
```

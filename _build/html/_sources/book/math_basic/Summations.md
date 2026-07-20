# Summations

A **summation** is the operation of adding a sequence of numbers. In mathematics and data science, we represent this using the Greek capital letter **Sigma** ($\sum$).

---

## 1. What Is a Summation?

A summation is written in the following format:

$$\sum_{i=1}^{n} x_i$$

Where:
- $i$ is the **index of summation** (start variable).
- $1$ is the **lower limit** (starting point).
- $n$ is the **upper limit** (ending point).
- $x_i$ represents the term to be added at index $i$.

This expands to:
$$\sum_{i=1}^{n} x_i = x_1 + x_2 + x_3 + \dots + x_n$$

### Example:
$$\sum_{i=1}^{4} i = 1 + 2 + 3 + 4 = 10$$

---

## 2. Summations in Data Science

We use summations to define key algorithms and performance metrics.

### Mean:
$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}$$

### Mean Squared Error (MSE Loss):
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

---

## 3. Python Implementation

You can compute summations in Python using loops or NumPy's `sum()` function:

```python
import numpy as np

# Data points
x = [2, 4, 6, 8]

# 1. Summation using built-in sum()
total = sum(x)
print("Sum of elements:", total)

# 2. Summation using NumPy
np_total = np.sum(x)
print("NumPy sum:", np_total)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Evaluate the summation:
$$\sum_{i=2}^{5} (2i - 1)$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Expand the expression for $i = 2, 3, 4, 5$:
- For $i=2$: $2(2) - 1 = 3$
- For $i=3$: $2(3) - 1 = 5$
- For $i=4$: $2(4) - 1 = 7$
- For $i=5$: $2(5) - 1 = 9$

Sum the values:
$$3 + 5 + 7 + 9 = 24$$
```

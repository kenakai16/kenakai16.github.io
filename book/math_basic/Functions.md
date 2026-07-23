# Functions

A **function** is a mathematical rule that takes an input (usually denoted as $x$) and maps it to a unique output (usually denoted as $y$ or $f(x)$). In Data Science, we use functions to represent relationships between features (inputs) and targets (outputs).

---

## 1. What Is a Function?

Formally, a function $f$ maps elements from a domain $X$ to a codomain $Y$:

$$f: X \to Y$$

For every input $x \in X$, there is exactly one output $y \in Y$ such that $y = f(x)$.

---

## 2. Linear Functions

A **linear function** is a function that creates a straight line when graphed. Its general algebraic form is:

$$y = mx + c$$

Where:
- $m$ is the **slope** (rate of change, or gradient). It determines the steepness of the line:

  $$m = \frac{y_2 - y_1}{x_2 - x_1}$$
- $c$ is the **y-intercept** (where the line crosses the y-axis, i.e., $f(0)$).

In Machine Learning, this equation forms the basis of **Simple Linear Regression**, where $m$ is the weight ($w$) and $c$ is the bias ($b$):

$$y = wx + b$$

---

## 3. Plotting Linear Functions in Python

We can use `matplotlib` to plot linear functions and visualize their slopes and intercepts:

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-10, 10, 100)

# Define two linear functions
y1 = 2 * x + 3   # slope = 2, intercept = 3
y2 = -0.5 * x - 1 # slope = -0.5, intercept = -1

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label="y = 2x + 3", color="blue")
plt.plot(x, y2, label="y = -0.5x - 1", color="red")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Linear Functions")
plt.savefig('../../images/linear_functions.png', dpi=150)
plt.show()
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
A line passes through the points $(1, 3)$ and $(3, 7)$. 
1. Find the slope of the line.
2. Determine the equation of the line.
```

```{admonition} Solution — Exercise 1
:class: dropdown
1. Slope ($m$):

   $$m = \frac{7 - 3}{3 - 1} = \frac{4}{2} = 2$$
2. Using the point-slope form $y - y_1 = m(x - x_1)$ with point $(1, 3)$:

   $$y - 3 = 2(x - 1) \implies y = 2x + 1$$
```

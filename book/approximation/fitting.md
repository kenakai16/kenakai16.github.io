# Approximation and Fitting

In data science, we often approximate complex data points or functions using mathematical models. This page covers norm approximation, regularization, robust approximation, and function fitting based on Chapter 6 of Stephen Boyd's *Convex Optimization*.

---

## 1. Norm Approximation (Xấp xỉ chuẩn)

The simplest norm approximation problem has the form:

$$\text{minimize} \quad \|Ax - b\|$$

Where $A \in \mathbb{R}^{m \times n}$ ($m > n$) and $\|\cdot\|$ is any norm (such as $L_1$, $L_2$, or $L_\infty$).
- **$L_2$ Norm (Least-squares)**: Minimizes the sum of squared residuals ($\sum r_i^2$). It is highly sensitive to outliers.
- **$L_1$ Norm (Robust approximation)**: Minimizes the sum of absolute residuals ($\sum |r_i|$). It is more robust to outliers and leads to sparse residuals.
- **$L_\infty$ Norm (Chebyshev approximation)**: Minimizes the maximum absolute residual ($\max |r_i|$).

---

## 2. Least-Norm Problems (Bài toán chuẩn tối thiểu)

When a system of linear equations $Ax = b$ is underdetermined ($m < n$, meaning there are more variables than equations), we want to find the solution that has the smallest norm:

$$\begin{aligned}
\text{minimize} \quad & \|x\| \\
\text{subject to} \quad & Ax = b
\end{aligned}$$

For the $L_2$ norm, the analytical solution is $x = A^T(A A^T)^{-1} b$.

---

## 3. Regularized Approximation (Xấp xỉ chính quy hóa)

To balance the trade-off between fitting the data well (minimizing $\|Ax - b\|$) and keeping the model weights small (minimizing $\|x\|$), we use **regularization**:

$$\text{minimize} \quad \|Ax - b\| + \gamma \|x\|$$

Where $\gamma > 0$ is the regularization parameter.

- **Tikhonov Regularization ($L_2$ / Ridge)**: Minimizes $\|Ax - b\|_2^2 + \gamma \|x\|_2^2$. It prevents overfitting by shrinking coefficients.
- **Lasso Regularization ($L_1$)**: Minimizes $\|Ax - b\|_2^2 + \gamma \|x\|_1$. It performs feature selection by driving some coefficients to exactly zero.

---

## 4. Robust Approximation

When there is uncertainty or noise in the matrix $A$, we use robust approximation to optimize for the worst-case scenario:

$$\text{minimize} \quad \sup_{u \in \mathcal{U}} \|(A + \Delta(u))x - b\|$$

Where $\mathcal{U}$ represents the set of possible perturbations. This ensures the model remains stable even under input perturbations.

---

## 5. Function Fitting & Interpolation

We want to fit a continuous function $f(x)$ using a linear combination of basis functions $\phi_i(x)$:

$$\hat{f}(x) = \sum_{i=1}^k c_i \phi_i(x)$$

### Common Basis Functions:
- **Polynomial Fitting**: $\phi_i(x) = x^i$
- **Spline Interpolation**: Piecewise polynomials connected smoothly at knots.

### Python Example: Polynomial Fitting (L2 vs. L1 Robust Fitting)
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Generate data with an outlier
np.random.seed(42)
x = np.linspace(-3, 3, 20)
y = 2 * x + 1 + np.random.normal(0, 0.5, 20)
y[15] += 10  # Introduce a massive outlier

# L2 Loss (Least-squares)
def l2_loss(coeffs):
    return np.sum((y - (coeffs[0] * x + coeffs[1]))**2)

# L1 Loss (Robust absolute loss)
def l1_loss(coeffs):
    return np.sum(np.abs(y - (coeffs[0] * x + coeffs[1])))

c_l2 = minimize(l2_loss, [0.0, 0.0]).x
c_l1 = minimize(l1_loss, [0.0, 0.0]).x

print("L2 Coefficients (Slope, Intercept):", c_l2)
print("L1 Coefficients (Slope, Intercept):", c_l1)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Explain why Lasso ($L_1$ regularization) produces sparse solutions (weights set to 0) while Ridge ($L_2$ regularization) does not.
```

```{admonition} Solution — Exercise 1
:class: dropdown
The constraint region for $L_1$ regularization is a diamond shape (with sharp corners on the axes), whereas the constraint region for $L_2$ regularization is a circle. 
When optimizing, the contours of the loss function are highly likely to hit the sharp corners of the $L_1$ diamond first (which lie exactly on the axes, meaning some variables are set to 0). For the $L_2$ circle, the contact point can be anywhere, resulting in small but non-zero weights.
```

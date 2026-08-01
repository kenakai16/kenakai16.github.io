# Norms & Orthogonality

Vector norms and orthogonality are foundational to geometry, optimization, and Machine Learning regularization techniques.

---

## 1. Vector Norms ($L_1, L_2, L_\infty$)

A **Norm** $\|\cdot\|$ measures the length or magnitude of a vector $x \in \mathbb{R}^n$. It satisfies three conditions: non-negativity ($\|x\| \ge 0$), absolute scalability ($\|c x\| = |c| \|x\|$), and triangle inequality ($\|x + y\| \le \|x\| + \|y\|$).

### 1.1 $L_1$ Norm (Manhattan / Taxicab Norm)
The sum of the absolute values of the vector components:

$$\|x\|_1 = \sum_{i=1}^n |x_i|$$

### 1.2 $L_2$ Norm (Euclidean Norm)
The standard geometric distance from the origin:

$$\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2} = \sqrt{x^T x}$$

### 1.3 $L_\infty$ Norm (Max Norm)
The maximum absolute component value:

$$\|x\|_\infty = \max_{1 \le i \le n} |x_i|$$

---

## 2. Orthogonality & Gram-Schmidt Process

### 2.1 Orthogonal Vectors
Two vectors $u, v$ are **orthogonal** ($u \perp v$) if their inner product (dot product) is zero:

$$u^T v = \sum_{i=1}^n u_i v_i = 0$$

An **Orthonormal Set** of vectors is mutually orthogonal ($q_i^T q_j = 0$ for $i \neq j$) and normalized ($\|q_i\|_2 = 1$).

### 2.2 Gram-Schmidt Process
The **Gram-Schmidt process** converts a set of linearly independent vectors $\{v_1, v_2, \dots, v_k\}$ into an orthonormal basis $\{q_1, q_2, \dots, q_k\}$:

1. $u_1 = v_1 \implies q_1 = \frac{u_1}{\|u_1\|}$
2. $u_2 = v_2 - (v_2^T q_1) q_1 \implies q_2 = \frac{u_2}{\|u_2\|}$
3. $u_k = v_k - \sum_{j=1}^{k-1} (v_k^T q_j) q_j \implies q_k = \frac{u_k}{\|u_k\|}$

---

## 3. Machine Learning Application: Regularization (Lasso & Ridge)

In Machine Learning, when a model has too many parameters, it risks **overfitting** (memorizing noise in the training data). To prevent this, we add a norm penalty on the model weight vector $w$ to the loss function:

$$\text{Loss}_{\text{regularized}} = \text{Loss}_{\text{original}} + \lambda \cdot \text{Penalty}(w)$$

### Ridge Regression ($L_2$ Regularization)
* **Penalty:** $\lambda \|w\|_2^2 = \lambda \sum w_i^2$
* **Effect:** Penalizes large weights smoothly, shrinking parameters towards zero without making them exactly zero.

### Lasso Regression ($L_1$ Regularization)
* **Penalty:** $\lambda \|w\|_1 = \lambda \sum |w_i|$
* **Effect:** Encourages **sparsity** (drives irrelevant feature weights strictly to 0.0), functioning as an automated feature selection tool!

```python
import numpy as np

# Model weights
w = np.array([3.0, -4.0, 0.0])

# Compute norms
l1_norm = np.linalg.norm(w, ord=1)
l2_norm = np.linalg.norm(w, ord=2)

print(f"Weights w: {w}")
print(f"L1 Norm (Lasso Penalty): {l1_norm:.2f}")  # 3 + 4 = 7.0
print(f"L2 Norm (Ridge Penalty): {l2_norm:.2f}")  # sqrt(9 + 16) = 5.0
```

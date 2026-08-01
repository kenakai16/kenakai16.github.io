# SVD & Matrix Factorizations

Matrix factorizations decompose complex matrices into product forms that are easier to analyze, invert, or compute.

---

## 1. Singular Value Decomposition (SVD)

### 1.1 Mathematical Definition
While Eigendecomposition $A = P D P^{-1}$ only works for square matrices, **Singular Value Decomposition (SVD)** applies to **any** $m \times n$ matrix $A$:

$$A = U \Sigma V^T$$

Where:
* $U$ is an $m \times m$ **orthogonal matrix** containing left-singular vectors (eigenvectors of $A A^T$).
* $\Sigma$ is an $m \times n$ **diagonal matrix** containing singular values $\sigma_1 \ge \sigma_2 \ge \dots \ge 0$ (square roots of eigenvalues of $A^T A$).
* $V^T$ is the transpose of an $n \times n$ **orthogonal matrix** $V$ containing right-singular vectors (eigenvectors of $A^T A$).

```{figure} ../../images/svd_decomposition_ai_diagram.png
---
name: svd_decomposition_ai_diagram
align: center
---
Singular value decomposition of a matrix.
```

### 1.2 Truncated SVD & Applications
By keeping only the top $k$ largest singular values ($\Sigma_k$), we get the optimal rank-$k$ approximation of $A$ (Eckart–Young–Mirsky Theorem):

$$A \approx U_k \Sigma_k V_k^T$$

**Applications in AI & Data Science:**
1. **Recommender Systems (Matrix Factorization):** Decomposing user-item rating matrices (e.g., Collaborative Filtering on Netflix/Spotify).
2. **Natural Language Processing:** Truncated SVD on term-document matrices (Latent Semantic Analysis - LSA).
3. **Image Compression:** Storing high-resolution images using only a fraction of singular values.

```python
import numpy as np

# Sample 5x4 matrix
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20]
])

# Full SVD
U, s, Vt = np.linalg.svd(A)

print("U shape:", U.shape)     # (5, 5)
print("Singular values:", s)   # Singular values
print("Vt shape:", Vt.shape)   # (4, 4)

# Truncated SVD (Rank 2 Approximation)
k = 2
S_k = np.diag(s[:k])
A_reconstructed = U[:, :k] @ S_k @ Vt[:k, :]
print("\nReconstructed Matrix (Rank 2 Approximation):\n", np.round(A_reconstructed, 2))
```

---

## 2. LU Decomposition

LU Decomposition factors a square matrix $A$ into a lower triangular matrix $L$ and an upper triangular matrix $U$:

$$A = L U$$

**Why use LU?** Solving $Ax = b$ via standard Gaussian elimination takes $O(n^3)$ operations. Once $A$ is factored into $LU$, solving for multiple target vectors $b$ takes only $O(n^2)$ via forward and backward substitution!

---

## 3. QR Decomposition & Least Squares

QR Decomposition factors an $m \times n$ matrix $A$ into an orthogonal matrix $Q$ ($Q^T Q = I$) and an upper triangular matrix $R$:

$$A = Q R$$

### Application: Numerically Stable Least Squares
In linear regression ($X w = y$), computing $(X^T X)^{-1}$ directly can be numerically unstable if $X^T X$ has a high condition number. Using QR decomposition ($X = QR$):

$$w = R^{-1} Q^T y$$

This avoids explicitly computing matrix inverses, vastly improving numerical precision!

```python
import numpy as np

X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([6, 5, 7])

# QR Decomposition of Feature Matrix X
Q, R = np.linalg.qr(X)

# Solve w = R^-1 @ Q.T @ y
w = np.linalg.inv(R) @ Q.T @ y
print("Weights via QR Decomposition:", w)
```

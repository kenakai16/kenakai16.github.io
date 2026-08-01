# Linear Algebra

Linear Algebra is the mathematical language of Data Science and Machine Learning. It allows us to represent, manipulate, and compute on large datasets efficiently using vectors, matrices, and tensor operations.

This module is organized into six specialized chapters:

1. **{doc}`Vector Spaces & Matrix Rank <vector_spaces>`:** Explores vector space foundations, linear independence, basis, dimension, and rank deficiency (multicollinearity).
2. **{doc}`Norms & Orthogonality <norms_and_orthogonality>`:** Introduces vector norms ($L_1, L_2, L_\infty$), orthogonality, Gram-Schmidt process, and ML regularization (Lasso & Ridge).
3. **{doc}`Eigenvalues, Eigenvectors & PCA <eigen_and_pca>`:** Covers matrix diagonalization, eigendecomposition, and Principal Component Analysis (PCA) for dimensionality reduction.
4. **{doc}`SVD & Matrix Factorizations <svd_and_factorizations>`:** Explores Singular Value Decomposition (SVD), LU & QR Factorizations, and numerically stable Least Squares.
5. **{doc}`Linear Transformations & Neural Networks <linear_transformations>`:** Explains geometric matrix transformations and how Dense layers in Neural Networks operate.

---

## Quick Primer: Vectors & Matrices

### Vectors & Data Points
A **vector** $x \in \mathbb{R}^d$ represents a data point with $d$ features:

$$x = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_d \end{bmatrix}$$

### Feature Matrices
A **matrix** $A \in \mathbb{R}^{m \times n}$ represents a dataset with $m$ samples and $n$ features:

$$A = \begin{bmatrix} A_{11} & A_{12} & \dots & A_{1n} \\ A_{21} & A_{22} & \dots & A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{m1} & A_{m2} & \dots & A_{mn} \end{bmatrix}$$

### Basic Python NumPy Operations

```python
import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix Multiplication (Dot product)
C = A @ B
print("A @ B =\n", C)

# Transpose & Determinant
print("\nTranspose of A =\n", A.T)
print(f"Determinant of A: {np.linalg.det(A):.4f}")
```

Now, let's dive into the first chapter: **{doc}`Vector Spaces & Matrix Rank <vector_spaces>`**!

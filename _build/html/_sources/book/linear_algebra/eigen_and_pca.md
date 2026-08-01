# Eigenvalues, Eigenvectors & PCA

Matrix Diagonalization, Eigendecomposition, and Principal Component Analysis (PCA) are central to dimensionality reduction and feature extraction in Machine Learning.

---

## 1. Eigenvalues & Eigenvectors

When a square matrix $A \in \mathbb{R}^{n \times n}$ multiplies a vector $x$, it generally changes both the vector's length and direction. However, for certain special vectors, the transformation only **scales** the vector without changing its direction.

$$\begin{equation} A v = \lambda v \end{equation}$$

* **Eigenvector ($v$):** A non-zero vector whose direction remains unchanged after transformation by $A$.
* **Eigenvalue ($\lambda$):** The scaling factor corresponding to eigenvector $v$.

### Finding Eigenvalues & Eigenvectors
1. **Solve Characteristic Polynomial:** $\det(A - \lambda I) = 0$ to find eigenvalues $\lambda_i$.
2. **Solve Linear System:** $(A - \lambda_i I) v_i = 0$ to find corresponding eigenvectors $v_i$.

---

## 2. Matrix Diagonalization

A square matrix $A$ is **diagonalizable** if it can be written as:

$$A = P D P^{-1}$$

Where:
* $D$ is a **diagonal matrix** containing the eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$.
* $P$ is an invertible matrix whose columns are the corresponding eigenvectors $v_1, v_2, \dots, v_n$.

### Computing Matrix Powers ($A^k$)
Diagonalization dramatically simplifies matrix exponentiation:

$$A^k = (P D P^{-1})^k = P D^k P^{-1}$$

Since $D$ is diagonal, $D^k$ is computed instantaneously by raising each diagonal element to power $k$.

---

## 3. Principal Component Analysis (PCA)

Principal Component Analysis (PCA) is one of the most fundamental Machine Learning algorithms for dimensionality reduction, feature extraction, and data visualization.

Given a dataset with many correlated features, PCA transforms the data into a new coordinate system of orthogonal axes called **Principal Components (PCs)** using Eigendecomposition or Singular Value Decomposition (SVD) on the centered/standardized Covariance Matrix:

* **First Principal Component (PC1):** The axis along which the data has the **maximum variance** (spread).
* **Second Principal Component (PC2):** The axis orthogonal (perpendicular) to PC1 that captures the second highest variance.
* **Subsequent Components ($PC_k$):** Orthogonal to all previous components, capturing maximum remaining variance.

```{figure} ../../images/pca_ai_illustration.png
---
name: pca_ai_illustration
align: center
---
Principal Component Analysis (PCA) diagram showing 3D original space reduced to 2D PC space.
```

---

## 4. Python Implementation of PCA

Here is how to perform PCA step-by-step using NumPy:

```python
import numpy as np

# 1. Generate correlated 2D dataset (100 samples, 2 features)
np.random.seed(42)
X = np.random.multivariate_normal([0, 0], [[3, 2.2], [2.2, 2]], 100)

# 2. Step 1: Center the data (subtract mean)
X_centered = X - np.mean(X, axis=0)

# 3. Step 2: Compute Covariance Matrix
cov_matrix = np.cov(X_centered.T)

# 4. Step 3: Compute Eigenvalues & Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# 5. Step 4: Sort eigenvectors by eigenvalues in descending order
sorted_idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_idx]
eigenvectors = eigenvectors[:, sorted_idx]

print("Principal Component 1 (PC1) Vector:", eigenvectors[:, 0])
print(f"Variance explained by PC1: {eigenvalues[0] / np.sum(eigenvalues) * 100:.2f}%")

# 6. Step 5: Project 2D data onto 1D (Dimensionality Reduction)
X_1D = X_centered @ eigenvectors[:, 0]
print("Shape of reduced data:", X_1D.shape) # Reduced from (100, 2) to (100,)
```

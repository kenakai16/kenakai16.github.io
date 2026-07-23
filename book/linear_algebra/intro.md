# Linear Algebra

Linear Algebra is the mathematical language of Machine Learning. It allows us to represent and perform calculations on large datasets efficiently using vectors and matrices.

---

## 1. Vectors

A **vector** is an ordered list of numbers. In Data Science, we represent a data point (or feature vector) as a vector.

For example, a vector $x \in \mathbb{R}^3$ is written as:

$$x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$

---

## 2. Matrices

A **matrix** is a 2D grid of numbers. We write an $m \times n$ matrix $A$ (having $m$ rows and $n$ columns) as:

$$A = \begin{bmatrix} A_{11} & A_{12} & \dots & A_{1n} \\ A_{21} & A_{22} & \dots & A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{m1} & A_{m2} & \dots & A_{mn} \end{bmatrix}$$

### Matrix Transpose
The transpose of a matrix $A$ (written as $A^T$) is obtained by swapping its rows and columns:

$$(A^T)_{ij} = A_{ji}$$

---

## 3. Core Matrix Operations

### Matrix Multiplication
If $A$ is an $m \times p$ matrix and $B$ is a $p \times n$ matrix, their product $C = AB$ is an $m \times n$ matrix where each element is:

$$C_{ij} = \sum_{k=1}^p A_{ik} B_{kj}$$

### Identity Matrix
The identity matrix $I$ is a square matrix with ones on the main diagonal and zeros elsewhere:

$$I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

For any matrix $A$, $AI = IA = A$.

### Determinant
For a $2 \times 2$ matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the determinant is:

$$\det(A) = ad - bc$$

If $\det(A) \neq 0$, the matrix has an inverse $A^{-1}$ such that $A A^{-1} = I$.

---

## 4. Python Implementation (NumPy)

```python
import numpy as np

# Define matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 1. Matrix Multiplication
C = np.dot(A, B)  # or A @ B
print("A @ B =\n", C)

# 2. Transpose
print("\nTranspose of A =\n", A.T)

# 3. Determinant
det_A = np.linalg.det(A)
print(f"\nDeterminant of A: {det_A:.4f}")
```

---

## 5. Matrix Diagonalization

Matrix Diagonalization is one of the most important concepts in Linear Algebra. It allows us to decompose a square matrix into a simpler diagonal form, making complex matrix operations (such as computing matrix powers) extremely fast and computationally efficient.

### Definition of Diagonalization
Let $A$ be an $n \times n$ square matrix. We say $A$ is **diagonalizable** if there exists an invertible matrix $P$ and a diagonal matrix $D$ such that:

$$A = PDP^{-1}$$

equivalently, $P^{-1}AP = D$.

*   **$D$ (Diagonal Matrix)**: A matrix whose off-diagonal entries are all zero. The diagonal entries of $D$ are the **eigenvalues** of $A$.
*   **$P$ (Change of Basis Matrix)**: A matrix whose columns are the **eigenvectors** of $A$ corresponding to the eigenvalues in $D$.

### Eigenvalues and Eigenvectors
Before diagonalizing a matrix, we must find its eigenvalues and eigenvectors:
*   **Eigenvalues ($\lambda$)**: The scalars $\lambda$ that satisfy the characteristic equation:

    $$\det(A - \lambda I) = 0$$

    where $I$ is the identity matrix of the same size.
*   **Eigenvectors ($v$)**: The non-zero vectors $v$ that satisfy:

    $$(A - \lambda I)v = 0$$

### Conditions for Diagonalizability
An $n \times n$ matrix $A$ is diagonalizable if and only if it has **$n$ linearly independent eigenvectors**.
*   **Distinct Eigenvalues**: If $A$ has $n$ distinct eigenvalues, it is guaranteed to be diagonalizable.
*   **Repeated Eigenvalues**: If eigenvalues are repeated (multiplicity $> 1$), we must compare:
    *   **Algebraic Multiplicity**: The number of times $\lambda$ appears as a root of the characteristic polynomial.
    *   **Geometric Multiplicity**: The number of linearly independent eigenvectors associated with $\lambda$ (the dimension of the eigenspace).
    *   **Theorem**: $A$ is diagonalizable if and only if the algebraic multiplicity equals the geometric multiplicity for every eigenvalue.

---

### Step-by-Step Diagonalization Process

1.  **Find the Eigenvalues**: Solve the polynomial equation $\det(A - \lambda I) = 0$ for $\lambda$.
2.  **Find the Eigenvectors**: For each eigenvalue $\lambda_i$, solve the linear system $(A - \lambda_i I)v = 0$.
3.  **Check Independence**: Verify that the total number of linearly independent eigenvectors is $n$.
4.  **Form $P$ and $D$**:
    *   Place the eigenvectors as columns in $P$.
    *   Place the corresponding eigenvalues along the diagonal of $D$.
    *   *Important*: The order of eigenvalues in $D$ must match the order of eigenvectors in $P$.

---

### Numerical Example
Let us diagonalize the matrix:

$$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$$

#### Step 1: Find Eigenvalues
We compute the characteristic determinant:

$$\det(A - \lambda I) = \det \begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix} = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$$

Solving the quadratic equation gives two distinct eigenvalues:

$$\lambda_1 = 5, \quad \lambda_2 = 2$$

Since the eigenvalues are distinct, $A$ is diagonalizable.

#### Step 2: Find Eigenvectors
*   **For $\lambda_1 = 5$**: Solve $(A - 5I)v = 0$:

    $$\begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies -x + y = 0 \implies x = y$$

    Choosing $x = 1$, we obtain the eigenvector:

    $$v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

*   **For $\lambda_2 = 2$**: Solve $(A - 2I)v = 0$:

    $$\begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies 2x + y = 0 \implies y = -2x$$

    Choosing $x = 1$, we obtain the eigenvector:

    $$v_2 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}$$

#### Step 3: Form $P$ and $D$
We stack $v_1$ and $v_2$ as columns to form $P$, and place $\lambda_1$ and $\lambda_2$ on the diagonal of $D$:

$$P = \begin{pmatrix} 1 & 1 \\ 1 & -2 \end{pmatrix}, \quad D = \begin{pmatrix} 5 & 0 \\ 0 & 2 \end{pmatrix}$$

Thus, $A$ is diagonalized as $A = PDP^{-1}$.

---

### Key Applications
1.  **Computing Matrix Powers ($A^k$)**:
    Multiplying a matrix by itself $k$ times is computationally expensive. However, using diagonalization:

    $$A^k = (PDP^{-1})^k = P D^k P^{-1}$$
    Since $D$ is diagonal, $D^k$ is computed instantly by raising its diagonal entries to the power of $k$:

    $$D^k = \begin{pmatrix} 5^k & 0 \\ 0 & 2^k \end{pmatrix}$$
2.  **Machine Learning Foundations**:
    Diagonalization and eigendecomposition form the mathematical backbone of **Principal Component Analysis (PCA)**, which is used for dimensionality reduction and feature extraction in high-dimensional datasets.

---

### Python Implementation with NumPy

```python
import numpy as np

# Define the matrix
A = np.array([[4, 1], [2, 3]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors (as columns):")
print(eigenvectors)

# Reconstruct A from P, D, P^-1 to verify
P = eigenvectors
D = np.diag(eigenvalues)
P_inv = np.linalg.inv(P)

A_reconstructed = P @ D @ P_inv
print("\nReconstructed Matrix A:")
print(A_reconstructed)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Multiply the two matrices:

$$A = \begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 0 \\ 1 & 5 \end{bmatrix}$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Compute the dot product element by element:

$$AB = \begin{bmatrix} (1 \cdot 2 + 3 \cdot 1) & (1 \cdot 0 + 3 \cdot 5) \\ (2 \cdot 2 + 4 \cdot 1) & (2 \cdot 0 + 4 \cdot 5) \end{bmatrix} = \begin{bmatrix} 5 & 15 \\ 8 & 20 \end{bmatrix}$$
```

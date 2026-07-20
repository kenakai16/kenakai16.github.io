# Linear Algebra Basics

Linear Algebra is the mathematical language of Machine Learning. It allows us to represent and perform calculations on large datasets efficiently using vectors and matrices.

---

## 1. Vectors (Vectơ)

A **vector** is an ordered list of numbers. In Data Science, we represent a data point (or feature vector) as a vector.

For example, a vector $x \in \mathbb{R}^3$ is written as:

$$x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$$

---

## 2. Matrices (Ma trận)

A **matrix** is a 2D grid of numbers. We write an $m \times n$ matrix $A$ (having $m$ rows and $n$ columns) as:

$$A = \begin{bmatrix} A_{11} & A_{12} & \dots & A_{1n} \\ A_{21} & A_{22} & \dots & A_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ A_{m1} & A_{m2} & \dots & A_{mn} \end{bmatrix}$$

### Matrix Transpose (Chuyển vị)
The transpose of a matrix $A$ (written as $A^T$) is obtained by swapping its rows and columns:

$$(A^T)_{ij} = A_{ji}$$

---

## 3. Core Matrix Operations

### Matrix Multiplication (Nhân ma trận)
If $A$ is an $m \times p$ matrix and $B$ is a $p \times n$ matrix, their product $C = AB$ is an $m \times n$ matrix where each element is:

$$C_{ij} = \sum_{k=1}^p A_{ik} B_{kj}$$

### Identity Matrix (Ma trận đơn vị)
The identity matrix $I$ is a square matrix with ones on the main diagonal and zeros elsewhere:

$$I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

For any matrix $A$, $AI = IA = A$.

### Determinant (Định thức)
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

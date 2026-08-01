# Determinants

Given a square matrix, is there an easy way to know when it is invertible? Answering this fundamental question is the main goal of this chapter. The **determinant** of a square matrix is a single scalar value that determines whether the matrix is invertible (non-singular) and measures how the matrix scales areas or volumes under linear transformations.

---

## 1. Simple Examples (Small Cases)

For small matrices, the determinant formula is straightforward:

* **$1 \times 1$ Matrix:**
  If $M = \begin{bmatrix} m \end{bmatrix}$, then $M^{-1} = \begin{bmatrix} 1/m \end{bmatrix}$. Thus, $M$ is invertible if and only if:
  
  $$\det(M) = m \neq 0$$

* **$2 \times 2$ Matrix:**
  If $M = \begin{bmatrix} m_{11} & m_{12} \\ m_{21} & m_{22} \end{bmatrix}$, its inverse is:
  
  $$M^{-1} = \frac{1}{m_{11}m_{22} - m_{12}m_{21}} \begin{bmatrix} m_{22} & -m_{12} \\ -m_{21} & m_{11} \end{bmatrix}$$
  
  Thus, $M$ is invertible if and only if the denominator is non-zero. This quantity is defined as the determinant:
  
  $$\det(M) = m_{11}m_{22} - m_{12}m_{21}$$

* **$3 \times 3$ Matrix:**
  For $M = \begin{bmatrix} m_{11} & m_{12} & m_{13} \\ m_{21} & m_{22} & m_{23} \\ m_{31} & m_{32} & m_{33} \end{bmatrix}$, the determinant is:
  
  $$\det(M) = m_{11}m_{22}m_{33} - m_{11}m_{23}m_{32} + m_{12}m_{23}m_{31} - m_{12}m_{21}m_{33} + m_{13}m_{21}m_{32} - m_{13}m_{22}m_{31}$$

---

## 2. Permutations and the General Definition

To generalize the determinant formula to $n \times n$ matrices, we use the mathematics of **permutations**.

### What is a Permutation?
A permutation $\sigma$ of the set $\{1, 2, \dots, n\}$ is a bijective mapping of the set onto itself (a shuffle).
* There are $n!$ possible permutations of $n$ distinct objects.
* Every permutation can be built by successively swapping pairs of objects (transpositions).
* **Parity (Sign of Permutation):** A permutation is **even** if it requires an even number of swaps to be built from the identity permutation $[1, 2, \dots, n]$, and **odd** if it requires an odd number of swaps.

We define the sign function $\operatorname{sgn}(\sigma)$ as:

$$\operatorname{sgn}(\sigma) = \begin{cases} 1 & \text{if } \sigma \text{ is even} \\ -1 & \text{if } \sigma \text{ is odd} \end{cases}$$

### General Definition of the Determinant
The determinant of an $n \times n$ matrix $M = (m_{ij})$ is defined by the Leibniz formula:

$$\det(M) = \sum_{\sigma} \operatorname{sgn}(\sigma) m_{1\sigma(1)} m_{2\sigma(2)} \cdots m_{n\sigma(n)}$$

The sum is taken over all $n!$ possible permutations $\sigma$ of the set $\{1, \dots, n\}$.

---

## 3. Properties under Row and Column Operations

We can compute the determinant of larger matrices efficiently by analyzing how elementary row operations affect the determinant:

1. **Row Swap ($E_{ij}$):** Swapping two rows of a matrix flips the sign of the determinant:
   
   $$\det(E_{ij}M) = -\det(M)$$
   
   * *Corollary:* If a matrix $M$ has two identical rows, then swapping them changes the sign of the determinant but leaves the matrix unchanged ($\det(M) = -\det(M)$), which means **$\det(M) = 0$**.

2. **Row Scaling ($R_i(\lambda)$):** Multiplying a single row by a scalar $\lambda$ scales the determinant by $\lambda$:
   
   $$\det(R_i(\lambda)M) = \lambda \det(M)$$

3. **Row Addition ($S_{ij}(\mu)$):** Adding a scalar multiple of one row to another row leaves the determinant unchanged:
   
   $$\det(S_{ij}(\mu)M) = \det(M)$$

### Transpose Invariance
An important theorem states that the transpose of a matrix has the same determinant as the original matrix:

$$\det(M^T) = \det(M)$$

Because of this property, **every property of determinants regarding rows also applies to columns** (e.g., swapping two columns flips the sign of the determinant).

---

## 4. Expansion by Minors (Cofactor Expansion)

For matrices larger than $2 \times 2$, we can recursively calculate the determinant by expanding along any row or column using **minors** and **cofactors**.

* **Minor ($M_{ij}$):** The determinant of the submatrix obtained by deleting row $i$ and column $j$ from $M$.
* **Cofactor ($C_{ij}$):** The minor multiplied by a grid sign factor:
  
  $$\text{cofactor}(m_{ij}) = C_{ij} = (-1)^{i+j} M_{ij}$$

### Expansion Formula
Expanding along the $i$-th row:

$$\det(M) = \sum_{j=1}^{n} m_{ij} C_{ij} = \sum_{j=1}^{n} (-1)^{i+j} m_{ij} M_{ij}$$

### Example: $3 \times 3$ Expansion by Minors
Let's compute the determinant of:

$$M = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$$

Expanding along the first row:

$$\det(M) = 1 \det \begin{bmatrix} 5 & 6 \\ 8 & 9 \end{bmatrix} - 2 \det \begin{bmatrix} 4 & 6 \\ 7 & 9 \end{bmatrix} + 3 \det \begin{bmatrix} 4 & 5 \\ 7 & 8 \end{bmatrix}$$

$$\det(M) = 1(5 \cdot 9 - 8 \cdot 6) - 2(4 \cdot 9 - 7 \cdot 6) + 3(4 \cdot 8 - 7 \cdot 5)$$

$$\det(M) = 1(-3) - 2(-6) + 3(-3) = -3 + 12 - 9 = 0$$

Since $\det(M) = 0$, $M$ is not invertible.

### Simplification Using Row Operations
We can apply row operations to introduce zeros into a row or column before performing cofactor expansion to simplify calculations:

$$N = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 0 & 0 \\ 7 & 8 & 9 \end{bmatrix}$$

Since the second row has many zeros, we can swap Row 1 and Row 2 (which multiplies the determinant by $-1$):

$$\det(N) = -\det \begin{bmatrix} 4 & 0 & 0 \\ 1 & 2 & 3 \\ 7 & 8 & 9 \end{bmatrix} = -4 \det \begin{bmatrix} 2 & 3 \\ 8 & 9 \end{bmatrix} = -4(2 \cdot 9 - 8 \cdot 3) = 24$$

---

## 5. Determinants of Products, Diagonals, and Inverses

* **Diagonal Matrices:** The determinant of a diagonal matrix is the product of its diagonal entries.
  
  $$\det(\text{diag}(d_1, \dots, d_n)) = d_1 d_2 \cdots d_n \implies \det(I) = 1$$

* **Product Rule:** For any two square matrices $M$ and $N$:
  
  $$\det(MN) = \det(M) \det(N)$$

* **Inverse Rule:**
  
  $$\det(M^{-1}) = \frac{1}{\det(M)}$$

---

## 6. The Adjoint Matrix and Inverse Formula

For any square matrix $M$, we can define the **Cofactor Matrix** $C$ where each entry is $C_{ij} = \text{cofactor}(m_{ij})$. 
The transpose of the cofactor matrix is called the **Adjoint (or Adjuggate) Matrix**, denoted as $\operatorname{adj}(M)$:

$$\operatorname{adj}(M) = C^T$$

### Important Relation
The product of a matrix and its adjoint always yields a diagonal matrix of determinants:

$$M \operatorname{adj}(M) = \det(M) I$$

This gives us an explicit analytical formula for the inverse matrix:

$$M^{-1} = \frac{1}{\det(M)} \operatorname{adj}(M)$$

---

## 7. Geometric Application: Volume of a Parallelepiped

In three-dimensional space, the absolute value of the determinant of a $3 \times 3$ matrix represents the **volume of the parallelepiped** spanned by its column vectors $u, v$, and $w$:

$$\text{Volume} = |\det(\begin{bmatrix} u & v & w \end{bmatrix})|$$

This matches the scalar triple product $|u \cdot (v \times w)|$ learned in multivariate calculus.

---

## 8. Python Implementation (NumPy & SymPy)

We can compute determinants, transposes, inverses, and adjoint matrices in Python:

```python
import numpy as np
import sympy as sp

# 1. Numerical calculations with NumPy
M_num = np.array([
    [3, -1, -1],
    [1,  2,  0],
    [0,  1,  1]
])
det_num = np.linalg.det(M_num)
print("Numerical Determinant (NumPy):", round(det_num, 4))  # 6.0
print("Numerical Inverse (NumPy):\n", np.linalg.inv(M_num))

# 2. Symbolic and Adjoint calculations with SymPy
a, b, c, d = sp.symbols('a b c d')
M_sym = sp.Matrix([[a, b], [c, d]])

# Compute symbolic determinant, inverse, and adjoint
print("\nSymbolic Determinant:", M_sym.det())
print("Symbolic Adjoint (adj M):\n", M_sym.adjugate())
print("Symbolic Inverse (M^-1):\n", M_sym.inv())
```

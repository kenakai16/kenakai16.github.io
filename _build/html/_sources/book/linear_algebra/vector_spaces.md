# Vector Spaces & Matrix Rank

Vector spaces and matrix rank form the foundation of linear algebra. Understanding these concepts helps Data Scientists detect feature redundancy and solve linear systems efficiently.

---

## 1. Vector Spaces & Subspaces

A **Vector Space** $V$ is a set of vectors closed under vector addition and scalar multiplication. 

A **Subspace** $S \subseteq V$ is a subset of a vector space that is itself a vector space. It must satisfy three rules:
1. Contains the zero vector $\vec{0} \in S$.
2. **Closed under addition:** If $u, v \in S$, then $u + v \in S$.
3. **Closed under scalar multiplication:** If $v \in S$ and $c \in \mathbb{R}$, then $c v \in S$.

---

## 2. Linear Independence, Span & Basis

### Linear Combination & Span
* **Linear Combination:** A vector $v$ is a linear combination of $\{v_1, \dots, v_k\}$ if:
  
  $$v = c_1 v_1 + c_2 v_2 + \dots + c_k v_k \quad (c_i \in \mathbb{R})$$

* **Span:** The set of all possible linear combinations of vectors $\{v_1, \dots, v_k\}$:
  
  $$\text{Span}(v_1, \dots, v_k) = \{c_1 v_1 + \dots + c_k v_k \mid c_i \in \mathbb{R}\}$$

### Linear Independence
A set of vectors $\{v_1, \dots, v_k\}$ is **linearly independent** if no vector in the set can be written as a linear combination of the others. Mathematically, the only solution to:

$$c_1 v_1 + c_2 v_2 + \dots + c_k v_k = \vec{0}$$

is $c_1 = c_2 = \dots = c_k = 0$. If non-zero constants $c_i$ exist, the vectors are **linearly dependent**.

### Basis & Dimension
* **Basis:** A minimal set of linearly independent vectors that spans a vector space $V$.
* **Dimension ($\dim(V)$):** The number of vectors in any basis for $V$. For example, $\mathbb{R}^3$ has dimension 3.

---

## 3. Matrix Rank & Multicollinearity

The **Rank** of a matrix $A \in \mathbb{R}^{m \times n}$ (denoted $\text{rank}(A)$) is the maximum number of linearly independent column vectors (which equals the maximum number of linearly independent row vectors).

* **Full Rank:** $\text{rank}(A) = \min(m, n)$.
* **Rank Deficient:** $\text{rank}(A) < \min(m, n)$, meaning at least one column/row is a linear combination of others.

### Data Science Insight: Multicollinearity in Regression
In linear regression ($y = X w$), if two features are perfectly correlated (e.g., house size in sq ft and sq meters), the feature matrix $X$ becomes rank deficient.

Consequently, the matrix $(X^T X)$ is non-invertible (singular), causing Ordinary Least Squares (OLS) estimation $w = (X^T X)^{-1} X^T y$ to fail or yield wildly unstable weights!

```python
import numpy as np

# Feature matrix X with a redundant column (Col 3 = 2 * Col 1)
X = np.array([
    [1, 2, 2],
    [2, 5, 4],
    [3, 1, 6]
])

# Compute rank
rank = np.linalg.matrix_rank(X)
print("Matrix Rank:", rank)  # Output: 2 (Rank deficient because Col 3 is dependent!)

# Attempting to invert (X^T X) will result in numerical instability or high condition number
XTX = X.T @ X
print("Condition Number of X^T X:", np.linalg.cond(XTX))  # Very large number!
```

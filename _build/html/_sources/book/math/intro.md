# Essential Mathematics

Essential Mathematics is the foundation for Data Science and Machine Learning. Having a strong intuition of these mathematical principles allows you to understand how machine learning models work under the hood.

---

## 1. Linear Algebra (Đại số tuyến tính)

Linear algebra is the mathematics of data. Matrices and vectors are used to represent data, weights, and operations in machine learning algorithms.

### Vectors & Matrices
- A **Vector** is an ordered list of numbers.
- A **Matrix** is a 2D grid of numbers.

$$\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}$$

---

## 2. Calculus & Derivatives (Giải tích & Đạo hàm)

Calculus helps us understand how functions change. In machine learning, we use optimization (which relies heavily on derivatives and gradients) to train models by minimizing loss functions.

### The Gradient
The gradient is a vector of partial derivatives, pointing in the direction of the steepest increase of a function:

$$\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$

---

## 3. Integration (Tích phân)

Integration is the reverse of differentiation. It is primarily used to find the area under a curve, which is essential for calculating probabilities from continuous probability distributions.

$$\int_{a}^{b} f(x) \, dx$$

---

## Exercises

```{admonition} Exercise 1
:class: tip
Find the gradient of the function $f(x, y) = 3x^2 + 2y^3$ at the point $(1, 2)$.
```

```{admonition} Solution — Exercise 1
:class: dropdown
The partial derivatives are:
- $\frac{\partial f}{\partial x} = 6x \implies 6(1) = 6$
- $\frac{\partial f}{\partial y} = 6y^2 \implies 6(2^2) = 24$

Therefore, the gradient at $(1, 2)$ is:
$$\nabla f(1, 2) = \begin{bmatrix} 6 \\ 24 \end{bmatrix}$$
```

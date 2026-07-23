# Convex Sets & Functions

This page covers the mathematical definition and geometric properties of convex sets and convex functions, based on Chapters 2 and 3 of Stephen Boyd's *Convex Optimization*.

---

## Part I: Convex Sets

A set $C \subseteq \mathbb{R}^n$ is **convex** if the line segment between any two points in $C$ lies entirely in $C$. That is, for any $x_1, x_2 \in C$ and $0 \leq \theta \leq 1$:

$$\theta x_1 + (1-\theta)x_2 \in C$$

---

## Part II: Convex Functions (Chapter 3)

A function $f: \mathbb{R}^n \to \mathbb{R}$ is **convex** if its domain $\text{dom } f$ is a convex set and for all $x, y \in \text{dom } f$, $0 \leq \theta \leq 1$:

$$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$

### 1. Basic Properties and Examples (3.1)

#### First-order Condition for Convexity
A differentiable function $f$ is convex if and only if $\text{dom } f$ is convex and:

$$f(y) \geq f(x) + \nabla f(x)^T (y-x) \quad \text{for all } x, y \in \text{dom } f$$

Geometrically, the tangent plane at any point acts as a global lower bound.

#### Second-order Condition for Convexity
A twice-differentiable function $f$ is convex if and only if its Hessian matrix is positive semi-definite:

$$\nabla^2 f(x) \succeq 0 \quad \text{for all } x \in \text{dom } f$$

#### Important Examples:
- **Exponential**: $e^{ax}$ is convex on $\mathbb{R}$.
- **Powers**: $x^p$ is convex on $\mathbb{R}_{++}$ for $p \geq 1$ or $p \leq 0$.
- **Negative Logarithm**: $-\ln(x)$ is convex on $\mathbb{R}_{++}$.
- **Max function**: $\max(x_1, \dots, x_n)$ is convex on $\mathbb{R}^n$.

---

### 2. Operations that Preserve Convexity (3.2)

- **Nonnegative weighted sum**: $f = w_1 f_1 + w_2 f_2$ is convex if $f_1, f_2$ are convex and $w_1, w_2 \geq 0$.
- **Composition with affine mapping**: $g(x) = f(Ax + b)$ is convex if $f$ is convex.
- **Pointwise maximum**: If $f_s(x)$ is convex for each $s \in \mathcal{S}$, then $f(x) = \sup_{s \in \mathcal{S}} f_s(x)$ is convex.
- **Partial Minimization**: If $g(x, y)$ is convex in $(x, y)$ and $C$ is a convex set, then $f(x) = \inf_{y \in C} g(x, y)$ is convex.

---

### 3. The Conjugate Function (3.3)

Let $f: \mathbb{R}^n \to \mathbb{R}$. The **conjugate function** $f^*: \mathbb{R}^n \to \mathbb{R}$ (also known as the Fenchel conjugate) is defined as:

$$f^*(y) = \sup_{x \in \text{dom } f} (y^T x - f(x))$$

The conjugate function $f^*$ is **always convex**, even if the original function $f$ is not convex, because it is the pointwise supremum of a family of affine functions of $y$.

#### Example:
For $f(x) = \frac{1}{2} x^T Q x$ where $Q$ is symmetric positive definite:

$$f^*(y) = \frac{1}{2} y^T Q^{-1} y$$

---

### 4. Quasiconvex Functions (3.4)

A function $f: \mathbb{R}^n \to \mathbb{R}$ is **quasiconvex** (or unimodal) if its domain and all its **sublevel sets** are convex:

$$S_\alpha = \{x \in \text{dom } f \mid f(x) \leq \alpha\}$$

#### Modified Jensen's Inequality
A function $f$ is quasiconvex if and only if its domain is convex and for any $x, y \in \text{dom } f$ and $0 \leq \theta \leq 1$:

$$f(\theta x + (1-\theta)y) \leq \max(f(x), f(y))$$

#### First-order Condition for Quasiconvexity
A differentiable function $f$ with convex domain is quasiconvex if and only if:

$$f(y) \leq f(x) \implies \nabla f(x)^T (y-x) \leq 0 \quad \text{for all } x, y \in \text{dom } f$$

This means that if we move in a direction that decreases the function value, the directional derivative must be negative or zero.

#### Key Property: Sums
Unlike convex functions, the sum of two quasiconvex functions is **not necessarily quasiconvex**. For example, the functions:

$$f(x) = x^3 \quad \text{and} \quad g(x) = -x$$

are both quasiconvex on $\mathbb{R}$, but their sum:

$$(f+g)(x) = x^3 - x$$

is not (it is not unimodal and has multiple local extrema on $\mathbb{R}$).

---

### 5. Log-Concave and Log-Convex Functions (3.5)

A function $f: \mathbb{R}^n \to \mathbb{R}$ is **log-concave** if $f(x) > 0$ for all $x \in \text{dom } f$ and the logarithm $\ln f(x)$ is a concave function:

$$f(\theta x + (1-\theta)y) \geq f(x)^\theta f(y)^{1-\theta} \quad \text{for } 0 \leq \theta \leq 1$$

Similarly, $f$ is **log-convex** if $\ln f(x)$ is convex.

#### Second-order Condition for Log-Concavity
A twice-differentiable function $f$ with convex domain is log-concave if and only if:

$$f(x) \nabla^2 f(x) \preceq \nabla f(x) \nabla f(x)^T \quad \text{for all } x \in \text{dom } f$$

#### Important Examples
*   **Powers**: $f(x) = x^a$ on $\mathbb{R}_{++}$ is log-convex for $a \leq 0$, and log-concave for $a \geq 0$.
*   **Normal Distribution**: The Gaussian PDF is log-concave.
*   **Cumulative Gaussian Distribution**: The cumulative distribution function is log-concave:

    $$\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-u^2/2} \, du$$

#### Properties and Integration
*   **Product & Sum Rules**:
    *   The product of log-concave functions is log-concave.
    *   The sum of log-concave functions is **not always** log-concave.
*   **Integration Theorem**: If $f: \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R}$ is log-concave, then the marginal integral function:

    $$g(x) = \int f(x, y) \, dy$$

    is log-concave.
*   **Consequences**:
    *   **Convolution**: The convolution of two log-concave functions is log-concave:

        $$(f * g)(x) = \int f(x-y)g(y) \, dy$$

    *   **Probability over Convex Sets**: If $y$ is a random variable with a log-concave PDF, the probability that $x+y$ lies in a convex set $C$ is log-concave in $x$:

        $$f(x) = \text{prob}(x+y \in C)$$

    *   **Yield Function Example**: In manufacturing, the yield function (where $x$ represents nominal parameters, $w$ is random variation, and $S$ is the set of acceptable values) is log-concave:

        $$Y(x) = \text{prob}(x+w \in S)$$

        Therefore, the yield regions $\{x \mid Y(x) \geq \alpha\}$ are convex sets.

---

### 6. Convexity with Respect to Generalized Inequalities (3.6)

Let $K \subseteq \mathbb{R}^m$ be a proper cone.
- A function $f: \mathbb{R}^n \to \mathbb{R}^m$ is **$K$-convex** if for all $x, y \in \text{dom } f$ and $0 \leq \theta \leq 1$:

$$f(\theta x + (1-\theta)y) \preceq_K \theta f(x) + (1-\theta) f(y)$$

This maps the classical definition of convexity to vector-valued functions using cone-based ordering relations.

#### Example: Matrix Square
The matrix square function $f: \mathbb{S}^m \to \mathbb{S}^m$, defined as $f(X) = X^2$, is $\mathbb{S}^m_+$-convex.

**Proof**:
For any fixed vector $z \in \mathbb{R}^m$, we can evaluate the scalar function:

$$g(X) = z^T X^2 z = z^T X X z = \| X z \|_2^2$$

Since the Euclidean norm is convex, $g(X) = \| X z \|_2^2$ is a convex function of $X$. Therefore, for all $X, Y \in \mathbb{S}^m$ and $0 \leq \theta \leq 1$:

$$z^T (\theta X + (1-\theta) Y)^2 z \leq \theta z^T X^2 z + (1-\theta) z^T Y^2 z$$

Since this inequality holds for all vectors $z \in \mathbb{R}^m$, by definition of the positive semidefinite cone $\mathbb{S}^m_+$, it implies:

$$(\theta X + (1-\theta) Y)^2 \preceq_{\mathbb{S}^m_+} \theta X^2 + (1-\theta) Y^2$$

This proves that $f(X) = X^2$ is indeed $\mathbb{S}^m_+$-convex.

---

## Exercises

```{admonition} Exercise 1
:class: tip
Find the conjugate function $f^*(y)$ of the negative entropy function:

$$f(x) = x \ln x \quad (\text{domain } x > 0)$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
The conjugate is defined as $f^*(y) = \sup_{x > 0} (yx - x \ln x)$.
To find the supremum, take the derivative with respect to $x$ and set to zero:

$$\frac{d}{dx}(yx - x\ln x) = y - \ln x - 1 = 0 \implies \ln x = y - 1 \implies x^* = e^{y-1}$$
Substitute $x^*$ back into the equation:

$$f^*(y) = y(e^{y-1}) - e^{y-1}(y-1) = e^{y-1}(y - y + 1) = e^{y-1}$$
Thus, the conjugate function is $f^*(y) = e^{y-1}$.
```

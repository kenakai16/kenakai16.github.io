# Exponents

An **exponent** (or power) represents repeated multiplication of a number by itself. In Data Science, exponential functions model growth rates, decay rates, and activation functions.

---

## 1. What Is an Exponent?

An exponent is written as:

$$x^n$$

Where:
- $x$ is the **base**.
- $n$ is the **exponent** (or power).

This represents $x$ multiplied by itself $n$ times:
$$3^4 = 3 \times 3 \times 3 \times 3 = 81$$

### Rules of Exponents
Exponents follow specific algebraic properties:
- **Product Rule**: $x^a \cdot x^b = x^{a+b}$
- **Quotient Rule**: $\frac{x^a}{x^b} = x^{a-b}$
- **Power of a Power Rule**: $(x^a)^b = x^{a \cdot b}$
- **Negative Exponent Rule**: $x^{-n} = \frac{1}{x^n}$
- **Fractional Exponents (Roots)**: $x^{\frac{1}{n}} = \sqrt[n]{x}$

---

## 2. Euler's Number ($e$)

Of special importance in calculus and data science is **Euler's number** $e \approx 2.71828$. It is an irrational number that represents the base of natural growth:

$$y = e^x$$

---

## 3. Python Implementation

```python
import math

# Exponential calculations: 3^4
print("3^4 =", 3**4)

# Euler's number calculation: e^2
print("e^2 =", math.exp(2))
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Simplify the expression:
$$\frac{x^5 \cdot x^2}{x^3}$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Apply the rules of exponents:
1. Product Rule: $x^5 \cdot x^2 = x^{5+2} = x^7$
2. Quotient Rule: $\frac{x^7}{x^3} = x^{7-3} = x^4$
```

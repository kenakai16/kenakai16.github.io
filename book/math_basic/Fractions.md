# Fractions

Fractions represent a part of a whole. In data science, fractions are the foundation of probabilities, proportions, and ratios (such as precision and recall).

---

## 1. What Is a Fraction?

A fraction is written as:

$$\frac{a}{b}$$

Where:
- $a$ is the **numerator** (how many parts we have).
- $b$ is the **denominator** (how many equal parts the whole is divided into).

---

## 2. Basic Operations

### Addition & Subtraction
To add or subtract fractions, they must have a **common denominator**:

$$\frac{1}{3} + \frac{1}{2} = \frac{2}{6} + \frac{3}{6} = \frac{5}{6}$$

### Multiplication
Multiply numerators together and denominators together:

$$\frac{a}{b} \times \frac{c}{d} = \frac{a \cdot c}{b \cdot d}$$

$$\frac{2}{3} \times \frac{3}{4} = \frac{6}{12} = \frac{1}{2}$$

### Division
To divide by a fraction, multiply by its **reciprocal**:

$$\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \times \frac{d}{c} = \frac{a \cdot d}{b \cdot c}$$

---

## 3. Python Fraction Module

Python has a built-in module `fractions` to handle exact fraction arithmetic:

```python
from fractions import Fraction

# Create fractions
f1 = Fraction(1, 3)
f2 = Fraction(1, 2)

# Arithmetic operations
print("1/3 + 1/2 =", f1 + f2)
print("2/3 * 3/4 =", Fraction(2, 3) * Fraction(3, 4))
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Calculate:
$$\frac{3}{4} \div \frac{2}{3} - \frac{1}{2}$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
1. Perform division first:

   $$\frac{3}{4} \times \frac{3}{2} = \frac{9}{8}$$
2. Perform subtraction:

   $$\frac{9}{8} - \frac{1}{2} = \frac{9}{8} - \frac{4}{8} = \frac{5}{8}$$
```

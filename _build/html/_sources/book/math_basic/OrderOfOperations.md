# Order of Operations

In mathematics and computer science, we evaluate expressions based on a strict order of operations to avoid ambiguity. The standard convention is **PEMDAS** (or **BODMAS** in some regions).

---

## 1. The PEMDAS Rule

When solving mathematical expressions, perform calculations in the following order:

1. **P**arentheses `()`
2. **E**xponents (Powers, Roots)
3. **M**ultiplication and **D**ivision (evaluated from left to right)
4. **A**ddition and **S**ubtraction (evaluated from left to right)

---

## 2. Python Implementation

Python automatically follows PEMDAS rules when calculating expressions:

```python
# Expression: 3 + 5 * 2^3 - (4 / 2)
# Step-by-step:
# 1. Parentheses: (4 / 2) -> 2.0
# 2. Exponents: 2**3 -> 8
# 3. Multiplication: 5 * 8 -> 40
# 4. Add/Subtract: 3 + 40 - 2.0 -> 41.0

result = 3 + 5 * 2**3 - (4 / 2)
print("Computed result:", result)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Evaluate the expression manually:
$$10 - 2 \times (3 + 1)^2 \div 8 + 5$$
Verify your answer with Python.
```

```{admonition} Solution — Exercise 1
:class: dropdown
Using PEMDAS:
1. Parentheses: $(3 + 1) = 4$
2. Exponents: $4^2 = 16$
3. Multiplication/Division (left to right):
   - $2 \times 16 = 32$
   - $32 \div 8 = 4$
4. Addition/Subtraction (left to right):
   - $10 - 4 = 6$
   - $6 + 5 = 11$
```

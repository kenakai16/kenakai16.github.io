# Decimals & Percentages

Decimals and percentages are alternative ways of expressing fractions and proportions. In Data Science, we constantly work with probability values as decimals (e.g., $0.85$) and interpret evaluation metrics as percentages (e.g., $85\%$).

---

## 1. Decimals

A decimal is a fraction whose denominator is a power of ten (10, 100, 1000, etc.), written using a decimal point.

For example:

$$\frac{7}{10} = 0.7$$
$$\frac{125}{1000} = 0.125$$

### Repeating Decimals
Some fractions produce infinitely repeating decimals:

$$\frac{1}{3} = 0.3333\dots$$

---

## 2. Percentages

The word **percent** means "per hundred". To convert a decimal to a percentage, multiply by 100 and add the $\%$ sign.

$$0.85 \times 100 = 85\%$$

### Percentage Change
In data analysis, we often compute the percentage change between two values (e.g. increase in website traffic):

$$\text{Percentage Change} = \frac{\text{New Value} - \text{Old Value}}{\text{Old Value}} \times 100\%$$

---

## 3. Python Implementations

```python
# Calculating percentage change
old_revenue = 150
new_revenue = 180

pct_change = ((new_revenue - old_revenue) / old_revenue) * 100
print(f"Revenue growth: {pct_change:.1f}%")
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
A model correctly classified 45 out of 60 test images. What is the classification accuracy in percentage?
```

```{admonition} Solution — Exercise 1
:class: dropdown
Compute the proportion:

$$\text{Accuracy} = \frac{45}{60} = 0.75$$
Convert to percentage:

$$0.75 \times 100\% = 75\%$$
```

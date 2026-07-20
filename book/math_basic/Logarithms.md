# Logarithms

A **logarithm** is the mathematical operation that is the inverse of exponentiation. Logarithms are widely used in Data Science to scale skewed data (log-transform) and calculate errors in classification loss functions.

---

## 1. What Is a Logarithm?

The logarithm answers the question: *To what power must we raise the base to get a certain number?*

If:

$$b^y = x$$

Then:

$$\log_b(x) = y$$

For example:

$$\log_2(8) = 3 \quad \text{because} \quad 2^3 = 8$$

### Intuition: The "Zero-Counting" Operation

To understand logarithms intuitively, think of the **base-10 logarithm** ($\log_{10}$) as a tool that **counts the number of zeros** in a number (when written as a power of 10):

- $10$ has **1** zero $\implies \log_{10}(10) = 1$
- $100$ has **2** zeros $\implies \log_{10}(100) = 2$
- $1,000$ has **3** zeros $\implies \log_{10}(1,000) = 3$
- $1,000,000$ (1 million) has **6** zeros $\implies \log_{10}(1,000,000) = 6$

Thus, the logarithm tells us the "scale" or "order of magnitude" of a number. If a number falls between $100$ and $1,000$ (e.g., $500$), its logarithm will be a decimal between $2$ and $3$ ($\log_{10}(500) \approx 2.699$).

### Why Do We Use Logarithms?

Logarithms are essential tools in both scientific measurements and modern data science for several key reasons:

#### A. Simplifying Arithmetic: Multiplication to Addition (Historical)
Before calculators existed, multiplying extremely large numbers (like astronomical distances) was highly tedious and error-prone. Logarithms solve this through the product rule:

$$\log_b(x \cdot y) = \log_b(x) + \log_b(y)$$

Astronomers and mathematicians only needed to look up the log values of their numbers in physical "log tables," **add** them together, and then perform an inverse lookup (anti-logarithm) to find the final product. Adding two numbers is far simpler than multiplying them.

#### B. Compressing Scales for Real-World Measurements
In nature, many physical phenomena have ranges of intensity so vast that linear scales are completely impractical. We use logarithmic scales to compress these into human-readable ranges:

1. **Earthquakes (Richter Scale)**: The Richter scale is logarithmic. An earthquake of magnitude 6 is not just "one unit" stronger than a magnitude 5; its seismic wave amplitude is actually $10$ times larger. A magnitude 8 earthquake is $1,000$ times stronger than a magnitude 5.
2. **Acidity (pH Scale)**: The pH scale measures the concentration of hydrogen ions $[H^+]$. A pH of 3 is $10$ times more acidic than a pH of 4, and $100$ times more acidic than a pH of 5.
3. **Sound Intensity (Decibel Scale)**: Human hearing can detect sound intensities spanning over 12 orders of magnitude. The decibel (dB) scale uses logarithms to map this massive range to a manageable scale from 0 dB (threshold of hearing) to 120 dB (pain threshold).

#### C. Handling Skewed Data (Modern Data Science)
In data science, we frequently encounter features with highly skewed distributions where a few data points are orders of magnitude larger than the rest. Examples include individual income, video view counts on YouTube, or word frequencies in a text corpus.

If we train a Machine Learning model on this raw, skewed data, the model might overfit to the extreme values (outliers) or fail to capture patterns in the smaller values. By applying a **Log-transform**, we compress the scale:
- For \$100,000: $100,000 = 10^5 \implies \log_{10}(100,000) = 5$
- For \$1,000,000,000: $1,000,000,000 = 10^9 \implies \log_{10}(1,000,000,000) = 9$

Instead of handling the massive gap between \$100,000 and \$1,000,000,000, the machine learning algorithm works with a balanced range from $5$ to $9$. This scale compression helps optimization algorithms (like gradient descent) converge much faster and makes models robust to outliers.

---

## 2. Euler's Number ($e$) and the Natural Logarithm ($\ln$)

### What is Euler's Number ($e$)?
Euler's number, denoted as $e$, is a mathematical constant approximately equal to $2.71828$. It is the base of natural growth and decay. 

The value of $e$ is defined as the limit of the compound interest formula as the number of compounding periods approaches infinity:

$$e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n \approx 2.71828$$

The **Natural Logarithm ($\ln(x)$)** is simply a logarithm with base $e$:

$$\ln(x) = \log_e(x)$$

Because $e$ and $\ln$ are inverse functions, they cancel each other out:

$$\ln(e^x) = x \quad \text{and} \quad e^{\ln(x)} = x$$

---

### Real-World Application: Continuous Compound Interest
In finance, if an investment of principal $P$ grows at an annual interest rate $r$ compounded $n$ times a year for $t$ years, the final amount $A$ is:

$$A = P\left(1 + \frac{r}{n}\right)^{nt}$$

If the interest is compounded **continuously** (meaning $n \to \infty$, compounding every microsecond), the formula simplifies using Euler's number $e$ (often called the **PERT formula**):

$$A = P e^{rt}$$

---

### Deriving the "Rule of 72" in Investing
The **Rule of 72** is a quick shortcut used to estimate how many years ($t$) it takes to double your money at a given annual interest rate ($r$ expressed as a percentage, e.g., $r\%$). 

$$\text{Years to double} \approx \frac{72}{\text{Interest Rate}}$$

We can mathematically derive this rule using the natural logarithm:

1. To double our money ($A = 2P$), we substitute this into the continuous compound interest formula:

   $$2P = P e^{rt} \implies 2 = e^{rt}$$

2. Take the natural logarithm ($\ln$) of both sides to get rid of $e$:

   $$\ln(2) = \ln(e^{rt})$$

   $$\ln(2) = rt$$

3. Since $\ln(2) \approx 0.693$, we get:

   $$rt \approx 0.693 \implies t \approx \frac{0.693}{r}$$

4. If we express the interest rate $r$ as a percentage (e.g., $R = r \times 100$, so $R = 8$ for $8\%$), the formula becomes:

   $$t \approx \frac{69.3}{R}$$

5. While $69.3$ is the exact mathematical numerator for continuous compounding, $72$ is used in finance because it is highly divisible by many common interest rates (such as 2, 3, 4, 6, 8, 9, 12), making mental math extremely easy. For example, at an $8\%$ interest rate, money will double in approximately $72 / 8 = 9$ years (the exact value is about $8.66$ years).

---

## 3. Common Properties of Logarithms

Logarithms possess unique mathematical properties that simplify complex operations:

- **Product Rule**: $\log_b(x \cdot y) = \log_b(x) + \log_b(y)$
- **Quotient Rule**: $\log_b(\frac{x}{y}) = \log_b(x) - \log_b(y)$
- **Power Rule**: $\log_b(x^k) = k \cdot \log_b(x)$

### Two Crucial Bases:
1. **Natural Logarithm ($\ln(x)$)**: Logarithm with base $e \approx 2.71828$.
2. **Common Logarithm ($\log_{10}(x)$)**: Logarithm with base 10.

---

## 4. Python Implementation

We can compute logarithms in Python using the `math` and `numpy` libraries:

```python
import math
import numpy as np

# Natural logarithm: ln(10)
print("ln(10) =", math.log(10)) # math.log defaults to base e

# Base 10 logarithm
print("log10(100) =", math.log10(100))

# NumPy log-transform on an array
data = np.array([1, 10, 100, 1000])
log_data = np.log10(data)
print("Log-transformed data:", log_data)
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Solve for $x$:

$$\log_3(x) = 4$$
```

```{admonition} Exercise 2
:class: tip
Expand the expression using logarithm properties:

$$\ln\left(\frac{x^3}{y}\right)$$
```

```{admonition} Solution — Exercise 1
:class: dropdown
Convert to exponential form:

$$x = 3^4 = 81$$
```

```{admonition} Solution — Exercise 2
:class: dropdown
Apply the quotient and power rules:

$$\ln\left(\frac{x^3}{y}\right) = \ln(x^3) - \ln(y) = 3\ln(x) - \ln(y)$$
```

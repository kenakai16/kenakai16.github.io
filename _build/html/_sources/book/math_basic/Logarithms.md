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

---

### Why Do We Use Logarithms? Real-World Applications

In nature, human senses and physical phenomena span vast scales of magnitude. Linearly graphing numbers from $1$ to $10,000,000,000$ on a single piece of paper is impossible. Logarithms compress these huge numbers into human-manageable scales.

Here is how logarithms are used across various scientific domains and real-world phenomena:

#### 1. Earthquakes (The Richter Scale)

The Richter scale quantifies the energy released by earthquakes on a base-10 logarithmic scale:

$$\text{Magnitude } M = \log_{10}(A) - \log_{10}(A_0)$$

Where $A$ is the maximum amplitude recorded by a seismograph.

* **Seismic Wave Amplitude:** Because of the $\log_{10}$ scale, each whole unit increase of $+1.0$ on the Richter scale means the ground shaking amplitude is **10 times greater**.
  - A magnitude 6.0 earthquake has **10 times** the amplitude of a 5.0 earthquake.
  - A magnitude 7.0 earthquake has $10 \times 10 = \mathbf{100\text{ times}}$ the amplitude of a 5.0 earthquake.

* **Radiated Energy ($E$):** The actual energy released scales exponentially as $10^{1.5 \times M}$ (or $\approx 31.6^M$):
  
  $$\frac{E_2}{E_1} = 10^{1.5 \times (M_2 - M_1)}$$

  - An increase of $+1.0$ in magnitude releases $10^{1.5} \approx \mathbf{31.6\text{ times}}$ more energy.
  - An increase of $+2.0$ in magnitude (e.g., from 5.0 to 7.0) releases $10^{1.5 \times 2} = 10^3 = \mathbf{1,000\text{ times}}$ more energy!

#### 2. Sound Intensity (Decibel Scale - dB)
Human ears can process sound power ranging from a quiet whisper ($10^{-12} \text{ W/m}^2$) to a jet engine takeoff ($10^2 \text{ W/m}^2$) — a difference of **100,000,000,000,000 times** ($10^{14}$).
- We use decibels: $L = 10 \cdot \log_{10}\left(\frac{I}{I_0}\right)$
- Every addition of **10 dB** represents a **10-fold increase** in sound intensity.
- A 60 dB sound (normal conversation) is 1,000 times more intense than a 30 dB sound (whisper).

#### 3. Acidity and Chemistry (pH Scale)
The pH scale measures hydrogen ion concentration $[H^+]$ in a liquid: $\text{pH} = -\log_{10}[H^+]$.
- A pH drop of 1 unit means the solution is **10 times more acidic**.
- Battery acid ($\text{pH} \approx 1$) is **100,000 times more acidic** than coffee ($\text{pH} \approx 5$).

#### 4. Atmospheric Pressure, Hurricanes & Altitude
Atmospheric pressure decreases exponentially with increasing altitude ($P = P_0 e^{-h/H}$). 
- Meteorologists use log-scale calculations to estimate altitude from pressure readings or track pressure drops during **hurricanes and tropical storms**.
- In hurricane tracking, central barometric pressure drops exponentially as wind speeds increase.

#### 5. Stellar Brightness (Astronomy - Magnitude Scale)
Astronomers rank star brightness using a reverse logarithmic scale where a difference of 5 magnitudes corresponds to a factor of exactly **100 in light intensity** (each magnitude step is a factor of $100^{1/5} \approx 2.512$).

#### 6. Viral Growth & Data Science (Log-Transform)

* **Epidemics & Social Trends (Logarithmic Scaling):**
  Viral phenomena—such as the spread of infectious diseases (e.g., COVID-19) or viral social media videos—begin with **exponential growth** (e.g., $y = 2^t$ or $y = e^{kt}$). On a standard linear axis, these curves shoot up almost vertically, making early trends impossible to analyze.
  
  By plotting data on a **logarithmic scale** ($\log(y)$ vs. $t$), exponential growth curves transform into **straight lines**:
  
  $$\ln(y) = \ln(e^{kt}) = kt$$
  
  The slope of this line represents the constant growth rate $k$. A bending of the line downward indicates that the growth rate is flattening out (turning point), making log plots essential for epidemiologists and growth analysts.

* **Handling Skewed Data in Machine Learning (Log Feature Scaling):**
  Real-world features like income levels, housing prices, or website traffic usually exhibit extreme **right-skewness** (heavy-tailed distributions) with values ranging over several orders of magnitude (e.g., \$10,000 to \$1,000,000,000).
  
  Applying a log transformation (such as $y = \log_{10}(x)$ or $y = \ln(1 + x)$) compresses these extreme scales:
  - $\$10,000 \implies \log_{10}(10,000) = 4$
  - $\$100,000 \implies \log_{10}(100,000) = 5$
  - $\$1,000,000,000 \implies \log_{10}(1,000,000,000) = 9$
  
  **Why this matters in ML:**
  1. It transforms highly skewed distributions into bell-shaped (Gaussian-like) distributions, satisfying key assumptions of algorithms like Linear Regression.
  2. It stabilizes feature variance and prevents extreme outliers from producing massive gradients, allowing gradient descent to converge faster and more reliably.

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

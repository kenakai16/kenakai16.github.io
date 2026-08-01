# Random Variables & Probability Distributions

While the sample space $\Omega$ contains raw outcomes (e.g., "Heads", "Tails"), we often want to work with numbers for easier mathematical computation. **Random Variables (RV)** serve as this bridge.

A random variable, often denoted as $X, Y, Z$, is a mathematical function that maps outcomes from the sample space to a real number: $X: \Omega \rightarrow \mathbb{R}$.

## 1. Discrete vs. Continuous Random Variables

### Discrete Random Variables
Discrete random variables take on countable values (e.g., the number of Heads in 3 coin flips, the number of customers entering a store).

* **Probability Mass Function (PMF):** Describes the probability that the random variable $X$ takes on a specific value $x$, denoted as $P(X = x)$ or $p(x)$.

  $$P(X = x) \ge 0 \quad \forall x$$

  The sum of probabilities for all possible values must equal 1:

  $$\sum_{x} P(X = x) = 1$$

### Continuous Random Variables
Continuous random variables take on values within a continuous range (e.g., a person's height, waiting time for a bus).

* **Probability Density Function (PDF):** Unlike a PMF, the probability that a continuous variable $X$ takes on a *specific, exact* value is always 0 (e.g., $P(X = 170.0000...) = 0$). Instead, the PDF $f(x)$ describes the probability density, allowing us to find the probability that $X$ falls within a range $[a, b]$ by integrating:

  $$P(a \le X \le b) = \int_{a}^{b} f(x) dx$$

  The total area under the PDF curve must equal 1:

  $$\int_{-\infty}^{\infty} f(x) dx = 1$$

### Cumulative Distribution Function (CDF)
The CDF, denoted as $F(x)$, is the probability that the random variable $X$ takes on a value less than or equal to $x$. It applies to both discrete and continuous variables:

$$F(x) = P(X \le x)$$

---

## 2. Expectation, Variance & Moments

### Expected Value ($\mu$ or $E[X]$)
The expected value is the average value we expect $X$ to take if we run the experiment many times. It acts as the "center of mass" of the distribution.

* **Discrete Expected Value:**
  
  $$E[X] = \sum_{x} x \cdot P(X=x)$$

* **Continuous Expected Value:**
  
  $$E[X] = \int_{-\infty}^{\infty} x \cdot f(x) dx$$

### Variance ($\sigma^2$ or $\operatorname{Var}(X)$)
Variance measures the spread or dispersion of the data around the expected value.

$$\operatorname{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2$$

Standard Deviation ($\sigma$) is the square root of the variance, which brings the unit back to the same scale as $X$.

### Moments
* 1st Moment: Expected Value (Mean).
* 2nd Central Moment: Variance.
* 3rd Moment (Skewness): Measures the asymmetry of the distribution.
* 4th Moment (Kurtosis): Measures the "peakedness" of the distribution and the heaviness of its tails.

## 3. Joint Distributions and Correlation

When working with multiple variables (e.g., having many features in Machine Learning), we use Joint Distributions.

* **Marginal Distribution:** The probability of one variable when we ignore (integrate/sum out) the other variables.
* **Covariance ($\operatorname{Cov}(X, Y)$):** Measures the tendency of two variables to change together.

  $$\operatorname{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)]$$

* **Pearson Correlation Coefficient ($\rho$):** Normalizes covariance to the range $[-1, 1]$:

  $$\rho = \frac{\operatorname{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

  *(Note: Correlation does not imply causation).*

## 4. Common Distributions in Data Science

Choosing the right distribution to model your data is a key step in Machine Learning and Statistical Modeling. Below are the most frequently encountered probability distributions.

**4.1 Discrete Distributions**

Discrete distributions model variables that take on distinct, countable values.

* **Bernoulli Distribution ($\text{Bernoulli}(p)$):** 
  Models a single trial with exactly two outcomes: Success (1) with probability $p$, and Failure (0) with probability $1-p$.
  - *Parameters:* $p \in [0, 1]$ (success probability).
  - *PMF:* $P(X = x) = p^x (1-p)^{1-x}$ for $x \in \{0, 1\}$.
  - *Mean / Variance:* $\mathbb{E}[X] = p$, $\text{Var}(X) = p(1-p)$.
  - *Example:* Flipping a coin, whether a user clicks an ad or not.

* **Binomial Distribution ($\text{Bin}(n, p)$):** 
  Models the number of successes in $n$ independent Bernoulli trials.
  - *Parameters:* $n \in \mathbb{N}$ (number of trials), $p \in [0, 1]$.
  - *PMF:* $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$.
  - *Mean / Variance:* $\mathbb{E}[X] = np$, $\text{Var}(X) = np(1-p)$.
  - *Example:* The number of clicks from 100 users visiting a website.

* **Poisson Distribution ($\text{Poisson}(\lambda)$):** 
  Models the number of times an event occurs within a fixed interval of time or space.
  - *Parameters:* $\lambda > 0$ (average rate of occurrence).
  - *PMF:* $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
  - *Mean / Variance:* $\mathbb{E}[X] = \lambda$, $\text{Var}(X) = \lambda$.
  - *Example:* Number of customer service calls received per hour.

---

**4.2 Continuous Distributions**

Continuous distributions model variables that take on any real value within a continuous range or interval.

* **Uniform Distribution ($\mathcal{U}(a, b)$):** 
  All values within the continuous interval $[a, b]$ are equally likely to occur.
  - *Parameters:* $a$ (lower bound), $b$ (upper bound).
  - *PDF:* $f(x) = \frac{1}{b-a}$ for $x \in [a, b]$.
  - *Mean / Variance:* $\mathbb{E}[X] = \frac{a+b}{2}$, $\text{Var}(X) = \frac{(b-a)^2}{12}$.
  - *Example:* Random seed generation in model initialization.

* **Normal / Gaussian Distribution ($\mathcal{N}(\mu, \sigma^2)$):** 
  The most important distribution in Data Science. It features a symmetric, bell-shaped curve centered around the mean.
  - *Parameters:* $\mu$ (mean), $\sigma^2$ (variance).
  - *PDF:* $f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^2}$.
  - *Mean / Variance:* $\mathbb{E}[X] = \mu$, $\text{Var}(X) = \sigma^2$.
  - *Example:* Distribution of measurement errors, model residuals, or human heights.

* **Exponential Distribution ($\text{Exp}(\beta)$):** 
  Models the time or distance between consecutive events in a Poisson process.
  - *Parameters:* $\beta > 0$ (rate parameter).
  - *PDF:* $f(x) = \beta e^{-\beta x}$ for $x \ge 0$.
  - *Mean / Variance:* $\mathbb{E}[X] = \frac{1}{\beta}$, $\text{Var}(X) = \frac{1}{\beta^2}$.
  - *Example:* The waiting time between phone calls at a call center.

* **Beta Distribution ($\text{Beta}(\alpha, \beta)$):** 
  A continuous distribution defined on the interval $[0, 1]$, widely used in Bayesian inference to model the probability distribution of an *unknown* probability parameter.
  - *Parameters:* $\alpha > 0$ (success shape parameter), $\beta > 0$ (failure shape parameter).
  - *PDF:* $f(x) = \frac{x^{\alpha-1} (1-x)^{\beta-1}}{\text{B}(\alpha, \beta)}$, where $\text{B}$ is the Beta function.
  - *Example:* Modeling the uncertainty of the click-through rate (CTR) of a new banner ad.

### Visualization with Python (Scipy & Matplotlib)

Here is how to use the `scipy.stats` library to work with the Normal distribution.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Create X-axis data
x = np.linspace(-5, 5, 1000)

# PDF of the Normal distribution with mu=0, sigma=1 (Standard Normal)
pdf = norm.pdf(x, loc=0, scale=1)

# CDF of the Normal distribution
cdf = norm.cdf(x, loc=0, scale=1)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(x, pdf, color='blue')
plt.title("Probability Density Function (PDF)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, cdf, color='red')
plt.title("Cumulative Distribution Function (CDF)")
plt.grid(True)
plt.show()

# Calculate probability P(X < 1.96)
prob = norm.cdf(1.96, loc=0, scale=1)
print(f"P(X < 1.96) = {prob:.4f}") # Output: 0.9750
```

# Convergence & Limit Theorems

In Data Science and Machine Learning, we rarely have access to an entire "population". Instead, we collect a finite "sample" of size $n$.

Limit Theorems are the fundamental theorems of probability theory that describe how sample statistics (such as the sample mean $\bar{X}_n$) behave as the sample size approaches infinity ($n \to \infty$).

---

## 1. What Are Limit Theorems?

A Limit Theorem describes the asymptotic behavior of a sequence of random variables $(X_n)_{n=1}^\infty$.

In probability theory, there are two primary pillars of Limit Theorems:
* **Law of Large Numbers (LLN):** Governs the **value convergence** — establishing that as $n \to \infty$, the sample mean $\bar{X}_n$ converges to the true population expectation $\mu$.
* **Central Limit Theorem (CLT):** Governs the **distribution shape convergence** — establishing that as $n \to \infty$, the normalized sum or sample mean converges in distribution to a standard Normal Distribution $\mathcal{N}(0, 1)$, regardless of the underlying distribution shape.

---

## 2. Modes of Convergence

To understand how a sequence of random variables $X_n$ behaves as $n \to \infty$, mathematicians define three primary modes of convergence:

### 2.1 Convergence in Probability ($X_n \xrightarrow{P} X$)

A sequence $X_n$ converges in probability to a random variable $X$ if, as the sequence progresses, the probability that the difference between them is larger than any arbitrarily small positive number $\epsilon$ vanishes to zero.

**Mathematical Definition:**

$$\lim_{n \to \infty} P(\vert{}X_n - X\vert{} > \epsilon) = 0 \quad \forall \epsilon > 0$$

> **Machine Learning Intuition:** This forms the basis of the **Weak Law of Large Numbers (WLLN)**. It guarantees that as you collect more data points, the sample statistic (like the sample mean) will cluster closer and closer to the true population value, with the probability of a large error dropping to zero.

---

### 2.2 Almost Sure Convergence ($X_n \xrightarrow{a.s.} X$)

A sequence $X_n$ converges almost surely (with probability 1) to $X$ if the sequence of actual values realized by $X_n$ converges to the realized value $X$ for almost all outcomes.

**Mathematical Definition:**

$$P\left(\lim_{n \to \infty} X_n = X\right) = 1$$

> **Machine Learning Intuition:** This is a stronger form of convergence that underpins the **Strong Law of Large Numbers (SLLN)**. While convergence in probability states that large deviations become rare at any single step $n$, almost sure convergence guarantees that the entire path of sample statistics will eventually enter and never leave an arbitrarily small interval around the true mean.

---

### 2.3 Convergence in Distribution ($X_n \xrightarrow{d} X$)

A sequence $X_n$ converges in distribution to $X$ if their Cumulative Distribution Functions (CDFs) converge to the CDF of $X$ at all points where the limiting CDF is continuous.

**Mathematical Definition:**

$$\lim_{n \to \infty} F_{X_n}(x) = F_X(x) \quad \forall x \text{ where } F_X \text{ is continuous}$$

> **Machine Learning Intuition:** This is the weakest form of convergence and serves as the mathematical foundation for the **Central Limit Theorem (CLT)**. It doesn’t mean the individual sample values become equal, but rather that the overall shape of the histogram of these values settles into a specific probability distribution (like the Gaussian bell curve).

---

### 2.4 Hierarchy of Convergence

The relationship and strength between these three modes of convergence can be ordered hierarchically:

$$X_n \xrightarrow{a.s.} X \implies X_n \xrightarrow{P} X \implies X_n \xrightarrow{d} X$$

*(Almost Sure Convergence is the strongest mode, implying Convergence in Probability, which in turn implies Convergence in Distribution. The reverse implications do not hold in general without additional conditions).*

---

## 3. Law of Large Numbers (LLN)

The Law of Large Numbers (LLN) is a fundamental theorem in probability. It states that as the number of independent trials increases, the empirical average (observed average) of the results converges to the theoretical expected value.

For example, when rolling a fair 6-sided die, the theoretical expected value (mean) of a roll is:

$$\mathbb{E}[X] = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = 3.5$$

If you roll the die 10 times, your average roll might be $2.1$ or $4.8$ (high variance). However, if you roll it 10,000 times, the average will be extremely close to $3.5$ as $n \to \infty$.

```{figure} ../../images/lln_simulation.gif
---
name: lln_simulation
align: center
---
Simulation demonstrating the Law of Large Numbers.
```

### Why LLN Matters in Data Science
* **Guarantees Sample Reliability:** Collecting more data increases estimation precision.
* **Foundation of Machine Learning:** Ensures that training model parameters on finite sample datasets generalizes to true population distributions.

### Python Simulation: Roll Average Comparison

```python
import numpy as np

# Theoretical expected value for a fair die roll
expected_value = 3.5

for rolls in [10, 100, 1000, 10000, 100000]:
    # Simulate die rolls (1 to 6)
    simulated_rolls = np.random.randint(1, 7, size=rolls)
    empirical_average = np.mean(simulated_rolls)
    difference = abs(empirical_average - expected_value)
    print(f"Rolls: {rolls:<6} | Average: {empirical_average:.4f} | Difference: {difference:.4f}")
```

### Python Simulation: Cumulative Convergence Curve

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 1000
rolls = np.random.randint(1, 7, size=N)
sample_means = np.cumsum(rolls) / np.arange(1, N + 1)

plt.figure(figsize=(9, 4.5))
plt.plot(sample_means, label=r'Sample Mean $\bar{X}_n$')
plt.axhline(y=3.5, color='r', linestyle='--', label=r'True Mean $\mu = 3.5$')
plt.xlabel('Number of rolls (n)')
plt.ylabel('Sample Mean')
plt.title('Law of Large Numbers Convergence')
plt.legend()
plt.grid(True)
plt.show()
```

---

## 4. Central Limit Theorem (CLT)

While LLN explains *what value* the sample mean converges to, the Central Limit Theorem (CLT) explains the *shape of the distribution* of sample means.

### Theorem Statement

Given independent and identically distributed (i.i.d) random variables $X_1, X_2, \dots, X_n$ with finite mean $\mu$ and variance $\sigma^2$, as $n \to \infty$ (typically $n \ge 30$):

$$\bar{X}_n \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$$

Or in standardized form:

$$Z = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

### Why CLT is the "Mathematical Miracle" of Statistics

* **Distribution Agnostic:** The original population can be uniform, exponential, or skewed. The distribution of sample means $\bar{X}_n$ will always form a Gaussian bell curve.
* **Enables Hypothesis Testing:** Provides the foundation for confidence intervals, z-tests, t-tests, and A/B testing in Data Science.

### Python Simulation: CLT

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

n_samples = 50
n_trials = 10000

# Generate Uniform random matrix (10,000 trials x 50 samples)
data = np.random.uniform(0, 1, size=(n_trials, n_samples))
sample_means = np.mean(data, axis=1)

plt.figure(figsize=(8, 4.5))
sns.histplot(sample_means, kde=True, color='blue', bins=50)
plt.title(f'CLT: Distribution of Sample Means (n={n_samples})')
plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.grid(True)
plt.show()
```

# Probability

Probability is the study of uncertainty. In data science and machine learning, we use probability to build models under uncertainty, estimate parameters, evaluate classifiers (using metrics like precision and recall), and build complex systems like Naive Bayes classifiers or Bayesian networks.

---

## 1. What is Probability?

Probability quantifies how likely an event is to occur. It is always a value between $0$ (impossible) and $1$ (certain).

### Probability vs. Odds

- **Probability**: The ratio of the target event's occurrence to all possible outcomes.
  $$\text{Probability} = \frac{\text{Successes}}{\text{Total Outcomes}}$$
- **Odds**: The ratio of the probability of the event occurring to the probability of the event *not* occurring.
  $$\text{Odds} = \frac{P(\text{Event})}{1 - P(\text{Event})}$$

For example, if you roll a 6-sided die, the probability of rolling a $4$ is $1/6 \approx 0.1667$. The odds of rolling a $4$ are $\frac{1/6}{5/6} = 1:5$ (one to five).

---

### Joint Probabilities (AND)

The probability of two events $A$ and $B$ both happening is denoted as $P(A \cap B)$.

- **For Independent Events**: The occurrence of one event does not affect the other.
  $$P(A \cap B) = P(A) \cdot P(B)$$
  *Example*: Flipping a coin and rolling a die.

- **For Dependent Events**: The occurrence of one event affects the probability of the other.
  $$P(A \cap B) = P(A) \cdot P(B|A)$$
  *Example*: Drawing two aces consecutively from a deck of cards without replacement.

### Union Probabilities (OR)

The probability of event $A$ or event $B$ occurring is:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

If the events are **mutually exclusive** (cannot happen at the same time, meaning $P(A \cap B) = 0$), then:

$$P(A \cup B) = P(A) + P(B)$$

---

## 3. Conditional Probability & Bayes' Theorem

**Conditional probability** is the probability of event $A$ occurring *given* that event $B$ has already occurred. It is written as $P(A|B)$:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

### Bayes' Theorem

By rearranging the conditional probability formula, we get **Bayes' Theorem**, which updates our belief in a hypothesis ($A$) after observing new evidence ($B$):

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

Where:
- $P(A|B)$ is the **posterior** probability.
- $P(B|A)$ is the **likelihood**.
- $P(A)$ is the **prior** probability.
- $P(B)$ is the **marginal** probability (evidence).

### Python Implementation of Bayes' Theorem

Suppose a diagnostic medical test has a $99\%$ sensitivity (true positive rate) and a $99\%$ specificity (true negative rate). The disease is rare, affecting only $0.1\%$ of the population. What is the probability that a person who tests positive actually has the disease?

```python
# Priors
p_disease = 0.001           # P(Disease)
p_no_disease = 1 - p_disease  # P(No Disease)

# Likelihoods
p_pos_given_disease = 0.99   # P(Positive | Disease) - Sensitivity
p_pos_given_no_disease = 0.01 # P(Positive | No Disease) - 1 - Specificity

# Marginal Probability of testing positive P(B)
p_positive = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * p_no_disease)

# Bayes' Theorem: P(Disease | Positive)
p_disease_given_positive = (p_pos_given_disease * p_disease) / p_positive

print(f"P(Disease | Positive) = {p_disease_given_positive:.4f} ({p_disease_given_positive * 100:.2f}%)")
```

**Output:**
```
P(Disease | Positive) = 0.0902 (9.02%)
```
Despite the test being $99\%$ accurate, a positive test only translates to a $9\%$ chance of having the disease because the disease is extremely rare!

---

## 4. Probability Distributions

### Binomial Distribution

The binomial distribution models the number of successes in $n$ independent trials, where each trial has a binary outcome (success/failure) and a constant probability of success $p$.

The probability mass function (PMF) is:

$$P(k) = \binom{n}{k} p^k (1-p)^{n-k}$$

#### Implement with SciPy:

Suppose we flip a fair coin ($p=0.5$) 10 times. What is the probability of getting exactly 5 heads?

```python
from scipy.stats import binom

n = 10  # trials
p = 0.5  # probability of success
k = 5   # target successes

# Exact probability of 5 successes
prob_5 = binom.pmf(k, n, p)
print(f"P(5 heads in 10 flips) = {prob_5:.6f}")

# Probability of getting 5 or fewer heads (Cumulative Distribution Function)
prob_5_or_less = binom.cdf(k, n, p)
print(f"P(<= 5 heads in 10 flips) = {prob_5_or_less:.6f}")
```

**Output:**
```
P(5 heads in 10 flips) = 0.246094
P(<= 5 heads in 10 flips) = 0.623047
```

### Beta Distribution

The Beta distribution is a continuous probability distribution defined on the interval $[0, 1]$. In Bayesian inference, it is frequently used to model the probability distribution of an *unknown* probability parameter (like the click-through rate of an ad).

It is parameterized by two shape parameters: $\alpha$ (successes + 1) and $\beta$ (failures + 1).

#### Implement with SciPy:

Suppose you launched an ad campaign. You saw 8 clicks (successes) and 2 non-clicks (failures). Let's model the probability of success using a Beta distribution:

```python
from scipy.stats import beta
import numpy as np
import matplotlib.pyplot as plt

# shape parameters (adding 1 as a prior)
a = 8 + 1  # alpha
b = 2 + 1  # beta

# Probability density function at x = 0.8
pdf_val = beta.pdf(0.8, a, b)
print(f"PDF at x=0.8: {pdf_val:.4f}")

# What is the probability that the actual success rate is greater than 90%?
# P(X > 0.9) = 1 - CDF(0.9)
prob_greater_90 = 1 - beta.cdf(0.9, a, b)
print(f"P(Success rate > 90%): {prob_greater_90:.4f}")
```

**Output:**
```
PDF at x=0.8: 3.0223
P(Success rate > 90%): 0.2252
```

---

## 5. Law of Large Numbers (Luật số lớn)

The **Law of Large Numbers (LLN)** is a fundamental theorem in probability. It states that as the number of independent trials increases, the empirical average (observed average) of the results converges to the theoretical expected value.

For example, when rolling a fair 6-sided die, the theoretical average of a roll is:
$$\text{Expected Value} = \frac{1+2+3+4+5+6}{6} = 3.5$$

If you roll the die 10 times, your average roll might be $2.8$ or $4.2$. However, if you roll it 10,000 times, the average will be extremely close to $3.5$.

### Python Simulation
Here is a simulation of the Law of Large Numbers using Python:

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

---

## Exercises

```{admonition} Exercise 1
:class: tip
A coin is flipped 15 times. The coin is biased, with a probability of heads $p = 0.7$.
Calculate:
1. The probability of getting exactly 10 heads.
2. The probability of getting 12 or more heads.
```

```{admonition} Exercise 2
:class: tip
A test for a rare drug has a $95\%$ true positive rate and a $98\%$ true negative rate. Only $0.5\%$ of tested people actually use the drug. If a randomly tested person tests positive, what is the probability that they are actually a drug user?
```

```{admonition} Exercise 3
:class: tip
You ran a small A/B test. 
- Variant A had 2 clicks and 8 ignores.
- Variant B had 6 clicks and 4 ignores.
Use `scipy.stats.beta` to find the probability that Variant B's true CTR is greater than $50\%$.
```

```{admonition} Solution — Exercise 1
:class: dropdown

\`\`\`python
from scipy.stats import binom

n = 15
p = 0.7

# 1. Exactly 10 heads
p_10 = binom.pmf(10, n, p)
print(f"Exactly 10: {p_10:.6f}")

# 2. 12 or more heads = 1 - P(<= 11)
p_12_plus = 1 - binom.cdf(11, n, p)
print(f"12 or more: {p_12_plus:.6f}")
\`\`\`
```
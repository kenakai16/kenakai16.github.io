# Probability

Probability is the mathematical language of uncertainty. In data science and machine learning, we use probability to build models under uncertainty, estimate parameters, evaluate classifiers, and construct complex systems like Bayesian networks.

This module is divided into four main chapters:

1. **{doc}`Foundations of Probability <foundations>`:** Covers the core axioms, conditional probability, and Bayes' Theorem (the backbone of Bayesian Inference).
2. **{doc}`Random Variables & Probability Distributions <random_variables>`:** Introduces discrete and continuous random variables, expectations, variance, and common distributions (Normal, Binomial, Poisson).
3. **{doc}`Convergence & Limit Theorems <limit_theorems>`:** Explores what happens when we collect a lot of data, featuring the Law of Large Numbers (LLN) and the Central Limit Theorem (CLT).
4. **{doc}`Information Theory Basics <information_theory>`:** Connects probability to information theory, explaining Entropy, Cross-Entropy, and KL Divergence—concepts foundational to Deep Learning loss functions.

---

## A Quick Primer: Probability vs. Odds

Before diving into the chapters, it is crucial to distinguish between **Probability** and **Odds**, two concepts often confused in casual language but mathematically distinct.

* **Probability ($P$)**: The ratio of the target event's occurrence to all possible outcomes. It is always bounded between $0$ and $1$.
  
  $$P = \frac{\text{Successes}}{\text{Total Outcomes}}$$

* **Odds ($O$)**: The ratio of the probability of the event occurring ($P$) to the probability of the event *not* occurring ($1 - P$). Its value can range from $0$ to $\infty$.
  
  $$O = \frac{P}{1 - P}$$

| Feature | Probability ($P$) | Odds ($O$) |
| :--- | :--- | :--- |
| **Definition** | Likelihood of event over total outcomes | Likelihood of event over non-event |
| **Range** | $[0, 1]$ or $[0\%, 100\%]$ | $[0, \infty)$ |
| **Example (Rolling a 4 on a 6-sided die)** | $\frac{1}{6} \approx 0.1667 \ (16.67\%)$ | $\frac{1/6}{5/6} = \frac{1}{5} \ (1:5 \text{ or } 0.2)$ |

```{note}
In machine learning, **Odds** are highly important in **Logistic Regression**. The model outputs log-odds (logit): $\ln(\frac{P}{1-P}) = wx + b$.
```

Now, let's move on to the first chapter: **{doc}`Foundations of Probability <foundations>`**!
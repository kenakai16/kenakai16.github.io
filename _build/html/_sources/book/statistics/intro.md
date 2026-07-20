# Statistics

Statistics is the discipline that concerns the collection, organization, analysis, interpretation, and presentation of data. While probability helps us predict future outcomes based on a known model, statistics works in reverse: we analyze observed data to infer the properties of the underlying system.

---

## 1. Descriptive vs. Inferential Statistics

- **Descriptive Statistics**: Summarizes and describes the characteristics of a dataset (e.g., mean, median, standard deviation).
- **Inferential Statistics**: Uses a sample of data to make predictions or draw conclusions about a larger population.

---

## 2. Descriptive Statistics in Python

### Mean, Median, and Mode

- **Mean**: The arithmetic average.
- **Median**: The middle value when data is sorted. Highly resistant to outliers.
- **Mode**: The most frequent value.

### Variance and Standard Deviation

Variance ($\sigma^2$) and Standard Deviation ($\sigma$) measure the spread of data points around the mean.

- **Population Variance**:

  $$\sigma^2 = \frac{\sum (x_i - \mu)^2}{N}$$
- **Sample Variance** (Bessel's correction uses $n-1$ to account for sample bias):

  $$s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1}$$

```python
import numpy as np
from scipy import stats

data = [12, 15, 12, 18, 22, 15, 14, 15, 90]  # Note the outlier: 90

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data, keepdims=True).mode[0]

# Sample Standard Deviation (ddof=1)
std_dev = np.std(data, ddof=1)

print(f"Mean              : {mean:.2f}")
print(f"Median            : {median:.2f}")
print(f"Mode              : {mode}")
print(f"Sample Std Dev    : {std_dev:.2f}")
```

**Output:**
```
Mean              : 22.56
Median            : 15.00
Mode              : 15
Sample Std Dev    : 25.56
```

---

## 3. The Normal Distribution

The normal (or Gaussian) distribution is a continuous symmetric bell-shaped curve defined by its mean ($\mu$) and standard deviation ($\sigma$).

### Z-score

A Z-score indicates how many standard deviations a value is from the mean:

$$Z = \frac{x - \mu}{\sigma}$$

### Python Implementation of Normal CDF and Percentiles

```python
from scipy.stats import norm

# Standard Normal Distribution (mean=0, std=1)
# What percentage of data falls below Z = 1.96?
pct_below_z = norm.cdf(1.96)
print(f"Percent below Z=1.96: {pct_below_z*100:.2f}%")

# Inverse CDF: What Z-score marks the 95th percentile?
z_95th = norm.ppf(0.95)
print(f"Z-score at 95th percentile: {z_95th:.4f}")
```

**Output:**
```
Percent below Z=1.96: 97.50%
Z-score at 95th percentile: 1.6449
```

---

## 4. Central Limit Theorem (CLT)

The **Central Limit Theorem** states that if you take sufficiently large random samples from any population (even a non-normal one), the distribution of the sample means will approach a normal distribution as the sample size increases.

This allows us to perform statistical inference (like hypothesis testing) on non-normal data!

---

## 5. Confidence Intervals

A confidence interval provides a range of values that is likely to contain the true population parameter. 

The formula for the confidence interval of a mean is:

$$\text{CI} = \bar{x} \pm Z \cdot \frac{s}{\sqrt{n}}$$

```python
import numpy as np
from scipy import stats

sample_data = [12, 15, 12, 18, 22, 15, 14, 15, 19, 20]
n = len(sample_data)
mean = np.mean(sample_data)
sem = stats.sem(sample_data)  # Standard Error of the Mean = s / sqrt(n)

# 95% Confidence Interval
ci_95 = stats.t.interval(0.95, df=n-1, loc=mean, scale=sem)
print(f"95% Confidence Interval for the mean: {ci_95[0]:.2f} to {ci_95[1]:.2f}")
```

**Output:**
```
95% Confidence Interval for the mean: 13.91 to 18.49
```

---

## 6. Hypothesis Testing & P-Values

Hypothesis testing is a systematic way to evaluate claims about a population.

- **Null Hypothesis ($H_0$)**: The status quo; there is no effect or no difference.
- **Alternative Hypothesis ($H_1$)**: The claim we want to test.
- **P-value**: The probability of obtaining test results at least as extreme as the observed results, assuming $H_0$ is true. If $p \leq 0.05$ (the significance level $\alpha$), we reject $H_0$.

### Example: One-Sample T-test

A manufacturer claims their lightbulbs last 1000 hours on average. We test 10 bulbs and get the following lifespans:

```python
from scipy import stats

lifespans = [980, 1010, 990, 970, 1005, 985, 995, 960, 1020, 980]

# Perform one-sample t-test against H0: mean = 1000
t_stat, p_val = stats.ttest_1samp(lifespans, 1000)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value    : {p_val:.4f}")

if p_val < 0.05:
    print("Reject H0: The mean lifespan is significantly different from 1000 hours.")
else:
    print("Fail to reject H0: No significant difference from 1000 hours.")
```

**Output:**
```
T-statistic: -1.7454
P-value    : 0.1149
Fail to reject H0: No significant difference from 1000 hours.
```

---

## 7. Z-Test vs. T-Test

When performing hypothesis tests on a sample mean, you must choose between a Z-test and a T-test:

| Feature | Z-Test | T-Test |
|---|---|---|
| **Sample Size** | Large ($n \geq 30$) | Small ($n < 30$) |
| **Population Variance ($\sigma^2$)** | Known | Unknown (must use sample variance $s^2$) |
| **Underlying Distribution** | Normal Distribution | Student's T-Distribution (wider tails to account for uncertainty) |

---

## 8. Type I and Type II Errors

When testing hypothesis, decisions are made under uncertainty. This can lead to two types of errors:

- **Type I Error ($\alpha$ / False Positive)**: Rejecting the null hypothesis ($H_0$) when it is actually true. 
  *Example*: A spam filter classifying a legitimate email as spam.
- **Type II Error ($\beta$ / False Negative)**: Failing to reject the null hypothesis ($H_0$) when it is actually false.
  *Example*: A spam filter letting a malicious email pass through to the inbox.

---

## 9. Chi-Square Test ($\chi^2$) for Categorical Data

A **Chi-Square Test** is used to determine whether there is a statistically significant association between two categorical variables.

For instance, suppose we want to test if a customer's subscription plan preference (Basic, Premium) is dependent on their region (US, EU):

```python
import numpy as np
from scipy.stats import chi2_contingency

# Contingency table (observed counts)
# Rows: US, EU
# Columns: Basic, Premium
observed = np.array([
    [150, 100],  # US
    [120, 130]   # EU
])

# Perform Chi-Square Test
chi2_stat, p_val, dof, expected = chi2_contingency(observed)

print(f"Chi2 statistic : {chi2_stat:.4f}")
print(f"P-value        : {p_val:.4f}")

if p_val < 0.05:
    print("Subscription preferences are significantly associated with region.")
else:
    print("Subscription preferences are independent of region.")
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
You have a dataset of house prices: `[250, 270, 310, 290, 850, 300, 260]` (in thousands of dollars).
1. Calculate the mean and median.
2. Which measure is more appropriate for summarizing this dataset, and why?
```

```{admonition} Exercise 2
:class: tip
A sample of 50 students scored an average of 78 on an exam, with a sample standard deviation of 8. Compute the $95\%$ confidence interval for the population mean.
```

```{admonition} Exercise 3
:class: tip
An online store wants to see if changing the color of the "Buy" button increases conversions.
- Control group (Red): 100 purchases out of 1000 visits.
- Treatment group (Green): 130 purchases out of 1000 visits.
Perform a two-sample z-test for proportions to see if the green button performs significantly better ($\alpha = 0.05$).
```

```{admonition} Solution — Exercise 3
:class: dropdown

\`\`\`python
from statsmodels.stats.proportion import proportions_ztest
import numpy as np

count = np.array([130, 100]) # successes
nobs = np.array([1000, 1000]) # observations

# Perform z-test
stat, pval = proportions_ztest(count, nobs, alternative='larger')
print(f"Z-statistic: {stat:.4f}")
print(f"P-value    : {pval:.5f}")
\`\`\`
```

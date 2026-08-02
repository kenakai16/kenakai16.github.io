# Statistical Inference

While Probability goes from a general mathematical model to predict data (Model $\rightarrow$ Data), **Statistical Inference** does the reverse: it goes from collected data (Sample) to predict and draw conclusions about the general model of the real world (Data $\rightarrow$ Model).

This is the foundation of the training process in Machine Learning: relying on a finite training dataset to find the best parameters for a model.

## 1. Point Estimation

The goal of point estimation is to find a single value (called $\hat{\theta}$) that best approximates the true population parameter $\theta$ based on sample data.

### Maximum Likelihood Estimation (MLE)
MLE is the most common method in Machine Learning. The core idea: **"Choose the parameter $\theta$ such that the probability of observing the current dataset is maximized."**

The Likelihood function $L(\theta)$ is the probability of the data $X$ given the parameter $\theta$. If the data points $x_i$ are independent and identically distributed (i.i.d):

$$ L(\theta) = P(X|\theta) = \prod_{i=1}^{n} P(x_i | \theta) $$


For ease of computation (to avoid underflow and turn products into sums), we typically use **Log-Likelihood**:

$$ \log L(\theta) = \sum_{i=1}^{n} \log P(x_i | \theta) $$


The goal of MLE is to find $\theta$ to maximize this Log-Likelihood function. *(Note: In Deep Learning, minimizing the Cross-Entropy Loss is exactly performing MLE!).*

### Maximum A Posteriori (MAP)
MAP is an extension of MLE based on Bayes' theorem, allowing us to incorporate our **initial belief (Prior - $P(\theta)$)** into the estimation process.

$$ \hat{\theta}_{MAP} = \arg\max_{\theta} P(X|\theta) P(\theta) $$

*(Note: Adding Regularization (L1/L2) in Machine Learning is exactly performing MAP estimation where the Prior is a Laplace/Gaussian distribution, respectively).*

## 2. Confidence Intervals (CI)

A point estimate (like MLE) only gives us a single number, but it doesn't tell us the certainty of that number. A **Confidence Interval** provides a range of values within which we believe the true parameter $\theta$ lies with a certain level of confidence (e.g., 95%).

Suppose we calculate the sample mean $\bar{X}$ and the sample standard deviation $S$. Based on the Central Limit Theorem (CLT), the 95% confidence interval for the population mean $\mu$ is:

$$ CI = \bar{X} \pm 1.96 \frac{S}{\sqrt{n}} $$

(The number 1.96 is the z-score corresponding to 95% of the area under the Normal distribution curve).

## 3. Hypothesis Testing and p-value

Hypothesis testing is the backbone of scientific research and **A/B Testing** in the industry (e.g., Does Interface A or B bring more clicks?).

The basic steps:
1. **Establish $H_0$ (Null Hypothesis):** The default assumption (usually "No difference", "No effect").
2. **Establish $H_A$ (Alternative Hypothesis):** What we want to prove ("There is a difference", "The drug has an effect").
3. **Calculate the Test Statistic:** A statistical metric derived from the sample data (e.g., t-score, z-score).
4. **Calculate the p-value:** The probability of obtaining a result equal to (or more extreme than) the current sample data, *assuming that $H_0$ is true*.
5. **Conclusion:** If the p-value is smaller than a threshold $\alpha$ (usually 0.05), we reject $H_0$ and accept $H_A$ (The result is Statistically significant).

*Careful:* The p-value is **not** the probability that $H_0$ is true. It is only the probability of observing this data if $H_0$ were true.

### Common types of tests:
* **T-test:** Used to compare the means of 1 or 2 groups (when the population variance is unknown or the sample size is small). Frequently used in A/B testing.
* **ANOVA:** Used to compare the means of 3 or more groups.
* **Chi-square Test:** Used for categorical data to check for independence between categorical variables.

### Python Example (T-test for A/B Testing)
Suppose we run an A/B Test for two buttons on a website, recording the time users stay on the page (in seconds).

```python
import numpy as np
from scipy import stats

np.random.seed(42)
# Interface A (Control)
time_A = np.random.normal(loc=120, scale=30, size=100)
# Interface B (Treatment) - Seems users stay slightly longer
time_B = np.random.normal(loc=130, scale=30, size=100)

# Perform an Independent 2-sample t-test
t_stat, p_value = stats.ttest_ind(time_B, time_A, alternative='greater')

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject H0: Interface B genuinely retains users longer than interface A (Statistically significant).")
else:
    print("Not enough evidence to reject H0: The difference might just be due to random chance.")
    
# Output:
# T-statistic: 2.2223
# P-value: 0.0137
# Reject H0: Interface B genuinely retains users longer than interface A (Statistically significant).
```

---

## 4. Case Study: Analyzing Vietnam's 2024 High School Graduation Exam Scores

Let's look at a practical application of distribution analysis and hypothesis testing using the foreign language (English) scores from Vietnam's 2024 High School Graduation (THPT) Exam.

### Bimodal Score Distribution
Looking at the overall distribution of English exam scores, we observe a distinct bimodal (two-peak) distribution. This is a common pattern in heterogeneous datasets where two different populations are mixed together.

```{figure} ../../images/thpt_2024_bimodal_distribution.png
---
name: bimodal-distribution
width: 70%
align: center
---
Bimodal distribution of the 2024 THPT English exam scores.
```

A common hypothesis is that these two peaks represent two distinct student demographics: rural and urban areas. Let's test this hypothesis.

### Hypothesis 1: Classification by Region (Urban vs. Rural)
To test this, we divide the data into two groups: major metropolitan cities (urban centers) and the remaining provinces (primarily rural regions). 

```{figure} ../../images/thpt_2024_regional_comparison.png
---
name: regional-comparison
width: 70%
align: center
---
Comparison of score distributions: Major Cities vs. Other Provinces.
```

Comparing the histograms and Kernel Density Estimation (KDE) curves reveals that scores in major cities are significantly shifted to the right compared to other provinces.

To verify if this difference is statistically significant, we perform an independent two-sample t-test:
*   **T-statistic**: $122.39$
*   **P-value**: $0.0$

Since the p-value is effectively $0.0$ (far below the significance threshold $\alpha = 0.05$), we reject the null hypothesis $H_0$ (which assumes no difference in mean scores). This confirms that geographical region has a highly significant effect on foreign language exam scores.

### Hypothesis 2: Impact of Wealth (Provincial GRDP)
We also analyze whether provincial wealth, measured by Gross Regional Domestic Product (GRDP), influences exam scores. We split the provinces into two groups: high GRDP and low GRDP.

```{figure} ../../images/thpt_2024_grdp_comparison.png
---
name: grdp-comparison
width: 70%
align: center
---
Comparison of score distributions: High GRDP vs. Low GRDP Provinces.
```

The KDE curves show a clear distinction between the two groups. To test the significance, we perform another independent t-test:
*   **T-statistic**: $128.67$
*   **P-value**: $0.0$

The t-statistic of $128.67$ and a p-value of $0.0$ lead us to reject $H_0$. This demonstrates that economic development and provincial wealth (GRDP) are strongly associated with higher student performance on the foreign language exam.


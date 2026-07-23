# Math for Data Science

<div class="book-cover-container">
  <div class="book-cover-title">Math for Data Science</div>
  <div class="book-cover-subtitle">A Comprehensive Reference & Learning Guide to Advanced Mathematics, Machine Learning, and Deep Learning</div>
  <div class="book-cover-author">Huỳnh Trung Nghĩa (NghiaHoang)</div>
</div>

<style>
  /* Hide default H1 heading to show the styled cover banner instead */
  #math-for-data-science > h1 {
    display: none !important;
  }

  .book-cover-container {
    background: linear-gradient(135deg, #0b0f19 0%, #111827 50%, #1e1b4b 100%);
    color: #ffffff;
    padding: 70px 40px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.35);
    border: 1px solid rgba(255, 255, 255, 0.05);
    position: relative;
    overflow: hidden;
  }
  .book-cover-container::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 0%, transparent 60%);
    pointer-events: none;
  }
  .book-cover-title {
    font-size: 3.5rem;
    font-weight: 900;
    letter-spacing: -0.05em;
    background: linear-gradient(to right, #38bdf8, #818cf8, #fb923c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 15px;
    text-transform: uppercase;
  }
  .book-cover-subtitle {
    font-size: 1.2rem;
    color: #94a3b8;
    max-width: 700px;
    margin: 0 auto 30px auto;
    font-weight: 300;
    line-height: 1.6;
  }
  .book-cover-author {
    font-size: 1.1rem;
    color: #38bdf8;
    font-weight: 600;
    letter-spacing: 0.05em;
  }

  @media print {
    /* Hide navigation sidebars, headers, footers, and buttons */
    .bd-sidebar,
    .bd-sidebar-primary,
    .bd-sidebar-secondary,
    .bd-toc,
    .bd-header,
    .bd-footer,
    .topbar,
    .prev-next-area,
    .bd-header-article,
    #site-navigation,
    footer {
      display: none !important;
    }

    /* Expand main content container to full page width */
    main,
    .bd-content,
    .bd-main,
    #main-content,
    .bd-article-container {
      width: 100% !important;
      max-width: 100% !important;
      padding: 0 !important;
      margin: 0 !important;
      box-shadow: none !important;
      border: none !important;
    }

    .book-cover-container {
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border-radius: 0;
      margin: 0;
      border: none;
      box-shadow: none;
      page-break-after: always;
    }
    .book-cover-title {
      font-size: 4.5rem;
    }
    .book-cover-subtitle {
      font-size: 1.5rem;
    }
  }
</style>

Welcome to the **Math for Data Science** blog. This resource is a curated reference and learning guide on the core mathematical foundations of Data Science, Machine Learning, and Deep Learning, authored by **Huỳnh Trung Nghĩa**.

---

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} 🎯 Core Pillars
:class-header: bg-light font-weight-bold
- **Calculus & Linear Algebra**: Functions, matrices, eigenvalues, gradients, and integration.
- **Probability & Statistics**: Distributions, conditional probability, Bayes' theorem, and descriptive/inferential statistics.
- **Optimization**: Convexity, duality, optimization algorithms (like gradient descent), and combinatorial optimization.
:::

:::{grid-item-card} 🚀 Practical Focus
:class-header: bg-light font-weight-bold
Rather than dry mathematical proofs, we focus on **conceptual intuition** coupled with **step-by-step Python implementations** using libraries like `numpy`, `scipy`, `matplotlib`, and `scikit-learn`.
:::
::::

---

## 📚 Reference Textbooks

Our content and structure draw inspiration from these highly recommended books:

::::{grid} 1 2 2 2
:gutter: 2

:::{grid-item-card} 📘 Applied Math
**Essential Math for Data Science**
*Thomas Nield* (O'Reilly, 2022)
:::

:::{grid-item-card} 📗 Mathematical Exercises
**1001 Math Problems**
*LearningExpress* (2nd Edition)
:::
::::

---

## 🗺️ Blog Map & Chapters

The content is organized into 9 key modules, guiding you from basic arithmetic to advanced machine learning foundations:

### 📖 Part 1: Basic Math & Calculus
- **Fundamentals**: Number systems, fractions, decimals, order of operations, and algebraic variables.
- **Functions & Graphs**: Linear and curvilinear functions, summations, exponents, and logarithms (featuring Euler's number and the Rule of 72).
- **Advanced Core**: Introductions to Linear Algebra, Calculus (derivatives, gradients), and Integration.

### 🎲 Part 2: Probability & Statistics
- **Probability**: Core rules, joint and union probability, conditional probability, Bayes' Theorem, and probability distributions (Binomial, Beta).
- **Statistics**: Mean, median, mode, variance, standard deviation, and key statistical concepts.

### ⚡ Part 3: Optimization
- **Convexity**: Convex sets, convex functions, and convex optimization problems.
- **Theory & Algorithms**: Duality (Lagrangian, KKT conditions), gradient descent algorithms, and combinatorial optimization.

### 🌀 Part 4: Functional Analysis & Measure Theory
- **Functional Analysis**: Banach spaces, bounded linear operators, quotient spaces, Baire Category Theorem, and Hahn-Banach Theorem.
- **Measure Theory**: Outer measure, $\sigma$-algebras, Lebesgue measure, measurable functions, and simple functions.

### 🌐 Part 5: Topology
- **General Topology**: Metric spaces, open sets, neighborhoods, compactness, and connectedness.
- **Manifolds**: The Manifold Hypothesis, homeomorphisms (and their role in neural networks), and topological dimensionality reduction (t-SNE, UMAP).
- **Topological Data Analysis (TDA)**: Simplicial complexes, Betti numbers, and Persistent Homology (barcodes and diagrams).

### 📈 Part 6: Approximation Theory
- **Fitting**: Curve fitting, regression analysis, interpolation, and approximating continuous functions.

### 🤖 Part 7: Machine Learning
- **Math Foundations**: Practical methodology, supervised learning math, unsupervised learning math, and distributed learning structures.

### 🧠 Part 8: Deep Learning
- **Neural Networks**: Artificial neurons, activation functions, loss functions, backpropagation, and gradient descent optimization in deep networks.

### 📚 Part 9: Recommended Reading
- **Reading**: Our curated list of recommended textbook resources for mathematics and AI.

---

## 📖 Table of Contents

```{tableofcontents}
```
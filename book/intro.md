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

## 🗺️ Blog Map & Chapters

The content is organized into 10 key modules, guiding you from basic arithmetic to advanced machine learning foundations:

### 📖 Part 1: Basic Math & Calculus
- **Fundamentals**: Number systems, fractions, decimals, order of operations, and algebraic variables.
- **Functions & Graphs**: Linear and curvilinear functions, summations, exponents, and logarithms (featuring Euler's number and the Rule of 72).
- **Calculus Core**: Introductions to Calculus (derivatives, gradients) and Integration (Riemann sums, symbolic/numerical integration).

### 🧮 Part 2: Linear Algebra
- **Linear Algebra**: Vectors, matrices, matrix transpose, matrix multiplication, systems of linear equations, eigenvalues/eigenvectors, and diagonalization.

### 🎲 Part 3: Probability & Statistics
- **Probability**: Core rules, joint and union probability, conditional probability, Bayes' Theorem, and probability distributions (Binomial, Beta).
- **Statistics**: Mean, median, mode, variance, standard deviation, and key statistical concepts.

### ⚡ Part 4: Optimization
- **Convexity**: Convex sets, convex functions (including quasiconvexity, log-concavity, log-convexity, and $K$-convexity), and standard optimization problems (LP, QP, SOCP, SDP, GP).
- **Theory & Algorithms**: Duality (Lagrangian, KKT conditions), unconstrained/equality-constrained Newton's methods, and Interior-Point algorithms.
- **Applications**: Geometric & statistical optimization (MLE, MAP, minimum ellipsoids) and combinatorial optimization.

### 🌀 Part 5: Functional Analysis & Measure Theory
- **Functional Analysis**: Banach spaces, bounded linear operators, quotient spaces, Baire Category Theorem, and Hahn-Banach Theorem.
- **Measure Theory**: Outer measure, $\sigma$-algebras, Lebesgue measure, measurable functions, and simple functions.

### 🌐 Part 6: Topology
- **General Topology**: Metric spaces, open sets, neighborhoods, compactness, and connectedness.
- **Manifolds**: The Manifold Hypothesis, homeomorphisms (and their role in neural networks), and topological dimensionality reduction (t-SNE, UMAP).
- **Topological Data Analysis (TDA)**: Simplicial complexes, Betti numbers, and Persistent Homology (barcodes and diagrams).

### 📈 Part 7: Approximation Theory
- **Fitting**: Curve fitting, regression analysis, interpolation, and approximating continuous functions.

### 🤖 Part 8: Machine Learning
- **Math Foundations**: Practical methodology, supervised learning math, unsupervised learning math, and distributed learning structures.

### 🧠 Part 9: Deep Learning
- **Neural Networks**: Artificial neurons, activation functions, loss functions, backpropagation, and gradient descent optimization in deep networks.

### 📚 Part 10: Recommended Reading
- **Reading**: Our curated list of recommended textbook resources for mathematics and AI.

---

## ☕️ Buy Me a Coffee / Ủng hộ tác giả

Nếu bạn thấy các bài viết trên blog hữu ích và muốn tiếp thêm động lực cho tác giả duy trì & phát triển nội dung kiến thức Data Science / AI chất lượng:

<div style="display: flex; justify-content: center; margin: 30px 0;">
  <div style="background: linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%); border: 1px solid rgba(99, 102, 241, 0.3); border-radius: 16px; padding: 25px; max-width: 440px; text-align: center; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3); color: #ffffff;">
    <h3 style="margin-top: 0; color: #38bdf8; font-size: 1.4rem;">☕️ Mua tặng tác giả 1 ly cà phê</h3>
    <p style="color: #94a3b8; font-size: 0.95rem; margin-bottom: 20px;">Mọi đóng góp dù lớn hay nhỏ đều là nguồn động lực rất lớn đối với mình!</p>
    
    <!-- VietQR for domestic support -->
    <div style="background: #ffffff; padding: 12px; border-radius: 12px; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
      <img src="https://img.vietqr.io/image/TPB-02149545701-compact2.png?accountName=HUYNH%20TRUNG%20NGHIA&addInfo=Ung%20ho%20kenakai16%20blog" alt="VietQR TPBank HUYNH TRUNG NGHIA" style="width: 250px; height: auto; display: block; border-radius: 8px;" />
    </div>

    <!-- Bank details -->
    <div style="margin-top: 18px; text-align: left; background: rgba(255, 255, 255, 0.05); padding: 12px 16px; border-radius: 8px; font-size: 0.9rem;">
      <div style="margin-bottom: 4px;"><strong>Ngân hàng:</strong> <span style="color: #38bdf8;">TPBank (Ngân hàng Tiên Phong)</span></div>
      <div style="margin-bottom: 4px;"><strong>Số tài khoản:</strong> <code style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 2px 6px; border-radius: 4px;">0214 9545 701</code></div>
      <div><strong>Chủ tài khoản:</strong> <span style="color: #f1f5f9;">HUYNH TRUNG NGHIA</span></div>
    </div>

    <!-- Divider -->
    <div style="margin: 20px 0 15px 0; border-top: 1px dashed rgba(255, 255, 255, 0.15); position: relative;">
      <span style="background: #0f172a; color: #64748b; padding: 0 10px; font-size: 0.8rem; position: absolute; top: -10px; left: 50%; transform: translateX(-50%);">HOẶC (QUỐC TẾ)</span>
    </div>

    <!-- Ko-fi Button -->
    <div style="margin-top: 15px;">
      <a href="https://ko-fi.com/kenakai16" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; background-color: #ff5e5b; color: #ffffff; font-weight: 700; padding: 10px 20px; border-radius: 10px; text-decoration: none; font-size: 0.95rem; box-shadow: 0 4px 12px rgba(255, 94, 91, 0.3); transition: transform 0.2s;">
        <img src="https://storage.ko-fi.com/cdn/cup-border.png" alt="Ko-fi" style="width: 20px; height: 20px;" />
        Support me on Ko-fi
      </a>
    </div>
  </div>
</div>

---

## 📖 Table of Contents

```{tableofcontents}
```
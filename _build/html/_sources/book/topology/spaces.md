# Topological Spaces & Metric Spaces

This section covers the mathematical formulations of Point-Set Topology, defining how spaces are constructed, how limits and closeness are generalized, and how structure-preserving maps are defined.

---

## 1. What is a Topological Space?
Formally, a **topological space** is a pair $(X, \tau)$, where $X$ is a set and $\tau$ is a collection of subsets of $X$ (called the **topology** on $X$) that satisfies the following three axioms:

1. **Trivial Sets**: The empty set $\emptyset$ and the set $X$ itself must belong to $\tau$:
   $$\emptyset \in \tau \quad \text{and} \quad X \in \tau$$
2. **Arbitrary Unions**: The union of any collection of sets in $\tau$ must also be in $\tau$:
   $$\bigcup_{U \in S} U \in \tau \quad \text{for any } S \subseteq \tau$$
3. **Finite Intersections**: The intersection of any finite collection of sets in $\tau$ must also be in $\tau$:
   $$\bigcap_{i=1}^n U_i \in \tau \quad \text{where } U_i \in \tau$$

The subsets in $\tau$ are called the **open sets** of the space $X$. By defining which sets are "open", a topology defines the structure of the space (such as neighborhood and convergence) without relying on distance measurements.

---

## 2. Metric Spaces: A Concrete Example
A **metric space** is a specific type of topological space where open sets are defined using a distance function (metric). 

A metric space is a set $X$ equipped with a metric $d: X \times X \to \mathbb{R}$ that satisfies four axioms for all points $x, y, z \in X$:
1. **Non-negativity**: $d(x, y) \ge 0$
2. **Identity of Indiscernibles**: $d(x, y) = 0 \iff x = y$
3. **Symmetry**: $d(x, y) = d(y, x)$
4. **Triangle Inequality**: $d(x, z) \le d(x, y) + d(y, z)$

In a metric space, we define an **open ball** of radius $r > 0$ centered at $x$ as:
$$B(x, r) = \{y \in X \mid d(x, y) < r\}$$

A set $U \subseteq X$ is then defined as **open** if every point $x \in U$ is the center of some open ball completely contained inside $U$. The collection of all such open sets forms a valid topology $\tau$ on $X$.

Common metrics in Data Science include:
- **Euclidean Distance ($L_2$)**: $d(x, y) = \sqrt{\sum (x_i - y_i)^2}$
- **Manhattan Distance ($L_1$)**: $d(x, y) = \sum |x_i - y_i|$
- **Cosine Distance**: $d(x, y) = 1 - \frac{x \cdot y}{\|x\| \|y\|}$

---

## 3. Continuous Functions and Homeomorphisms
In topology, the equivalent of a structure-preserving map between two spaces is a **continuous function**:

*   **Continuous Function**: A function $f: X \to Y$ between two topological spaces is continuous if the preimage of every open set in $Y$ is an open set in $X$:
    $$f^{-1}(V) \in \tau_X \quad \text{for every open } V \subseteq Y$$
*   **Homeomorphism**: A **homeomorphism** (or topological isomorphism) is a bijective function $f: X \to Y$ such that both $f$ and its inverse $f^{-1}$ are continuous. 

If a homeomorphism exists between $X$ and $Y$, the two spaces are said to be **homeomorphic** (topologically equivalent). They share all topological properties, meaning one can be continuously morphed into the other without tearing, cutting, or gluing (e.g., a donut morphing into a coffee cup).

---

## 4. Compactness and Connectedness
Using open sets, we can define two fundamental topological properties used in optimization and machine learning:
- **Compactness**: A space is compact if every open cover has a finite subcover (in $\mathbb{R}^n$, this means the set is closed and bounded). Compactness guarantees that continuous functions reach their minimum and maximum values—a crucial property for optimization algorithms.
- **Connectedness**: A space is connected if it cannot be partitioned into two disjoint open sets. Connectedness forms the mathematical backbone of clustering algorithms (e.g., Single Linkage Hierarchical Clustering).

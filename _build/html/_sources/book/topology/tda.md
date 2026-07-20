# Topological Data Analysis (TDA) & Persistent Homology

Topological Data Analysis (TDA) treats data points as a cloud from which we want to extract the underlying shape and connectivity.

---

## 1. Simplicial Complexes
To analyze a discrete set of data points topologically, we connect them using **simplices** (points, lines, triangles, tetrahedrons) to build a continuous geometric structure called a **Simplicial Complex**:
- **0-simplex**: A point (representing a data point).
- **1-simplex**: A line segment (connecting two close points).
- **2-simplex**: A filled triangle (connecting three mutually close points).
- **3-simplex**: A solid tetrahedron.

A common method is the **Vietoris-Rips Complex**: We grow a sphere of radius $\epsilon/2$ around each point. If the spheres of two points intersect (i.e., their distance is $\le \epsilon$), we draw a 1-simplex between them. If three spheres intersect mutually, we fill in a 2-simplex, and so on.

---

## 2. Betti Numbers
**Betti numbers** ($\beta_k$) are topological invariants that count the number of $k$-dimensional holes in a simplicial complex:
- $\beta_0$: The number of **connected components**.
- $\beta_1$: The number of **1D circular holes** (like a loop or a circle).
- $\beta_2$: The number of **2D voids** (like the empty space inside a hollow sphere or balloon).

---

## 3. Persistent Homology
Instead of choosing a single radius $\epsilon$, **Persistent Homology** computes the simplicial complexes for *all* values of $\epsilon$ from $0$ to $\infty$. As $\epsilon$ grows:
- New simplices are born (connecting components).
- New holes are born.
- Existing holes are filled in and "die."

We track the **birth** and **death** of topological features across different scales of $\epsilon$ using:
- **Persistence Barcodes**: Horizontal lines showing the lifespan of each hole (x-axis is $\epsilon$).
- **Persistence Diagrams**: 2D scatter plots where the x-axis is the birth scale and the y-axis is the death scale.

```{image} ../../images/persistence_diagram_example.png
:alt: Persistent Homology Barcode and Diagram
:class: bg-primary mb-1
:width: 85%
:align: center
```

Long-lived features (bars that persist over a wide range of $\epsilon$) represent true topological structures of the data, while short-lived features represent noise.

---

## 4. Python Example: Calculating Betti Numbers with `GUDHI`

You can perform Topological Data Analysis in Python using the `gudhi` library:

```python
# To run this example, install gudhi: pip install gudhi
import numpy as np
import gudhi as gd

# Generate points on a circle with some noise
theta = np.linspace(0, 2 * np.pi, 100)
x = np.cos(theta) + np.random.normal(0, 0.05, 100)
y = np.sin(theta) + np.random.normal(0, 0.05, 100)
points = np.vstack((x, y)).T

# Compute Vietoris-Rips complex
rip_complex = gd.RipsComplex(points=points, max_edge_length=2.0)
simplex_tree = rip_complex.create_simplex_tree(max_dimension=2)

# Compute persistence
persistence = simplex_tree.persistence()

# Print topological features: dimension, (birth, death)
for feature in persistence:
    dim, (birth, death) = feature
    # We look for features that persist (have a large lifespan)
    if (death - birth) > 0.5:
        print(f"Dimension {dim} hole born at {birth:.3f}, dies at {death:.3f} (Lifespan: {death - birth:.3f})")
```

**Expected Output:**
```
Dimension 0 hole born at 0.000, dies at inf (Lifespan: inf)
Dimension 1 hole born at 0.120, dies at 1.450 (Lifespan: 1.330)
```
- The infinite dimension 0 hole shows that all points eventually merge into a single connected component.
- The dimension 1 hole (large lifespan) indicates the loop structure of the circle we generated.

# Linear Transformations & Neural Networks

Matrix operations can be geometrically viewed as transformations of vector spaces. Understanding linear maps sheds light on how Neural Networks process and reshape data.

---

## 1. Matrix as a Geometric Transformation

A matrix $A \in \mathbb{R}^{m \times n}$ acts as a function $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$ defined by:

$$T(x) = A x$$

Linear transformations satisfy two fundamental properties for any vectors $u, v$ and scalar $c$:
1. **Additivity:** $T(u + v) = T(u) + T(v)$
2. **Homogeneity:** $T(c v) = c T(v)$

### Common 2D Geometric Transformations
* **Scaling:** $\begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}$ (resizes vectors along axes).
* **Rotation:** $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ (rotates vectors counter-clockwise by angle $\theta$).
* **Shearing:** $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ (slants shapes horizontally).

```python
import numpy as np

# Rotation matrix for theta = 90 degrees (pi/2)
theta = np.pi / 2
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

v = np.array([1.0, 0.0]) # Vector pointing right along X-axis
v_rotated = R @ v

print("Original vector:", v)
print("Rotated vector (90 deg counter-clockwise):", np.round(v_rotated, 2)) # Points up along Y-axis!
```

---

## 2. Deep Learning: Dense Layers as Linear Maps

In Deep Learning, a single fully connected (Dense) layer transforms an input feature vector $x \in \mathbb{R}^n$ into an output representation $h \in \mathbb{R}^m$:

$$h = \sigma(W x + b)$$

Where:
* $W \in \mathbb{R}^{m \times n}$ is the Weight Matrix (Linear Transformation mapping feature space).
* $b \in \mathbb{R}^m$ is the Bias Vector (Translation / Shift).
* $\sigma(\cdot)$ is a non-linear Activation Function (e.g., ReLU, Sigmoid, Tanh).

### Why Non-Linearity Matters
If we stack 100 neural network layers without non-linear activations ($\sigma$), the entire network reduces to a single combined linear transformation:

$$y = W_{100} W_{99} \dots W_1 x + b' = W_{\text{combined}} x + b'$$

No matter how deep the network is, a linear transformation can only draw straight decision boundaries (hyperplanes). Non-linear activation functions bend and warp the feature space, allowing Deep Learning models to learn highly complex, non-linear patterns!

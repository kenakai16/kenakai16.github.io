# Deep Learning Foundations

Deep Learning is a subset of Machine Learning that is based on Artificial Neural Networks (ANNs). It is designed to learn representations of data automatically by passing inputs through multiple layers of nodes (neurons), mimicking the human brain's neural connections.

---

## 1. The Perceptron: The Atom of Neural Networks

The basic building block of a neural network is the **neuron** (or Perceptron). It takes several inputs, multiplies them by their corresponding weights, adds a bias term, and passes the result through an **activation function** to produce an output.

Mathematically, a single neuron computes:

$$z = w_1 x_1 + w_2 x_2 + \dots + w_n x_n + b = \mathbf{w}^T \mathbf{x} + b$$
$$a = \sigma(z)$$

Where:
- $\mathbf{x}$ is the input vector.
- $\mathbf{w}$ is the weight vector.
- $b$ is the bias.
- $\sigma$ is the activation function.

---

## 2. Activation Functions

Without activation functions, a neural network is just a giant linear regression model (linear transformations stacked on linear transformations are still linear). Activation functions introduce **non-linearity**, allowing neural networks to learn complex, non-linear relationships.

| Name | Formula | Use Case |
|------|---------|----------|
| **Sigmoid** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | Output layer of binary classification |
| **ReLU (Rectified Linear Unit)** | $f(z) = \max(0, z)$ | Default for hidden layers |
| **Tanh (Hyperbolic Tangent)** | $\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$ | Hidden layers (zero-centered outputs) |

```python
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0, z)

# Plotting the functions
z = np.linspace(-5, 5, 200)
plt.figure(figsize=(10, 4))
plt.plot(z, sigmoid(z), label='Sigmoid', color='blue')
plt.plot(z, relu(z), label='ReLU', color='red')
plt.axhline(0, color='black',linewidth=0.5, linestyle='--')
plt.axvline(0, color='black',linewidth=0.5, linestyle='--')
plt.title('Activation Functions')
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig('../../images/activations.png')
plt.show()
```

---

## 3. How a Neural Network Learns

Training a neural network is an iterative process consisting of three main phases:

### Phase 1: Forward Propagation
Inputs are fed forward through the network layer by layer to compute a prediction ($\hat{y}$).

### Phase 2: Loss (Cost) Computation
We evaluate the error of our prediction using a **Loss Function**. For regression, we typically use Mean Squared Error (MSE):

$$L = \frac{1}{2}(\hat{y} - y)^2$$

### Phase 3: Backpropagation
Backpropagation calculates the gradient of the loss function with respect to each weight in the network. It uses the **Chain Rule** (from Calculus) to trace the gradient from the output layer back to the input layer.

For a weight $w$, we find:

$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial a} \cdot \frac{\partial a}{\partial z} \cdot \frac{\partial z}{\partial w}$$

Then we update the weight using **Gradient Descent**:

$$w_{new} = w_{old} - \alpha \frac{\partial L}{\partial w}$$

Where $\alpha$ is the **learning rate**.

---

## 4. Implementing a Basic Neural Network from Scratch in Python

Let's write a simple network with one input layer (2 features), one hidden layer (3 neurons), and one output layer (1 neuron) to solve a binary classification task.

```python
import numpy as np

# Activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Dataset (XOR problem)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0], [1], [1], [0]])

# Seed random numbers for reproducibility
np.random.seed(42)

# Weight initialization
input_size = 2
hidden_size = 3
output_size = 1

weights_input_hidden = np.random.uniform(-1, 1, (input_size, hidden_size))
weights_hidden_output = np.random.uniform(-1, 1, (hidden_size, output_size))

learning_rate = 0.5
epochs = 10000

# Training Loop
for epoch in range(epochs):
    # --- Forward Propagation ---
    hidden_input = np.dot(X, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)
    
    final_input = np.dot(hidden_output, weights_hidden_output)
    predictions = sigmoid(final_input)
    
    # --- Backward Propagation ---
    # 1. Compute loss derivative at output
    error = y - predictions
    d_predicted_output = error * sigmoid_derivative(predictions)
    
    # 2. Backpropagate error to hidden layer
    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_output)
    
    # 3. Update weights
    weights_hidden_output += hidden_output.T.dot(d_predicted_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

# Final Predictions
print("Predictions after training:")
print(np.round(predictions, 2))
```

**Output:**
```
Predictions after training:
[[0.06]
 [0.93]
 [0.93]
 [0.08]]
```
The simple neural network successfully learned the non-linear XOR function!

---

## Exercises

```{admonition} Exercise 1
:class: tip
Derive the derivative of the Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$ by hand and show that:

$$\frac{d\sigma}{dz} = \sigma(z)(1 - \sigma(z))$$
```

```{admonition} Exercise 2
:class: tip
Modify the scratch Python neural network above to use a different learning rate (e.g., $0.05$ and $2.0$). Trace how the learning rate affects training convergence.
```

```{admonition} Exercise 3
:class: tip
Install PyTorch and write a simple script using `torch.nn` to solve the same XOR classification problem.
```
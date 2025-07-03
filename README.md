# Linear Regression

A pure Python implementation of linear regression, built as a first step into the world of ***machine learning*** — no libraries, just logic and math.

## Overview

This project analyzes the relationship between the number of tutorial hours and the number of days it takes to feel confident. By training on a dataset, it fits a straight line to the data using gradient descent and predicts outcomes based on the linear relationship.

## Features

* Implements **linear regression** from the ground up
* Uses **gradient descent** function for optimization
* Custom **mean square error** function
* No machine learning libraries used
* Visualizes the learning outcome with **matplotlib**

## How It Works

1. Loads a dataset from a CSV file
2. Initializes a linear model with zero slope and intercept
3. Runs **1000 iterations of gradient descent** to minimize prediction error
4. Prints training progress every 100 steps
5. Plots the original data along with the learned regression line

## ML Relevance

This project is a basic example of **supervised learning**, where the model learns from labeled data (tutorial hours → days to confidence).
To place it in context:

* **Supervised Learning**: Learns from input-output pairs (e.g., predicting prices, classifications)
* **Unsupervised Learning**: Finds patterns in unlabeled data (e.g., clustering, dimensionality reduction)
* **Reinforcement Learning**: Learns through feedback from actions (e.g., games, robotics)

This project focuses on the first: supervised learning — one of the most fundamental techniques in machine learning.

Absolutely — you can include a section in your README like this to explain the math behind your implementation. It breaks down **Mean Squared Error** and the **derivatives used in gradient descent**, with reference to the visuals you've attached.

---

## Math Behind the Model

To fit a line $y = mx + b$ to the data, we use a technique called **Gradient Descent** to minimize the **Mean Squared Error (MSE)**.

### Mean Squared Error (MSE)

The error function (cost/loss) we want to minimize is:

$$
E = \frac{1}{n} \sum_{i=0}^{n} (y_i - (m \cdot x_i + b))^2
$$

Where:

* $n$ = number of data points
* $y_i$ = actual value
* $x_i$ = input (tutorial hours)
* $m$, $b$ = slope and intercept of the line

This measures how far our predicted values are from the actual ones — squaring them ensures no negative cancellation.

---

### Gradient Descent: Minimizing Error

To update the slope (`m`) and intercept (`b`), we compute the gradients of the error function w\.r.t. each parameter.

**Partial Derivative w\.r.t. `m`:**

$$
\frac{\partial E}{\partial m} = -\frac{2}{n} \sum_{i=0}^{n} x_i (y_i - (m \cdot x_i + b))
$$

**Partial Derivative w\.r.t. `b`:**

$$
\frac{\partial E}{\partial b} = -\frac{2}{n} \sum_{i=0}^{n} (y_i - (m \cdot x_i + b))
$$

These derivatives tell us the **direction of steepest increase**, so we subtract them to move downhill — reducing error.

---

### Updating Parameters

We use a learning rate $\mathcal{L}$ (a small number) to scale the step size during updates:

$$
m = m_{new} - \mathcal{rate} \cdot  {m_{gradient}}
$$

$$
b = b_{new} - \mathcal{rate} \cdot  {b_{gradient}}
$$

This iterative update process is repeated (in our case, **1000 times**) to gradually reach the optimal line.

___


## Scatter Plot with Best-Fit Line

<img src="https://github.com/user-attachments/assets/d8ddd293-f640-40fa-8109-ed72adf5aa42" alt="Regression Plot" width="500">



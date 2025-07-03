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

## Scatter Plot with Best-Fit Line

<img src="https://github.com/user-attachments/assets/d8ddd293-f640-40fa-8109-ed72adf5aa42" alt="Regression Plot" width="500">



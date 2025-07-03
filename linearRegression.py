import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('linearRegression/learning_curve_vs_tutorial_hours.csv')

# dataset visualization-
# print(data.head)
# plt.scatter(data.Tutorial_Hours, data.Days_To_Confidence)
# plt.show()

def mean_sqaure_error(m, b, points):
    total_error=0
    for i in range(len(points)):
        x= points.iloc[i].Tutorial_Hours
        y= points.iloc[i].Days_To_Confidence
        total_error+= (y - (m*x + b)) ** 2
        
    total_error / float(len(points))

def gradient_descent(m_new, b_new, points, rate):
    m_gradient =0
    b_gradient =0

    n= len(points)

    for i in range(n):
        x= points.iloc[i].Tutorial_Hours
        y= points.iloc[i].Days_To_Confidence

        m_gradient += -(2/n) * x * (y - (m_new * x + b_new))
        b_gradient += -(2/n) * (y - (m_new * x + b_new))
    
    m = m_new - m_gradient * rate
    b = b_new - b_gradient * rate
    return m,b


m=0
b=0
rate=0.0001
epochs = 1000

for i in range(epochs):
    if i % 100 ==0:
        print(F"Epoch: {i}")
    m, b = gradient_descent(m, b, data, rate)

print(m, b)

plt.scatter(data.Tutorial_Hours, data.Days_To_Confidence, color="black")
plt.plot(list(range(1, 20)), [m * x + b for x in range(1,20)], color="red")

plt.xlabel("Tutorial Hours")
plt.ylabel("Days to Confidence")
plt.title("Learning Curve: Tutorial Hours vs Days to Confidence")

plt.show()
import matplotlib.pyplot as plt

# Basic Plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.show()

# Line Plot
plt.plot([1, 2, 3], [10, 20, 30], label="Trend")
plt.title("Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

# Bar Plot
categories = ["A", "B", "C"]
values = [10, 15, 7]
plt.bar(categories, values, color="red")
plt.title("Bar Chart")
plt.show()

# Histogram
data = [1, 2, 2, 3,3,3,4,4,4,4]
plt.hist(data, bins=4, color="green", edgecolor="black")
plt.title("Histogram")
plt.show()

# Scatter Plot
x = [1,2,3,4,5]
y = [10,12,25,30,45]
plt.scatter(x, y, color="red")
plt.title("Scatter Plot")
plt.show()

# Introduction to Seaborn for Advance Visualization
import seaborn as sns
import numpy as np

data = np.random.rand(5, 5)
sns.heatmap(data, annot=True, cmap="colorwarm")
plt.title("Heatmap")
plt.show()
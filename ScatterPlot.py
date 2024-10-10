import random
import matplotlib.pyplot as plt

# Step 1: Generate a random dataset
X = [random.random() for _ in range(100)]  # Generate 100 random values for X
Y = [2 * x + random.random() for x in X]   # Generate corresponding Y values

# Step 2: Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, Y, s=20, color='blue', alpha=0.7, edgecolor='black', marker=".")  # Adjusting marker size, color, and transparency

# Step 3: Add labels and title
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Scatter Plot of X vs Y')

plt.show()

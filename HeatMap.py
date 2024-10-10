import matplotlib.pyplot as plt
import random

# Step 1: Generate a 10x10 matrix of random values
matrix = [[random.random() for _ in range(10)] for _ in range(10)]

# Step 2: Plot a heatmap of the matrix using plt.imshow()
plt.imshow(matrix, cmap='coolwarm', interpolation='nearest')

# Step 3: Add a color bar
plt.colorbar()

# Step 4: Give the plot a title
plt.title("Heatmap of Random Data")

# Display the plot
plt.show()

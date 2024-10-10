import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# Step 1: Generate random stock prices for 100 time points
random.seed(0)  # For reproducibility
stock_prices = [100]  # Starting price

for _ in range(99):  # Generate 99 more prices
    change = random.uniform(-5, 5)  # Random change between -5 and 5
    stock_prices.append(stock_prices[-1] + change)  # Update the price

# Step 2: Create a time index
start_date = datetime(2024, 1, 1)  # Starting date
time_index = [start_date + timedelta(days=i) for i in range(100)]  # Generate 100 days

# Step 3: Create the plot
plt.figure(figsize=(12, 6))
plt.plot(time_index, stock_prices, marker='o', color='blue')

# Step 4: Format the x-axis to show time
plt.xticks(rotation=45)  # Rotate date labels for better visibility

# Step 5: Label the axes and add a title
plt.xlabel("Time")
plt.ylabel("Stock Prices")
plt.title("Random Time Series Plot")

# Step 6: Show grid for better readability
plt.grid()

# Step 7: Display the plot
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()

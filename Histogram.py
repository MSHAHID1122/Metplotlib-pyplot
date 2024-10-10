import matplotlib.pyplot as plt
import random

data = [random.gauss(0, 1) for _ in range(500)]
plt.hist(data, bins=20, color='blue', edgecolor='black')

plt.title("Histogram of Random Data")    
plt.xlabel("Value")                     
plt.ylabel("Frequency")                
plt.show()

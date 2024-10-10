import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 10)  


y1 = x**2  
y2 = x**3 

plt.figure(figsize=(10, 6)) 

plt.plot(x, y1, color='blue', linestyle='--', marker='o', label='y = x^2')  

plt.plot(x, y2, color='green', linestyle='--', marker='s', label='y = x^3',alpha=0.7)  
plt.title("Plot of y = x^2 and y = x^3")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.grid()  

plt.show()

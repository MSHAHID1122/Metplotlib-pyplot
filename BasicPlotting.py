import matplotlib.pyplot as plt

x = [ i for i in range(-10,11)]

y = [1*i + 3 for i in x]

plt.plot(x,y,marker='*',color="green")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('line equation graph')
plt.show()

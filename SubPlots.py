import matplotlib.pyplot as plt 
import math



def tan_deg(x):
    angle_rad = math.radians(x)
    return math.tan(angle_rad)



x = [i for i in range(-180,180,30)]
y1 = [math.sin(math.radians(i)) for i in x]
y2 = [math.cos(math.radians(i)) for i in x]
y3 = [math.tan(math.radians(i)) for i in x]
y4 = [math.exp(math.radians(i)) for i in x]

fig,axes= plt.subplots(2,2,figsize=(10,10))
(ax1 ,ax2),(ax3,ax4) = axes
ax1.plot(x,y1,marker = "*",color="red")

ax1.set_title("graph 1")
ax1.set_xlabel("x axis")
ax1.set_ylabel("y axis")

ax2.plot(x,y2,marker = "o",color="green")
ax2.set_title("graph 2")
ax2.set_xlabel("x axis")
ax2.set_ylabel("y axis")

ax3.plot(x,y3,marker = "<",color="yellow")
ax3.set_title("graph 3")
ax3.set_xlabel("x axis")
ax3.set_ylabel("y axis")


ax4.plot(x,y4,marker = ">",color="pink")
ax4.set_title("graph 3")
ax4.set_xlabel("x axis")
ax4.set_ylabel("y axis")
plt.tight_layout()
plt.show()



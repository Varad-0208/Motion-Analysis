import numpy as np
import matplotlib.pyplot as plt

v=float(input("Enter the velocity:"))

# all the values and parameters
g=9.81
time=int(2*v)/g
height=v*v/(2*g)
distance=[]

# dividing into small time parts
time_steps=np.linspace(0,time,100)
for t in time_steps:
 s= v*t - 0.5*g*t**2
 distance.append(s)

print("The maximum height reached by the particle is: ", height,"m")

# plotting the graph
plt.plot(time_steps,distance)
plt.xlabel("Height travelled")
plt.ylabel("Time")
plt.title("Curve followed by particle thrown upward")
plt.grid(True)

plt.show()


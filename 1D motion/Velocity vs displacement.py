import matplotlib.pyplot as plt
import numpy as np
import math

v=int(input("Enter the velocity:"))

# constants and parameters
g=9.81
velocity=[]
s=v**2/(2*g)

dist_steps=np.linspace(0,s,100)

for s in dist_steps:
    vel=v**2-2*g*s
    fvel=math.sqrt(vel)
    velocity.append(fvel)

# graph plotting
plt.plot(dist_steps,velocity)
plt.xlabel("Distance")
plt.ylabel("Velocity")
plt.title("Velocity v/s Distance")
plt.grid(True)

plt.show()
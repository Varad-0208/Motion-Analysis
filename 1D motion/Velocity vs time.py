import matplotlib.pyplot as plt
import numpy as np

v=int(input("Enter the velocity:"))

g=9.81
velocity=[]
time=int(v)/g
finalv=v-g*time
time_steps=np.linspace(0,time,100)

for t in time_steps:
    vel=v-g*t
    velocity.append(vel)

print("Final velocity is:", finalv)
plt.plot(time_steps,velocity)
plt.xlabel("Velocity")
plt.ylabel("Time")
plt.title("Velocity v/s Time graph")
plt.grid(True)

plt.show()

 
import numpy as np
import matplotlib.pyplot as plt
import math

v=int(input("Enter the initial velocity:"))
theta=float(input("Enter the angle:"))

angle=math.radians(theta)
sin2=math.sin(2*angle)
cos=math.cos(angle)
sin=math.sin(angle)
tan=math.tan(angle)
g=9.81
vx=v*cos
velocity=[]

time=2*v*sin/g
time_steps=np.linspace(0,time,100)
for t in time_steps:
    vy=v*sin - g*t
    fvel=vx*vx + vy*vy
    final_vel=math.sqrt(fvel)
    velocity.append(final_vel)

plt.plot(time_steps,velocity)
plt.xlabel("Time")
plt.ylabel("Velocity")
plt.title("Velocity v/s Time")
plt.grid(True)

plt.show()
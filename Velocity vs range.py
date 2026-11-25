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
final_vel=[]
vel_x=v*cos
vel_y=v*sin

range=(v**2)*sin2/(g)
height=2*(v*sin)**2/(2*g)

distance_step=np.linspace(0,range,100)
alt=np.linspace(0,height,100)
for h in alt:
    vely=vel_y**2 - 2*g*h
    if(vely<0):
        vely=(-vely)
    vel=vel_x*vel_x + vely
    fvel=math.sqrt(vel)
    final_vel.append(fvel)

plt.plot(distance_step,final_vel)
plt.xlabel("Range")
plt.ylabel("Velocity")
plt.title("Velocity v/s Range")
plt.grid(True)

plt.show()


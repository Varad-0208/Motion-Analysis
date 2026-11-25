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

height=[]
range=(v**2)*sin2/(g)
distance=np.linspace(0,range,100)

for x in distance:
    y=x*tan - (g*x*x)/(2*v*v*cos*cos)
    height.append(y)

plt.plot(distance,height)
plt.xlabel("Range")
plt.ylabel("Height")
plt.title("Height v/s Range")
plt.grid(True)

plt.show()
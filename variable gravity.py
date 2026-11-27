
G = 6.67430e-11  
Me = 5.972e24     
R = 6.371e6      

def variable_gravity(h, v, dt, g=None):
    if g is None:
        g = []
        # initial g_0 
        g_0 = -(G * Me) / ((R + h) ** 2)
        g.append(abs(g_0))
    else:
        g_0 = -g[-1]

    #stop when height reaches below 0
    if h <= 0:
        return g


    h_next = h + v * dt
    v_next = v + g_0 * dt
    g_next = (G * Me) / ((R + h_next) ** 2)
    g.append(g_next)


    return variable_gravity(h_next, v_next, dt, g)

initial_h=float(input("Enter initial height"))
initial_v=float(input("Enter initial velocity"))
dt=float(input("Enter time intervals"))
g_values = variable_gravity(initial_h, initial_v, dt)
print(f"Total steps: {len(g_values)}")
print(f"Initial g: {g_values[0]:.6f} m/s^2")
print(f"Final g near ground: {g_values[-1]:.6f} m/s^2")
import matplotlib.pyplot as plt
mass = 0.5
v = 0
p = 400
acceleration_due_gravity = -9.81
radius = 0.05
weight = mass * acceleration_due_gravity
projected_area = 3.14159 * radius * radius
duration = 15
dt = 0.01
t = 0
iteration = int(duration / dt)
t1 = []
p1 = []
v1 = []

for i in range(iteration):
    air_friction  = -0.5 * projected_area * v * abs(v)
    total_force = weight + air_friction
    acceleration = total_force / mass
    v += acceleration * dt
    p += v*dt
    t = i * dt
    speed = abs(v)
    t1.append(t)
    p1.append(p)
    v1.append(speed*10)

plt.plot(t1, v1 , label = "speed line")
plt.plot(t1, p1 , label = "Position line")
plt.legend()
plt.show()

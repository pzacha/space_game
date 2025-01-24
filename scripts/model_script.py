import math


class Planet:
    def __init__(self, mass: float, position: list[float]):
        self.mass = mass
        self.position = position
        self.velocity = [0, 0]


planet1 = Planet(10, position=[0, 0])
planet2 = Planet(100, [3, 4])
planet3 = Planet(1, [1, 1])

planets = [planet1, planet2, planet3]


for obj in planets:
    sum_force_x = 0
    sum_force_y = 0
    for obj2 in planets:
        if obj == obj2:
            continue
        distance = math.sqrt((obj2.position[0] - obj.position[0]) ** 2 + (obj2.position[1] - obj.position[1]) ** 2)
        force = obj.mass * obj2.mass / distance**2
        sum_force_x += (obj2.position[0] - obj.position[0]) * force / distance
        sum_force_y += (obj2.position[1] - obj.position[1]) * force / distance
    print(sum_force_x)
    print(sum_force_y)


import numpy as np


class Planet:
    def __init__(self, mass: float, position: list[float]):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = [0, 0]


planet1 = Planet(10, position=[0, 0])
planet2 = Planet(100, [3, 4])
planet3 = Planet(1, [1, 1])
planets = [planet1, planet2, planet3]

mass = np.array([obj.mass for obj in planets])

x = np.array([obj.position[0] for obj in planets])
y = np.array([obj.position[1] for obj in planets])

dx = np.subtract.outer(x, x)
dy = np.subtract.outer(y, y)


distance = np.sqrt(dx**2 + dy**2)

forces = np.divide(np.outer(mass, mass), distance**2, out=np.zeros_like(distance), where=distance != 0)

force_x = np.divide(forces * dx, distance, out=np.zeros_like(distance), where=distance != 0)
force_y = np.divide(forces * dy, distance, out=np.zeros_like(distance), where=distance != 0)


sum_forces_x, sum_forces_y = force_x.sum(axis=0), force_y.sum(axis=0)
pass

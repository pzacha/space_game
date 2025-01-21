import numpy as np


GRAV_CONST = 1


class SpaceObject:
    def __init__(self, mass: float, position: list[float] = [0, 0]):
        self.mass = float(mass)
        self.position = np.array(position, dtype=np.float64)


object1 = SpaceObject(10, [0, 0])
object2 = SpaceObject(100, [3, 4])
object3 = SpaceObject(1, [1, 1])


mass = np.array([object1.mass, object2.mass, object3.mass])
x_pos = np.array([object1.position[0], object2.position[0], object3.position[0]])
y_pos = np.array([object1.position[1], object2.position[1], object3.position[1]])


dx = np.subtract.outer(x_pos, x_pos)
dy = np.subtract.outer(y_pos, y_pos)
distance = np.sqrt(dx**2 + dy**2)

forces = (
    GRAV_CONST
    * np.divide(
        np.outer(mass, mass),
        distance**2,
        out=np.zeros_like(np.outer(mass, mass)),
        where=distance != 0,
    )
    * (np.divide(distance, abs(distance), out=np.zeros_like(distance), where=abs(distance) != 0))
)
forces_x = np.divide(forces * dx, distance, out=np.zeros_like(np.outer(mass, mass)), where=distance != 0)
forces_y = np.divide(forces * dy, distance, out=np.zeros_like(np.outer(mass, mass)), where=distance != 0)
print(forces)
print(forces_x)
print(forces_y)
sum_forces, sum_force_x, sum_force_y = forces.sum(axis=0), forces_x.sum(axis=0), forces_y.sum(axis=0)
print(sum_forces, sum_force_x, sum_force_y)

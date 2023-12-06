import numpy as np


class MassObject:
    id: int
    mass: int
    position: np.array
    velocity: np.array

    def __init__(
        self,
        id: int,
        mass: int,
        position: np.array,
        velocity: np.array = np.array([0, 0]),
    ):
        self.id = id
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def update_velocity(self, acceleration: np.array, timestamp: int):
        self.velocity = self.velocity + acceleration * timestamp

    def update_position(self, timestamp: int):
        self.position = self.position + self.velocity * timestamp

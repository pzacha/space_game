import numpy as np


class MassObject:
    """
    Represents a physical object with mass, position, and velocity in space.
    """

    id: int
    mass: float
    position: np.array
    velocity: np.array

    def __init__(
        self,
        id: int,
        mass: float,
        position: np.array,
        velocity: np.array = np.array([0, 0], dtype=np.float64),
    ):
        self.id = id
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def update_velocity(self, acceleration: np.array, timestamp: float):
        self.velocity = self.velocity + acceleration * timestamp

    def update_position(self, timestamp: float):
        self.position = self.position + self.velocity * timestamp

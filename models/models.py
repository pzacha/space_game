import itertools

import numpy as np


class MassObject:
    cls_id = itertools.count()
    id: int
    mass: int
    position: np.array
    velocity: np.array

    def __init__(
        self,
        mass: int,
        position: np.array,
        velocity: np.array = np.array([0, 0]),
    ):
        self.id = next(MassObject.cls_id)
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def update_velocity(self, acceleration: np.array, timestamp: int):
        self.velocity = self.velocity + acceleration * timestamp

    def update_position(self, timestamp: int):
        self.position = self.position + self.velocity * timestamp


class ObjectCollection:
    objects: list[MassObject]
    timestamp: int = 1  # Timestamp in seconds

    def __init__(self):
        self.objects = []

    def create_object(
        self,
        mass: int,
        position: np.array,
        velocity: np.array = np.array([0, 0]),
    ) -> int:
        self.objects.append(MassObject(mass, position, velocity))

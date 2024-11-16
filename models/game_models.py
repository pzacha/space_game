from typing import Optional
import pygame
import numpy as np


class SpaceObject:
    def __init__(
        self,
        id: Optional[int] = None,
        pos: Optional[list[int]] = None,
        radius: float = 24,
    ):
        self.id = id
        self.pos = pos if pos else [0, 0]
        self.radius = radius


class Planet(SpaceObject):
    pass


class Sun(Planet):
    def __init__(self, pos: Optional[list[int]] = None, radius: int = 40):
        super().__init__(pos=pos, radius=radius)


class Spaceship(SpaceObject):
    def __init__(
        self,
        pos: Optional[list[int]] = None,
        radius: float = 16,
        power: float = 3,
    ):
        super().__init__(pos=pos, radius=radius)
        self.movement = [0, 0, 0, 0]
        self.power = power

    def move(self, event: pygame.event) -> np.array:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.movement[0] = 1
            if event.key == pygame.K_DOWN:
                self.movement[1] = 1
            if event.key == pygame.K_RIGHT:
                self.movement[2] = 1
            if event.key == pygame.K_LEFT:
                self.movement[3] = 1

        a_y = (self.movement[1] - self.movement[0]) * self.power
        a_x = (self.movement[2] - self.movement[3]) * self.power
        self.movement = [0, 0, 0, 0]
        return np.array([a_x, a_y], dtype=np.float64)

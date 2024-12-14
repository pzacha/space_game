from typing import Optional
import pygame as pg
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
        power: float = 1,
    ):
        super().__init__(pos=pos, radius=radius)
        self.movement = [0, 0, 0, 0]
        self.power = power
        self.ax = 0
        self.ay = 0

    @property
    def acc(self):
        return np.array([self.ax, self.ay], dtype=np.float64)

    def update_acc(self, event: pg.event) -> np.array:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                self.movement[0] = 1
            if event.key == pg.K_DOWN:
                self.movement[1] = 1
            if event.key == pg.K_RIGHT:
                self.movement[2] = 1
            if event.key == pg.K_LEFT:
                self.movement[3] = 1
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                self.movement[0] = 0
            if event.key == pg.K_DOWN:
                self.movement[1] = 0
            if event.key == pg.K_RIGHT:
                self.movement[2] = 0
            if event.key == pg.K_LEFT:
                self.movement[3] = 0

        self.ay = (self.movement[1] - self.movement[0]) * self.power
        self.ax = (self.movement[2] - self.movement[3]) * self.power

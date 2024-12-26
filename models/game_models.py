from typing import Optional
import pygame as pg
import numpy as np


class SpaceObject:
    """
    A class to represent a space object in the game.
    """

    def __init__(
        self,
        id: Optional[int] = None,
        pos: Optional[list[int]] = None,
        radius: float = 16,
        color: pg.Color = pg.Color("blue"),
    ):
        self.id = id
        self.pos = pos if pos else [0, 0]
        self.radius = radius
        self.color = color


class Planet(SpaceObject):
    """
    A class to represent a planet in the game.
    """

    pass


class Sun(Planet):
    """
    A class to represent a sun in the game.
    """

    def __init__(self, pos: Optional[list[int]] = None, radius: int = 40, color=pg.Color("yellow")):
        super().__init__(pos=pos, radius=radius, color=color)


class Spaceship(SpaceObject):
    """
    A class to represent a player's spaceship in the game.
    """

    def __init__(
        self,
        pos: Optional[list[int]] = None,
        radius: float = 16,
        power: float = 1,
        color: pg.Color = pg.Color("white"),
    ):
        super().__init__(pos=pos, radius=radius, color=color)
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

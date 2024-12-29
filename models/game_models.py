from math import pi
from typing import Optional
import pygame as pg
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


class SpaceObject(MassObject):
    """
    A class to represent a space object in the game.
    """

    game_pos: list[int]

    def __init__(
        self,
        id: int,
        mass: float,
        position: np.array,
        velocity: np.array = np.array([0, 0], dtype=np.float64),
        radius: float = 16,
        color: pg.Color = pg.Color("blue"),
        game_pos: Optional[list[int]] = None,
    ):
        super().__init__(id=id, mass=mass, position=position, velocity=velocity)
        self.radius = radius
        self.color = color
        self.game_pos = game_pos if game_pos else [0, 0]


class Planet(SpaceObject):
    """
    A class to represent a planet in the game.
    """

    pass


class Sun(Planet):
    """
    A class to represent a sun in the game.
    """

    def __init__(
        self,
        id: int,
        mass: float,
        position: Optional[list[int]] = None,
        velocity=np.array([0, 0], dtype=np.float64),
        radius: int = 40,
        color=pg.Color("yellow"),
        animation_ratio: Optional[float] = pi,
    ):
        super().__init__(id=id, mass=mass, position=position, velocity=velocity, radius=radius, color=color)
        self.animation_ratio = animation_ratio


class Spaceship(SpaceObject):
    """
    A class to represent a player's spaceship in the game.
    """

    def __init__(
        self,
        id: int,
        mass: float,
        position: Optional[list[int]] = None,
        velocity=np.array([0, 0], dtype=np.float64),
        radius: float = 16,
        color: pg.Color = pg.Color("white"),
        power: float = 1,
    ):
        super().__init__(id=id, mass=mass, position=position, velocity=velocity, radius=radius, color=color)
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

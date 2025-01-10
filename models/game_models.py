from math import pi
import math
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

    def update_velocity(self, acceleration: np.array, step_size: float):
        self.velocity = self.velocity + acceleration * step_size

    def update_position(self, step_size: float):
        self.position = self.position + self.velocity * step_size


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
        color: Optional[tuple[int]] = None,
        game_pos: Optional[list[int]] = None,
    ):
        super().__init__(id=id, mass=mass, position=position, velocity=velocity)
        self.radius = math.floor(math.log10(self.mass)) * 1.5
        self.color = color if color else pg.Color("blue")
        self.game_pos = game_pos if game_pos else [0, 0]
        self.collision_time: Optional[int] = None


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
        color: Optional[tuple[int]] = None,
        animation_ratio: Optional[float] = pi,
    ):
        super().__init__(id=id, mass=mass, position=position, velocity=velocity, color=color)
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
        color: Optional[tuple[int]] = None,
        power: float = 1,
    ):
        super().__init__(id=id, mass=mass, position=position, velocity=velocity, color=color)
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

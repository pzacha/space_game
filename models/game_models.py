from typing import Optional
import pygame
import numpy as np


class SpaceObject:
    def __init__(
        self,
        id: Optional[int] = None,
        pos: Optional[list[int]] = None,
        radius: float = 100,
        img: str = "planet1",
    ):
        self.id = id
        self.img = pygame.image.load(f"data/images/{img}.png")
        self.pos = pos if pos else [0, 0]
        self.radius = radius
        self.img = pygame.transform.scale(self.img, [self.radius, self.radius])

    @property
    def render_pos(self):
        return np.subtract(self.pos, np.divide(list(self.img.get_size()), 2))


class Planet(SpaceObject):
    pass


class Sun(Planet):
    def __init__(
        self, pos: Optional[list[int]] = None, radius: int = 100, img: str = "sun"
    ):
        super().__init__(pos=pos, radius=radius, img=img)
        self.img = pygame.transform.scale(self.img, [self.radius * 2, self.radius * 2])


class Spaceship(SpaceObject):
    def __init__(
        self,
        pos: Optional[list[int]] = None,
        radius: float = 100,
        img: str = "spaceship",
    ):
        super().__init__(pos=pos, radius=radius, img=img)
        self.movement = [False, False, False, False]
        self.speed = 5

    def move(self, event: pygame.event) -> np.array:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.movement[0] = True
            elif event.key == pygame.K_DOWN:
                self.movement[1] = True
            elif event.key == pygame.K_RIGHT:
                self.movement[2] = True
            elif event.key == pygame.K_LEFT:
                self.movement[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.movement[0] = False
            elif event.key == pygame.K_DOWN:
                self.movement[1] = False
            elif event.key == pygame.K_RIGHT:
                self.movement[2] = False
            elif event.key == pygame.K_LEFT:
                self.movement[3] = False

        vel_x = (self.movement[1] - self.movement[0]) * self.speed
        vel_y = (self.movement[2] - self.movement[3]) * self.speed
        return np.array([vel_x, vel_y], dtype=np.float64)

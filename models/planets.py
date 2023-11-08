import pygame
import numpy as np


class Planet:
    def __init__(self, pos: list = [160, 260], radius: int = 43):
        self.img = pygame.image.load("data/images/sun.png")
        self.pos = pos
        self.radius = radius
        self.movement = [False, False, False, False]

    @property
    def render_pos(self):
        return np.subtract(self.pos, np.divide(list(self.img.get_size()), 2))

    def surface(self):
        return pygame.Rect(*self.pos, self.radius, self.radius)

    def move(self, event: pygame.Event):
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

    def update(self):
        self.pos[1] += (self.movement[1] - self.movement[0]) * 5
        self.pos[0] += (self.movement[2] - self.movement[3]) * 5

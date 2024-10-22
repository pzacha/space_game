import sys
import pygame

from models.game_models import Spaceship, Sun
from models.simulation import Simulation


MOVEMENT_EVENTS_KEYS = {pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT}


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Test game")
        self.window = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.planet1 = Spaceship(img="planet2")
        self.planet2 = Spaceship(img="planet2")
        self.sun = Sun(img="sun")
        self.sim = Simulation()
        self.sim.create_object(
            mass=10000, position=[450, 350], game_object=self.planet1
        )
        self.sim.create_object(
            mass=10000, position=[550, 250], game_object=self.planet2
        )
        self.sim.create_object(
            mass=10000010000000000000000.0, position=[120, 540], game_object=self.sun
        )

    def run(self):
        self.sim.update_simulation()
        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(self.planet1.img, self.planet1.render_pos)
            self.window.blit(self.planet2.img, self.planet2.render_pos)
            self.window.blit(self.sun.img, self.sun.render_pos)
            self.sim.update_simulation()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    self.planet1.move(event)

            pygame.display.update()
            self.clock.tick(60)


Game().run()

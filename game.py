import sys
import pygame

from models.game_models import Planet, Spaceship, Sun
from models.simulation import Simulation


MOVEMENT_EVENTS_KEYS = {pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT}


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Test game")
        self.window = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.player = Spaceship(img="planet6")
        self.planet = Planet(img="planet2")
        self.sun = Sun(img="sun")
        self.sim = Simulation()
        self.sim.create_object(mass=10000, position=[450, 350], game_object=self.player)
        self.sim.create_object(
            mass=4.87 * (10**24),
            position=[320 - 1 / 3.3 * 320, 320],
            velocity=[0, -47400],
            game_object=self.planet,
        )
        self.sim.create_object(
            mass=1.989 * (10**30),
            position=[self.sim.resolution / 2, self.sim.resolution / 2],
            game_object=self.sun,
        )

    def run(self):
        self.sim.update_simulation()
        while True:
            self.window.fill((0, 0, 0))
            self.window.blit(self.player.img, self.player.render_pos)
            self.window.blit(self.planet.img, self.planet.render_pos)
            self.window.blit(self.sun.img, self.sun.render_pos)
            self.sim.update_simulation()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.sim.objects[self.player.id].update_velocity(
                        self.player.move(event), self.sim.timestamp
                    )

            pygame.display.update()
            self.clock.tick(60)


Game().run()

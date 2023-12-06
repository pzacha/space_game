import sys
import pygame

from models.game_models import Spaceship, Sun


MOVEMENT_EVENTS_KEYS = {pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT}


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Test game")
        self.window = pygame.display.set_mode((640, 640))
        self.clock = pygame.time.Clock()
        self.planet1 = Spaceship([0, 0], img="planet2")
        self.sun = Sun([320, 240], img="sun")

    def run(self):
        while True:
            self.window.fill((0, 0, 0))
            self.planet1.update(*self.planet1.pos)
            self.window.blit(self.planet1.img, self.planet1.render_pos)
            self.window.blit(self.sun.img, self.sun.render_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or pygame.KEYUP:
                    self.planet1.move(event)

            pygame.display.update()
            self.clock.tick(60)


Game().run()

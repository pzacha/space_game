import sys
import pygame

from models.planets import Planet


MOVEMENT_EVENTS_KEYS = {pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT}


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Test game")
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.collision_area = pygame.Rect(50, 50, 300, 50)
        self.planet = Planet([0, 0])

    def run(self):
        while True:
            self.window.fill((0, 0, 0))
            self.planet.update()
            self.window.blit(self.planet.img, self.planet.render_pos)

            # Collision detection
            if self.planet.surface().colliderect(self.collision_area):
                pygame.draw.rect(self.window, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.window, (50, 50, 155), self.collision_area)

            pygame.draw.rect(self.window, (155, 155, 155), self.planet.surface())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or pygame.KEYUP:
                    self.planet.move(event)

            pygame.display.update()
            self.clock.tick(60)


Game().run()

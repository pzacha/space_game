import sys
import pygame


class Game():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Test game")
        self.window = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load("data/images/sun.png") # TODO: Add transparency
        self.img_pos = [160, 260]
        self.movement = [False, False]
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.window.fill((0,0,0))
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            self.window.blit(self.img, self.img_pos)
            
            # Collision detection
            img_r = pygame.Rect(*self.img_pos, *self.img.get_size())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.window, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.window, (50, 50, 155), self.collision_area)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()
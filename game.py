import sys
import pygame as pg

from models.game_models import Planet, Spaceship, Sun
from models.simulation import Simulation
from utils.animations import draw_sun


MOVEMENT_EVENTS_KEYS = {pg.K_DOWN, pg.K_UP, pg.K_RIGHT, pg.K_LEFT}


class Game:
    i = 0

    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Test game")
        self.window = pg.display.set_mode((640, 640))
        self.clock = pg.time.Clock()
        self.player = Spaceship()
        self.planet = Planet()
        self.sun = Sun()
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
        timestamp = 0
        while True:
            self.window.fill((0, 0, 0))
            pg.draw.circle(self.window, pg.Color("green"), self.player.pos, radius=self.player.radius, width=2)
            pg.draw.circle(self.window, pg.Color("white"), self.planet.pos, radius=self.planet.radius, width=2)
            draw_sun(self.window, pg.Color("yellow"), self.sun.pos, self.sun.radius, timestamp)
            self.sim.update_simulation()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type in [pg.KEYDOWN, pg.KEYUP] and event.key in [pg.K_UP, pg.K_DOWN, pg.K_RIGHT, pg.K_LEFT]:
                    self.player.update_acc(event)
            self.sim.objects[self.player.id].update_velocity(self.player.acc, self.sim.timestamp)

            pg.display.update()
            self.clock.tick(60)
            timestamp += 1


Game().run()

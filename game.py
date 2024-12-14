import sys
import pygame as pg

from models.game_models import Planet, Spaceship, Sun
from models.simulation import Simulation
from utils.animations import draw_sun


MOVEMENT_EVENTS_KEYS = {pg.K_DOWN, pg.K_UP, pg.K_RIGHT, pg.K_LEFT}


class Game:
    i = 0

    def __init__(self):
        self._init_game_options()
        self._init_player_object()
        self._init_game_objects(1, 1)

    def _init_game_options(self):
        pg.init()
        pg.display.set_caption("Test game")
        self.window = pg.display.set_mode((640, 640))
        self.clock = pg.time.Clock()
        self.sim = Simulation()
        self.timestamp = 0

    def _init_player_object(self):
        self.player = Spaceship()
        self.sim.create_object(mass=10000, position=[450, 350], game_object=self.player)

    def _init_game_objects(self, sun_num: int, planet_num: int):
        for _ in range(sun_num):
            self.sim.create_object(
                mass=1.989 * (10**30),
                position=[self.sim.resolution / 2, self.sim.resolution / 2],
                game_object=Sun(),
            )
        for _ in range(planet_num):
            self.sim.create_object(
                mass=4.87 * (10**24),
                position=[320 - 1 / 3.3 * 320, 320],
                velocity=[0, -47400],
                game_object=Planet(),
            )

    def _draw_objects(self):
        self.window.fill((0, 0, 0))
        for obj in self.sim.game_objects:
            if type(obj) is Sun:
                draw_sun(self.window, pg.Color("yellow"), obj.pos, obj.radius, self.timestamp)
            elif type(obj) is Planet:
                pg.draw.circle(self.window, obj.color, obj.pos, radius=obj.radius)
            else:
                pg.draw.circle(self.window, obj.color, obj.pos, radius=obj.radius, width=2)

    def run(self):
        self.sim.update_simulation()
        while True:
            self._draw_objects()
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
            self.timestamp += 1


Game().run()

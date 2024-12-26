import random
import sys
import pygame as pg

from models.game_models import Planet, Sun
from utils.animations import draw_sun
from utils.game_setup import init_game_objects, init_game_options, init_player_object


MOVEMENT_EVENTS_KEYS = {pg.K_DOWN, pg.K_UP, pg.K_RIGHT, pg.K_LEFT}


class Game:
    i = 0

    def __init__(self):
        init_game_options(self)
        init_player_object(self)
        init_game_objects(self, sun_num=1, planet_num=4)

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

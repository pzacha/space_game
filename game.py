import pygame as pg

from models.game_config import GameConfig
from models.game_models import Spaceship
from utils.display import draw_game_statistics, draw_objects
from utils.game_mechanics import detect_collisions, handle_pygame_inputs
from utils.game_setup import init_game_objects, init_game_options, init_player_object


class Game:
    def __init__(self, config=GameConfig()):
        self.config = config
        init_game_options(self)
        init_player_object(self)
        init_game_objects(self)

    def run(self):
        """Main game loop"""
        self.sim.update_simulation()

        while Spaceship in [type(obj) for obj in self.sim.objects]:
            draw_objects(self)

            self.sim.update_simulation()
            detect_collisions(self)
            handle_pygame_inputs(self)
            draw_game_statistics(self)

            pg.display.update()
            self.clock.tick(self.fps)
            self.timestamp += 1


Game().run()

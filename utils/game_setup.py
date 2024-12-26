import random
import pygame as pg

from models.game_models import Planet, Spaceship, Sun
from utils.simulation import Simulation


def init_game_options(game):
    pg.init()
    pg.display.set_caption("Test game")
    game.window = pg.display.set_mode((640, 640))
    game.clock = pg.time.Clock()
    game.sim = Simulation()
    game.timestamp = 0


def init_player_object(game):
    game.player = Spaceship()
    game.sim.create_object(mass=10000, position=[450, 350], game_object=game.player)


def init_game_objects(game, sun_num: int, planet_num: int):
    def _random_position():
        return [random.uniform(0, game.window.get_width()), random.uniform(0, game.window.get_height())]

    def _create_sun():
        mass = 1.989 * (10**30) * random.uniform(0.1, 10)
        game.sim.create_object(
            mass=mass,
            position=[game.sim.resolution / 2, game.sim.resolution / 2],
            game_object=Sun(),
        )

    def _create_planet():
        mass = 4.87 * (10**24) * random.uniform(0.1, 10)
        game.sim.create_object(
            mass=mass,
            position=_random_position(),
            velocity=[0, -47400],
            game_object=Planet(),
        )

    for _ in range(sun_num):
        _create_sun()
    for _ in range(planet_num):
        _create_planet()

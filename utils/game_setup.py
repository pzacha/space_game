import random
import pygame as pg

from models.game_models import Planet, Spaceship, Sun
from utils.display import random_green, random_red
from utils.simulation import Simulation


def init_game_options(game):
    """
    Initializes game options.
    """
    pg.init()
    pg.display.set_caption("Test game")
    game.sim = Simulation(1)
    game.window = pg.display.set_mode(game.sim.resolution)
    game.clock = pg.time.Clock()
    game.timestamp = 0
    game.fps = 60
    game.font = pg.font.Font(None, 40)


def init_player_object(game):
    """
    Initializes the player object in the game.
    """
    game.player = game.sim.create_object(
        mass=10**20, position=[450, 350], game_object=Spaceship, color=pg.Color("white")
    )


def init_game_objects(game, sun_num: int, planet_num: int):
    """
    Initialize game objects by creating a specified number of suns and planets.
    """

    def _random_position():
        """
        Returns a random position within the window.
        """
        return [random.uniform(0, game.window.get_width()), random.uniform(0, game.window.get_height())]

    def _random_velocity():
        """
        Returns a random velocity.
        """

        return random.choice([1, -1]) * random.uniform(1, 10) * 10 ** random.randint(2, 5)

    def _create_sun():
        """
        Creates a sun in center of the screen.
        """
        mass = 1.989 * (10**30) * random.uniform(1, 10)
        game.sim.create_object(
            mass=mass,
            position=[game.sim.resolution[0] / 2, game.sim.resolution[1] / 2],
            game_object=Sun,
            color=pg.Color("yellow"),
        )

    def _create_planet():
        """
        Creates a planet with random mass, position, and velocity, and adds it to the game simulation.

        The mass of the planet is calculated as a random value between 10^10 and 10^20.
        The position of the planet is generated using the _random_position() function.
        The velocity of the planet is generated using the _random_velocity() function.
        """
        mass = (10**16) * random.uniform(1, 10) * 10 ** random.randint(1, 5)
        color = random_green() if mass <= game.player.mass else random_red()
        game.sim.create_object(
            mass=mass,
            position=_random_position(),
            velocity=[_random_velocity(), _random_velocity()],
            game_object=Planet,
            color=color,
        )

    for _ in range(sun_num):
        _create_sun()
    for _ in range(planet_num):
        _create_planet()

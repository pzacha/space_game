import random
import numpy as np
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
    game.sim = Simulation(
        grav_const_factor=game.config.grav_const_factor,
        step_size=game.config.step_size,
        resolution=game.config.resolution,
        max_dist=game.config.max_dist,
    )
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


def init_game_objects(game):
    """
    Initialize game objects by creating a specified number of suns and planets.
    """

    sun_num = game.config.sun_num
    planet_num = game.config.planet_num

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


def create_solar_system(game):
    game.sim.create_object(
        mass=1.989 * (10**30),
        position=[game.sim.resolution[0] / 2, game.sim.resolution[1] / 2],
        game_object=Sun,
        color=pg.Color("yellow"),
    )
    # # Inner planets
    mercury_position = game.sim.normalize(np.array([-57.9 * (10**9), 0.0]))
    game.sim.create_object(
        mass=0.33 * (10**24),
        position=[mercury_position[0] + game.sim.resolution[0] / 2, mercury_position[1] + game.sim.resolution[1] / 2],
        velocity=[0, -47400],
        game_object=Planet,
        color=pg.Color("grey"),
    )
    venus_position = game.sim.normalize(np.array([0.0, 108.2 * (10**9)]))
    game.sim.create_object(
        mass=4.87 * (10**24),
        position=[venus_position[0] + game.sim.resolution[0] / 2, venus_position[1] + game.sim.resolution[1] / 2],
        velocity=[-35000, 0],
        game_object=Planet,
        color=pg.Color("darkgoldenrod3"),
    )
    earth_position = game.sim.normalize(np.array([0.0, -149.6 * (10**9)]))
    game.sim.create_object(
        mass=5.972 * (10**24),
        position=[earth_position[0] + game.sim.resolution[0] / 2, earth_position[1] + game.sim.resolution[1] / 2],
        velocity=[29800, 0],
        game_object=Planet,
        color=pg.Color("blue"),
    )
    mars_position = game.sim.normalize(np.array([227.9 * (10**9), 0.0]))
    game.sim.create_object(
        mass=0.642 * (10**24),
        position=[mars_position[0] + game.sim.resolution[0] / 2, mars_position[1] + game.sim.resolution[1] / 2],
        velocity=[0, 24100],
        game_object=Planet,
        color=pg.Color("red"),
    )

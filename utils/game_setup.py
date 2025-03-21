import math
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
        resolution=game.config.display_settings.resolution,
        max_dist=game.config.max_dist,
    )
    game.window = pg.display.set_mode(game.sim.resolution)
    game.clock = pg.time.Clock()
    game.timestamp = 0
    game.fps = 60
    game.font = pg.font.Font(None, game.config.display_settings.font_size)


def init_player_object(game):
    """
    Initializes the player object in the game.
    """
    position = [450, 350]
    game.player = game.sim.create_object(
        mass=10**20, position=position, game_object=Spaceship, color=game.config.player_settings.color
    )


def init_game_objects(game):
    """
    Initialize game objects.
    """
    if game.config.game_mode == "Solar_system":
        create_solar_system(game)
    elif game.config.game_mode == "Randomize_planets":
        randomize_game_objects(game)


def randomize_game_objects(game):
    """
    Initialize game objects by creating a specified number of suns and planets.
    """

    sun_num = game.config.sun_num
    planet_num = game.config.planet_num

    def _random_position() -> list[float]:
        """
        Returns a random position within the window.
        """
        return [random.uniform(0, game.window.get_width()), random.uniform(0, game.window.get_height())]

    def _random_velocity(position: list[float]) -> list[float]:
        """
        Returns a random velocity not larger than escape velocity. Velocity vector is perpendicular to the position vector.
        """
        pos_x = position[0] - game.sim.resolution[0] / 2
        pos_y = position[1] - game.sim.resolution[1] / 2
        distance_from_center = math.sqrt(
            (pos_x * game.sim.max_dist / min(game.sim.resolution) / 2) ** 2
            + (pos_y * game.sim.max_dist / min(game.sim.resolution) / 2) ** 2
        )
        sun_masses = sum([obj.mass for obj in game.sim.objects if type(obj) == Sun])
        escape_vel = math.sqrt(2 * game.sim.grav_const * sun_masses / (distance_from_center))
        velocity = random.uniform(escape_vel * 0.4, escape_vel * 0.8)
        if pos_x != pos_y:
            vel_y = pos_x * velocity / math.sqrt(pos_y**2 + pos_x**2)
            vel_x = math.sqrt(velocity**2 - vel_y**2)
        else:
            vel_x = vel_y = velocity * math.sqrt(2)

        vel_x *= 1 if pos_x < 0 else -1
        vel_y *= 1 if pos_y < 0 else -1

        return [vel_x, vel_y]

    def _create_planet():
        """
        Creates a planet with random mass, position, and velocity, and adds it to the game simulation.

        The mass of the planet is calculated as a random value between 10^10 and 10^20.
        The position of the planet is generated using the _random_position() function.
        The velocity of the planet is generated using the _random_velocity() function.
        """
        mass = (10**16) * random.uniform(1, 10) * 10 ** random.randint(1, 5)
        color = random_green() if mass <= game.player.mass else random_red()
        position = _random_position()
        velocity = _random_velocity(position)
        game.sim.create_object(
            mass=mass,
            position=position,
            velocity=velocity,
            game_object=Planet,
            color=color,
        )

    def _create_sun():
        """
        Creates a sun in center of the screen.
        """
        mass = 1.989 * (10**30) * random.uniform(1, 10)
        position = [game.sim.resolution[0] / 2, game.sim.resolution[1] / 2]
        game.sim.create_object(
            mass=mass,
            position=position,
            game_object=Sun,
            color=pg.Color("yellow"),
        )

    for _ in range(sun_num):
        _create_sun()
    for _ in range(planet_num):
        _create_planet()


def create_solar_system(game):
    position = [game.sim.resolution[0] / 2, game.sim.resolution[1] / 2]
    position = np.array(position, dtype=np.float64) / min(game.sim.resolution) * game.sim.max_dist
    game.sim.create_object(
        mass=1.989 * (10**30),
        position=position,
        game_object=Sun,
        color=pg.Color("yellow"),
    )
    # Middle of the screen
    middle = [game.sim.max_dist * game.sim.resolution[0] / game.sim.resolution[1] / 2, game.sim.max_dist / 2]

    # Inner planets
    game.sim.create_object(
        mass=0.33 * (10**24),
        position=np.array([middle[0] - 57.9 * (10**9), middle[1]]),
        velocity=[0, -47400],
        game_object=Planet,
        color=pg.Color("grey"),
    )
    game.sim.create_object(
        mass=4.87 * (10**24),
        position=np.array([middle[0], middle[1] + 108.2 * (10**9)]),
        velocity=[-35000, 0],
        game_object=Planet,
        color=pg.Color("darkgoldenrod3"),
    )
    game.sim.create_object(
        mass=5.972 * (10**24),
        position=np.array([middle[0], middle[1] - 149.6 * (10**9)]),
        velocity=[29800, 0],
        game_object=Planet,
        color=pg.Color("blue"),
    )
    game.sim.create_object(
        mass=0.642 * (10**24),
        position=np.array([middle[0] + 227.9 * (10**9), middle[1]]),
        velocity=[0, 24100],
        game_object=Planet,
        color=pg.Color("red"),
    )

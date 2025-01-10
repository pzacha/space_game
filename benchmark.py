import random
import time
from models.game_models import Planet, Sun
from utils.simulation import Simulation


def init_game_objects(game, sun_num: int, planet_num: int):
    """
    Initialize game objects by creating a specified number of suns and planets.
    """

    def _random_position():
        return random.choice([1, -1]) * random.uniform(1, 10) * 10 ** random.randint(2, 12)

    def _random_velocity():
        return random.choice([1, -1]) * random.uniform(1, 10) * 10 ** random.randint(2, 5)

    def _create_sun():
        mass = 1.989 * (10**30) * random.uniform(1, 10)
        game.sim.create_object(
            mass=mass,
            position=[0, 0],
            game_object=Sun,
            color=None,
        )

    def _create_planet():
        mass = (10**16) * random.uniform(1, 10) * 10 ** random.randint(1, 5)
        game.sim.create_object(
            mass=mass,
            position=[_random_position(), _random_position()],
            velocity=[_random_velocity(), _random_velocity()],
            game_object=Planet,
            color=None,
        )

    for _ in range(sun_num):
        _create_sun()
    for _ in range(planet_num):
        _create_planet()


class Benchmark:
    def __init__(self, num_planets: int, num_of_iterations: int, step_size: int):
        self.sim = Simulation(grav_const_factor=1, step_size=step_size)
        self.num_of_iterations = num_of_iterations
        init_game_objects(self, sun_num=1, planet_num=num_planets)

    def run(self):
        for _ in range(self.num_of_iterations):
            self.sim.update_simulation()


start_time = time.time()
Benchmark(99, 365 * 24, 3600).run()
end_time = time.time()

print(f"Simulation took {end_time - start_time} seconds")

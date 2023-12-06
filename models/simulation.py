import itertools
from typing import Optional, Type
import numpy as np
from models.game_models import SpaceObject

from models.models import MassObject


class Simulation:
    objects: list[MassObject]
    game_objects: list[Type[SpaceObject]]
    timestamp: int = 1  # Timestamp in seconds
    id = itertools.count()
    max_dist = 3.3 * 10**11
    grav_const = 6.674 * 10 ** (-11)
    resolution = 640

    def __init__(self):
        self.objects = []
        self.game_objects = []

    def create_object(
        self,
        mass: int,
        position: np.array,
        velocity: np.array = np.array([0, 0]),
        game_object: Optional[Type[SpaceObject]] = None,
    ) -> int:
        id = next(self.id)
        self.objects.append(MassObject(id, mass, position, velocity))
        if game_object:
            game_object.id = id
            self.game_objects.append(game_object)

    def get_vectorized_data(self) -> tuple[np.array, np.array, np.array]:
        mass = []
        x_pos = []
        y_pos = []
        for obj in self.objects:
            mass.append(obj.mass)
            x_pos.append(obj.position[0])
            y_pos.append(obj.position[1])
        return np.array(mass), np.array(x_pos), np.array(y_pos)

    def calc_distance(
        self, x_pos: np.array, y_pos: np.array
    ) -> tuple[np.array, np.array, np.array]:
        dx = np.subtract.outer(x_pos, x_pos)
        dy = np.subtract.outer(y_pos, y_pos)
        return dx, dy

    def _calc_force(self, mass: np.array, dr: np.array) -> np.array:
        forces = (self.grav_const * np.outer(mass, mass) / dr**2) * (dr / (abs(dr)))
        forces = np.nan_to_num(forces)
        return forces.sum(axis=0)

    def calc_force(
        self, mass: np.array, dx: np.array, dy: np.array
    ) -> tuple[np.array, np.array]:
        return (self._calc_force(mass, dx), self._calc_force(mass, dy))

    def _calc_acceleration(self, force: np.array, mass: np.array):
        return force / mass

    def calc_acceleration(
        self, force_x: np.array, force_y: np.array, mass: np.array
    ) -> tuple[np.array, np.array]:
        return (
            self._calc_acceleration(force_x, mass),
            self._calc_acceleration(force_y, mass),
        )

    def update_data(self, a_x: np.array, a_y: np.array):
        for obj, val_x, val_y in zip(self.objects, a_x, a_y):
            obj.update_velocity(np.array([val_x, val_y]), self.timestamp)
            obj.update_position(self.timestamp)

    def run_simulation_step(self):
        mass, x_pos, y_pos = self.get_vectorized_data()
        dx, dy = self.calc_distance(x_pos, y_pos)
        force_x, force_y = self.calc_force(mass, dx, dy)
        a_x, a_y = self.calc_acceleration(force_x, force_y, mass)
        self.update_data(a_x, a_y)

    def normalize(self, position: float):
        return round(position / self.max_dist * self.resolution, 1)

    def update_simulation(self):
        self.run_simulation_step(self.objects)
        for obj, g_obj in zip(self.objects, self.game_objects):
            g_obj.pos[0] = self.normalize(obj.position[0])
            g_obj.pos[0] = self.normalize(obj.position[1])

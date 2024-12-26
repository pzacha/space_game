import itertools
from typing import Optional, Type
import numpy as np
from models.game_models import SpaceObject

from models.models import MassObject


class Simulation:
    objects: list[MassObject]
    game_objects: list[Type[SpaceObject]]
    timestamp: int = 2000  # Timestamp in seconds
    id = itertools.count()
    max_dist = 3.3 * 10**11
    grav_const = 6.674 * 10 ** (-11)
    resolution = 640

    def __init__(self):
        self.objects = []
        self.game_objects = []

    def create_object(
        self,
        mass: float,
        position: list[float],
        velocity: list[float] = [0, 0],
        game_object: Optional[Type[SpaceObject]] = None,
    ):
        id = next(self.id)
        position = np.array(position, dtype=np.float64) / self.resolution * self.max_dist
        velocity = np.array(velocity, dtype=np.float64)
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

    def calc_distance(self, x_pos: np.array, y_pos: np.array) -> tuple[np.array, np.array, np.array]:
        dx = np.subtract.outer(x_pos, x_pos)
        dy = np.subtract.outer(y_pos, y_pos)
        dr = np.sqrt(dx**2 + dy**2)
        return dx, dy, dr

    def calc_force(self, mass: np.array, dx: np.array, dy: np.array, dr: np.array) -> tuple[np.array, np.array]:
        """np.divide is used to assign 0 to output when division by 0 happens"""
        forces = (
            self.grav_const
            * np.divide(
                np.outer(mass, mass),
                dr**2,
                out=np.zeros_like(np.outer(mass, mass)),
                where=dr != 0,
            )
            * (np.divide(dr, abs(dr), out=np.zeros_like(dr), where=abs(dr) != 0))
        )
        forces_x = np.divide(forces * dx, dr, out=np.zeros_like(np.outer(mass, mass)), where=dr != 0)
        forces_y = np.divide(forces * dy, dr, out=np.zeros_like(np.outer(mass, mass)), where=dr != 0)
        return forces_x.sum(axis=0), forces_y.sum(axis=0)

    def calc_acceleration(self, force_x: np.array, force_y: np.array, mass: np.array) -> tuple[np.array, np.array]:
        return (
            force_x / mass,
            force_y / mass,
        )

    def update_data(self, a_x: np.array, a_y: np.array):
        for obj, val_x, val_y in zip(self.objects, a_x, a_y):
            obj.update_velocity(np.array([val_x, val_y]), self.timestamp)
            obj.update_position(self.timestamp)

    def run_simulation_step(self):
        """Update mass objects."""
        mass, x_pos, y_pos = self.get_vectorized_data()
        dx, dy, dr = self.calc_distance(x_pos, y_pos)
        force_x, force_y = self.calc_force(mass, dx, dy, dr)
        a_x, a_y = self.calc_acceleration(force_x, force_y, mass)
        self.update_data(a_x, a_y)

    def normalize(self, position: float):
        return int(round(position / self.max_dist * self.resolution))

    def update_simulation(self):
        self.run_simulation_step()
        for obj, g_obj in zip(self.objects, self.game_objects):
            # Update game objects
            g_obj.pos[0] = self.normalize(obj.position[0])
            g_obj.pos[1] = self.normalize(obj.position[1])

import itertools
from typing import Optional, Type, Union
import numpy as np
from models.game_models import SpaceObject


class Simulation:
    """
    A class to represent the simulation of space objects and their interactions.
    """

    def __init__(
        self,
        grav_const_factor: float,
        step_size: int,
        resolution: tuple[int],
        max_dist: float,
    ):
        """
        Initialize the simulation.
        """
        self.id = itertools.count()
        self.grav_const: float = 6.674 * 10 ** (-11) * grav_const_factor
        self.max_dist: float = max_dist
        self.step_size: int = step_size  # Step size in seconds
        self.resolution: tuple[int] = resolution
        self.objects: list[Type[SpaceObject]] = []

    def create_object(
        self,
        mass: float,
        position: Union[list[float], np.array],
        velocity: list[float] = [0, 0],
        game_object: Type[SpaceObject] = SpaceObject,
        color: Optional[tuple[int]] = None,
    ) -> Type[SpaceObject]:
        """
        Creates and returns a new object in the simulation.
        """
        id = next(self.id)
        if type(position) is list:
            position = np.array(position, dtype=np.float64) / self.resolution * self.max_dist
        velocity = np.array(velocity, dtype=np.float64)
        game_obj = game_object(id, mass, position, velocity, color)
        self.objects.append(game_obj)
        return game_obj

    def delete_object(self, obj_id: int):
        """
        Delete an object from the simulation.
        """
        self.objects = [obj for obj in self.objects if obj.id != obj_id]

    def get_vectorized_data(self) -> tuple[np.array, np.array, np.array]:
        """
        Get vectorized data of the objects in the simulation.
        """
        mass = []
        x_pos = []
        y_pos = []
        for obj in self.objects:
            mass.append(obj.mass)
            x_pos.append(obj.position[0])
            y_pos.append(obj.position[1])
        return np.array(mass), np.array(x_pos), np.array(y_pos)

    def calc_distance(self, x_pos: np.array, y_pos: np.array) -> tuple[np.array, np.array, np.array]:
        """
        Calculate the distance between objects.
        """
        dx = np.subtract.outer(x_pos, x_pos)
        dy = np.subtract.outer(y_pos, y_pos)
        dr = np.sqrt(dx**2 + dy**2)
        return dx, dy, dr

    def calc_force(self, mass: np.array, dx: np.array, dy: np.array, dr: np.array) -> tuple[np.array, np.array]:
        """
        Calculate the gravitational force between objects.
        np.divide is used to assign 0 to output when division by 0 happens
        """
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
        """
        Calculate the acceleration of objects based on the forces.
        """
        return (
            force_x / mass,
            force_y / mass,
        )

    def update_data(self, a_x: np.array, a_y: np.array):
        """
        Update the velocity and position of objects based on acceleration.
        """
        for obj, val_x, val_y in zip(self.objects, a_x, a_y):
            obj.update_velocity(np.array([val_x, val_y]), self.step_size)
            obj.update_position(self.step_size)

    def run_simulation_step(self):
        """
        Update mass objects by running a single simulation step.
        """
        mass, x_pos, y_pos = self.get_vectorized_data()
        dx, dy, dr = self.calc_distance(x_pos, y_pos)
        force_x, force_y = self.calc_force(mass, dx, dy, dr)
        a_x, a_y = self.calc_acceleration(force_x, force_y, mass)
        self.update_data(a_x, a_y)

    def normalize(self, position: np.array):
        """
        Normalize the position to fit within the resolution.
        """
        return int(round(position[0] / self.max_dist * self.resolution[0])), int(
            round(position[1] / self.max_dist * self.resolution[1])
        )

    def update_simulation(self):
        """
        Run a simulation step and update objects screen positions.
        """
        self.run_simulation_step()
        for obj in self.objects:
            obj.game_pos[0], obj.game_pos[1] = self.normalize(obj.position)

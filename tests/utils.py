from typing import Optional, Type
import numpy as np
from models.game_models import SpaceObject
from models.models import MassObject
from utils.simulation import Simulation


class FakeSimulation(Simulation):
    grav_const = 1
    timestamp: int = 1

    def create_object(
        self,
        mass: float,
        position: list[float],
        velocity: list[float] = [0, 0],
        game_object: Optional[Type[SpaceObject]] = None,
    ):
        id = next(self.id)
        position = np.array(position, dtype=np.float64)
        velocity = np.array(velocity, dtype=np.float64)
        self.objects.append(MassObject(id, mass, position, velocity))
        if game_object:
            game_object.id = id
            self.game_objects.append(game_object)

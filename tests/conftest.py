import numpy as np
import pytest
from models.simulation import Simulation


@pytest.fixture
def simulation_multiple():
    simulation = Simulation()
    simulation.create_object(mass=10.0, position=np.array([0, 0], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([3, 4], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([2, 2], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([3, 3], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([4, 4], dtype=np.float64))
    return simulation


@pytest.fixture
def simulation():
    simulation = Simulation()
    simulation.create_object(mass=2.0, position=np.array([0, 0], dtype=np.float64))
    simulation.create_object(mass=4.0, position=np.array([2, 4], dtype=np.float64))
    return simulation

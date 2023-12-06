import numpy as np
import pytest
from models.simulation import Simulation


@pytest.fixture
def simulation_multiple():
    simulation = Simulation()
    simulation.create_object(mass=10, position=np.array([0, 0]))
    simulation.create_object(mass=10, position=np.array([3, 4]))
    simulation.create_object(mass=10, position=np.array([2, 2]))
    simulation.create_object(mass=10, position=np.array([3, 3]))
    simulation.create_object(mass=10, position=np.array([4, 4]))
    return simulation


@pytest.fixture
def simulation():
    simulation = Simulation()
    simulation.create_object(mass=2, position=np.array([0, 0]))
    simulation.create_object(mass=4, position=np.array([2, 4]))
    return simulation

import numpy as np
import pytest
from tests.utils import FakeSimulation


@pytest.fixture
def simulation_multiple():
    simulation = FakeSimulation()
    simulation.create_object(mass=10.0, position=np.array([0, 0], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([3, 4], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([2, 2], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([3, 3], dtype=np.float64))
    simulation.create_object(mass=10.0, position=np.array([4, 4], dtype=np.float64))
    return simulation


@pytest.fixture
def simulation():
    simulation = FakeSimulation()
    simulation.create_object(mass=2.0, position=np.array([0, 0], dtype=np.float64))
    simulation.create_object(mass=4.0, position=np.array([2, 4], dtype=np.float64))
    return simulation

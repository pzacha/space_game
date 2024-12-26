import numpy as np

from models.models import MassObject
from utils.simulation import Simulation


class TestMassObject:
    def test_mass_object_init(self):
        test_obj = MassObject(1, 10, np.array([0, 0]))
        assert test_obj.mass == 10
        np.testing.assert_array_equal(test_obj.position, np.array([0, 0]))
        np.testing.assert_array_equal(test_obj.velocity, np.array([0, 0]))


class TestSimulation:
    simulation = Simulation()

    def test_object_collection_init(self):
        simulation = Simulation()
        assert simulation.objects == []

    def test_create_object(self, simulation):
        assert simulation.objects[0].mass == 2
        np.testing.assert_array_equal(simulation.objects[0].position, np.array([0, 0]))
        np.testing.assert_array_equal(simulation.objects[0].velocity, np.array([0, 0]))

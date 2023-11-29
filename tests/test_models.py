import numpy as np

from models.models import MassObject, ObjectCollection


class TestMassObject:
    def test_mass_object_init(self):
        test_obj = MassObject(10, np.array([0, 0]))
        assert test_obj.mass == 10
        np.testing.assert_array_equal(test_obj.position, np.array([0, 0]))
        np.testing.assert_array_equal(test_obj.velocity, np.array([0, 0]))


class TestObjectCollection:
    obj_collection = ObjectCollection()

    def test_object_collection_init(self):
        obj_collection = ObjectCollection()
        assert obj_collection.objects == []

    def test_create_object(self, obj_collection):
        assert obj_collection.objects[0].mass == 2
        np.testing.assert_array_equal(
            obj_collection.objects[0].position, np.array([0, 0])
        )
        np.testing.assert_array_equal(
            obj_collection.objects[0].velocity, np.array([0, 0])
        )

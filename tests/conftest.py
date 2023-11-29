import numpy as np
import pytest
from models.models import ObjectCollection


@pytest.fixture
def obj_collection_multiple():
    obj_collection = ObjectCollection()
    obj_collection.create_object(10, np.array([0, 0]))
    obj_collection.create_object(10, np.array([3, 4]))
    obj_collection.create_object(10, np.array([2, 2]))
    obj_collection.create_object(10, np.array([3, 3]))
    obj_collection.create_object(10, np.array([4, 4]))
    return obj_collection


@pytest.fixture
def obj_collection():
    obj_collection = ObjectCollection()
    obj_collection.create_object(2, np.array([0, 0]))
    obj_collection.create_object(4, np.array([2, 4]))
    return obj_collection

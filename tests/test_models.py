import pytest

from models.models import MassObject


def test_mass_object():
    test_obj = MassObject(10, (0, 0))
    assert test_obj.id == 0
    assert test_obj.mass == 10
    assert test_obj.position == (0, 0)
    assert test_obj.velocity == (0, 0)

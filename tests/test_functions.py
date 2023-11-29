import numpy as np
from unittest.mock import patch

from functions.math import (
    calc_acceleration,
    calc_distance,
    calc_force,
    get_vectorized_data,
    update_data,
)


def test_get_data(obj_collection_multiple):
    mass, x_pos, y_pos = get_vectorized_data(obj_collection_multiple)
    np.testing.assert_array_equal(mass, np.array([10, 10, 10, 10, 10]))
    np.testing.assert_array_equal(x_pos, np.array([0, 3, 2, 3, 4]))
    np.testing.assert_array_equal(y_pos, np.array([0, 4, 2, 3, 4]))


def test_calc_distance(obj_collection_multiple):
    _, x_pos, y_pos = get_vectorized_data(obj_collection_multiple)
    dx, dy = calc_distance(x_pos, y_pos)
    np.testing.assert_array_equal(dx[0], np.array([0, -3, -2, -3, -4]))
    np.testing.assert_array_equal(dx[2], np.array([2, -1, 0, -1, -2]))
    np.testing.assert_array_equal(dy[0], np.array([0, -4, -2, -3, -4]))
    np.testing.assert_array_equal(dy[2], np.array([2, -2, 0, -1, -2]))


@patch("functions.math.GRAV_CONST", 1)
def test_calc_force(obj_collection):
    mass, x_pos, y_pos = get_vectorized_data(obj_collection)
    dx, dy = calc_distance(x_pos, y_pos)
    force_x, force_y = calc_force(mass, dx, dy)
    np.testing.assert_array_equal(force_x, np.array([2, -2]))
    np.testing.assert_array_equal(force_y, np.array([0.5, -0.5]))


@patch("functions.math.GRAV_CONST", 1)
def test_calc_acceleration(obj_collection):
    mass, x_pos, y_pos = get_vectorized_data(obj_collection)
    dx, dy = calc_distance(x_pos, y_pos)
    force_x, force_y = calc_force(mass, dx, dy)
    a_x, a_y = calc_acceleration(force_x, force_y, mass)
    np.testing.assert_array_equal(a_x, np.array([1, -0.5]))
    np.testing.assert_array_equal(a_y, np.array([0.25, -0.125]))


@patch("functions.math.GRAV_CONST", 1)
def test_update_data(obj_collection):
    mass, x_pos, y_pos = get_vectorized_data(obj_collection)
    dx, dy = calc_distance(x_pos, y_pos)
    force_x, force_y = calc_force(mass, dx, dy)
    a_x, a_y = calc_acceleration(force_x, force_y, mass)
    update_data(obj_collection, a_x, a_y)
    np.testing.assert_array_equal(
        obj_collection.objects[0].velocity, np.array([1, 0.25])
    )
    np.testing.assert_array_equal(
        obj_collection.objects[1].velocity, np.array([-0.5, -0.125])
    )
    np.testing.assert_array_equal(
        obj_collection.objects[0].position, np.array([1, 0.25])
    )
    np.testing.assert_array_equal(
        obj_collection.objects[1].position, np.array([1.5, 3.875])
    )

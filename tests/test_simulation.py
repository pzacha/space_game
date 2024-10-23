import numpy as np
from unittest.mock import patch


def test_get_data(simulation_multiple):
    mass, x_pos, y_pos = simulation_multiple.get_vectorized_data()
    np.testing.assert_array_equal(mass, np.array([10, 10, 10, 10, 10]))
    np.testing.assert_array_equal(x_pos, np.array([0, 3, 2, 3, 4]))
    np.testing.assert_array_equal(y_pos, np.array([0, 4, 2, 3, 4]))


def test_calc_distance(simulation_multiple):
    _, x_pos, y_pos = simulation_multiple.get_vectorized_data()
    dx, dy, dr = simulation_multiple.calc_distance(x_pos, y_pos)
    np.testing.assert_array_equal(dx[0], np.array([0, -3, -2, -3, -4]))
    np.testing.assert_array_equal(dx[2], np.array([2, -1, 0, -1, -2]))
    np.testing.assert_array_equal(dy[0], np.array([0, -4, -2, -3, -4]))
    np.testing.assert_array_equal(dy[2], np.array([2, -2, 0, -1, -2]))
    assert dr[0][1] == 5


def test_calc_force(simulation):
    mass, x_pos, y_pos = simulation.get_vectorized_data()
    dx, dy, dr = simulation.calc_distance(x_pos, y_pos)
    force_x, force_y = simulation.calc_force(mass, dx, dy, dr)
    np.testing.assert_array_equal(force_x.round(2), np.array([0.18, -0.18]))
    np.testing.assert_array_equal(force_y.round(2), np.array([0.36, -0.36]))


def test_calc_acceleration(simulation):
    mass, x_pos, y_pos = simulation.get_vectorized_data()
    dx, dy, dr = simulation.calc_distance(x_pos, y_pos)
    force_x, force_y = simulation.calc_force(mass, dx, dy, dr)
    a_x, a_y = simulation.calc_acceleration(force_x, force_y, mass)
    np.testing.assert_array_equal(a_x.round(2), np.array([0.09, -0.04]))
    np.testing.assert_array_equal(a_y.round(2), np.array([0.18, -0.09]))


def test_update_data(simulation):
    simulation.run_simulation_step()
    np.testing.assert_array_equal(
        simulation.objects[0].velocity.round(2), np.array([0.09, 0.18])
    )
    np.testing.assert_array_equal(
        simulation.objects[1].velocity.round(2), np.array([-0.04, -0.09])
    )
    np.testing.assert_array_equal(
        simulation.objects[0].position.round(2), np.array([0.09, 0.18])
    )
    np.testing.assert_array_equal(
        simulation.objects[1].position.round(2), np.array([1.96, 3.91])
    )

import numpy as np

from models.models import ObjectCollection

GRAV_CONST = 6.674 * 10 ** (-11)


def get_vectorized_data(
    obj_collection: ObjectCollection,
) -> tuple[np.array, np.array, np.array]:
    mass = []
    x_pos = []
    y_pos = []
    for obj in obj_collection.objects:
        mass.append(obj.mass)
        x_pos.append(obj.position[0])
        y_pos.append(obj.position[1])
    return np.array(mass), np.array(x_pos), np.array(y_pos)


def calc_distance(
    x_pos: np.array, y_pos: np.array
) -> tuple[np.array, np.array, np.array]:
    dx = np.subtract.outer(x_pos, x_pos)
    dy = np.subtract.outer(y_pos, y_pos)
    return dx, dy


def _calc_force(mass: np.array, dr: np.array) -> np.array:
    forces = (GRAV_CONST * np.outer(mass, mass) / dr**2) * (dr / (abs(dr)))
    forces = np.nan_to_num(forces)
    return forces.sum(axis=0)


def calc_force(mass: np.array, dx: np.array, dy: np.array) -> tuple[np.array, np.array]:
    return (_calc_force(mass, dx), _calc_force(mass, dy))


def _calc_acceleration(force: np.array, mass: np.array):
    return force / mass


def calc_acceleration(
    force_x: np.array, force_y: np.array, mass: np.array
) -> tuple[np.array, np.array]:
    return (_calc_acceleration(force_x, mass), _calc_acceleration(force_y, mass))


def update_data(obj_collection: ObjectCollection, a_x: np.array, a_y: np.array):
    for obj, val_x, val_y in zip(obj_collection.objects, a_x, a_y):
        obj.update_velocity(np.array([val_x, val_y]), obj_collection.timestamp)
        obj.update_position(obj_collection.timestamp)

import numpy as np


def calc_distance(
    position_a: tuple[float, float], position_b: tuple[float, float]
) -> float:
    return np.sqrt(
        (position_a[0] - position_b[0]) ** 2 + (position_a[1] - position_b[1]) ** 2
    )

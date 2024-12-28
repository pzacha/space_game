from itertools import combinations
import math
from utils.simulation import Simulation


def detect_collisions(sim: Simulation):
    """Detects collisions between objects in the game."""
    for obj, other_obj in list(combinations(sim.objects, 2)):
        if math.dist(obj.game_pos, other_obj.game_pos) <= obj.radius + other_obj.radius:
            if obj.mass >= other_obj.mass:
                obj.mass += other_obj.mass
                sim.delete_object(other_obj.id)
            else:
                other_obj.mass += obj.mass
                sim.delete_object(obj.id)

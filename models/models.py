import itertools

from models.game_models import SpaceObject


class MassObject:
    cls_id = itertools.count()
    mass: int
    position: tuple[float, float]
    velocity: tuple[float, float]
    acceleration: tuple[float, float]

    def __init__(
        self, mass: int, position: tuple[int, int], velocity: tuple[float, float]
    ):
        self.id = next(MassObject.cls_id)
        self.mass = mass
        self.position = position
        self.velocity = velocity


class ObjectCollection:
    grav_const: float = 6.674 * 10 ** (-11)
    objects: dict[int, MassObject]

    def __init__(self):
        pass

    def create_object(
        self,
        mass: int,
        position: tuple[int, int],
        velocity: tuple[float, float],
    ) -> int:
        object = MassObject(mass, position, velocity)
        self.objects[object.id] = object
        return object.id

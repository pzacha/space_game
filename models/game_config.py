class GameConfig:
    def __init__(
        self,
        sun_num: int = 1,
        planet_num: int = 15,
        resolution: tuple[int] = (1920, 1080),
        grav_const_factor: float = 1,
        max_dist: float = 3.3 * (10**11),
        step_size: int = 3600,
    ):
        self.sun_num = sun_num
        self.planet_num = planet_num
        self.resolution = resolution
        self.grav_const_factor = grav_const_factor
        self.max_dist = max_dist
        self.step_size = step_size

from enum import StrEnum
from typing import Optional

import pygame as pg


class GameMode(StrEnum):
    SOLAR_SYSTEM = "Solar_system"
    RANDOMIZE_PLANETS = "Randomize_planets"


class DisplaySettings:
    def __init__(
        self,
        resolution: tuple[int] = (1920, 1080),
        font_size: int = 40,
        draw_collisions: bool = False,
        animate_sun: bool = False,
    ):
        self.resolution = resolution
        self.font_size = font_size
        self.animate_sun = animate_sun
        self.draw_collisions = draw_collisions


class PlayerSettings:
    def __init__(
        self,
        color: pg.Color = pg.Color("white"),
        push_pull: bool = False,
    ):
        self.color = color
        self.push_pull = push_pull


class GameConfig:
    def __init__(
        self,
        sun_num: int = 1,
        planet_num: int = 10,
        grav_const_factor: float = 1,
        max_dist: float = 3.3 * (10**11),
        step_size: int = 3600,
        game_mode: GameMode = GameMode.SOLAR_SYSTEM,
        display_settings: Optional[DisplaySettings] = None,
        player_settings: Optional[PlayerSettings] = None,
    ):
        self.sun_num = sun_num
        self.planet_num = planet_num
        self.grav_const_factor = grav_const_factor
        self.max_dist = max_dist
        self.step_size = step_size
        self.game_mode = game_mode
        self.display_settings = display_settings if display_settings else DisplaySettings()
        self.player_settings = player_settings if player_settings else PlayerSettings()

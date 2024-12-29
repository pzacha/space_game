import pygame as pg

from models.game_models import Planet, Sun
from utils.animations import draw_sun


def draw_objects(game):
    """
    Draws all game objects onto the game window.
    """
    game.window.fill((0, 0, 0))
    for obj in game.sim.objects:
        if type(obj) is Sun:
            draw_sun(game.window, pg.Color("yellow"), obj.game_pos, obj.radius, game.timestamp, obj.animation_ratio)
        elif type(obj) is Planet:
            pg.draw.circle(game.window, obj.color, obj.game_pos, radius=obj.radius)
        else:
            pg.draw.circle(game.window, obj.color, obj.game_pos, radius=obj.radius, width=2)

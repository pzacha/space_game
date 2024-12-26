import pygame as pg

from models.game_models import Planet, Sun
from utils.animations import draw_sun


def draw_objects(game):
    game.window.fill((0, 0, 0))
    for obj in game.sim.game_objects:
        if type(obj) is Sun:
            draw_sun(game.window, pg.Color("yellow"), obj.pos, obj.radius, game.timestamp)
        elif type(obj) is Planet:
            pg.draw.circle(game.window, obj.color, obj.pos, radius=obj.radius)
        else:
            pg.draw.circle(game.window, obj.color, obj.pos, radius=obj.radius, width=2)

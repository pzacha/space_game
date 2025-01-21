import random

import pygame as pg

from models.game_models import Sun
from utils.animations import draw_collision, draw_sun


def random_green():
    """
    Return randomized green color.
    """
    green = random.randint(100, 255)
    return (0, green, 0)


def random_red():
    """
    Return randomized red color.
    """
    red = random.randint(100, 255)
    return (red, 0, 0)


def draw_objects(game):
    """
    Draws all game objects onto the game window.
    """
    game.window.fill((0, 0, 0))
    for obj in game.sim.objects:
        if type(obj) is Sun:
            if game.config.display_settings.animate_sun:
                draw_sun(
                    game.window, pg.Color("yellow"), obj.game_pos, obj.radius, game.timestamp, obj.animation_ratio
                )
            else:
                pg.draw.circle(game.window, pg.Color("yellow"), obj.game_pos, radius=obj.radius)
        else:
            if obj.collision_time:
                draw_collision(game, obj)
            else:
                pg.draw.circle(game.window, obj.color, obj.game_pos, radius=obj.radius)


def draw_game_statistics(game):
    """
    Draws the game statistics onto the game window.
    """
    game.window.blit(game.font.render(f"Mass = {game.player.mass:.1e}", True, pg.Color("white")), (30, 30))
    game.window.blit(
        game.font.render(f"Remaining planets = {len(game.sim.objects) - 2}", True, pg.Color("white")),
        (30, 65),
    )

import math
import sys
from itertools import combinations

import pygame as pg

from models.game_models import Planet
from utils.display import random_green, random_red


def update_planet_colors(game):
    """Updates the color of planets of their mass relative to players changed."""
    for planet in [obj for obj in game.sim.objects if type(obj) is Planet]:
        if planet.mass <= game.player.mass:
            planet.color = random_green() if planet.color[1] == 0 else planet.color
        else:
            planet.color = random_red() if planet.color[0] == 0 else planet.color


def detect_collisions(game):
    """Detects collisions between objects in the game."""
    for obj, other_obj in list(combinations(game.sim.objects, 2)):
        if math.dist(obj.game_pos, other_obj.game_pos) <= obj.radius + other_obj.radius:
            if obj.mass >= other_obj.mass:
                obj.mass += other_obj.mass
                obj.collision_time = game.timestamp
                game.sim.delete_object(other_obj.id)
            else:
                other_obj.mass += obj.mass
                other_obj.collision_time = game.timestamp
                game.sim.delete_object(obj.id)
            update_planet_colors(game)


def handle_pygame_inputs(game):
    """Handle pygame events"""
    for event in pg.event.get():
        # If the user closes the window, quit the game
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        # If a arrow key is pressed or released, update player acceleration
        if event.type in [pg.KEYDOWN, pg.KEYUP] and event.key in [pg.K_UP, pg.K_DOWN, pg.K_RIGHT, pg.K_LEFT]:
            game.player.update_acc(event)
    game.player.modify_velocity_based_on_input(game.sim.step_size)

import sys
import pygame as pg

from utils.game_setup import init_game_objects, init_game_options, init_player_object
from utils.display import draw_objects


MOVEMENT_EVENTS_KEYS = {pg.K_DOWN, pg.K_UP, pg.K_RIGHT, pg.K_LEFT}


class Game:
    i = 0

    def __init__(self):
        init_game_options(self)
        init_player_object(self)
        init_game_objects(self, sun_num=1, planet_num=4)

    def run(self):
        """Main game loop"""
        self.sim.update_simulation()

        while True:
            # Draw all game objects on the screen
            draw_objects(self)
            self.sim.update_simulation()

            # Handle events
            for event in pg.event.get():
                # If the user closes the window, quit the game
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                # If a arrow key is pressed or released, update player acceleration
                if event.type in [pg.KEYDOWN, pg.KEYUP] and event.key in [pg.K_UP, pg.K_DOWN, pg.K_RIGHT, pg.K_LEFT]:
                    self.player.update_acc(event)

            # Update the player's velocity
            self.sim.objects[self.player.id].update_velocity(self.player.acc, self.sim.timestamp)

            pg.display.update()
            self.clock.tick(60)
            self.timestamp += 1


Game().run()

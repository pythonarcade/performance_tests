"""
Moving Sprite Stress Test

Simple program to test how fast we can draw sprites that are moving

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.stress_test_draw_moving
"""

import arcade
import random
import os
from performance_timing import PerformanceTiming

# --- Constants ---
SPRITE_SCALING_COIN = 0.09
SPRITE_SCALING_PLAYER = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Moving Sprite Stress Test - Arcade"

USE_SPATIAL_HASHING = True
RESULTS_FILE = "../../result_data/arcade/collision.csv"
RESULTS_IMAGE = "../../result_data/arcade/collision.png"


class MyGameCollision(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.cleanup_texture_cache()

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.coin_list = None
        self.player_list = None
        self.player = None

        self.performance_timing = PerformanceTiming(results_file=RESULTS_FILE,
                                                    start_n=0,
                                                    increment_n=200,
                                                    end_time=60)

        arcade.set_background_color(arcade.color.AMAZON)

        # Open file to save timings
        self.results_file = open(RESULTS_FILE, "w")

        self.frame = 0

    def add_coins(self, amount):

        # Create the coins
        for i in range(amount):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE)
            coin.center_y = random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.coin_list = arcade.SpriteList(use_spatial_hash=USE_SPATIAL_HASHING)
        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING_PLAYER)
        self.player.center_x = random.randrange(SCREEN_WIDTH)
        self.player.center_y = random.randrange(SCREEN_HEIGHT)
        self.player.change_x = 3
        self.player.change_y = 5
        self.player_list.append(self.player)

    def on_draw(self):
        """ Draw everything """

        # Start timing how long this takes
        self.performance_timing.start_timer('draw')

        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()

        # Stop timing how long this takes
        self.performance_timing.stop_timer('draw')

    def update(self, delta_time):
        # Start update timer
        self.performance_timing.start_timer('update')

        self.player_list.update()
        if self.player.center_x < 0 and self.player.change_x < 0:
            self.player.change_x *= -1
        if self.player.center_y < 0 and self.player.change_y < 0:
            self.player.change_y *= -1

        if self.player.center_x > SCREEN_WIDTH and self.player.change_x > 0:
            self.player.change_x *= -1
        if self.player.center_y > SCREEN_HEIGHT and self.player.change_y > 0:
            self.player.change_y *= -1

        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)
        for coin in coin_hit_list:
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

        # Stop timing the update
        self.performance_timing.stop_timer('update')

        # Figure out if we need more coins
        if self.performance_timing.target_n > len(self.coin_list):
            new_coin_amount = self.performance_timing.target_n - len(self.coin_list)
            self.add_coins(new_coin_amount)

        # End the program run
        if self.performance_timing.end_run():
            # Save screenshot
            image = arcade.get_image()
            image.save(RESULTS_IMAGE, 'PNG')
            self.close()
            import pyglet
            pyglet.app.exit()


def main():
    """ Main method """
    window = MyGameCollision()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

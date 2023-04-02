"""
Moving Sprite Stress Test

Simple program to test how fast we can draw sprites that are moving

Artwork from https://kenney.nl
"""

import random
import arcade
import os
from performance_timing import PerformanceTiming

# --- Constants ---
SPRITE_SCALING_COIN = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)

RESULTS_FILE = "../../result_data/arcade/draw_stationary_sprites.csv"
RESULTS_IMAGE = "../../result_data/arcade/draw_stationary_sprites.png"
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Arcade - Stationary Sprite Stress Test"


class Coin(arcade.Sprite):

    def on_update(self, delta_time):
        """
        Update the sprite.
        """
        self.position = (self.position[0] + self.change_x, self.position[1] + self.change_y)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # arcade.cleanup_texture_cache()

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.coin_list = None
        self.sprite_count_list = []

        self.performance_timing = PerformanceTiming(results_file=RESULTS_FILE,
                                                    start_n=0,
                                                    increment_n=1000,
                                                    end_time=180)

        arcade.set_background_color(arcade.color.AMAZON)

    def add_coins(self, amount):

        texture = arcade.load_texture("../resources/coinGold.png")
        # Create the coins
        for i in range(amount):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin(texture, SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE)
            coin.center_y = random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.coin_list = arcade.SpriteList()

    def on_draw(self):
        """ Draw everything """

        # Start timing how long this takes
        self.performance_timing.start_timer('draw')

        # Clear the screen
        self.clear()

        # Draw all the sprites
        self.coin_list.draw()

        # Stop timing how long this takes
        self.performance_timing.stop_timer('draw')

    def on_update(self, delta_time):

        # Start update timer
        self.performance_timing.start_timer('update')

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


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()
    # arcade.set_window(None)


if __name__ == "__main__":
    main()

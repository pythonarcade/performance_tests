"""
Moving Sprite Stress Test

Simple program to test how fast we can draw sprites that are moving

Artwork from https://kenney.nl
"""
import os
import random

import arcade
from arcade_perf.tests.base import ArcadePerfTest

# --- Constants ---
SPRITE_SCALING_COIN = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Arcade - Moving Sprite Stress Test"


class Coin(arcade.Sprite):

    def on_update(self, dt):
        """
        Update the sprite.
        """
        self.position = (
            self.position[0] + self.change_x,
            self.position[1] + self.change_y,
        )


class Test(ArcadePerfTest):

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.coin_list = None
        self.sprite_count_list = []

    def add_coins(self, amount):

        # Create the coins
        for i in range(amount):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("../resources/coinGold.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE)
            coin.center_y = random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE)

            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.window.background_color = arcade.color.AMAZON
        self.coin_list = arcade.SpriteList(use_spatial_hash=False)

    def on_draw(self):
        """ Draw everything """
        self.coin_list.draw()

    def on_update(self, delta_time):
        self.coin_list.update()

        for sprite in self.coin_list:

            if sprite.position[0] < 0:
                sprite.change_x *= -1
            elif sprite.position[0] > SCREEN_WIDTH:
                sprite.change_x *= -1
            if sprite.position[1] < 0:
                sprite.change_y *= -1
            elif sprite.position[1] > SCREEN_HEIGHT:
                sprite.change_y *= -1

        # Figure out if we need more coins
        if self.performance_timing.target_n > len(self.coin_list):
            new_coin_amount = self.performance_timing.target_n - len(self.coin_list)
            self.add_coins(new_coin_amount)

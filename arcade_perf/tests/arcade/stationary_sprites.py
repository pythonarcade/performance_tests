"""
Moving Sprite Stress Test

Simple program to test how fast we can draw sprites that are moving

Artwork from https://kenney.nl
"""
import random
import arcade
from arcade_perf.tests.base import ArcadePerfTest

# --- Constants ---
SPRITE_SCALING_COIN = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Arcade - Stationary Sprite Stress Test"


class Coin(arcade.Sprite):

    def on_update(self, delta_time):
        """
        Update the sprite.
        """
        self.position = (
            self.position[0] + self.change_x,
            self.position[1] + self.change_y,
        )


class Test(ArcadePerfTest):
    name = "stationary-sprites"

    def __init__(self):
        super().__init__(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            title=SCREEN_TITLE,
            start_count=0,
            increment_count=250,
            duration=60,
        )
        self.coin_list = None

    def setup(self):
        """Set up the game and initialize the variables"""
        self.coin_list = arcade.SpriteList()
        self.coin_texture = arcade.load_texture(":textures:coinGold.png")

    def add_coins(self, amount):
        """add mount coins to the spritelist"""
        for _ in range(amount):
            coin = Coin(
                self.coin_texture,
                center_x=random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE),
                center_y=random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE),
                scale=SPRITE_SCALING_COIN,
            )
            self.coin_list.append(coin)

    def on_draw(self):
        self.coin_list.draw()

    def on_update(self, delta_time):
        pass

    def update_state(self):
        # Figure out if we need more coins
        if self.timing.target_n > len(self.coin_list):
            new_coin_amount = self.timing.target_n - len(self.coin_list)
            self.add_coins(new_coin_amount)

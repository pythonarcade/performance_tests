"""
Moving Sprite Stress Test

Simple program to test how fast we can draw sprites that are moving

Artwork from http://kenney.nl
"""
# noinspection PyPackageRequirements
import pygame
import random
from arcade_perf.tests.base import PygamePerfTest
from arcade.resources import resolve_resource_path

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- Constants ---
SPRITE_SCALING_COIN = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)

RESULTS_FILE = "../../result_data/pygame/draw_moving_sprites.csv"
RESULTS_IMAGE = "../../result_data/pygame/draw_moving_sprites.png"
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Pygame - Moving Sprite Stress Test"


class Coin(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    # Static coin image
    coin_image = None

    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # In Pygame, if we load and scale a coin image every time we create a sprite,
        # this will result in a noticeable performance hit. Therefore we do it once,
        # and re-use that image over-and-over.
        if Coin.coin_image is None:
            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            path = resolve_resource_path(":textures:coinGold.png")
            Coin.coin_image = pygame.image.load(path)
            rect = Coin.coin_image.get_rect()
            Coin.coin_image = pygame.transform.scale(
                Coin.coin_image,
                (int(rect.width * SPRITE_SCALING_COIN), int(rect.height * SPRITE_SCALING_COIN)))
            Coin.coin_image.convert()
            Coin.coin_image.set_colorkey(BLACK)

        self.image = Coin.coin_image

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        # Instance variables for our current speed and direction
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Test(PygamePerfTest):
    name = "moving-sprites"

    def __init__(self):
        super().__init__(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            title=SCREEN_TITLE,
            start_count=0,
            increment_count=250,
            duration=60,
        )

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.coin_list = pygame.sprite.Group()

    def add_coins(self, amount):
        """Add mount coins to the list"""
        for _ in range(amount):
            coin = Coin()

            # Position the coin
            coin.rect.x = random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE)
            coin.rect.y = random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE)

            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.add(coin)

    def on_draw(self):
        # Draw all the spites
        self.coin_list.draw(self.window)

    def on_update(self, _delta_time):
        self.coin_list.update()

        for sprite in self.coin_list:

            if sprite.rect.x < 0:
                sprite.change_x *= -1
            elif sprite.rect.x > SCREEN_WIDTH:
                sprite.change_x *= -1
            if sprite.rect.y < 0:
                sprite.change_y *= -1
            elif sprite.rect.y > SCREEN_HEIGHT:
                sprite.change_y *= -1

    def update_state(self):
        # Figure out if we need more coins
        if self.timing.target_n > len(self.coin_list):
            new_coin_amount = self.timing.target_n - len(self.coin_list)
            self.add_coins(new_coin_amount)

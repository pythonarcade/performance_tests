"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
import arcade
import pygame
import random
from arcade_perf.tests.base import PygamePerfTest

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- Constants ---
SPRITE_SCALING_COIN = 0.09
SPRITE_SCALING_PLAYER = 0.5
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)

SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Pygame - Moving Sprite Stress Test"

RESULTS_FILE = "../../result_data/pygame/collision.csv"
RESULTS_IMAGE = "../../result_data/pygame/collision.png"


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
        image_path = arcade.resources.resolve_resource_path(":textures:coinGold.png")
        if Coin.coin_image is None:
            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            Coin.coin_image = pygame.image.load(image_path)
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


class Player(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        image_path = arcade.resources.resolve_resource_path(":textures:femalePerson_idle.png")
        image = pygame.image.load(image_path)
        rect = image.get_rect()
        image = pygame.transform.scale(image, (
            int(rect.width * SPRITE_SCALING_PLAYER), int(rect.height * SPRITE_SCALING_PLAYER)))
        self.image = image.convert()
        self.image.set_colorkey(BLACK)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Test(PygamePerfTest):
    name = "collision"

    def __init__(self):
        """ Initializer """
        super().__init__(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            title=SCREEN_TITLE,
        )

    def setup(self):
        # This is a list of every sprite. All blocks and the player block as well.
        self.coin_list = pygame.sprite.Group()
        self.player_list = pygame.sprite.Group()

        # Create the player instance
        self.player = Player()

        self.player.rect.x = random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE)
        self.player.rect.y = random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE)
        self.player.change_x = 3
        self.player.change_y = 5

        self.player_list.add(self.player)

        self.font = pygame.font.SysFont('Calibri', 25, True, False)

    def add_coins(self, amount):

        # Create the coins
        for i in range(amount):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin()

            # Position the coin
            coin.rect.x = random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE)
            coin.rect.y = random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE)

            # Add the coin to the lists
            self.coin_list.add(coin)

    def on_draw(self):
        """ Draw everything """
        self.coin_list.draw(self.window)
        self.player_list.draw(self.window)

    def on_update(self, delta_time):
        # Start update timer
        self.player_list.update()

        if self.player.rect.x < 0 and self.player.change_x < 0:
            self.player.change_x *= -1
        if self.player.rect.y < 0 and self.player.change_y < 0:
            self.player.change_y *= -1

        if self.player.rect.x > SCREEN_WIDTH and self.player.change_x > 0:
            self.player.change_x *= -1
        if self.player.rect.y > SCREEN_HEIGHT and self.player.change_y > 0:
            self.player.change_y *= -1

        coin_hit_list = pygame.sprite.spritecollide(self.player, self.coin_list, False)
        for coin in coin_hit_list:
            coin.rect.x = random.randrange(SCREEN_WIDTH)
            coin.rect.y = random.randrange(SCREEN_HEIGHT)

    def update_state(self):
        # Figure out if we need more coins
        if self.timing.target_n > len(self.coin_list):
            new_coin_amount = self.timing.target_n - len(self.coin_list)
            self.add_coins(new_coin_amount)

"""
Moving Sprite Stress Test

Simple program to test how fast we can draw sprites that are moving

Artwork from http://kenney.nl
"""

# noinspection PyPackageRequirements
import pygame
import random
import os
from performance_timing import PerformanceTiming

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- Constants ---
SPRITE_SCALING_COIN = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)
COIN_COUNT_INCREMENT = 500

STOP_COUNT = 10000
RESULTS_FILE = "../../result_data/pygame/draw_moving_sprites.csv"
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Moving Sprite Stress Test"


class Coin(pygame.sprite.Sprite):
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
        image = pygame.image.load("../resources/coinGold.png")
        rect = image.get_rect()
        image = pygame.transform.scale(
            image,
            (int(rect.width * SPRITE_SCALING_COIN), int(rect.height * SPRITE_SCALING_COIN)))
        self.image = image.convert()
        self.image.set_colorkey(BLACK)

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


class MyGame:
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.coin_list = None

        self.performance_timing = PerformanceTiming(results_file=RESULTS_FILE)

        # Initialize Pygame
        pygame.init()

        # Set the height and width of the screen
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        # This is a list of every sprite. All blocks and the player block as well.
        self.coin_list = pygame.sprite.Group()

        self.font = pygame.font.SysFont('Calibri', 25, True, False)

    def add_coins(self, coin_amount):

        # Create the coins
        for i in range(coin_amount):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin()

            # Position the coin
            coin.rect.x = random.randrange(SPRITE_SIZE, SCREEN_WIDTH - SPRITE_SIZE)
            coin.rect.y = random.randrange(SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE)

            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.coin_list.add(coin)

    def on_draw(self):
        """ Draw everything """

        # Start timing how long this takes
        self.performance_timing.start_timer('draw')

        # Clear the screen
        self.screen.fill((59, 122, 87))

        # Draw all the spites
        self.coin_list.draw(self.screen)

        pygame.display.flip()

        # Stop timing how long this takes
        self.performance_timing.stop_timer('draw')

    def update(self, _delta_time):
        # Start update timer
        self.performance_timing.start_timer('update')

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

        # Stop timing the update
        self.performance_timing.stop_timer('update')

        # Figure out if we need more coins
        if self.performance_timing.target_n > len(self.coin_list):
            new_coin_amount =  self.performance_timing.target_n - len(self.coin_list)
            self.add_coins(new_coin_amount)

def main():
    """ Main method """
    window = MyGame()

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not window.performance_timing.end_run():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.update(0)
        window.on_draw()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
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
        if Coin.coin_image is None:
            # Create an image of the block, and fill it with a color.
            # This could also be an image loaded from the disk.
            Coin.coin_image = pygame.image.load("../resources/coinGold.png")
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
        image = pygame.image.load("../resources/femalePerson_idle.png")
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

        self.performance_timing = PerformanceTiming(results_file=RESULTS_FILE,
                                                    start_n=0,
                                                    increment_n=200,
                                                    end_time=60)


        # Initialize Pygame
        pygame.init()

        # Set the height and width of the screen
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

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

        # Start timing how long this takes
        self.performance_timing.start_timer('draw')

        # Clear the screen
        self.screen.fill((59, 122, 87))

        # Draw all the spites
        self.coin_list.draw(self.screen)
        self.player_list.draw(self.screen)

        pygame.display.flip()

        # Stop timing how long this takes
        self.performance_timing.stop_timer('draw')

    def update(self, _delta_time):
        # Start update timer
        self.performance_timing.start_timer('update')

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

        # Stop timing the update
        self.performance_timing.stop_timer('update')

        # Figure out if we need more coins
        if self.performance_timing.target_n > len(self.coin_list):
            new_coin_amount = self.performance_timing.target_n - len(self.coin_list)
            self.add_coins(new_coin_amount)


def main():
    """ Main method """
    window = MyGame()

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not window.performance_timing.end_run() and not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.update(0)
        window.on_draw()
        clock.tick(60)

    # Save screenshot
    pygame.image.save(window.screen, RESULTS_IMAGE)

    pygame.quit()


if __name__ == "__main__":
    main()

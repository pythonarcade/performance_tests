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

RESULTS_FILE = "../../result_data/pygame/moving_shapes.csv"
RESULTS_IMAGE = "../../result_data/pygame/moving_shapes.png"
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Pygame - Moving Shapes Stress Test"


class Shape:
    """ Generic base shape class """
    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.delta_angle = delta_angle
        self.color = color

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        self.angle += self.delta_angle
        if self.x < 0 and self.delta_x < 0:
            self.delta_x *= -1
        if self.y < 0 and self.delta_y < 0:
            self.delta_y *= -1
        if self.x > SCREEN_WIDTH and self.delta_x > 0:
            self.delta_x *= -1
        if self.y > SCREEN_HEIGHT and self.delta_y > 0:
            self.delta_y *= -1

class Rectangle(Shape):

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.color, rect)

class Ellipse(Shape):

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(surface, self.color, rect)

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
        self.shape_list = []

        self.performance_timing = PerformanceTiming(results_file=RESULTS_FILE,
                                                    start_n=0,
                                                    increment_n=200,
                                                    end_time=60)


        # Initialize Pygame
        pygame.init()
        pygame.display.set_caption(SCREEN_TITLE)

        # Set the height and width of the screen
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

        # This is a list of every sprite. All blocks and the player block as well.
        self.coin_list = pygame.sprite.Group()

        self.font = pygame.font.SysFont('Calibri', 25, True, False)

    def add_shapes(self, amount):
        for i in range(amount):
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            width = random.randrange(10, 30)
            height = random.randrange(10, 30)
            angle = random.randrange(0, 360)

            d_x = random.randrange(-3, 4)
            d_y = random.randrange(-3, 4)
            d_angle = random.randrange(-3, 4)

            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            # alpha = random.randrange(256)

            shape_type = random.randrange(2)
            shape_type = 0

            if shape_type == 0:
                shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                  d_angle, (red, green, blue))
            elif shape_type == 1:
                shape = Ellipse(x, y, width, height, angle, d_x, d_y,
                            d_angle, (red, green, blue))
            # elif shape_type == 2:
            #     shape = Line(x, y, width, height, angle, d_x, d_y,
            #                  d_angle, (red, green, blue, alpha))

            self.shape_list.append(shape)

    def on_draw(self):
        """ Draw everything """

        # Start timing how long this takes
        self.performance_timing.start_timer('draw')

        # Clear the screen
        self.screen.fill((0, 0, 0))

        for shape in self.shape_list:
            shape.draw(self.screen)

        pygame.display.flip()

        # Stop timing how long this takes
        self.performance_timing.stop_timer('draw')

    def update(self, _delta_time):
        # Start update timer
        self.performance_timing.start_timer('update')

        for shape in self.shape_list:
            shape.move()

        # Stop timing the update
        self.performance_timing.stop_timer('update')

        # Figure out if we need more coins
        if self.performance_timing.target_n > len(self.shape_list):
            new_coin_amount = self.performance_timing.target_n - len(self.shape_list)
            self.add_shapes(new_coin_amount)


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

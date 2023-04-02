"""
Moving Sprites Stress Test
"""

import random
import os
import arcade
import arcade.shape_list
from performance_timing import PerformanceTiming
import pyglet.shapes

# Set up the constants
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Pyglet Moving Shapes"


class MovingEllipse(pyglet.shapes.Rectangle):
    """ Generic base shape class """
    def __init__(self, x, y, a, b, color=(255, 255, 255, 255), batch=None, group=None):
        super().__init__(x, y, a, b, color, batch, group)
        self.delta_x = 0
        self.delta_y = 0
        self.delta_angle = 0
        # Anchor the rotation to the middle of the rectangle, instead of the corner.
        self.anchor_x = a / 2
        self.anchor_y = b / 2

    def move(self):
        # self.x += self.delta_x
        # self.y += self.delta_y
        # self.rotation += self.delta_angle
        # if self.x < 0 and self.delta_x < 0:
        #     self.delta_x *= -1
        # if self.y < 0 and self.delta_y < 0:
        #     self.delta_y *= -1
        # if self.x > SCREEN_WIDTH and self.delta_x > 0:
        #     self.delta_x *= -1
        # if self.y > SCREEN_HEIGHT and self.delta_y > 0:
        #     self.delta_y *= -1

        x, y = self.position
        x += self.delta_x
        y += self.delta_y
        self.position = x, y
        if x < 0 and self.delta_x < 0:
            self.delta_x *= -1
        if y < 0 and self.delta_y < 0:
            self.delta_y *= -1
        if x > SCREEN_WIDTH and self.delta_x > 0:
            self.delta_x *= -1
        if y > SCREEN_HEIGHT and self.delta_y > 0:
            self.delta_y *= -1


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.shape_list = None
        self.batch = pyglet.graphics.Batch()

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.results_file = "../../result_data/pyglet/moving_shapes.csv"
        self.results_image = "../../result_data/pyglet/moving_shapes.png"

        self.performance_timing = PerformanceTiming(results_file=self.results_file,
                                                    start_n=0,
                                                    increment_n=200,
                                                    end_time=60)

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.shape_list = []

    def add_shapes(self, amount):
        for i in range(amount):
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(0, SCREEN_HEIGHT)
            width = random.randrange(10, 30)
            height = random.randrange(10, 30)

            d_x = random.randrange(-3, 4)
            d_y = random.randrange(-3, 4)

            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            # alpha = random.randrange(256)

            shape = MovingEllipse(x, y, width, height,
                                  color=(red, green, blue),
                                  batch=self.batch)
            shape.delta_x = d_x
            shape.delta_y = d_y
            self.shape_list.append(shape)

    def on_update(self, dt):
        """ Move everything """

        # Start update timer
        self.performance_timing.start_timer('update')

        for shape in self.shape_list:
            shape.move()

        # Stop timing the update
        self.performance_timing.stop_timer('update')

        # Figure out if we need more shapes
        if self.performance_timing.target_n > len(self.shape_list):
            new_amount = self.performance_timing.target_n - len(self.shape_list)
            self.add_shapes(new_amount)

        # End the program run
        if self.performance_timing.end_run():
            # Save screenshot
            image = arcade.get_image()
            image.save(self.results_image, 'PNG')
            self.close()

    def on_draw(self):
        """ Render the screen. """
        # Start timing how long this takes
        self.performance_timing.start_timer('draw')

        self.clear()
        self.batch.draw()

        # Stop timing how long this takes
        self.performance_timing.stop_timer('draw')


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

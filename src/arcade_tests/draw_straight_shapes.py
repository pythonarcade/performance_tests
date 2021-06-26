"""
Moving Sprites Stress Test
"""

import random
import os
import arcade
from performance_timing import PerformanceTiming

# Set up the constants
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Arcade - Moving Shapes Non-Buffered"

RECT_WIDTH = 50
RECT_HEIGHT = 50


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


class Ellipse(Shape):

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height,
                                   self.color, self.angle)


class Rectangle(Shape):

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color, self.angle)


class Line(Shape):

    def draw(self):
        arcade.draw_line(self.x, self.y,
                         self.x + self.width, self.y + self.height,
                         self.color, 2)


class ShapeBuffered:
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
        self.shape_list = None

    def move(self):
        self.x += self.delta_x
        self.y += self.delta_y
        if self.delta_angle:
            self.angle += self.delta_angle
        if self.x < 0 and self.delta_x < 0:
            self.delta_x *= -1
        if self.y < 0 and self.delta_y < 0:
            self.delta_y *= -1
        if self.x > SCREEN_WIDTH and self.delta_x > 0:
            self.delta_x *= -1
        if self.y > SCREEN_HEIGHT and self.delta_y > 0:
            self.delta_y *= -1

    def draw(self):
        self.shape_list.center_x = self.x
        self.shape_list.center_y = self.y
        # self.shape_list.angle = self.angle
        self.shape_list.draw()


class EllipseBuffered(ShapeBuffered):

    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):

        super().__init__(x, y, width, height, angle, delta_x, delta_y,
                         delta_angle, color)

        shape = arcade.create_ellipse_filled(0, 0,
                                             self.width, self.height,
                                             self.color, self.angle)
        self.shape_list = arcade.ShapeElementList()
        self.shape_list.append(shape)


class RectangleBuffered(ShapeBuffered):

    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):

        super().__init__(x, y, width, height, angle, delta_x, delta_y,
                         delta_angle, color)

        shape = arcade.create_rectangle_filled(0, 0,
                                               self.width, self.height,
                                               self.color, self.angle)
        self.shape_list = arcade.ShapeElementList()
        self.shape_list.append(shape)


class LineBuffered(ShapeBuffered):

    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):

        super().__init__(x, y, width, height, angle, delta_x, delta_y,
                         delta_angle, color)

        shape = arcade.create_line(0, 0,
                                   self.width, self.height,
                                   self.color, 2)
        self.shape_list = arcade.ShapeElementList()
        self.shape_list.append(shape)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, buffered):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.shape_list = None
        self.buffered = buffered

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        if self.buffered:
            self.results_file = "../../result_data/arcade/moving_shapes_buffered.csv"
            self.results_image = "../../result_data/arcade/moving_shapes_buffered.png"
        else:
            self.results_file = "../../result_data/arcade/moving_shapes_unbuffered.csv"
            self.results_image = "../../result_data/arcade/moving_shapes_unbuffered.png"

        self.performance_timing = PerformanceTiming(results_file=self.results_file,
                                                    start_n=0,
                                                    increment_n=100,
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
            # angle = random.randrange(0, 360)
            angle = 0

            # d_x = random.randrange(-3, 4)
            # d_y = random.randrange(-3, 4)
            d_x = 0
            d_y = 0
            # d_angle = random.randrange(-3, 4)
            d_angle = 0

            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            # alpha = random.randrange(256)
            alpha = 255
            shape_type = random.randrange(1)
            # shape_type = 1

            if not self.buffered:
                if shape_type == 0:
                    shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                      d_angle, (red, green, blue, alpha))
                elif shape_type == 1:
                    shape = Ellipse(x, y, width, height, angle, d_x, d_y,
                                    d_angle, (red, green, blue, alpha))
                elif shape_type == 2:
                    shape = Line(x, y, width, height, angle, d_x, d_y,
                                 d_angle, (red, green, blue, alpha))
            else:
                if shape_type == 0:
                    shape = RectangleBuffered(x, y, width, height, angle, d_x, d_y,
                                              d_angle, (red, green, blue, alpha))
                elif shape_type == 1:
                    shape = EllipseBuffered(x, y, width, height, angle, d_x, d_y,
                                            d_angle, (red, green, blue, alpha))
                elif shape_type == 2:
                    shape = LineBuffered(x, y, width, height, angle, d_x, d_y,
                                         d_angle, (red, green, blue, alpha))

            self.shape_list.append(shape)

    def on_update(self, dt):
        """ Move everything """

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

        # End the program run
        if self.performance_timing.end_run():
            # Save screenshot
            image = arcade.get_image()
            image.save(self.results_image, 'PNG')
            self.close()

    def on_draw(self):
        """
        Render the screen.
        """
        # Start timing how long this takes
        self.performance_timing.start_timer('draw')

        arcade.start_render()

        for shape in self.shape_list:
            shape.draw()

        # Stop timing how long this takes
        self.performance_timing.stop_timer('draw')


def main(buffered):
    window = MyGame(buffered)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    # main(True)
    main(False)

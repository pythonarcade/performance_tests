import random

from arcade_perf.tests.base import ArcadePerfTest
import arcade

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

        shape = arcade.shape_list.create_rectangle_filled(0, 0,
                                               self.width, self.height,
                                               self.color, self.angle)
        self.shape_list = arcade.shape_list.ShapeElementList()
        self.shape_list.append(shape)


class LineBuffered(ShapeBuffered):

    def __init__(self, x, y, width, height, angle, delta_x, delta_y,
                 delta_angle, color):

        super().__init__(x, y, width, height, angle, delta_x, delta_y,
                         delta_angle, color)

        shape = arcade.shape_list.create_line(0, 0,
                                   self.width, self.height,
                                   self.color, 2)
        self.shape_list = arcade.shape_list.ShapeElementList()
        self.shape_list.append(shape)


class Test(ArcadePerfTest):
    name = "moving-shapes"
    instances = [
        ({"mode": "buffered"}, "Shapes Unbuffered"),
        ({"mode": "unbuffered"}, "Shapes buffered"),
    ]

    def __init__(self, mode: str = "buffered"):
        super().__init__(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            title=SCREEN_TITLE,
            start_count=0,
            increment_count=20,
            duration=60.0,
        )
        self.shape_list = None
        self.buffered = True if mode == "buffered" else False
        self.name = f"{self.name}-{mode}"

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

            d_x = random.randrange(-3, 4)
            d_y = random.randrange(-3, 4)
            # d_angle = random.randrange(-3, 4)
            d_angle = 0

            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            alpha = random.randrange(256)

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
        for shape in self.shape_list:
            shape.move()

    def update_state(self):
        # Figure out if we need more coins
        if self.timing.target_n > len(self.shape_list):
            new_coin_amount = self.timing.target_n - len(self.shape_list)
            self.add_shapes(new_coin_amount)

    def on_draw(self):
        for shape in self.shape_list:
            shape.draw()

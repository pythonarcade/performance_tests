import random
import arcade
import arcade.shape_list
from arcade_perf.tests.base import ArcadePerfTest

# Set up the constants
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Arcade - Moving Shapes"

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

    def get_shape(self):
        shape = arcade.shape_list.create_ellipse_filled(self.x, self.y,
                                             self.width, self.height,
                                             self.color, self.angle)
        return shape


class Rectangle(Shape):

    def get_shape(self):
        shape = arcade.shape_list.create_rectangle_filled(self.x, self.y,
                                               self.width, self.height,
                                               self.color, self.angle)
        return shape



class Test(ArcadePerfTest):
    name = "moving-shapes2"
    instances = [
        ({"mode": "buffered"}, "Unbuffered"),
        ({"mode": "unbuffered"}, "Buffered"),
    ]

    def __init__(self, mode: str):
        super().__init__(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            title=SCREEN_TITLE,
            start_count=0,
            increment_count=20,
            duration=60,
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
            angle = random.randrange(0, 360)

            d_x = random.randrange(-3, 4)
            d_y = random.randrange(-3, 4)
            d_angle = random.randrange(-3, 4)

            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            alpha = random.randrange(256)

            shape_type = random.randrange(2)
            # shape_type = 1

            if shape_type == 0:
                shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                  d_angle, (red, green, blue, alpha))
            elif shape_type == 1:
                shape = Ellipse(x, y, width, height, angle, d_x, d_y,
                            d_angle, (red, green, blue, alpha))

            self.shape_list.append(shape)

    def on_update(self, dt):
        for shape in self.shape_list:
            shape.move()

    def update_state(self):
        if self.timing.target_n > len(self.shape_list):
            new_coin_amount = self.timing.target_n - len(self.shape_list)
            self.add_shapes(new_coin_amount)

    def on_draw(self):
        self.window.clear()

        shape_element_list = arcade.shape_list.ShapeElementList()
        for shape in self.shape_list:
            shape_element_list.append(shape.get_shape())

        shape_element_list.draw()

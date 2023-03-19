import random
import pyglet.shapes
from arcade_perf.tests.arcade.moving_sprites import ArcadePerfTest

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
        self.rotation += self.delta_angle
        if x < 0 and self.delta_x < 0:
            self.delta_x *= -1
        if y < 0 and self.delta_y < 0:
            self.delta_y *= -1
        if x > SCREEN_WIDTH and self.delta_x > 0:
            self.delta_x *= -1
        if y > SCREEN_HEIGHT and self.delta_y > 0:
            self.delta_y *= -1


class Test(ArcadePerfTest):
    """ Main application class. """
    type = "pyglet"
    name = "moving-shapes"

    def __init__(self):
        super().__init__(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT), 
            title=SCREEN_TITLE,
            start_count=0,
            increment_count=1,
            duration=60,
        )

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.batch = pyglet.graphics.Batch()
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

            shape = MovingEllipse(x, y, width, height,
                                  color=(red, green, blue, alpha),
                                  batch=self.batch)
            shape.rotation = angle
            shape.delta_x = d_x
            shape.delta_y = d_y
            shape.delta_angle = d_angle
            self.shape_list.append(shape)

    def on_update(self, dt):
        for shape in self.shape_list:
            shape.move()

    def on_draw(self):
        self.batch.draw()

    def update_state(self):
        # Figure out if we need more shapes
        if self.timing.target_n > len(self.shape_list):
            new_amount = self.timing.target_n - len(self.shape_list)
            self.add_shapes(new_amount)

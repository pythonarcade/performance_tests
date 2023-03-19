# noinspection PyPackageRequirements
import pygame
import random
from arcade_perf.tests.base import PygamePerfTest

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- Constants ---
SPRITE_SCALING_COIN = 0.25
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING_COIN)

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
        self.orig_image = pygame.Surface((width , height))
        self.orig_image.fill(color)

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
        image = self.orig_image.copy()
        image.set_colorkey(BLACK)
        rotated_image = pygame.transform.rotate(image, self.angle)
        surface.blit(rotated_image, (self.x, self.y))


class Ellipse(Shape):

    def draw(self, surface):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.ellipse(surface, self.color, rect)


class Test(PygamePerfTest):
    name = "moving-shapes"

    def __init__(self):
        super().__init__(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
            title=SCREEN_TITLE,
            start_count=0,
            increment_count=100,
            duration=60,
        )

    def setup(self):
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

            # d_x = 0
            # d_y = 0
            # d_angle = 0

            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            # alpha = random.randrange(256)
            alpha = 255

            shape_type = random.randrange(1)
            # shape_type = 0

            if shape_type == 0:
                shape = Rectangle(x, y, width, height, angle, d_x, d_y,
                                  d_angle, (red, green, blue, alpha))
            elif shape_type == 1:
                shape = Ellipse(x, y, width, height, angle, d_x, d_y,
                            d_angle, (red, green, blue, alpha))
            # elif shape_type == 2:
            #     shape = Line(x, y, width, height, angle, d_x, d_y,
            #                  d_angle, (red, green, blue, alpha))

            self.shape_list.append(shape)

    def on_draw(self):
        for shape in self.shape_list:
            shape.draw(self.window)

    def on_update(self, _delta_time):
        for shape in self.shape_list:
            shape.move()

    def update_state(self):
        # Figure out if we need more coins
        if self.timing.target_n > len(self.shape_list):
            amount = self.timing.target_n - len(self.shape_list)
            self.add_shapes(amount)

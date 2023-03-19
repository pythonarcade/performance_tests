import arcade
from .moving_sprites import Test as MovingSpritesTest


class Coin(arcade.BasicSprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """
        Update the sprite.
        """
        self.position = (
            self.position[0] + self.change_x,
            self.position[1] + self.change_y,
        )


class Test(MovingSpritesTest):
    name = "moving-sprites-basic"
    coin_cls = Coin

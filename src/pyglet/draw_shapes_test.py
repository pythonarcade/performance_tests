import pyglet
from pyglet import shapes
import arcade

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(800, 600, "Hi")

        self.batch = pyglet.graphics.Batch()

        circle = shapes.Circle(700, 150, 100, color=(50, 225, 30), batch=self.batch)
        square = shapes.Rectangle(200, 200, 200, 200, color=(55, 55, 255), batch=self.batch)
        rectangle = shapes.Rectangle(250, 300, 400, 200, color=(255, 22, 20), batch=self.batch)
        rectangle.opacity = 128
        rectangle.rotation = 33
        line = shapes.Line(100, 100, 100, 200, width=19, batch=self.batch)
        line2 = shapes.Line(150, 150, 444, 111, width=4, color=(200, 20, 20), batch=self.batch)
        star = shapes.Star(800, 400, 60, 40, num_spikes=20, color=(255, 255, 0), batch=self.batch)

    def on_draw(self):
        self.clear()
        self.batch.draw()

def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
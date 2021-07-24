"""
Developer Tag: Davis-52
Creation Date: 23-JUL-2021
Last Modified: 23-JUL-2021
Source Credit: Paul Vincent Craven (Python Arcade Academy)
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLUE)

        # Sprite list variables here, set to None

    def setup(self):
        """ Set up game variables. Call to restart game. """
        # Create sprites and sprite lists here
        pass

    def on_draw(self):
        """ Render graphics to screen. """
        arcade.start_render()

        # Call draw() method of sprite lists here

    def on_update(self, delta_time):
        """ Holds movement and game logic. """

        # Call update() method of sprite lists here
        pass

    def on_key_press(self, key, key_modifiers):
        """ Respond to keyboard key-press. """
        pass

    def on_key_release(self, key, key_modifiers):
        """ Respond to keyboard key-release. """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Respond to mouse movement. """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Respond to mouse key-press. """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """ Respond to mouse key-release. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

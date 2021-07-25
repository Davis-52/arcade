"""
Developer Tag: Davis-52
Creation Date: 24-JUL-2021
Last Modified: 24-JUL-2021
Source Credit: Paul Vincent Craven (Python Arcade Academy)
"""
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Simple Platformer"

CHARACTER_IMAGE = "images/blue-collar-zombie-large.png"
GRASS_IMAGE = "images/ground-tile.png"
CRATE_IMAGE = "images/crate-tile.png"
COIN_IMAGE = ""
CHARACTER_SCALING = 4.0/3.0
TILE_SCALING = 4.0/3.0
COIN_SCALING = 4.0/3.0


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.DARK_VIOLET)

        # Sprite list variables
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Player character variable
        self.player_sprite = None

    def setup(self):
        """ Set up game variables. Call to restart game. """
        # Create sprite lists
        self.player_list = arcade.SpriteList()
        # Note: spatial hashing speeds collision-finding time,
        # but slows sprite movement time
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list = arcade.SpriteList(use_spatial_hash=True)

        # Setup player character
        self.player_sprite = arcade.Sprite(CHARACTER_IMAGE, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)

        # Add grass
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(GRASS_IMAGE, TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Add crates
        for coordinate in [[512, 96], [256, 96], [768, 96]]:
            wall = arcade.Sprite(CRATE_IMAGE, TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

    def on_draw(self):
        """ Render graphics to screen. """
        arcade.start_render()

        # Call draw() method of sprite lists here
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

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
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

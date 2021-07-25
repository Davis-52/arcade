"""
Developer Tag: Davis-52
Creation Date: 24-JUL-2021
Last Modified: 24-JUL-2021
Source Credit: Paul Vincent Craven (Python Arcade Library)
"""
import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
SCREEN_TITLE = "Sprite Player Movement - Sprite Textures"

SPRITE_SCALING_PLAYER = 1.0
SPRITE_SETUP_CENTER_X_PLAYER = 50
SPRITE_SETUP_CENTER_Y_PLAYER = 50
SPRITE_SPEED_PLAYER = 2


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Sprite list variables here, set to None
        self.player_list = None

        # Player info here, set sprite to None
        self.player_sprite = None

        # Keyboard info here
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        arcade.set_background_color(arcade.color.LEMON_LIME)

    def setup(self):
        """ Set up game variables. Call to restart game. """
        # Create sprites and sprite lists here
        self.player_list = arcade.SpriteList()

        # Player setup here
        self.player_sprite = arcade.Sprite()
        self.player_sprite.scale = SPRITE_SCALING_PLAYER
        self.player_sprite.center_x = SPRITE_SETUP_CENTER_X_PLAYER
        self.player_sprite.center_y = SPRITE_SETUP_CENTER_Y_PLAYER
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_sprite.textures = {
            'up': arcade.load_texture("images/blue-collar-zombie-up.png"),
            'down': arcade.load_texture("images/blue-collar-zombie-down.png"),
            'left': arcade.load_texture("images/blue-collar-zombie-left.png"),
            'right': arcade.load_texture("images/blue-collar-zombie-right.png")}
        self.player_sprite.texture = self.player_sprite.textures['down']
        self.player_list.append(self.player_sprite)

        # Keyboard setup here
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def on_activate(self):
        """ Window comes into focus. """
        pass

    def on_deactivate(self):
        """ Window goes out of focus. """
        # Nullify keyboard input
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

    def on_draw(self):
        """ Render graphics to screen. """
        arcade.start_render()

        # Call draw() method of sprite lists here
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Holds movement and game logic. """
        # Update change_x and change_y
        acceleration_x = 0
        acceleration_y = 0

        if self.left_pressed:
            acceleration_x -= SPRITE_SPEED_PLAYER
        if self.right_pressed:
            acceleration_x += SPRITE_SPEED_PLAYER
        if self.up_pressed:
            acceleration_y += SPRITE_SPEED_PLAYER
        if self.down_pressed:
            acceleration_y -= SPRITE_SPEED_PLAYER

        self.player_sprite.change_x = acceleration_x
        self.player_sprite.change_y = acceleration_y

        # Update facing direction
        if self.player_sprite.change_x < 0:
            self.player_sprite.texture = self.player_sprite.textures['left']
        elif self.player_sprite.change_x > 0:
            self.player_sprite.texture = self.player_sprite.textures['right']
        else:
            if self.player_sprite.change_y > 0:
                self.player_sprite.texture = self.player_sprite.textures['up']
            elif self.player_sprite.change_y < 0:
                self.player_sprite.texture = self.player_sprite.textures['down']

        # Call update() method of sprite lists here
        self.player_list.update()

    def on_key_press(self, key, key_modifiers):
        """ Respond to keyboard key-press. """
        if key == arcade.key.A:
            self.left_pressed = True
        if key == arcade.key.D:
            self.right_pressed = True
        if key == arcade.key.W:
            self.up_pressed = True
        if key == arcade.key.S:
            self.down_pressed = True

    def on_key_release(self, key, key_modifiers):
        """ Respond to keyboard key-release. """
        if key == arcade.key.A:
            self.left_pressed = False
        if key == arcade.key.D:
            self.right_pressed = False
        if key == arcade.key.W:
            self.up_pressed = False
        if key == arcade.key.S:
            self.down_pressed = False

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


if __name__ == "__main__":
    main()

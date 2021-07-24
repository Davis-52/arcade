"""
Developer Tag: Davis-52
Creation Date: 24-JUL-2021
Last Modified: 24-JUL-2021
Source Credit: Paul Vincent Craven (Python Arcade Library)
"""
import arcade

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
SCREEN_TITLE = "Sprite Player Movement - Mouse Path"

SPRITE_IMAGE_PLAYER = "images/blue-collar-zombie.png"
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

        arcade.set_background_color(arcade.color.LEMON_LIME)

    def setup(self):
        """ Set up game variables. Call to restart game. """
        # Create sprites and sprite lists here
        self.player_list = arcade.SpriteList()

        # Player setup here
        self.player_sprite = arcade.Sprite(SPRITE_IMAGE_PLAYER, SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = SPRITE_SETUP_CENTER_X_PLAYER
        self.player_sprite.center_y = SPRITE_SETUP_CENTER_Y_PLAYER
        self.player_sprite.destination_x = SPRITE_SETUP_CENTER_X_PLAYER
        self.player_sprite.destination_y = SPRITE_SETUP_CENTER_Y_PLAYER
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """ Render graphics to screen. """
        arcade.start_render()

        # Call draw() method of sprite lists here
        self.player_list.draw()

    def on_update(self, delta_time):
        while self.player_sprite.destination_x % SPRITE_SPEED_PLAYER != 0:
            self.player_sprite.destination_x += 1
        while self.player_sprite.destination_y % SPRITE_SPEED_PLAYER != 0:
            self.player_sprite.destination_y += 1

        """ Holds movement and game logic. """
        # move x, then y
        self.player_sprite.change_x = 0
        change_x = False
        if self.player_sprite.destination_x > self.player_sprite.center_x:
            self.player_sprite.change_x = SPRITE_SPEED_PLAYER
            change_x = True
        elif self.player_sprite.destination_x < self.player_sprite.center_x:
            self.player_sprite.change_x = -SPRITE_SPEED_PLAYER
            change_x = True

        # move y after x
        self.player_sprite.change_y = 0
        if not change_x:
            if self.player_sprite.destination_y > self.player_sprite.center_y:
                self.player_sprite.change_y = SPRITE_SPEED_PLAYER
            elif self.player_sprite.destination_y < self.player_sprite.center_y:
                self.player_sprite.change_y = -SPRITE_SPEED_PLAYER

        # Call update() method of sprite lists here
        self.player_list.update()

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
        self.player_sprite.destination_x = x
        self.player_sprite.destination_y = y


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

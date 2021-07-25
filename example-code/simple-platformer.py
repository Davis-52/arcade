"""
Developer Tag: Davis-52
Creation Date: 24-JUL-2021
Last Modified: 24-JUL-2021
Source Credit: Paul Vincent Craven (Python Arcade Academy)
Sound Files:
  Caroline Ford (SoundBible, 'Eat Chips-SoundBible.com-1842806405')
  dklon (OpenGameArt, 'jump_11-Platformer Jumping Sounds')
"""
import arcade

# Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Simple Platformer"

# Viewport
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 50
TOP_VIEWPORT_MARGIN = 100

# World
GRAVITY = 5

# Character
CHARACTER_IMAGE = "images/blue-collar-zombie-large.png"
CHARACTER_SCALING = 4.0/3.0
CHARACTER_SPEED = 6
CHARACTER_JUMP_SOUND = "sounds/jump-11.wav"
CHARACTER_JUMP_SPEED = 12
CHARACTER_JUMP_LIMIT = 192

# Tiles
GRASS_IMAGE = "images/ground-tile.png"
CRATE_IMAGE = "images/crate-tile.png"
TILE_SCALING = 4.0/3.0

# Collectables
COIN_IMAGE = "images/brain-collectable.png"
COIN_COLLECT_SOUND = "sounds/eat-chips.mp3"
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

        # Keyboard input variables
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Physics engine variable
        self.physics_engine = None

        # Viewport scrolling variables
        self.view_bottom = 0
        self.view_left = 0

        # Load sounds
        self.collect_coin_sound = arcade.load_sound(COIN_COLLECT_SOUND)
        self.jump_sound = arcade.load_sound(CHARACTER_JUMP_SOUND)

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
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_list.append(self.player_sprite)
        self.player_list.jump_height = 0

        # Add grass
        for x in range(0, 1250+256, 64):
            wall = arcade.Sprite(GRASS_IMAGE, TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        # Add crates
        for coordinate in [[512, 96], [256, 96], [768, 96]]:
            wall = arcade.Sprite(CRATE_IMAGE, TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        # Add coins
        for x in range(256+128, 1250+512, 256):
            coin = arcade.Sprite(COIN_IMAGE, COIN_SCALING)
            coin.center_x = x
            coin.center_y = 96
            self.coin_list.append(coin)

        # Reset keyboard input
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False

        # Setup physics engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

        # Reset viewport
        self.view_bottom = 0
        self.view_left = 0

    def on_activate(self):
        """ Window comes into focus. """
        pass

    def on_deactivate(self):
        """ Window goes out of focus. """
        # Nullify keyboard input
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False

    def on_draw(self):
        """ Render graphics to screen. """
        arcade.start_render()

        # Call draw() method of sprite lists here
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        """ Holds movement and game logic. """
        # Viewport scrolling
        changed = False

        left_bound = self.view_left + LEFT_VIEWPORT_MARGIN
        right_bound = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        top_bound = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        bottom_bound = self.view_bottom + BOTTOM_VIEWPORT_MARGIN

        if self.player_sprite.left < left_bound:
            self.view_left -= left_bound - self.player_sprite.left
            changed = True
        if self.player_sprite.right > right_bound:
            self.view_left += self.player_sprite.right - right_bound
            changed = True
        if self.player_sprite.top > top_bound:
            self.view_bottom += self.player_sprite.top - top_bound
            changed = True
        if self.player_sprite.bottom < bottom_bound:
            self.view_bottom -= bottom_bound - self.player_sprite.bottom
            changed = True

        if changed:
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            arcade.set_viewport(self.view_left, SCREEN_WIDTH + self.view_left,
                                self.view_bottom, SCREEN_HEIGHT + self.view_bottom)

        # Character movement
        acceleration_x = 0
        acceleration_y = 0

        if self.left_pressed:
            acceleration_x -= CHARACTER_SPEED
        if self.right_pressed:
            acceleration_x += CHARACTER_SPEED
        if self.up_pressed:
            if self.player_list.jump_height < CHARACTER_JUMP_LIMIT:
                acceleration_y += CHARACTER_JUMP_SPEED
                self.player_list.jump_height += acceleration_y
        else:
            self.player_list.jump_height = 0
            self.up_pressed = False

        self.player_sprite.change_x = acceleration_x
        self.player_sprite.change_y = acceleration_y

        # Call physics engine updates
        self.physics_engine.update()

        # Coin collisions
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)

    def on_key_press(self, key, key_modifiers):
        """ Respond to keyboard key-press. """
        if key == arcade.key.A:
            self.left_pressed = True
        if key == arcade.key.D:
            self.right_pressed = True
        if key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.up_pressed = True
                arcade.play_sound(self.jump_sound)

    def on_key_release(self, key, key_modifiers):
        """ Respond to keyboard key-release. """
        if key == arcade.key.A:
            self.left_pressed = False
        if key == arcade.key.D:
            self.right_pressed = False
        if key == arcade.key.W:
            self.up_pressed = False

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

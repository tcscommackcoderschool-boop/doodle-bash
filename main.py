import arcade
import os


this_folder = os.path.dirname(__file__)

#
#
def main():
    """ Creates a Window for the game """

    # The Window for this game
    window = arcade.Window(*arcade.get_display_size(), fullscreen=True)
    
    # A View inside of the Window
    game_view = GameView()
    
    
    # Show the View
    window.show_view(game_view)


    # Run the game
    arcade.run()



class GameView(arcade.View):
    """ Represents a view inside of a Window """

    def __init__(self):
        """ Handles what to do when this view is created """
        super().__init__()

        
        
    # 
    #
    def on_show_view(self):
        """ Handles what to do when the window switches to this view """
        self.background_color = arcade.color.AMAZON
        self.map = arcade.TileMap(os.path.join(this_folder, "assets", "doodle land war.tmx"), use_spatial_hash=True)
        player_spawn = self.map.sprite_lists["spawn point player"][0].position


        self.player = arcade.Sprite(":resources:/images/enemies/bee.png")
        self.player.position = player_spawn
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)


        self.keys = set()

        self.camera = arcade.Camera2D()
        
    #
    #
    def on_hide_view(self):
        """ Handles what to do when the window switches away from this view """
        
        
    #
    #
    def on_draw(self):
        """ Handles drawing object each frame """

        self.clear()
        self.camera.use()
        
        for layer in self.map.sprite_lists:
            if layer != "gravity changing background":
                self.map.sprite_lists[layer].draw()
        self.player_list.draw()


        
    #
    #
    def on_update(self, delta_time):
        """ Handles updating objects each frame """
        if arcade.key.W in self.keys:
            self.player.center_y += 10
        if arcade.key.A in self.keys:
            self.player.center_x -= 10
        if arcade.key.S in self.keys:
            self.player.center_y -= 10
        if arcade.key.D in self.keys:
            self.player.center_x += 10

        self.camera.position = self.player.position
        
        
    #
    #
    def on_key_press(self, symbol: int, modifiers: int):
        """ Handles what to do when a key is initially pressed """
        self.keys.add(symbol)
        
        
    #
    #
    def on_key_release(self, symbol: int, modifiers: int):
        """ Handles what to do when a key is released. See arcade.key """
        self.keys.discard(symbol)

        
    #
    #
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        """ Handles what to do when the mouse is moved. See arcade.key """
        
        
    #
    #
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """ Handles what to do when a button on the mouse is pressed. """
        
        
    #
    #
    def on_mouse_released(self, x: int, y: int, button: int, modifiers: int):
        """ Handles what to do when a button on the mouse is released """
        
        
    #
    #
    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        """ Handles what to do when the scroll wheel is used """
        
        
    #
    #
    def on_mouse_enter(self, x: int, y: int):
        """ Handles what to do when the mouse enters the window area """
        
        
    #
    #
    def on_mouse_leave(self, x: int, y: int):
        """ Handles what to do when the mouse leaves the window area """
        
        
        
        
        





    
#
#
if __name__ == "__main__":
    main()














































































































































































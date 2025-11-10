#группа ПК211
import arcade

SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Первый платформер!'
GRAVITY = 1


class MyApp(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.state = 0
        self.key_counter = 0
        self.player_sprite = None
        self.player_lst = None
        self.ground_list = None
        self.ground_Sprite = None
        self.keys_lst = None

    def setup(self):
        texture3 = arcade.load_texture(":resources:images/alien/alienBlue_front.png")
        self.player_sprite = arcade.Sprite(texture3, scale=0.2)
        self.player_sprite.position = [32,32+84]
        
        self.state = 0
        self.key_counter = 0
        arcade.set_background_color(arcade.color.ELECTRIC_BLUE)
        self.title_text = arcade.Text("Первый платформер",
                                      0,
                                      SCREEN_HEIGHT/2,
                                      arcade.color.APRICOT,
                                      30,
                                      width=SCREEN_WIDTH,
                                      align='center'
                                      )
        self.start_text = arcade.Text("ENTER Тык!!!",
                                      0,
                                      SCREEN_HEIGHT/3,
                                      arcade.color.BRONZE,
                                      30,
                                      width=SCREEN_WIDTH,
                                      align='left')
        self.exit_text = arcade.Text("ESC ЖМЯК!!!",
                                      0,
                                      SCREEN_HEIGHT/3,
                                      arcade.color.BRONZE,
                                      30,
                                      width=SCREEN_WIDTH,
                                      align='right')
        self.key_counter_text = arcade.Text("Ключей: ",20,680,font_size=24)
        
        layers = {
            'coins':{"use_spartial_hash":False},
            'walls':{"use_spartial_hash":True},
            'background2':{"use_spartial_hash":False},
            'background1':{"use_spartial_hash":False}
        }
        self.tile_map = arcade.load_tilemap(
            'tiled/tiled_prj_pk211/pk211_level.tmx',
            layer_options=layers
        )
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        self.scene.add_sprite("Player",self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
                                                            self.player_sprite, 
                                                            walls= self.scene['walls'], 
                                                            gravity_constant=GRAVITY
                                                            )

    def on_key_press(self, key, modifiers):
        if self.state == 0:
            if key == arcade.key.ENTER:
                self.state = 1
            elif key == arcade.key.ESCAPE:
                arcade.close_window()
        elif self.state == 1:
            if key == arcade.key.UP or key == arcade.key.W:
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = 13
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = -3
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = 3
            if key == arcade.key.TAB:
                self.state = 0
                self.setup()

    def on_key_release(self, key, modifiers):
        if self.state == 1:
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = 0
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = 0

    
    def on_update(self, delta_time):
        self.physics_engine.update()
        
        

    def on_draw(self):
        self.clear()
        if self.state == 0:
            self.title_text.draw()
            self.start_text.draw()
            self.exit_text.draw()
        elif self.state == 1:
            self.scene.draw()
            self.key_counter_text.draw()


game = MyApp()
game.setup()
arcade.run()

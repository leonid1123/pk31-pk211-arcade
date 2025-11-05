import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Платформер группы ПК-41")
        self.state = 0
        self.start_text = None
        self.exit_text = None
        self.title_text = None
        self.ground_texture = None
        self.ground_sprite_list = None
        self.player_texture = None
        self.player_sprite = None
        self.player_sprite_lst = None
        self.physics_engine = None

    def setup(self):
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
        self.start_text = arcade.Text("Для начала нажмите ENTER",0,SCREEN_HEIGHT/3,
                                      arcade.color.AERO_BLUE,30,width=SCREEN_WIDTH,align='left')
        self.exit_text = arcade.Text("Для выхода нажмите ESC",0,SCREEN_HEIGHT/3,
                                      arcade.color.AERO_BLUE,30,width=SCREEN_WIDTH,align='right')
        self.title_text = arcade.Text("Платформер!",
                                      10,
                                      SCREEN_HEIGHT*2/3,
                                      arcade.color.CADMIUM_RED,
                                      30,
                                      width=SCREEN_WIDTH,
                                      align='center')
        layers = {
            "spikes": {"use_spartial_hash":False},
            "walls": {"use_spartial_hash":True},
            "background": {"use_spartial_hash":False},
            "background_far": {"use_spartial_hash":False}
        }
        self.tile_map = arcade.load_tilemap(
            "D:/share/prj/безымянный.tmx",
            layer_options=layers
            )
        self.scene = arcade.Scene.from_tilemap(self.tile_map)


        

        self.player_texture = arcade.load_texture(":resources:images/alien/alienBlue_front.png")
        self.player_sprite = arcade.Sprite(self.player_texture,scale=0.5)
        self.player_sprite.position = [100,200]
        """self.player_sprite_lst = arcade.SpriteList()
        self.player_sprite_lst.append(self.player_sprite)"""
        self.scene.add_sprite("Player",self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
                                                            self.player_sprite, 
                                                            walls=self.scene['walls'], 
                                                            gravity_constant=1
                                                            )

    def on_key_press(self, key, modifiers):
        if self.state == 0:
            if key == arcade.key.ENTER:
                self.state = 1
            elif key == arcade.key.ESCAPE and self.state == 0:
                arcade.close_window()
        elif self.state == 1:
            if key == arcade.key.W or key == arcade.key.UP:
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = 13
            if key == arcade.key.A or key == arcade.key.LEFT:
                self.player_sprite.change_x = -5
            if key == arcade.key.D or key == arcade.key.RIGHT:
                self.player_sprite.change_x = 5
            if key == arcade.key.ESCAPE:
                self.setup()

    def on_key_release(self, key, modifiers):
        if self.state == 1:
            if key in [arcade.key.A, arcade.key.D,arcade.key.LEFT,arcade.key.RIGHT]:
                self.player_sprite.change_x = 0


    def on_update(self, delta_time):
        self.physics_engine.update()

    def on_draw(self):
        self.clear()
        if self.state == 0:
            self.title_text.draw()
            self.exit_text.draw()
            self.start_text.draw()
        elif self.state == 1:
            #self.player_sprite_lst.draw()
            self.scene.draw()


game = MyGame()
game.setup()
arcade.run()

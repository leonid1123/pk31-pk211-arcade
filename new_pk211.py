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
        texture1 = arcade.load_texture(":resources:images/tiles/grassMid.png")
        texture2 = arcade.load_texture(":resources:images/tiles/rock.png")
        texture3 = arcade.load_texture(":resources:images/alien/alienBlue_front.png")
        texture4 = arcade.load_texture(":resources:images/items/keyBlue.png")
        

        self.player_sprite = arcade.Sprite(texture3, scale=0.5)
        self.player_sprite.position = [32,32+84]
        self.player_lst = arcade.SpriteList()
        self.player_lst.append(self.player_sprite)

        self.ground_list = arcade.SpriteList()
        k=0
        while k <= 38:
            self.ground_Sprite = arcade.Sprite(texture1, scale=0.5)
            self.ground_Sprite.center_x = 32+32*k
            self.ground_Sprite.center_y = 32
            self.ground_list.append(self.ground_Sprite)
            k = k + 2

        coordinate_list = [[256, 96], [512, 96+64] ,[768, 96+2*64]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite(texture2, scale=0.5)
            wall.position = coordinate
            self.ground_list.append(wall)

        self.keys_lst = arcade.SpriteList()
        keys_coordinates = [[200,200],[400,400],[600,400],[800,480]]
        for coords in keys_coordinates:
            key = arcade.Sprite(texture4, scale=0.5)
            key.position = coords
            self.keys_lst.append(key)
            
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
        self.physics_engine = arcade.PhysicsEnginePlatformer(
                                                            self.player_sprite, 
                                                            walls= self.ground_list, 
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
                    self.player_sprite.change_y = 20
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = -5
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = 5
            if key == arcade.key.TAB:#пауза, а должен быть перезапуск
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
        key_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, 
            self.keys_lst
        )
        for item in key_hit_list:
            item.remove_from_sprite_lists()
            self.key_counter += 1
            self.key_counter_text.text = f"Ключей: {self.key_counter}"

        if self.player_sprite.center_x <20:
            self.player_sprite.change_x = 0.5
        if self.player_sprite.center_x >1200:
            self.player_sprite.change_x = -0.5
        

    def on_draw(self):
        self.clear()
        if self.state == 0:
            self.title_text.draw()
            self.start_text.draw()
            self.exit_text.draw()
        elif self.state == 1:
            self.ground_list.draw()
            self.player_lst.draw()
            self.keys_lst.draw()
            self.key_counter_text.draw()


game = MyApp()
game.setup()
arcade.run()

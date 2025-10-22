import arcade
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Платформер"
TILE_SCALING = 0.5
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)
        self.lvl = 0
        self.coins = 0
        self.player_texture = None
        self.player_sprite = None
        self.player_list = None
        self.coin_texture = None
        self.coin_sprite = None
        self.coin_list = None
        self.wall_list = None
        
        

    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.player_texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list = arcade.SpriteList()

        self.player_list.append(self.player_sprite)

        self.coin_texture = arcade.load_texture(":resources:images/items/coinBronze.png", )
        self.coin_sprite = arcade.Sprite(self.coin_texture, scale=0.5)
        self.coin_sprite.center_x = 768 
        self.coin_sprite.center_y = 224 + 256

        self.coin_list = arcade.SpriteList(use_spatial_hash=True)
        self.coin_list.append(self.coin_sprite)

        self.lvl = 0
        self.coins = 0
        self.title = arcade.Text("Стартовая игра", 0, SCREEN_HEIGHT/1.8,
        arcade.color.WHITE,width=SCREEN_WIDTH, font_size=30, align="center")
        self.start_game = arcade.Text("Нажмите ENTER для начала",0,SCREEN_HEIGHT/3
                                      ,arcade.color.AIR_SUPERIORITY_BLUE,
                                      font_size=30, align="right", width=SCREEN_WIDTH) 
        self.exit_game = arcade.Text('Для выхода нажмите Esc',0,SCREEN_HEIGHT/3,
                                     arcade.color.AIR_SUPERIORITY_BLUE, align='left',
                                     width=SCREEN_WIDTH, font_size=30)
        self.coin_counter_text = arcade.Text("Монеток:",0,SCREEN_HEIGHT-50, font_size=20, )
        
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        for x in range(0, 1280+64, 64):
            wall = arcade.Sprite(":resources:images/tiles/grassMid.png", scale=TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        coordinate_list = [[256, 96], [512, 96+64] ,[768, 96+2*64]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", scale=TILE_SCALING)
            wall.position = coordinate
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
                                                            self.player_sprite, 
                                                            walls=self.wall_list, 
                                                            gravity_constant=GRAVITY
                                                            )

    def on_update(self, delta_time):
        self.physics_engine.update()
        coin_hit_list = arcade.check_for_collision_with_list(
        self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.coins += 1
            self.coin_counter_text.text = f'Монеток: {self.coins}'

        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.setup()
        if self.player_sprite.center_x < 0:
            self.setup() 


    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            self.setup()
        if self.lvl == 0:
            if key == arcade.key.ENTER:
                print("Игра начинается!")  
                self.lvl = 1
            elif key == arcade.key.ESCAPE:
                arcade.close_window()
        if self.lvl == 1:
            if key == arcade.key.UP or key == arcade.key.W:
                if self.physics_engine.can_jump():
                    self.player_sprite.change_y = PLAYER_JUMP_SPEED
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            if key == arcade.key.ESCAPE:
                arcade.close_window()

    def on_key_release(self, key, modifiers):
        if self.lvl == 1:
            if key == arcade.key.LEFT or key == arcade.key.A:
                self.player_sprite.change_x = 0
            elif key == arcade.key.RIGHT or key == arcade.key.D:
                self.player_sprite.change_x = 0



    def on_draw(self):
        self.clear()
        if self.lvl == 0:
            self.title.draw()
            self.start_game.draw()
            self.exit_game.draw()
        if self.lvl == 1:
            self.wall_list.draw()
            self.player_list.draw()
            self.coin_list.draw()
            self.coin_counter_text.draw()
        

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()

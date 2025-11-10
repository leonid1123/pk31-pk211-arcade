import arcade
#https://opengameart.org
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="Платформер группы ПК-41", center_window=True)
        self.state = 0
        self.start_text = None
        self.exit_text = None
        self.title_text = None
        self.coins_text = None
        self.ground_texture = None
        self.ground_sprite_list = None
        self.player_texture = None
        self.player_sprite = None
        self.player_sprite_lst = None
        self.physics_engine = None
        self.player_HP = None

        self.heart_texture = None
        self.heart_sprite_lst = None
        self.heart_sprite = None

        self.coins = None


    def setup(self):
        self.player_HP = 3
        self.coins = 0
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)
        self.start_text = arcade.Text("Для начала \nнажмите ENTER",0,SCREEN_HEIGHT/3,
                                      arcade.color.AERO_BLUE,
                                      30,
                                      width=SCREEN_WIDTH,
                                      align='left',
                                      multiline=True)
        self.exit_text = arcade.Text("Для выхода \nнажмите ESC",0,SCREEN_HEIGHT/3,
                                      arcade.color.AERO_BLUE,
                                      30,
                                      width=SCREEN_WIDTH,
                                      align='right',
                                      multiline=True)
        self.title_text = arcade.Text("Платформер!",
                                      10,
                                      SCREEN_HEIGHT*2/3,
                                      arcade.color.CADMIUM_RED,
                                      30,
                                      width=SCREEN_WIDTH,
                                      align='center')
        self.coins_text = arcade.Text("Монеток: ",
                                      20,
                                      780,
                                      arcade.color.GOLD_FUSION,
                                      20)
        layers = {
            'coins': {"use_spartial_hash":False},
            "spikes": {"use_spartial_hash":False},
            "walls": {"use_spartial_hash":True},
            "background": {"use_spartial_hash":False},
            "background_far": {"use_spartial_hash":False}
        }
        self.tile_map = arcade.load_tilemap(
            "tiled/безымянный.tmx",
            layer_options=layers
            )
        self.scene = arcade.Scene.from_tilemap(self.tile_map)


        
        self.heart_texture = arcade.load_texture("tiled/heart.png")
        self.heart_sprite_lst = arcade.SpriteList()
        for i in range(0,3):
            self.heart_sprite = arcade.Sprite(self.heart_texture, scale=1.5)
            self.heart_sprite.position = [40+i*30,750]
            self.heart_sprite_lst.append(self.heart_sprite)

        self.player_texture = arcade.load_texture(":resources:images/alien/alienBlue_front.png")
        self.player_sprite = arcade.Sprite(self.player_texture,scale=0.2)
        self.player_sprite.position = [100,200]
        """self.player_sprite_lst = arcade.SpriteList()
        self.player_sprite_lst.append(self.player_sprite)"""
        self.scene.add_sprite("Player",self.player_sprite)
        self.scene.add_sprite_list("Hearts",sprite_list=self.heart_sprite_lst)#тут
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
        pikes_collision = arcade.check_for_collision_with_list(self.player_sprite
                                                               ,self.scene['spikes'])
        if pikes_collision:
            self.player_HP -= 1
            self.player_sprite.change_y = 10
            self.heart_sprite.remove_from_sprite_lists()
            if self.player_HP <=0:
                self.setup()

        coins_collision = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.scene['coins'])
        for coin in coins_collision:
            self.coins += 1
            self.coins_text.text = f"Монеток: {self.coins}"
            coin.remove_from_sprite_lists()

    def on_draw(self):
        self.clear()
        if self.state == 0:
            self.title_text.draw()
            self.exit_text.draw()
            self.start_text.draw()
        elif self.state == 1:
            #self.player_sprite_lst.draw()
            self.scene.draw()
            self.coins_text.draw()


game = MyGame()
game.setup()
arcade.run()

'''
На автомат по двум предметам, всего два студента:
Разработать игру в Arcade по следующим требованиям:
1. Персонаж: ходит, прыгает, есть 3 жизни. Есть анимация хотьбы и прыжка.
2. Уровень: 200х100 спрайтов, спрайты 16х16 или 32х32. Платформы минимум на 4 уровня вверх.
            есть два типа подбираемых предметов. Есть места со сложным доступом.
            есть "опасные места", например пики или лужи с кислотой.
3. Камера: использовать камеру для перемещения за персонажем.
4. Стартовый экран: элементарный с началом игры и выходом из игры
5. Экран окончания игры: по окончанию игры выводить экран с количеством собранных
                         элементов.
'''
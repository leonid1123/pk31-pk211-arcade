import arcade

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, title="ПУПУПУ!!!")
        self.state = 0
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
        
        self.ground_texture = arcade.load_texture(":resources:images/tiles/grassMid.png")

        self.ground_sprite_list = arcade.SpriteList()
        k = 0
        while k <= 18: 
            ground_sprite = arcade.Sprite(self.ground_texture)
            ground_sprite.center_x = 64+64*k
            ground_sprite.center_y = 64
            self.ground_sprite_list.append(ground_sprite)
            k = k + 2

        coordinate_list = [[256, 128+64], [512, 128+64+128] ,[768, 128+64+128*2]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png")
            wall.position = coordinate
            self.ground_sprite_list.append(wall)


    def setup(self):
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.state = 1
        elif key == arcade.key.ESCAPE and self.state == 0:
            arcade.close_window()

    def on_draw(self):
        self.clear()
        if self.state == 0:
            self.title_text.draw()
            self.exit_text.draw()
            self.start_text.draw()
        elif self.state == 1:
            self.ground_sprite_list.draw()


game = MyGame()
game.setup()
arcade.run()

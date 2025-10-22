#группа ПК-31
import arcade
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Платформер'

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,center_window = True)

    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.title_text = arcade.Text("Пора играть!!!",
                                      0,
                                      SCREEN_HEIGHT/2,
                                      arcade.color.WHITE,
                                      30, 
                                      align="center", 
                                      width=SCREEN_WIDTH)
        self.start_text = arcade.Text("Нажмите ENTER чтобы начать",
                                      0,
                                      SCREEN_HEIGHT/3,
                                      arcade.color.AFRICAN_VIOLET,
                                      30, 
                                      width=SCREEN_WIDTH,
                                      align="right")
        self.exit_text = arcade.Text("Нажмите ESC чтобы выйти",
                                     0,
                                     SCREEN_HEIGHT/3,
                                     arcade.color.BLUSH,
                                     30,
                                     width=SCREEN_WIDTH,
                                     align="left")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            print("начинаем")

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()
        self.title_text.draw()
        self.start_text.draw()
        self.exit_text.draw()


game = MyGame()
game.setup()
arcade.run()
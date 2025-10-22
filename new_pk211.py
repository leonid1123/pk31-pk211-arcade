#группа ПК211
import arcade

SCREEN_WIDTH = 1240
SCREEN_HEIGHT = 720
SCREEN_TITLE = 'Первый платформер!'


class MyApp(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)
        self.state = 0
        texture1 = arcade.load_texture(":resources:images/")

    def setup(self):
        self.state = 0
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

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.state = 1
        elif key == arcade.key.ESCAPE:
            arcade.close_window()
    
    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear()
        if self.state == 0:
            self.title_text.draw()
            self.start_text.draw()
            self.exit_text.draw()
        elif self.state == 1:
            pass


game = MyApp()
game.setup()
arcade.run()

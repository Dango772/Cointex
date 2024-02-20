from kivy.app import App
import random
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.start_button = Button(text='Start', on_press=self.switch_to_game)
        self.add_widget(self.start_button)

    def switch_to_game(self, instance):
        self.manager.current = 'game'

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.game_widget = GameCoinWidget()
        self.add_widget(self.game_widget)


def collides(rect1, rect2):
    r1x, r1y = rect1[0]
    r2x, r2y = rect2[0]
    r1w, r1h = rect1[1]
    r2w, r2h = rect2[1]

    return (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y)

class GameCoinWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.move_step, 0)

        self.scorep1 = 0
        self.scorep2 = 0

        self.scorep1_label = Label(text="Score Player 1 : 0", pos=(100, 950), size=(50, 50))
        self.add_widget(self.scorep1_label)

        self.scorep2_label = Label(text="Score Player 2 : 0", pos=(500, 950), size=(50, 50))
        self.add_widget(self.scorep2_label)

        self.timer_label = Label(text="Time: 30", pos=(900, 950), size=(50, 50))
        self.add_widget(self.timer_label)
        self.timer_seconds = 45

        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='GrassMap1.png', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:
            self.hero = Image(source="cat2.png", pos=(250, 250), size=(100, 100))
            self.monster = Image(source="monster.png", pos=(250, 250), size=(100, 100))
            self.coin1 = Image(source="coin1.png", pos=(400, 400), size=(50, 50))
            self.coin2 = Image(source="coin1.png", pos=(400, 400), size=(50, 50))

    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = value

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.pressed_keys:
            self.pressed_keys.remove(text)

    def move_step(self, dt):
        cur_x1 = self.hero.pos[0]
        cur_y1 = self.hero.pos[1]
        step1 = 500 * dt

        # Adjust the hero's position based on key presses
        if 'w' in self.pressed_keys and cur_y1 + step1 + self.hero.height < Window.height:
            cur_y1 += step1

        if 's' in self.pressed_keys and cur_y1 - step1 > 0:
            cur_y1 -= step1

        if 'a' in self.pressed_keys and cur_x1 - step1 > 0:
            cur_x1 -= step1

        if 'd' in self.pressed_keys and cur_x1 + step1 + self.hero.width < Window.width:
            cur_x1 += step1

        self.hero.pos = (cur_x1, cur_y1)

        cur_x2 = self.monster.pos[0]
        cur_y2 = self.monster.pos[1]
        step2 = 500 * dt

        if 'i' in self.pressed_keys and cur_y2 + step2 + self.monster.height < Window.height:
            cur_y2 += step2

        if 'k' in self.pressed_keys and cur_y2 - step2 > 0:
            cur_y2 -= step2

        if 'j' in self.pressed_keys and cur_x2 - step2 > 0:
            cur_x2 -= step2

        if 'l' in self.pressed_keys and cur_x2 + step2 + self.monster.width < Window.width:
            cur_x2 += step2

        self.monster.pos = (cur_x2, cur_y2)

        if collides((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) or collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)):

            if collides ((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) == True :
                self.coin1.pos = (random.randint(0, Window.width - self.coin1.width),
                             random.randint(0, Window.height - self.coin1.height))
            if collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) :
                self.coin2.pos = (random.randint(0, Window.width - self.coin2.width),
                             random.randint(0, Window.height - self.coin2.height))
            
            self.scorep1 += 1
            self.scorep1_label.text = "Score Player 1 : " + str(self.scorep1)

    
        if collides((self.monster.pos, self.monster.size), (self.coin1.pos, self.coin1.size)) or collides((self.monster.pos, self.monster.size), (self.coin2.pos, self.coin2.size)):

            if collides ((self.monster.pos, self.monster.size), (self.coin1.pos, self.coin1.size)) == True :
                self.coin1.pos = (random.randint(0, Window.width - self.coin1.width),
                             random.randint(0, Window.height - self.coin1.height))
            if collides((self.monster.pos, self.monster.size), (self.coin2.pos, self.coin2.size)) :
                self.coin2.pos = (random.randint(0, Window.width - self.coin2.width),
                             random.randint(0, Window.height - self.coin2.height))
                
            self.scorep2 += 1
            self.scorep2_label.text = "Score Player 2 : " + str(self.scorep2)

        if self.timer_seconds == 0 :
            self.display_time_out_message()

    def update_timer(self, dt):
        self.timer_seconds -= 1
        self.timer_label.text = f"Time: {self.timer_seconds}"

        if self.timer_seconds == 0:
            self.timer_event.cancel()  # Stop the timer when it reaches 0

    def display_time_out_message(self):
        content = Label(text="Time Out", font_size=30)
        popup = Popup(title='Game Over', content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

class MyGame(App):
    def build(self):
        self.screen_manager = ScreenManager()

        main_menu = MainMenu(name='main_menu')
        game_screen = GameScreen(name='game')

        self.screen_manager.add_widget(main_menu)
        self.screen_manager.add_widget(game_screen)

        return self.screen_manager

if __name__ == '__main__':
    app = MyGame()
    app.run()
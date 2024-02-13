from kivy.app import App

import random

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label

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

        self.score = 0

        self.score_label = Label(text="Score : 0", pos=(20, 950), size=(50, 50))
        self.add_widget(self.score_label)

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='GrassMap1.png', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:
            self.hero = Image(source="cat2.png", pos=(250, 250), size=(100, 100))
            self.coin = Image(source="coin1.png", pos=(400, 400), size=(50, 50))

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
        cur_x = self.hero.pos[0]
        cur_y = self.hero.pos[1]
        step = 500 * dt

        # Adjust the hero's position based on key presses
        if 'w' in self.pressed_keys and cur_y + step + self.hero.height < Window.height:
            cur_y += step

        if 's' in self.pressed_keys and cur_y - step > 0:
            cur_y -= step

        if 'a' in self.pressed_keys and cur_x - step > 0:
            cur_x -= step

        if 'd' in self.pressed_keys and cur_x + step + self.hero.width < Window.width:
            cur_x += step

        self.hero.pos = (cur_x, cur_y)

        if collides((self.hero.pos, self.hero.size), (self.coin.pos, self.coin.size)):
            self.coin.pos = (random.randint(0, Window.width - self.coin.width),
                             random.randint(0, Window.height - self.coin.height))
            self.score += 1
            self.score_label.text = "Score : " + str(self.score)

class MyGame(App):
    def build(self):
        return GameCoinWidget()

if __name__ == '__main__':
    app = MyGame()
    app.run()

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

kivy.require('2.0.0')  # Update this to the version you have installed


class MarioGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.mario = Rectangle(pos=(0, 0), size=(50, 50))
        #self.add_widget(self.mario)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.mario.pos = (self.mario.pos[0] - 10, self.mario.pos[1])
        elif keycode[1] == 'right':
            self.mario.pos = (self.mario.pos[0] + 10, self.mario.pos[1])
        return True

    def update(self, dt):
        pass


class MarioGameApp(App):
    def build(self):
        return MarioGame()


if __name__ == '__main__':
    MarioGameApp().run()
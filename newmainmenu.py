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

class GameCoinWidget(Widget) :
    pass

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

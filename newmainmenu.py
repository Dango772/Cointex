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


#Class Main Menu
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.single_button = Button(text='Single Player', on_press=self.switch_to_Single)
        self.add_widget(self.single_button)

    def switch_to_Single(self, instance):
        self.manager.current = 'single'


# class GameScreen(Screen):
#     def __init__(self, **kwargs):
#         super(GameScreen, self).__init__(**kwargs)
#         self.game_widget = GameCoinWidget()
#         self.add_widget(self.game_widget)

# class GameCoinWidget(Widget) :
#     pass


#Single Mode
class GameSingleCoinScreen(Screen) :
    def __init__(self, **kwargs):
        super(GameSingleCoinScreen, self).__init__(**kwargs)
        self.single15_button = Button(text='15 seconds', on_press=self.switch_to_Single15)
        self.add_widget(self.single15_button)

    def switch_to_Single15(self, instance):
        self.manager.current = 'single15'

# class GameSingleCoin(Widget) :
#     pass


#Single 15 Mode
class GameSingleCoin15Screen(Screen) :
    def __init__(self, **kw):
        super(GameSingleCoin15Screen, self).__init__(**kw)
        self.game_single_15_widget = GameSingleCoin15()
        self.add_widget(self.game_single_15_widget)

class GameSingleCoin15(Widget) :
    pass

class MyGame(App):
    def build(self):
        self.screen_manager = ScreenManager()

        main_menu = MainMenu(name='main_menu')
        # game_screen = GameScreen(name='game')
        game_single = GameSingleCoinScreen(name='single')
        game_single_15 = GameSingleCoin15Screen(name = 'single15')

        self.screen_manager.add_widget(main_menu)
        # self.screen_manager.add_widget(game_screen)
        self.screen_manager.add_widget(game_single)
        self.screen_manager.add_widget(game_single_15)

        return self.screen_manager

if __name__ == '__main__':
    app = MyGame()
    app.run()

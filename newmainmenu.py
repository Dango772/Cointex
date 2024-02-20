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
from kivy.uix.boxlayout import BoxLayout



#Class Main Menu
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.single_button = Button(text='Single Player', on_press=self.switch_to_Single,size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.single_button)

        self.multi_button = Button(text='Multi Player', on_press=self.switch_to_Multi,size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.multi_button)

        self.add_widget(layout)


    def switch_to_Single(self, instance):
        self.manager.current = 'single'

    def switch_to_Multi(self, instance):
        self.manager.current = 'multi'


#Single Mode
class GameSingleCoinScreen(Screen) :
    def __init__(self, **kwargs):
        super(GameSingleCoinScreen, self).__init__(**kwargs)

        # สร้าง Layout แนวตั้ง
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # สร้างปุ่มแรก
        self.button1 = Button(text='45 Seconds', on_press=self.switch_to_Single45, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.button1)

        # สร้างปุ่มที่สอง
        self.button2 = Button(text='30 Seconds', on_press=self.switch_to_Single30, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.button2)
        
        # สร้างปุ่มที่สาม
        self.button3 = Button(text='15 Seconds', on_press=self.switch_to_Single15, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.button3)

        self.back_button = Button(text='Back', on_press=self.switch_to_previous_screen, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.back_button)

        self.add_widget(layout)


    def switch_to_Single15(self, instance):
        self.manager.current = 'single15'

    def switch_to_Single30(self, instance):
        self.manager.current = 'single30'

    def switch_to_Single45(self, instance):
        self.manager.current = 'single45'

    def switch_to_previous_screen(self, instance):
        self.manager.current = 'main_menu'
        pass


#Single 15 Mode
class GameSingleCoin15Screen(Screen) :
    def __init__(self, **kw):
        super(GameSingleCoin15Screen, self).__init__(**kw)
        self.game_single_15_widget = GameSingleCoin15()
        self.add_widget(self.game_single_15_widget)

class GameSingleCoin15(Widget) :
    pass


#Single 30 Mode
class GameSingleCoin30Screen(Screen) :
    def __init__(self, **kw):
        super(GameSingleCoin30Screen, self).__init__(**kw)
        self.game_single_30_widget = GameSingleCoin30()
        self.add_widget(self.game_single_30_widget)

class GameSingleCoin30(Widget) :
    pass

#Single 45 Mode
class GameSingleCoin45Screen(Screen) :
    def __init__(self, **kw):
        super(GameSingleCoin45Screen, self).__init__(**kw)
        self.game_single_45_widget = GameSingleCoin45()
        self.add_widget(self.game_single_45_widget)

class GameSingleCoin45(Widget) :
    pass


#Muti Mode
class GameMultiCoinScreen(Screen) :
    def __init__(self, **kwargs):
        super(GameSingleCoinScreen, self).__init__(**kwargs)

        # สร้าง Layout แนวตั้ง
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # สร้างปุ่มแรก
        self.button1 = Button(text='45 Seconds', on_press=self.switch_to_Multi45, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.button1)

        # สร้างปุ่มที่สอง
        self.button2 = Button(text='30 Seconds', on_press=self.switch_to_Multi30, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.button2)

        # สร้างปุ่มที่สาม
        self.button3 = Button(text='15 Seconds', on_press=self.switch_to_Multi15, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.button3)

        # เพิ่ม Layout เข้าไปใน Screen
        self.add_widget(layout)


    def switch_to_Multi15(self, instance):
        self.manager.current = 'multi15'

    def switch_to_Multi30(self, instance):
        self.manager.current = 'multi30'

    def switch_to_Multi45(self, instance):
        self.manager.current = 'multi45'

#Multi 15 Mode
class GameMultiCoin15Screen(Screen) :
    def __init__(self, **kw):
        super(GameMultiCoin15Screen, self).__init__(**kw)
        self.game_multi_15_widget = GameMultiCoin15()
        self.add_widget(self.game_multi_15_widget)

class GameMultiCoin15(Widget) :
    pass


#Multi 15 Mode
class GameMultiCoin30Screen(Screen) :
    def __init__(self, **kw):
        super(GameMultiCoin30Screen, self).__init__(**kw)
        self.game_multi_30_widget = GameMultiCoin30()
        self.add_widget(self.game_multi_30_widget)

class GameMultiCoin30(Widget) :
    pass

#Multi 45 Mode
class GameMultiCoin45Screen(Screen) :
    def __init__(self, **kw):
        super(GameMultiCoin45Screen, self).__init__(**kw)
        self.game_multi_45_widget = GameMultiCoin45()
        self.add_widget(self.game_multi_45_widget)

class GameMultiCoin45(Widget) :
    pass



class MyGame(App):
    def build(self):
        self.screen_manager = ScreenManager()

        main_menu = MainMenu(name='main_menu')

        game_single = GameSingleCoinScreen(name='single')
        game_single_15 = GameSingleCoin15Screen(name = 'single15')
        game_single_30 = GameSingleCoin30Screen(name = 'single30')
        game_single_45 = GameSingleCoin45Screen(name = 'single45')

        game_multi = GameSingleCoinScreen(name='multi')
        game_multi_15 = GameMultiCoin15Screen(name = 'multi15')
        game_multi_30 = GameMultiCoin30Screen(name = 'multi30')
        game_multi_45 = GameMultiCoin45Screen(name = 'multi45')

        self.screen_manager.add_widget(main_menu)

        self.screen_manager.add_widget(game_single)
        self.screen_manager.add_widget(game_single_15)
        self.screen_manager.add_widget(game_single_30)
        self.screen_manager.add_widget(game_single_45)

        self.screen_manager.add_widget(game_multi)
        self.screen_manager.add_widget(game_multi_15)
        self.screen_manager.add_widget(game_multi_30)
        self.screen_manager.add_widget(game_multi_45)


        return self.screen_manager

if __name__ == '__main__':
    app = MyGame()
    app.run()

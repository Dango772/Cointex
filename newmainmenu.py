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
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.core.audio import SoundLoader



#Check collides
def collides(rect1, rect2):
    r1x, r1y = rect1[0]
    r2x, r2y = rect2[0]
    r1w, r1h = rect1[1]
    r2w, r2h = rect2[1]

    return (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y)


#Class Main Menu
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        self.sound = SoundLoader.load('music1.mp3')
        if self.sound:
            self.sound.bind(on_stop=self.on_music_finish)
            self.sound.volume = 0.2  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
            self.sound.play()

        layout1 = FloatLayout()

        background = Image(source='screen2.jpg', allow_stretch=True, keep_ratio=False)
        layout1.add_widget(background)

        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.image = Image(source='alice-aris.gif', size_hint=(None, None), size=(200, 200))
        layout.add_widget(self.image)

        self.single_button = Button(text='Single Player', on_press=self.switch_to_Single,size_hint=(None, None), size=(200, 50))
        self.single_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.single_button)

        self.multi_button = Button(text='Multi Player', on_press=self.switch_to_Multi,size_hint=(None, None), size=(200, 50))
        self.multi_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.multi_button)

        self.character_button = Button(text='Character', on_press=self.switch_to_Character,size_hint=(None, None), size=(200, 50))
        self.character_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.character_button)

        self.setting_button = Button(text='Setting', size_hint=(None, None), size=(200, 50) )
        self.setting_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.setting_button)
        

        self.add_widget(layout1)
        self.add_widget(layout)


    def switch_to_Single(self, instance):
        self.manager.current = 'single'

    def switch_to_Multi(self, instance):
        self.manager.current = 'multi'
    
    def switch_to_Character(self, instance):
        self.manager.current = 'character'

    def on_music_finish(self, sound):
        sound.seek(0)  # เลื่อนตำแหน่งการเล่นกลับไปที่จุดเริ่มต้น
        sound.play()   # เล่นเพลงอีกครั้ง


#Single Mode
class GameSingleCoinScreen(Screen) :
    def __init__(self, **kwargs):
        super(GameSingleCoinScreen, self).__init__(**kwargs)

        layout1 = FloatLayout()

        background = Image(source='screen4.jpg', allow_stretch=True, keep_ratio=False)
        layout1.add_widget(background)

        # สร้าง Layout แนวตั้ง
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # สร้างปุ่มแรก
        self.button1 = Button(text='45 Seconds', on_press=self.switch_to_Single45, size_hint=(None, None), size=(200, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button1)

        # สร้างปุ่มที่สอง
        self.button2 = Button(text='30 Seconds', on_press=self.switch_to_Single30, size_hint=(None, None), size=(200, 50))
        self.button2.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button2)
        
        # สร้างปุ่มที่สาม
        self.button3 = Button(text='15 Seconds', on_press=self.switch_to_Single15, size_hint=(None, None), size=(200, 50))
        self.button3.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button3)

        self.back_button = Button(text='Back', on_press=self.switch_to_previous_screen, size_hint=(None, None), size=(200, 50))
        self.back_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.back_button)

        self.add_widget(layout1)
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
        super(GameMultiCoinScreen, self).__init__(**kwargs)

        layout1 = FloatLayout()

        background = Image(source='screen4.jpg', allow_stretch=True, keep_ratio=False)
        layout1.add_widget(background)

        # สร้าง Layout แนวตั้ง
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # สร้างปุ่มแรก
        self.button1 = Button(text='45 Seconds', on_press=self.switch_to_Multi45, size_hint=(None, None), size=(200, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button1)

        # สร้างปุ่มที่สอง
        self.button2 = Button(text='30 Seconds', on_press=self.switch_to_Multi30, size_hint=(None, None), size=(200, 50))
        self.button2.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button2)

        # สร้างปุ่มที่สาม
        self.button3 = Button(text='15 Seconds', on_press=self.switch_to_Multi15, size_hint=(None, None), size=(200, 50))
        self.button3.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button3)

        self.back_button = Button(text='Back', on_press=self.switch_to_previous_screen, size_hint=(None, None), size=(200, 50))
        self.back_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.back_button)

        # เพิ่ม Layout เข้าไปใน Screen
        self.add_widget(layout1)
        self.add_widget(layout)


    def switch_to_Multi15(self, instance):
        self.manager.current = 'multi15'

    def switch_to_Multi30(self, instance):
        self.manager.current = 'multi30'

    def switch_to_Multi45(self, instance):
        self.manager.current = 'multi45'

    def switch_to_previous_screen(self, instance):
        self.manager.current = 'main_menu'
        pass 

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

        

    
    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 45  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        self.countdown_time -= 1
        self.game_multi_45_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"

        if self.countdown_time <= 0:
            self.manager.current = 'main_menu' 

class GameMultiCoin45(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_label = Label(text="Time left: 45 seconds", pos=(300, 700), size=(200, 200), font_size=20)
        self.add_widget(self.timer_label)

        self.scorep1 = 0
        self.scorep2 = 0

        self.scorep1_label = Label(text="Score Player 1 : 0", pos=(100, 800), size=(200, 200),font_size=40)
        self.add_widget(self.scorep1_label)

        self.scorep2_label = Label(text="Score Player 2 : 0", pos=(500, 800), size=(200, 200),font_size=40)
        self.add_widget(self.scorep2_label)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.move_step, 0)
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='GrassMap1.png', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            Line(rectangle=(430, 865, 345, 65), width=2)
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(250, 250), size=(135, 135))

            #generate monster charector
            self.monster = Image(source="monster.png", pos=(1700, 250), size=(135, 135))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))

        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.button1 = Button(text='Menu', on_press=self.pause_menu, size_hint=(None, None), size=(200, 50))
        layout.add_widget(self.button1)

        self.add_widget(layout)

    def pause_menu(self,instance) :
        self.popup = Popup(title='Test popup',content=Label(text='Hello world'),size_hint=(None, None), size=(400, 400))
        return self.popup

    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

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
        if 'w' in self.pressed_keys and cur_y1 + step1 + self.hero.height < self.image.height:
            cur_y1 += step1

        if 's' in self.pressed_keys and cur_y1 - step1 > 0:
            cur_y1 -= step1

        if 'a' in self.pressed_keys and cur_x1 - step1 > 0:
            cur_x1 -= step1

        if 'd' in self.pressed_keys and cur_x1 + step1 + self.hero.width < self.image.width:
            cur_x1 += step1

        self.hero.pos = (cur_x1, cur_y1)

        cur_x2 = self.monster.pos[0]
        cur_y2 = self.monster.pos[1]
        step2 = 500 * dt

        if 'i' in self.pressed_keys and cur_y2 + step2 + self.monster.height < self.image.height:
            cur_y2 += step2

        if 'k' in self.pressed_keys and cur_y2 - step2 > 0:
            cur_y2 -= step2

        if 'j' in self.pressed_keys and cur_x2 - step2 > 0:
            cur_x2 -= step2

        if 'l' in self.pressed_keys and cur_x2 + step2 + self.monster.width < self.image.width:
            cur_x2 += step2

        self.monster.pos = (cur_x2, cur_y2)

        if collides((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) or collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) or collides((self.hero.pos, self.hero.size), (self.coin3.pos, self.coin3.size)):

            if collides ((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) == True :
                self.coin1.pos = (random.randint(0, self.image.width - self.coin1.width),
                             random.randint(0, self.image.height - self.coin1.height))
            if collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) :
                self.coin2.pos = (random.randint(0, self.image.width - self.coin2.width),
                             random.randint(0, self.image.height - self.coin2.height))
            if collides((self.hero.pos, self.hero.size), (self.coin3.pos, self.coin3.size)) :
                self.coin3.pos = (random.randint(0, self.image.width - self.coin3.width),
                             random.randint(0, self.image.height - self.coin3.height))
                
            self.scorep1 += 1
            self.scorep1_label.text = "Score Player 1 : " + str(self.scorep1)

    
        if collides((self.monster.pos, self.monster.size), (self.coin1.pos, self.coin1.size)) or collides((self.monster.pos, self.monster.size), (self.coin2.pos, self.coin2.size)) or collides((self.monster.pos, self.monster.size), (self.coin3.pos, self.coin3.size)):

            if collides ((self.monster.pos, self.monster.size), (self.coin1.pos, self.coin1.size)) == True :
                self.coin1.pos = (random.randint(0, self.image.width - self.coin1.width),
                             random.randint(0, self.image.height - self.coin1.height))
            if collides((self.monster.pos, self.monster.size), (self.coin2.pos, self.coin2.size)) :
                self.coin2.pos = (random.randint(0, self.image.width - self.coin2.width),
                             random.randint(0, self.image.height - self.coin2.height))
            if collides((self.monster.pos, self.monster.size), (self.coin3.pos, self.coin3.size)) :
                self.coin3.pos = (random.randint(0, self.image.width - self.coin3.width),
                             random.randint(0, self.image.height - self.coin3.height))
                
            self.scorep2 += 1
            self.scorep2_label.text = "Score Player 2 : " + str(self.scorep2)   

#class หน้าเปรี่ยนตัวละคร
class CharacterApp(Screen):
    def __init__(self, **kwargs):
        super(CharacterApp, self).__init__(**kwargs)

    def change_character_image(self):
        # ส่งข้อมูลเกี่ยวกับการเปลี่ยนรูปภาพตัวละครไปยังหน้าเล่นเกมส์
        self.manager.get_screen('game_multi_45').change_character_image("new_character_image.png")



class MyGame(App):
    def build(self):
        self.screen_manager = ScreenManager()

        main_menu = MainMenu(name='main_menu')

        game_single = GameSingleCoinScreen(name='single')
        game_single_15 = GameSingleCoin15Screen(name = 'single15')
        game_single_30 = GameSingleCoin30Screen(name = 'single30')
        game_single_45 = GameSingleCoin45Screen(name = 'single45')

        game_multi = GameMultiCoinScreen(name='multi')
        game_multi_15 = GameMultiCoin15Screen(name = 'multi15')
        game_multi_30 = GameMultiCoin30Screen(name = 'multi30')
        game_multi_45 = GameMultiCoin45Screen(name = 'multi45')

        game_character = CharacterApp(name='character')

        self.screen_manager.add_widget(main_menu)

        self.screen_manager.add_widget(game_single)
        self.screen_manager.add_widget(game_single_15)
        self.screen_manager.add_widget(game_single_30)
        self.screen_manager.add_widget(game_single_45)

        self.screen_manager.add_widget(game_multi)
        self.screen_manager.add_widget(game_multi_15)
        self.screen_manager.add_widget(game_multi_30)
        self.screen_manager.add_widget(game_multi_45)

        self.screen_manager.add_widget(game_character)

        return self.screen_manager

if __name__ == '__main__':
    app = MyGame()
    app.run()

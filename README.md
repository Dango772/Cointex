# My Kivy App -> ProjectCoin Cointex

My Kivy App is a simple application that demonstrates the usage of Kivy for creating graphical user interfaces.

## Features

- There is a game menu page.
- You can choose to play alone or with 2 people.
- You can choose a play time limit.
- When the character hits a coin, they will collect the coin and display it as a score.
- In 2-player mode, scores will be compared.
- You can press to restart the game or return to the menu again.
- You can change character(both player 1 and player 2)
- 
## Screenshots
menu : ![image](https://github.com/6410110236/Cointex/assets/125024335/2a2a2775-e8b1-4b49-bda1-95a1ed5c404f)
single or multi mode : ![image](https://github.com/6410110236/Cointex/assets/125024335/a23df7fc-5a4d-4832-9a84-5fb11814ac46)
single game : ![image](https://github.com/6410110236/Cointex/assets/125024335/48296548-96ce-46dc-93ed-f72ef75c5b3b)
multi game : ![image](https://github.com/6410110236/Cointex/assets/148541889/6fa76c09-61cc-4ae0-9f27-33b36872f44f) ![image](https://github.com/6410110236/Cointex/assets/148541889/254a63ac-4709-4a08-98a5-d461d0569f35)
Player1 character  : ![image](https://github.com/6410110236/Cointex/assets/148541889/6d34405d-2b38-443d-b5a0-d5bb45f8855d)
Player2 character  : ![image](https://github.com/6410110236/Cointex/assets/148541889/2b4569ce-897b-4950-bedb-af6709c1a4ad)

## Installation

1. Install Kivy:

    ```bash
    pip install kivy
    ```

2. Run the application:

    ```bash
    python newmainmenu.py
    ```

## Usage

1. Launch the application.
2. choose single or multi mode
3. choose time
4. keeping coin


## Contact

For any inquiries, please contact me at 6410110236@psu.ac.th

## Code

```import library
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
from kivy.graphics import Color, Rectangle

```
```create collides function
#Check collides
def collides(rect1, rect2):
    r1x, r1y = rect1[0]
    r2x, r2y = rect2[0]
    r1w, r1h = rect1[1]
    r2w, r2h = rect2[1]

    return (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y)
```

```create main menu page
#Class Main Menu
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        #self.sound = SoundLoader.load('music1.mp3')
        self.soundButton = SoundLoader.load('button1.mp3')

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
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'single'

    def switch_to_Multi(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'multi'
    
    def switch_to_Character(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'character'

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music1.mp3')
        if self.sound:
            self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()
```


```create single page
#Single Mode
class GameSingleCoinScreen(Screen) :
    def __init__(self, **kwargs):
        super(GameSingleCoinScreen, self).__init__(**kwargs)

        self.soundButton = SoundLoader.load('button1.mp3')

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


    def on_enter(self):
        if self.manager.get_screen('main_menu').sound:
            self.manager.get_screen('main_menu').sound.stop()
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music2.mp3')
        if self.sound:
            self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def switch_to_Single15(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'single15'

    def switch_to_Single30(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'single30'

    def switch_to_Single45(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'single45'

    def switch_to_previous_screen(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.sound.stop()
        #self.manager.get_screen('main_menu').sound.play()
        self.manager.current = 'main_menu'   

```

```create single 15 s page
#Single 15 Mode
class GameSingleCoin15Screen(Screen) :
    def __init__(self, **kw):
        super(GameSingleCoin15Screen, self).__init__(**kw)
        self.game_single_15_widget = GameSingleCoin15()
        self.add_widget(self.game_single_15_widget)

        self.soundButton = SoundLoader.load('button1.mp3')
        self.soundButton.volume = 0.3  # ตั้งระดับเสียงเพลงใหม่
        self.soundwin = SoundLoader.load('winsound.mp3')
        self.soundwin.volume = 1  # ตั้งระดับเสียงเพลงใหม่

        # Add a "Stop Game" button
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(200, 50), pos_hint={'top': 0.95, 'right': 1})
        self.button_stop_game = Button(text='Stop Game', on_press=self.stop_game, size_hint=(None, None), size=(180, 50))
        layout.add_widget(self.button_stop_game)
        self.add_widget(layout)
        
        self.is_game_running = True  # Flag to track the state of the game
        self.schedule = None  # Initialize the schedule variable

    def stop_game(self, instance):
        self.soundButton.play() 
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Pause', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep1win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title=f'You Got {self.scorep1} scores !!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    

    def restart_game(self, instance):
        self.soundButton.play() 
        self.sound.play()
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
            # Start the countdown timer
            self.start_countdown()

            # Dismiss the Popup
            self.popup.dismiss()

            # Reset character positions and scores
            self.game_single_15_widget.hero.pos = (900, 250)
            self.game_single_15_widget.scorep1 = 0
            self.game_single_15_widget.scorep1_label.text = "Score Player 1 : 0"

            # Reset timer label
            self.game_single_15_widget.timer_label.text = "Time left: 15 seconds"
            self.countdown_time = 30

            self.game_single_15_widget._keyboard = Window.request_keyboard(self.game_single_15_widget._on_keyboard_closed, self.game_single_15_widget)
            self.game_single_15_widget._keyboard.bind(on_key_down=self.game_single_15_widget._on_key_down)
            self.game_single_15_widget._keyboard.bind(on_key_up=self.game_single_15_widget._on_key_up)

            # Switch back to the game screen
            self.manager.current = 'single15'

    def switch_to_main_menu(self, instance):
        self.soundButton.play() 
        self.restart_game(None)
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
      
        # Close the Popup
        self.popup.dismiss()
        self.game_single_15_widget.hero.pos = (900,250)

        self.game_single_15_widget.scorep1 = 0
        self.game_single_15_widget.scorep1_label.text = "Score Player 1 : 0"

        self.game_single_15_widget.timer_label.text = "Time left: 15 seconds"
        self.countdown_time = 15
    
        # Switch to the main menu screen
        self.manager.current = 'main_menu'

    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 15  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        #เรียกใช้ scorep1 จาก class GameMultiCoin30
        self.scorep1 = self.game_single_15_widget.scorep1 
        # Decrement the countdown time if the game is running
        if self.is_game_running:
            self.countdown_time -= 1
        
            # Update the timer label in your game widget
            self.game_single_15_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"
 
            if self.countdown_time <= 0:
                # Stop the countdown timer when time runs out
                self.stop_countdown()
                self.soundwin.play()
                self.stop_gamep1win(None)
 
    def stop_countdown(self):
        if self.schedule is not None:
            # Unschedule the function responsible for updating the countdown timer
            self.schedule.cancel()
    def start_countdown(self):
        if self.is_game_running:  # Check if the game is running
            # Schedule a function to update the countdown timer every second
            self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music4.mp3')
        self.sound.volume = 0.1  # ตั้งระดับเสียงเพลงใหม่
        if self.sound:
            #self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_single_15_widget.change_character_imageP1(new_image_source)

```

```create game single 15 s
class GameSingleCoin15(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_label = Label(text="Time left: 15 seconds", pos=(300, 700), size=(200, 200), font_size=20)
        self.add_widget(self.timer_label)

        self.scorep1 = 0

        self.scorep1_label = Label(text="Score Player 1 : 0", pos=(100, 800), size=(200, 200),font_size=40)
        self.add_widget(self.scorep1_label)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.move_step, 0)

        self.keepcoinsound = SoundLoader.load('coinkeep.mp3')
        if self.keepcoinsound:
            self.keepcoinsound.volume = 0.7  # ตั้งระดับเสียงเพลงใหม่
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='screen10.jpeg', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(900, 250), size=(140, 140))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))


    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if self.parent.is_game_running and self.parent.manager.current == 'single15':
            self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        if self.parent.is_game_running and self.parent.manager.current == 'single15':
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

        if collides((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) or collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) or collides((self.hero.pos, self.hero.size), (self.coin3.pos, self.coin3.size)):


            self.keepcoinsound.play()

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

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.hero.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "hero"
```


```create single 30 s page
#Single 30 Mode
class GameSingleCoin30Screen(Screen) :
    def __init__(self, **kw):
        super(GameSingleCoin30Screen, self).__init__(**kw)
        self.game_single_30_widget = GameSingleCoin30()
        self.add_widget(self.game_single_30_widget)

        self.soundButton = SoundLoader.load('button1.mp3')
        self.soundButton.volume = 0.3  # ตั้งระดับเสียงเพลงใหม่
        self.soundwin = SoundLoader.load('winsound.mp3')
        self.soundwin.volume = 1  # ตั้งระดับเสียงเพลงใหม่

        # Add a "Stop Game" button
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(200, 50), pos_hint={'top': 0.95, 'right': 1})
        self.button_stop_game = Button(text='Stop Game', on_press=self.stop_game, size_hint=(None, None), size=(180, 50))
        layout.add_widget(self.button_stop_game)
        self.add_widget(layout)
        
        self.is_game_running = True  # Flag to track the state of the game
        self.schedule = None  # Initialize the schedule variable

    def stop_game(self, instance):
        self.soundButton.play() 
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Pause', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep1win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title=f'You Got {self.scorep1} scores !!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    

    def restart_game(self, instance):
        self.soundButton.play() 
        self.sound.play()
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
            # Start the countdown timer
            self.start_countdown()

            # Dismiss the Popup
            self.popup.dismiss()

            # Reset character positions and scores
            self.game_single_30_widget.hero.pos = (900, 250)
            self.game_single_30_widget.scorep1 = 0
            self.game_single_30_widget.scorep1_label.text = "Score Player 1 : 0"

            # Reset timer label
            self.game_single_30_widget.timer_label.text = "Time left: 30 seconds"
            self.countdown_time = 30

            self.game_single_30_widget._keyboard = Window.request_keyboard(self.game_single_30_widget._on_keyboard_closed, self.game_single_30_widget)
            self.game_single_30_widget._keyboard.bind(on_key_down=self.game_single_30_widget._on_key_down)
            self.game_single_30_widget._keyboard.bind(on_key_up=self.game_single_30_widget._on_key_up)

            # Switch back to the game screen
            self.manager.current = 'single30'

    def switch_to_main_menu(self, instance):
        self.soundButton.play() 
        self.restart_game(None)
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
      
        # Close the Popup
        self.popup.dismiss()
        self.game_single_30_widget.hero.pos = (900,250)

        self.game_single_30_widget.scorep1 = 0
        self.game_single_30_widget.scorep1_label.text = "Score Player 1 : 0"

        self.game_single_30_widget.timer_label.text = "Time left: 30 seconds"
        self.countdown_time = 30
    
        # Switch to the main menu screen
        self.manager.current = 'main_menu'

    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 30  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        #เรียกใช้ scorep1 จาก class GameMultiCoin30
        self.scorep1 = self.game_single_30_widget.scorep1 
        # Decrement the countdown time if the game is running
        if self.is_game_running:
            self.countdown_time -= 1
        
            # Update the timer label in your game widget
            self.game_single_30_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"
 
            if self.countdown_time <= 0:
                # Stop the countdown timer when time runs out
                self.stop_countdown()
                self.soundwin.play()
                self.stop_gamep1win(None)
 
    def stop_countdown(self):
        if self.schedule is not None:
            # Unschedule the function responsible for updating the countdown timer
            self.schedule.cancel()
    def start_countdown(self):
        if self.is_game_running:  # Check if the game is running
            # Schedule a function to update the countdown timer every second
            self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music4.mp3')
        self.sound.volume = 0.1  # ตั้งระดับเสียงเพลงใหม่
        if self.sound:
            #self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_single_30_widget.change_character_imageP1(new_image_source)
```

```create game single 30 s
class GameSingleCoin30(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_label = Label(text="Time left: 30 seconds", pos=(300, 700), size=(200, 200), font_size=20)
        self.add_widget(self.timer_label)

        self.scorep1 = 0

        self.scorep1_label = Label(text="Score Player 1 : 0", pos=(100, 800), size=(200, 200),font_size=40)
        self.add_widget(self.scorep1_label)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.move_step, 0)

        self.keepcoinsound = SoundLoader.load('coinkeep.mp3')
        if self.keepcoinsound:
            self.keepcoinsound.volume = 0.7  # ตั้งระดับเสียงเพลงใหม่
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='screen10.jpeg', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(900, 250), size=(140, 140))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))


    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if self.parent.is_game_running and self.parent.manager.current == 'single30':
            self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        if self.parent.is_game_running and self.parent.manager.current == 'single30':
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

        if collides((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) or collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) or collides((self.hero.pos, self.hero.size), (self.coin3.pos, self.coin3.size)):


            self.keepcoinsound.play()

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

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.hero.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "hero"
```


```create single 45 s page
#Single 45 Mode
class GameSingleCoin45Screen(Screen) :
    def __init__(self, **kw):
        super(GameSingleCoin45Screen, self).__init__(**kw)
        self.game_single_45_widget = GameSingleCoin45()
        self.add_widget(self.game_single_45_widget)

        self.soundButton = SoundLoader.load('button1.mp3')
        self.soundButton.volume = 0.3  # ตั้งระดับเสียงเพลงใหม่
        self.soundwin = SoundLoader.load('winsound.mp3')
        self.soundwin.volume = 1  # ตั้งระดับเสียงเพลงใหม่

        # Add a "Stop Game" button
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(200, 50), pos_hint={'top': 0.95, 'right': 1})
        self.button_stop_game = Button(text='Stop Game', on_press=self.stop_game, size_hint=(None, None), size=(180, 50))
        layout.add_widget(self.button_stop_game)
        self.add_widget(layout)
        
        self.is_game_running = True  # Flag to track the state of the game
        self.schedule = None  # Initialize the schedule variable

    def stop_game(self, instance):
        self.soundButton.play() 
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Pause', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep1win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title=f'You Got {self.scorep1} scores !!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    

    def restart_game(self, instance):
        self.soundButton.play() 
        self.sound.play()
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
            # Start the countdown timer
            self.start_countdown()

            # Dismiss the Popup
            self.popup.dismiss()

            # Reset character positions and scores
            self.game_single_45_widget.hero.pos = (900, 250)
            self.game_single_45_widget.scorep1 = 0
            self.game_single_45_widget.scorep1_label.text = "Score Player 1 : 0"

            # Reset timer label
            self.game_single_45_widget.timer_label.text = "Time left: 45 seconds"
            self.countdown_time = 45

            self.game_single_45_widget._keyboard = Window.request_keyboard(self.game_single_45_widget._on_keyboard_closed, self.game_single_45_widget)
            self.game_single_45_widget._keyboard.bind(on_key_down=self.game_single_45_widget._on_key_down)
            self.game_single_45_widget._keyboard.bind(on_key_up=self.game_single_45_widget._on_key_up)

            # Switch back to the game screen
            self.manager.current = 'single45'

    def switch_to_main_menu(self, instance):
        self.soundButton.play() 
        self.restart_game(None)
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
      
        # Close the Popup
        self.popup.dismiss()
        self.game_single_45_widget.hero.pos = (900,250)

        self.game_single_45_widget.scorep1 = 0
        self.game_single_45_widget.scorep1_label.text = "Score Player 1 : 0"

        self.game_single_45_widget.timer_label.text = "Time left: 45 seconds"
        self.countdown_time = 45
    
        # Switch to the main menu screen
        self.manager.current = 'main_menu'

    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 45  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        #เรียกใช้ scorep1 จาก class GameMultiCoin30
        self.scorep1 = self.game_single_45_widget.scorep1 
        # Decrement the countdown time if the game is running
        if self.is_game_running:
            self.countdown_time -= 1
        
            # Update the timer label in your game widget
            self.game_single_45_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"
 
            if self.countdown_time <= 0:
                # Stop the countdown timer when time runs out
                self.stop_countdown()
                self.soundwin.play()
                self.stop_gamep1win(None)
 
    def stop_countdown(self):
        if self.schedule is not None:
            # Unschedule the function responsible for updating the countdown timer
            self.schedule.cancel()
    def start_countdown(self):
        if self.is_game_running:  # Check if the game is running
            # Schedule a function to update the countdown timer every second
            self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music4.mp3')
        self.sound.volume = 0.1  # ตั้งระดับเสียงเพลงใหม่
        if self.sound:
            #self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_single_45_widget.change_character_imageP1(new_image_source)

```


```create game single 45 s
class GameSingleCoin45(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_label = Label(text="Time left: 45 seconds", pos=(300, 700), size=(200, 200), font_size=20)
        self.add_widget(self.timer_label)

        self.scorep1 = 0

        self.scorep1_label = Label(text="Score Player 1 : 0", pos=(100, 800), size=(200, 200),font_size=40)
        self.add_widget(self.scorep1_label)

        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self.pressed_keys = set()
        Clock.schedule_interval(self.move_step, 0)

        self.keepcoinsound = SoundLoader.load('coinkeep.mp3')
        if self.keepcoinsound:
            self.keepcoinsound.volume = 0.7  # ตั้งระดับเสียงเพลงใหม่
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='screen10.jpeg', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(900, 250), size=(140, 140))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))


    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if self.parent.is_game_running and self.parent.manager.current == 'single45':
            self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        if self.parent.is_game_running and self.parent.manager.current == 'single45':
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

        if collides((self.hero.pos, self.hero.size), (self.coin1.pos, self.coin1.size)) or collides((self.hero.pos, self.hero.size), (self.coin2.pos, self.coin2.size)) or collides((self.hero.pos, self.hero.size), (self.coin3.pos, self.coin3.size)):


            self.keepcoinsound.play()

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

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.hero.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "hero"
```


```create multi page
#Muti Mode
class GameMultiCoinScreen(Screen) :
    def __init__(self, **kwargs):
        super(GameMultiCoinScreen, self).__init__(**kwargs)

        self.soundButton = SoundLoader.load('button1.mp3')

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

    def on_enter(self):
        '''if self.manager.get_screen('main_menu').sound:
            self.manager.get_screen('main_menu').sound.stop()'''
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music2.mp3')
        if self.sound:
            self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def switch_to_Multi15(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'multi15'

    def switch_to_Multi30(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'multi30'

    def switch_to_Multi45(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'multi45'

    def switch_to_previous_screen(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.sound.stop()
        #self.manager.get_screen('main_menu').sound.play()
        self.manager.current = 'main_menu'   
```


```create multi 15 s page
#Multi 15 Mode
class GameMultiCoin15Screen(Screen) :
    def __init__(self, **kw):
        super(GameMultiCoin15Screen, self).__init__(**kw)
        self.game_multi_15_widget = GameMultiCoin15()
        self.add_widget(self.game_multi_15_widget)

        self.soundButton = SoundLoader.load('button1.mp3')
        self.soundButton.volume = 0.3  # ตั้งระดับเสียงเพลงใหม่
        self.soundwin = SoundLoader.load('winsound.mp3')
        self.soundwin.volume = 1  # ตั้งระดับเสียงเพลงใหม่

        # Add a "Stop Game" button
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(200, 50), pos_hint={'top': 0.95, 'right': 1})
        self.button_stop_game = Button(text='Stop Game', on_press=self.stop_game, size_hint=(None, None), size=(180, 50))
        layout.add_widget(self.button_stop_game)
        self.add_widget(layout)
        
        self.is_game_running = True  # Flag to track the state of the game
        self.schedule = None  # Initialize the schedule variable

    def stop_game(self, instance):
        self.soundButton.play() 
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Pause', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep1win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player1 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep2win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player2 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gameDraw(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Draw!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def restart_game(self, instance):
        self.soundButton.play() 
        self.sound.play()
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
            # Start the countdown timer
            self.start_countdown()

            # Dismiss the Popup
            self.popup.dismiss()

            # Reset character positions and scores
            self.game_multi_15_widget.hero.pos = (250, 250)
            self.game_multi_15_widget.monster.pos = (1700, 250)
            self.game_multi_15_widget.scorep1 = 0
            self.game_multi_15_widget.scorep1_label.text = "Score Player 1 : 0"
            self.game_multi_15_widget.scorep2 = 0
            self.game_multi_15_widget.scorep2_label.text = "Score Player 2 : 0"

            # Reset timer label
            self.game_multi_15_widget.timer_label.text = "Time left: 15 seconds"
            self.countdown_time = 15

            self.game_multi_15_widget._keyboard = Window.request_keyboard(self.game_multi_15_widget._on_keyboard_closed, self.game_multi_15_widget)
            self.game_multi_15_widget._keyboard.bind(on_key_down=self.game_multi_15_widget._on_key_down)
            self.game_multi_15_widget._keyboard.bind(on_key_up=self.game_multi_15_widget._on_key_up)

            # Switch back to the game screen
            self.manager.current = 'multi15'

    def switch_to_main_menu(self, instance):
        self.soundButton.play() 
        self.restart_game(None)
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
      
        # Close the Popup
        self.popup.dismiss()
        self.game_multi_15_widget.hero.pos = (250,250)
        self.game_multi_15_widget.monster.pos = (1700,250)

        self.game_multi_15_widget.scorep1 = 0
        self.game_multi_15_widget.scorep1_label.text = "Score Player 1 : 0"
        self.game_multi_15_widget.scorep2 = 0
        self.game_multi_15_widget.scorep2_label.text = "Score Player 2 : 0"

        self.game_multi_15_widget.timer_label.text = "Time left: 15 seconds"
        self.countdown_time = 15
    
        # Switch to the main menu screen
        self.manager.current = 'main_menu'

    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 15  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        #เรียกใช้ scorep1 จาก class GameMultiCoin30
        self.scorep1 = self.game_multi_15_widget.scorep1 
        self.scorep2 = self.game_multi_15_widget.scorep2 
        # Decrement the countdown time if the game is running
        if self.is_game_running:
            self.countdown_time -= 1
        
            # Update the timer label in your game widget
            self.game_multi_15_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"
 
            if self.countdown_time <= 0:
                # Stop the countdown timer when time runs out
                self.stop_countdown()
                if self.scorep1 > self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep1win(None)
                if self.scorep1 < self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep2win(None)
                if self.scorep1 == self.scorep2 :
                    self.soundwin.play()
                    self.stop_gameDraw(None)
 
    def stop_countdown(self):
        if self.schedule is not None:
            # Unschedule the function responsible for updating the countdown timer
            self.schedule.cancel()
    def start_countdown(self):
        if self.is_game_running:  # Check if the game is running
            # Schedule a function to update the countdown timer every second
            self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music4.mp3')
        self.sound.volume = 0.1  # ตั้งระดับเสียงเพลงใหม่
        if self.sound:
            #self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_15_widget.change_character_imageP1(new_image_source)
    def change_character_imageP2(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_15_widget.change_character_imageP2(new_image_source)  
```

```create game multi 15 s
class GameMultiCoin15(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_label = Label(text="Time left: 15 seconds", pos=(300, 700), size=(200, 200), font_size=20)
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

        self.keepcoinsound = SoundLoader.load('coinkeep.mp3')
        if self.keepcoinsound:
            self.keepcoinsound.volume = 0.7  # ตั้งระดับเสียงเพลงใหม่
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='screen10.jpeg', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            Line(rectangle=(430, 865, 345, 65), width=2)
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(250, 250), size=(140, 140))

            #generate monster charector
            self.monster = Image(source="character2.png", pos=(1700, 250), size=(140, 140))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))


    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if self.parent.is_game_running and self.parent.manager.current == 'multi15':
            self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        if self.parent.is_game_running and self.parent.manager.current == 'multi15':
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


            self.keepcoinsound.play()

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

            self.keepcoinsound.play()


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

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.hero.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "hero"
    def change_character_imageP2(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.monster.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "monster"
```


```create multi 30 s page
#Multi 30 Mode
class GameMultiCoin30Screen(Screen) :
    def __init__(self, **kw):
        super(GameMultiCoin30Screen, self).__init__(**kw)
        self.game_multi_30_widget = GameMultiCoin30()
        self.add_widget(self.game_multi_30_widget)

        self.soundButton = SoundLoader.load('button1.mp3')
        self.soundButton.volume = 0.3  # ตั้งระดับเสียงเพลงใหม่
        self.soundwin = SoundLoader.load('winsound.mp3')
        self.soundwin.volume = 1  # ตั้งระดับเสียงเพลงใหม่

        # Add a "Stop Game" button
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(200, 50), pos_hint={'top': 0.95, 'right': 1})
        self.button_stop_game = Button(text='Stop Game', on_press=self.stop_game, size_hint=(None, None), size=(180, 50))
        layout.add_widget(self.button_stop_game)
        self.add_widget(layout)
        
        self.is_game_running = True  # Flag to track the state of the game
        self.schedule = None  # Initialize the schedule variable

    def stop_game(self, instance):
        self.soundButton.play() 
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Pause', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep1win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player1 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep2win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player2 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gameDraw(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Draw!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def restart_game(self, instance):
        self.soundButton.play() 
        self.sound.play()
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
            # Start the countdown timer
            self.start_countdown()

            # Dismiss the Popup
            self.popup.dismiss()

            # Reset character positions and scores
            self.game_multi_30_widget.hero.pos = (250, 250)
            self.game_multi_30_widget.monster.pos = (1700, 250)
            self.game_multi_30_widget.scorep1 = 0
            self.game_multi_30_widget.scorep1_label.text = "Score Player 1 : 0"
            self.game_multi_30_widget.scorep2 = 0
            self.game_multi_30_widget.scorep2_label.text = "Score Player 2 : 0"

            # Reset timer label
            self.game_multi_30_widget.timer_label.text = "Time left: 30 seconds"
            self.countdown_time = 30

            self.game_multi_30_widget._keyboard = Window.request_keyboard(self.game_multi_30_widget._on_keyboard_closed, self.game_multi_30_widget)
            self.game_multi_30_widget._keyboard.bind(on_key_down=self.game_multi_30_widget._on_key_down)
            self.game_multi_30_widget._keyboard.bind(on_key_up=self.game_multi_30_widget._on_key_up)

            # Switch back to the game screen
            self.manager.current = 'multi30'

    def switch_to_main_menu(self, instance):
        self.soundButton.play() 
        self.restart_game(None)
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
      
        # Close the Popup
        self.popup.dismiss()
        self.game_multi_30_widget.hero.pos = (250,250)
        self.game_multi_30_widget.monster.pos = (1700,250)

        self.game_multi_30_widget.scorep1 = 0
        self.game_multi_30_widget.scorep1_label.text = "Score Player 1 : 0"
        self.game_multi_30_widget.scorep2 = 0
        self.game_multi_30_widget.scorep2_label.text = "Score Player 2 : 0"

        self.game_multi_30_widget.timer_label.text = "Time left: 30 seconds"
        self.countdown_time = 30
    
        # Switch to the main menu screen
        self.manager.current = 'main_menu'

    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 30  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        #เรียกใช้ scorep1 จาก class GameMultiCoin30
        self.scorep1 = self.game_multi_30_widget.scorep1 
        self.scorep2 = self.game_multi_30_widget.scorep2 
        # Decrement the countdown time if the game is running
        if self.is_game_running:
            self.countdown_time -= 1
        
            # Update the timer label in your game widget
            self.game_multi_30_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"
 
            if self.countdown_time <= 0:
                # Stop the countdown timer when time runs out
                self.stop_countdown()
                if self.scorep1 > self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep1win(None)
                if self.scorep1 < self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep2win(None)
                if self.scorep1 == self.scorep2 :
                    self.soundwin.play()
                    self.stop_gameDraw(None)
 
    def stop_countdown(self):
        if self.schedule is not None:
            # Unschedule the function responsible for updating the countdown timer
            self.schedule.cancel()
    def start_countdown(self):
        if self.is_game_running:  # Check if the game is running
            # Schedule a function to update the countdown timer every second
            self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music4.mp3')
        self.sound.volume = 0.1  # ตั้งระดับเสียงเพลงใหม่
        if self.sound:
            #self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_30_widget.change_character_imageP1(new_image_source)
    def change_character_imageP2(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_30_widget.change_character_imageP2(new_image_source)  
```


```create game multi 30 s
class GameMultiCoin30(Widget) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.timer_label = Label(text="Time left: 30 seconds", pos=(300, 700), size=(200, 200), font_size=20)
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

        self.keepcoinsound = SoundLoader.load('coinkeep.mp3')
        if self.keepcoinsound:
            self.keepcoinsound.volume = 0.7  # ตั้งระดับเสียงเพลงใหม่
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='screen10.jpeg', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            Line(rectangle=(430, 865, 345, 65), width=2)
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(250, 250), size=(140, 140))

            #generate monster charector
            self.monster = Image(source="character2.png", pos=(1700, 250), size=(140, 140))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))


    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if self.parent.is_game_running and self.parent.manager.current == 'multi30':
            self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        if self.parent.is_game_running and self.parent.manager.current == 'multi30':
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


            self.keepcoinsound.play()

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

            self.keepcoinsound.play()


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

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.hero.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "hero"
    def change_character_imageP2(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.monster.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "monster"
```


```create multi 45 s page
#Multi 45 Mode
class GameMultiCoin45Screen(Screen) :
    def __init__(self, **kw):
        super(GameMultiCoin45Screen, self).__init__(**kw)
        self.game_multi_45_widget = GameMultiCoin45()
        self.add_widget(self.game_multi_45_widget)

        self.soundButton = SoundLoader.load('button1.mp3')
        self.soundButton.volume = 0.3  # ตั้งระดับเสียงเพลงใหม่
        self.soundwin = SoundLoader.load('winsound.mp3')
        self.soundwin.volume = 1  # ตั้งระดับเสียงเพลงใหม่

        # Add a "Stop Game" button
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), size=(200, 50), pos_hint={'top': 0.95, 'right': 1})
        self.button_stop_game = Button(text='Stop Game', on_press=self.stop_game, size_hint=(None, None), size=(180, 50))
        layout.add_widget(self.button_stop_game)
        self.add_widget(layout)
        
        self.is_game_running = True  # Flag to track the state of the game
        self.schedule = None  # Initialize the schedule variable

    def stop_game(self, instance):
        self.soundButton.play() 
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Pause', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep1win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()

            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player1 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gamep2win(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()

            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Player2 Win!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def stop_gameDraw(self, instance):
        if self.sound:
            self.sound.stop()
        if self.is_game_running:  # Check if the game is running
            # Pause the game
            self.is_game_running = False
            # Stop the countdown timer
            self.stop_countdown()
            
            # Create a Popup for the player to choose whether to restart the game or go to the main menu
            self.popup = Popup(title='Draw!!!', size_hint=(None, None), size=(450, 200))
            
            # Create buttons for Restart Game and Main Menu
            restart_button = Button(text='Restart Game', size_hint=(None, None), size=(200, 50))
            restart_button.bind(on_press=self.restart_game)
            
            main_menu_button = Button(text='Main Menu', size_hint=(None, None), size=(200, 50))
            main_menu_button.bind(on_press=self.switch_to_main_menu)
            
            # Add buttons to a layout
            button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)
            button_layout.add_widget(restart_button)
            button_layout.add_widget(main_menu_button)
            # Add the layout to the Popup
            self.popup.content = button_layout
            # Open the Popup
            self.popup.open()

    def restart_game(self, instance):
        self.soundButton.play() 
        self.sound.play()
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
            # Start the countdown timer
            self.start_countdown()

            # Dismiss the Popup
            self.popup.dismiss()

            # Reset character positions and scores
            self.game_multi_45_widget.hero.pos = (250, 250)
            self.game_multi_45_widget.monster.pos = (1700, 250)
            self.game_multi_45_widget.scorep1 = 0
            self.game_multi_45_widget.scorep1_label.text = "Score Player 1 : 0"
            self.game_multi_45_widget.scorep2 = 0
            self.game_multi_45_widget.scorep2_label.text = "Score Player 2 : 0"

            # Reset timer label
            self.game_multi_45_widget.timer_label.text = "Time left: 45 seconds"
            self.countdown_time = 45

            self.game_multi_45_widget._keyboard = Window.request_keyboard(self.game_multi_45_widget._on_keyboard_closed, self.game_multi_45_widget)
            self.game_multi_45_widget._keyboard.bind(on_key_down=self.game_multi_45_widget._on_key_down)
            self.game_multi_45_widget._keyboard.bind(on_key_up=self.game_multi_45_widget._on_key_up)

            # Switch back to the game screen
            self.manager.current = 'multi45'

    def switch_to_main_menu(self, instance):
        self.soundButton.play() 
        self.restart_game(None)
        if not self.is_game_running:  # Check if the game is paused
            # Resume the game
            self.is_game_running = True
      
        # Close the Popup
        self.popup.dismiss()
        self.game_multi_45_widget.hero.pos = (250,250)
        self.game_multi_45_widget.monster.pos = (1700,250)

        self.game_multi_45_widget.scorep1 = 0
        self.game_multi_45_widget.scorep1_label.text = "Score Player 1 : 0"
        self.game_multi_45_widget.scorep2 = 0
        self.game_multi_45_widget.scorep2_label.text = "Score Player 2 : 0"

        self.game_multi_45_widget.timer_label.text = "Time left: 45 seconds"
        self.countdown_time = 45
    
        # Switch to the main menu screen
        self.manager.current = 'main_menu'

    def on_pre_enter(self, *args):
        # เริ่มต้นนับถอยหลังเมื่อเข้าหน้าจอ
        self.countdown_time = 45  # ระบุเวลาถอยหลังในวินาที
        self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_pre_leave(self, *args):
        # หยุดนับถอยหลังเมื่อออกจากหน้าจอ
        Clock.unschedule(self.schedule)

    def update_timer(self, dt):
        #เรียกใช้ scorep1 จาก class GameMultiCoin45
        self.scorep1 = self.game_multi_45_widget.scorep1 
        self.scorep2 = self.game_multi_45_widget.scorep2 
        # Decrement the countdown time if the game is running
        if self.is_game_running:
            self.countdown_time -= 1
        
            # Update the timer label in your game widget
            self.game_multi_45_widget.timer_label.text = f"Time left: {self.countdown_time} seconds"
 
            if self.countdown_time <= 0:
                # Stop the countdown timer when time runs out
                self.stop_countdown()
                if self.scorep1 > self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep1win(None)
                if self.scorep1 < self.scorep2 :
                    self.soundwin.play()
                    self.stop_gamep2win(None)
                if self.scorep1 == self.scorep2 :
                    self.soundwin.play()
                    self.stop_gameDraw(None)
 
    def stop_countdown(self):
        if self.schedule is not None:
            # Unschedule the function responsible for updating the countdown timer
            self.schedule.cancel()
    def start_countdown(self):
        if self.is_game_running:  # Check if the game is running
            # Schedule a function to update the countdown timer every second
            self.schedule = Clock.schedule_interval(self.update_timer, 1)

    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music4.mp3')
        self.sound.volume = 0.1  # ตั้งระดับเสียงเพลงใหม่
        if self.sound:
            #self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_45_widget.change_character_imageP1(new_image_source)
    def change_character_imageP2(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละครตามข้อมูลที่รับมา
        self.game_multi_45_widget.change_character_imageP2(new_image_source)  
```


```create game multi 45 s
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

        self.keepcoinsound = SoundLoader.load('coinkeep.mp3')
        if self.keepcoinsound:
            self.keepcoinsound.volume = 0.7  # ตั้งระดับเสียงเพลงใหม่
        

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='screen10.jpeg', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        # add character hero and coin
        with self.canvas:

            Line(rectangle=(30, 865, 345, 65), width=2)  # Rectangle around Score Player 1
            Line(rectangle=(430, 865, 345, 65), width=2)
            #generate cat charector
            self.hero = Image(source="character1.png", pos=(250, 250), size=(140, 140))

            #generate monster charector
            self.monster = Image(source="character2.png", pos=(1700, 250), size=(140, 140))

            #generate coins
            self.coin1 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin2 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))
            self.coin3 = Image(source="coin1.png", pos=(random.randint(0, 700), random.randint(0, 700)), size=(40, 40))


    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = (value[0], value[0]/2.5)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if self.parent.is_game_running and self.parent.manager.current == 'multi45':
            self.pressed_keys.add(text)

    def _on_key_up(self, keyboard, keycode):
        if self.parent.is_game_running and self.parent.manager.current == 'multi45':
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


            self.keepcoinsound.play()

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

            self.keepcoinsound.play()


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

    def change_character_imageP1(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.hero.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "hero"
    def change_character_imageP2(self, new_image_source):
        # ดำเนินการเปลี่ยนรูปภาพตัวละคร
        self.monster.source = new_image_source  # สมมติว่าตัวละครมีชื่อว่า "monster"
```

       
```create change character page
#class หน้าเปรี่ยนตัวละครเลือกระหว่าง P1 เเละ P2
class CharacterApp(Screen):
    def __init__(self, **kwargs):
        super(CharacterApp, self).__init__(**kwargs)

        self.soundButton = SoundLoader.load('button1.mp3')

        layout1 = FloatLayout()

        background = Image(source='screen4.jpg', allow_stretch=True, keep_ratio=False)
        layout1.add_widget(background)

        # สร้าง Layout แนวตั้ง
        layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # สร้างปุ่มไปหน้าP1
        self.button1 = Button(text='Player 1', on_press=self.switch_to_P1, size_hint=(None, None), size=(200, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button1)

        # สร้างปุ่มไปหน้าP2
        self.button1 = Button(text='Player 2', on_press=self.switch_to_P2, size_hint=(None, None), size=(200, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.button1)

        self.back_button = Button(text='Back', on_press=self.switch_to_previous_screen, size_hint=(None, None), size=(200, 50))
        self.back_button.background_color = get_color_from_hex('#9ec0e4')
        layout.add_widget(self.back_button)

        self.add_widget(layout1)
        self.add_widget(layout)
    
    def on_enter(self):
        if self.manager.get_screen('main_menu').sound:
            self.manager.get_screen('main_menu').sound.stop()
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music2.mp3')
        if self.sound:
            self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def switch_to_P1(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'characterP1'

    def switch_to_P2(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'characterP2'

    def switch_to_previous_screen(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.sound.stop()
        #self.manager.get_screen('main_menu').sound.play()
        self.manager.current = 'main_menu'
```


```create change character for player 1 page
#class หน้าเปรี่ยนตัวละครP1
class CharacterAppP1(Screen):
    def __init__(self, **kwargs):
        super(CharacterAppP1, self).__init__(**kwargs)

        self.soundButton = SoundLoader.load('button1.mp3')

        layout1 = FloatLayout()

        background = Image(source='screen6.jpg', allow_stretch=True, keep_ratio=False)
        layout1.add_widget(background)

        # สร้าง Layout แนวนอน
        layout2 = BoxLayout(orientation='horizontal', spacing=300, size_hint=(None, None), pos_hint={'center_x': 0.25, 'center_y': 0.35})

        layout3 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout4 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout5 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #layout6 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None))

        # สร้างปุ่มแรก
        self.image = Image(source='character1.png', size_hint=(None, None), size=(250, 250))
        layout3.add_widget(self.image)
        self.button1 = Button(text='Wakamo', on_press=self.change_character_image1, size_hint=(None, None), size=(250, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout3.add_widget(self.button1)

        self.image = Image(source='character3.png', size_hint=(None, None), size=(250, 250))
        layout4.add_widget(self.image)
        self.button1 = Button(text='Momoi', on_press=self.change_character_image2, size_hint=(None, None), size=(250, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout4.add_widget(self.button1)

        self.image = Image(source='character6.png', size_hint=(None, None), size=(250, 250))
        layout5.add_widget(self.image)
        self.button1 = Button(text='Yuuka', on_press=self.change_character_image3, size_hint=(None, None), size=(250, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout5.add_widget(self.button1)

        # สร้างปุ่มและระบุตำแหน่งด้วย pos_hint
        back_button = Button(text='Back', on_press=self.switch_to_previous_screen, size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.1, 'y': 0.1})
        back_button.background_color = get_color_from_hex('#9ec0e4')
        layout1.add_widget(back_button)

        #head line
        my_label = Label(text='[b]Player 1[/b]', size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.45, 'y': 0.8}, markup=True)
        my_label.font_size = '70sp'
        my_label.color = get_color_from_hex('#1e2925')
        layout1.add_widget(my_label)

        layout2.add_widget(layout3)
        layout2.add_widget(layout4)
        layout2.add_widget(layout5)

        self.add_widget(layout1)
        self.add_widget(layout2)
    
    def on_enter(self):
        '''if self.manager.get_screen('character').sound:
            self.manager.get_screen('character').sound.stop()'''
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music3.mp3')
        if self.sound:
            self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_image1(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        # ส่งข้อมูลเกี่ยวกับการเปลี่ยนรูปภาพตัวละครไปยังหน้าเล่นเกมส์
        self.manager.get_screen('multi45').change_character_imageP1("character1.png")
        self.manager.get_screen('multi30').change_character_imageP1("character1.png")
        self.manager.get_screen('multi15').change_character_imageP1("character1.png")
        self.manager.get_screen('single45').change_character_imageP1("character1.png")
        self.manager.get_screen('single30').change_character_imageP1("character1.png")
        self.manager.get_screen('single15').change_character_imageP1("character1.png")
    
    def change_character_image2(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        # ส่งข้อมูลเกี่ยวกับการเปลี่ยนรูปภาพตัวละครไปยังหน้าเล่นเกมส์
        self.manager.get_screen('multi45').change_character_imageP1("character3.png")
        self.manager.get_screen('multi30').change_character_imageP1("character3.png")
        self.manager.get_screen('multi15').change_character_imageP1("character3.png")
        self.manager.get_screen('single45').change_character_imageP1("character3.png")
        self.manager.get_screen('single30').change_character_imageP1("character3.png")
        self.manager.get_screen('single15').change_character_imageP1("character3.png")

    def change_character_image3(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        # ส่งข้อมูลเกี่ยวกับการเปลี่ยนรูปภาพตัวละครไปยังหน้าเล่นเกมส์
        self.manager.get_screen('multi45').change_character_imageP1("character6.png")
        self.manager.get_screen('multi30').change_character_imageP1("character6.png")
        self.manager.get_screen('multi15').change_character_imageP1("character6.png")
        self.manager.get_screen('single45').change_character_imageP1("character6.png")
        self.manager.get_screen('single30').change_character_imageP1("character6.png")
        self.manager.get_screen('single15').change_character_imageP1("character6.png")

    def switch_to_previous_screen(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'character'
```


```create change character for player 2 page
#class หน้าเปรี่ยนตัวละครP2
class CharacterAppP2(Screen):
    def __init__(self, **kwargs):
        super(CharacterAppP2, self).__init__(**kwargs)

        self.soundButton = SoundLoader.load('button1.mp3')

        layout1 = FloatLayout()

        background = Image(source='screen7.jpg', allow_stretch=True, keep_ratio=False)
        layout1.add_widget(background)

        # สร้าง Layout แนวนอน
        layout2 = BoxLayout(orientation='horizontal', spacing=300, size_hint=(None, None), pos_hint={'center_x': 0.25, 'center_y': 0.35})

        layout3 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout4 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout5 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #layout6 = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None))

        # สร้างปุ่มแรก
        self.image = Image(source='character2.png', size_hint=(None, None), size=(250, 250))
        layout3.add_widget(self.image)
        self.button1 = Button(text='Arisu', on_press=self.change_character_image1, size_hint=(None, None), size=(250, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout3.add_widget(self.button1)

        self.image = Image(source='character4.png', size_hint=(None, None), size=(250, 250))
        layout4.add_widget(self.image)
        self.button1 = Button(text='Midori', on_press=self.change_character_image2, size_hint=(None, None), size=(250, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout4.add_widget(self.button1)

        self.image = Image(source='character5.png', size_hint=(None, None), size=(250, 250))
        layout5.add_widget(self.image)
        self.button1 = Button(text='Yuzu', on_press=self.change_character_image3, size_hint=(None, None), size=(250, 50))
        self.button1.background_color = get_color_from_hex('#9ec0e4')
        layout5.add_widget(self.button1)

        # สร้างปุ่มและระบุตำแหน่งด้วย pos_hint
        back_button = Button(text='Back', on_press=self.switch_to_previous_screen, size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.1, 'y': 0.1})
        back_button.background_color = get_color_from_hex('#9ec0e4')
        layout1.add_widget(back_button)

        #head line
        my_label = Label(text='[b]Player 2[/b]', size_hint=(None, None), size=(200, 50), pos_hint={'x': 0.45, 'y': 0.8}, markup=True)
        my_label.font_size = '70sp'
        my_label.color = get_color_from_hex('#1e2925')
        layout1.add_widget(my_label)

        layout2.add_widget(layout3)
        layout2.add_widget(layout4)
        layout2.add_widget(layout5)

        self.add_widget(layout1)
        self.add_widget(layout2)
    
    def on_enter(self):
        # เริ่มเล่นเพลงเมื่อเข้าหน้า CharacterApp
        self.sound = SoundLoader.load('music3.mp3')
        if self.sound:
            self.sound.volume = 0.2  # ตั้งระดับเสียงเพลงใหม่
            self.sound.play()

    def on_leave(self):
        # หยุดการเล่นเพลงเมื่อออกจากหน้า CharacterApp
        if self.sound:
            self.sound.stop()

    def change_character_image1(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        # ส่งข้อมูลเกี่ยวกับการเปลี่ยนรูปภาพตัวละครไปยังหน้าเล่นเกมส์
        self.manager.get_screen('multi45').change_character_imageP2("character2.png")
    
    def change_character_image2(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        # ส่งข้อมูลเกี่ยวกับการเปลี่ยนรูปภาพตัวละครไปยังหน้าเล่นเกมส์
        self.manager.get_screen('multi45').change_character_imageP2("character4.png")

    def change_character_image3(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        # ส่งข้อมูลเกี่ยวกับการเปลี่ยนรูปภาพตัวละครไปยังหน้าเล่นเกมส์
        self.manager.get_screen('multi45').change_character_imageP2("character5.png")

    def switch_to_previous_screen(self, instance):
        self.soundButton.volume = 0.3  # กำหนดระดับเสียงเป็นครึ่งหนึ่งของระดับเสียงที่มีอยู่เต็มที่
        self.soundButton.play() 
        self.manager.current = 'character'
```


```create link to all page ni my game
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
        game_character_P1 = CharacterAppP1(name='characterP1')
        game_character_P2 = CharacterAppP2(name='characterP2')

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
        self.screen_manager.add_widget(game_character_P1)
        self.screen_manager.add_widget(game_character_P2)

        return self.screen_manager
```


```run my game
if __name__ == '__main__':
    app = MyGame()
    app.run() 
    
```

from kivy.app import App

import random

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color 
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.properties import NumericProperty

# -- His code --

import threading
import kivy.uix.screenmanager
import pygad

# class CollectCoinThread(threading.Thread):

#     def __init__(self, screen):
#         super().__init__()
#         self.screen = screen

#     def run(self):
#         ga_instance = pygad.GA(num_generations=9999,
#                                num_parents_mating=300, 
#                                fitness_func=fitness_func,
#                                sol_per_pop=1000, 
#                                num_genes=2,
#                                init_range_low=0.0,
#                                init_range_high=1.0,
#                                random_mutation_min_val=0.0,
#                                random_mutation_max_val=1.0,
#                                mutation_by_replacement=True,
#                                callback_generation=callback_generation,
#                                delay_after_gen=self.screen.char_anim_duration)
#         ga_instance.run()

# def fitness_func(solution, solution_idx):
#     curr_screen = app.root.screens[lvl_num]

#     coins = curr_screen.coins_ids
#     if len(coins.items()) == 0:
#         return 0

#     curr_coin = coins[list(coins.keys())[0]]

#     curr_coin_center = [curr_coin.pos_hint['x'], curr_coin.pos_hint['y']]

#     output = abs(solution[0] - curr_coin_center[0]) + abs(solution[1] - curr_coin_center[1])
#     output = 1.0 / output

#     monsters_pos = []
#     for i in range(curr_screen.num_monsters):
#         monster_image = curr_screen.ids['monster'+str(i+1)+'_image_lvl'+str(lvl_num)]
#         monsters_pos.append([monster_image.pos_hint['x'], monster_image.pos_hint['y']])

#     for monst_pos in monsters_pos:
#         char_monst_h_distance = abs(solution[0] - monst_pos[0])
#         char_monst_v_distance = abs(solution[1] - monst_pos[1])
#         if char_monst_h_distance <= 0.3 and char_monst_v_distance <= 0.3:
#             output -= 300
#         else:
#             output += 100

#     fires_pos = []
#     for i in range(curr_screen.num_fires):
#         fire_image = curr_screen.ids['fire'+str(i+1)+'_lvl'+str(lvl_num)]
#         fires_pos.append([fire_image.pos_hint['x'], fire_image.pos_hint['y']])

#     for fire_pos in fires_pos:
#         char_fire_h_distance = abs(solution[0] - fire_pos[0])
#         char_fire_v_distance = abs(solution[1] - fire_pos[1])
#         if char_fire_h_distance <= 0.3 and char_fire_v_distance <= 0.3:
#             output -= 300
#         else:
#             output += 100

#     fitness = output
#     return fitness

# last_fitness = 0

# def callback_generation(ga_instance):
#     global last_fitness
    
#     best_sol_fitness = ga_instance.best_solution()[1]
#     fitness_change = best_sol_fitness - last_fitness
#     curr_screen = app.root.screens[lvl_num]

#     last_fitness = best_sol_fitness

#     coins = curr_screen.coins_ids

#     if len(coins.items()) == 0 or curr_screen.character_killed:
#         # After either the level is completed or the character is killed, then stop the GA by returning the string "stop".
#         return "stop"
#     elif len(coins.items()) != 0 and fitness_change != 0:
#         best_sol = ga_instance.best_solution()[0]
#         app.start_char_animation(lvl_num, [float(best_sol[0]),  float(best_sol[1])])



# -- My code --
        
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
        self.pressed_keys =set()
        Clock.schedule_interval(self.move_step, 0)

        with self.canvas.before:
            # Set initial size of Image to match Window size
            self.image = Image(source='GrassMap1.png', size=Window.size, allow_stretch=True, keep_ratio=False)
            # Bind the size of Image to the Window size
            Window.bind(size=self.on_window_size)

        with self.canvas:
            self.hero = Image(source="cat2.png", pos=(250, 250), size=(100, 100))
            self.coin = Image(source = "coin1.png" , pos = (400,400) , size = (50,50))
    

    def on_window_size(self, instance, value):
        # Update the size of Image when the Window size changes
        self.image.size = value

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard =None
        
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

        if 'w' in self.pressed_keys:
            cur_y += step
            self.hero.pos = (cur_x, cur_y)

        if 's' in self.pressed_keys:
            cur_y -= step
            self.hero.pos = (cur_x, cur_y)

        if 'a' in self.pressed_keys:
            cur_x -= step
            self.hero.pos = (cur_x, cur_y)

        if 'd' in self.pressed_keys:
            cur_x += step
            self.hero.pos = (cur_x, cur_y)

        if collides((self.hero.pos, self.hero.size), (self.coin.pos, self.coin.size)):
            print("colliding")
            self.canvas.remove(self.coin)
        else:
            print("not colliding")

class MyGame(App):
    def build(self):

        return GameCoinWidget()
    
if __name__=='__main__':
    app = MyGame()
    app.run()
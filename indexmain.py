import kivy.app
import kivy.uix.screenmanager
import kivy.uix.image
import random
import kivy.core.audio
import os
import functools
import kivy.uix.behaviors
import pickle
import pygad
import threading
import kivy.base

class CollectCoinThread(threading.Thread):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def run(self):
        ga_instance = pygad.GA(num_generations=9999,
                               num_parents_mating=300,
                               sol_per_pop=1000, 
                               num_genes=2,
                               init_range_low=0.0,
                               init_range_high=1.0,
                               random_mutation_min_val=0.0,
                               random_mutation_max_val=1.0,
                               mutation_by_replacement=True)
        ga_instance.run()

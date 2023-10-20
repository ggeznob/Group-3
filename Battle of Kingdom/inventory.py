import pygame
from setting import *
from utils import Text


class Coin:
    def __init__(self, window, coin=init_coin):
        self.window = window
        self.value = coin
        self.text = Text(str(self.value), self.window, ALGER, (0, 255, 0), (0, 0, 0, 0),
                         (screen_width * 0.05, screen_height * 0.9), 40)

    def display(self):
        self.text.draw()

    def change(self, increment):
        self.value += increment
        self.text.change(str(self.value))

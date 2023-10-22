import pygame
from setting import *
from utils import Text


class CoinDisplay:
    def __init__(self, window, coin=init_coin):
        self.window = window
        self.value = coin
        self.text = Text(str(self.value), self.window, ALGER, (0, 255, 0),
                         (coin_box_pos[0] + 20, coin_box_pos[1]), 30)

    def display(self):
        self.text.draw()

    def change(self, increment):
        self.value += increment
        self.text.change(str(self.value))

# import module
import pygame
from level import Level1, Level2, Level3
from surface import MainPage
from setting import *


class Game:
    # initialize game
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Battle of Kingdom")
        self.clock = pygame.time.Clock()
        self.stage = MainPage(self.window)

    # draw surface and flip game
    def playing(self):
        self.stage.event_loop()
        if self.stage.upgrade:
            self.upgrade()
        else:
            self.to_menu()

    # jump to next surface
    def upgrade(self):
        self.window.fill((0, 0, 0))
        if self.stage.stage_num == 0:
            self.stage = Level1(self.window)
            self.playing()
        if self.stage.stage_num == 1:
            self.stage = Level2(self.window)
            self.playing()
        if self.stage.stage_num == 2:
            self.stage = Level3(self.window)
            self.playing()

    def to_menu(self):
        self.window.fill((0, 0, 0))
        self.stage = MainPage(self.window)
        self.playing()


if __name__ == '__main__':
    # start game
    game = Game()
    game.playing()

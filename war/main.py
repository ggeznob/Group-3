# import module
import pygame
import level
import user
from setting import *


class Game:
    PAUSE = False

    # initialize game
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.game_home = user.Home(self.window)
        self.game_level1 = level.Level1(self.window)
        self.game_level2 = level.Level2(self.window)
        self.game_level3 = level.Level3(self.window)

    # draw surface and flip game
    def playing(self, stage=None):
        if not stage:
            stage = self.game_home
        stage.draw_surface()
        stage.functions()
        if stage.upgrade:
            self.upgrade(stage.stage_num)

    # jump to next surface
    def upgrade(self, stage_num):
        if stage_num == 0:
            self.game_home.remove()
            self.playing(self.game_level1)
        if stage_num == 1:
            self.game_level1.remove()
            self.playing(self.game_level2)
        if stage_num == 2:
            self.game_home.remove()
            self.playing(self.game_level1)


if __name__ == '__main__':
    # start game
    game = Game()
    game.playing()

import pygame
import sys

from setting import *
from user import Surface
from inventory import Coin

fightimg = pygame.image.load(fight)
fightimg = pygame.transform.scale(fightimg, (screen_width, screen_height))


class Level1(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.stage_num = 1
        self.background = fightimg
        self.coin = Coin(self.window)

    def draw_surface(self):
        super(Level1, self).draw_surface()
        self.coin.display()

    # for getting events and update game
    def functions(self):
        pause = False
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                # for quiting
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        pause = not pause

            pygame.display.flip()

            clock.tick(fps)

    def remove(self):
        super().remove()


class Level2(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.stage_num = 2

    def draw_surface(self):
        super().draw_surface()

    # for getting events and update game
    def functions(self):
        pause = False
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                # for quiting
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event

                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        pause = not pause

            pygame.display.flip()

            clock.tick(fps)

    def remove(self):
        super().remove()


class Level3(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.stage_num = 2

    def draw_surface(self):
        super().draw_surface()

    # for getting events and update game
    def functions(self):
        pause = False
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                # for quiting
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event

                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        pause = not pause

            pygame.display.flip()

            clock.tick(fps)

    def remove(self):
        super().remove()

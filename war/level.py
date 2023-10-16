import pygame
import sys

from setting import *
from user import Surface, pause
from inventory import Coin
from common_classes import ImageButton, Card
from soldier import Infantry

fightimg = pygame.image.load(fight)
fightimg = pygame.transform.scale(fightimg, (screen_width, screen_height))


class Level1(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.stage_num = 1
        self.background = fightimg
        self.coin = Coin(self.window)
        self.my_soldier = pygame.sprite.Group()
        self.cards = [Card(infantry_card, self.window, (200, 620), 125, 125, Infantry)]
        self.pause = False
        self.b_pause = ImageButton(pause_button, self.window, (110, 35), 220, 70)

    def draw_surface(self):
        super(Level1, self).draw_surface()
        self.coin.display()
        self.b_pause.draw()
        for card in self.cards:
            card.draw()

    # for getting events and update game
    def event_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            if not self.pause:
                self.draw_surface()

            for event in pygame.event.get():
                # for quiting
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if self.b_pause.button_down(pos):
                        self.pause = not self.pause

                    if not self.pause:
                        for card in self.cards:
                            if card.button_down(pos):
                                card.ready = not card.ready
                            elif card.ready:
                                card.ready = not card.ready
                                species = card.species()
                                if self.coin.value + species.cost >= 0:
                                    species.set(pos)
                                    self.my_soldier.add(species)
                                    self.coin.change(species.cost)

                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        self.pause = not self.pause

            if not self.pause:
                self.load_mysoldier()
            else:
                pause(self.window)

            pygame.display.flip()

            clock.tick(fps)

    def remove(self):
        super().remove()

    def load_mysoldier(self):
        self.my_soldier.update()
        self.my_soldier.draw(self.window)


class Level2(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.stage_num = 2

    def draw_surface(self):
        super().draw_surface()

    # for getting events and update game
    def event_loop(self):
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
    def event_loop(self):
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

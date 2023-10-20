import pygame
import sys
from random import randint

from setting import *
from surface import Surface
from inventory import Coin
from utils import ImageButton, TextButton, Card, Map
from tower import Archer, Shield
from enemy import Infantry, Barbarian
from project import spritecollideany_smallratio, Flag

fightimg = pygame.transform.scale(pygame.image.load(fight), (screen_width, screen_height))
pauseimg = pygame.transform.scale(pygame.image.load(pause_page), (screen_width, screen_height))


class Level1(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.stage_num = 1
        self.background = fightimg
        self.coin = Coin(self.window)
        self.my_soldier = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.ornament = pygame.sprite.Group()
        self.projectile = pygame.sprite.Group()
        self.cards = [Card(shield_card, self.window, Shield, 1),
                      Card(archer_card, self.window, Archer, 2)]
        self.choose = None
        self.map = Map()
        self.pause = False
        self.b_pause = ImageButton(pause_button, self.window, (110, 35), 220, 70)
        self.last_wave_time = pygame.time.get_ticks()
        self.wave_num = 0
        self.b_back = ImageButton(back_button, window, (screen_center[0], 375), 150, 60)
        self.b_continue = ImageButton(continue_button, window, (screen_center[0], 225), 220, 60)
        self.waves = level1
        self.time_interval = self.waves[-1]

    def draw_surface(self):
        super(Level1, self).draw_surface()
        if self.pause:
            self.b_back.draw()
            self.b_continue.draw()
        else:
            self.b_pause.draw()
            self.coin.display()
            for card in self.cards:
                card.draw()

    # for getting events and update game
    def event_loop(self):
        clock = pygame.time.Clock()
        while self.running:

            self.draw_surface()

            for event in pygame.event.get():
                # for quiting
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    print(pos)

                    if not self.pause:
                        self.set_my_soldier(pos)

                        if self.b_pause.button_down(pos):
                            self.pause = True
                            self.background = pauseimg

                    else:
                        if self.b_continue.button_down(pos):
                            self.pause = False
                            self.background = fightimg

                        elif self.b_exit.button_down(pos):
                            self.upgrade = False
                            self.running = False

            if not self.pause:
                self.load_ornament()
                self.load_my_soldier()
                self.load_enemy()
                self.load_projectile()
                self.deal_wave()

            pygame.display.flip()
            clock.tick(fps)

    def remove(self):
        super().remove()

    def load_my_soldier(self):
        for my_soldier in self.my_soldier:
            if not my_soldier.live:
                if my_soldier.state != "dying":
                    my_soldier.y = 0
                    my_soldier.state = "dying"
                    self.map.get_cell(my_soldier.rect.center).is_empty = True

            else:
                if type(my_soldier) == Archer:
                    if my_soldier.spot(self.enemy):
                        if my_soldier.state == 'idle':
                            my_soldier.state = 'shooting'
                        my_soldier.shoot(self.projectile)
                    else:
                        if my_soldier.state == "shooting":
                            my_soldier.state = "idle"

                elif type(my_soldier) == Shield:
                    enemy = spritecollideany_smallratio(my_soldier, self.enemy)
                    if enemy:
                        if my_soldier.state == 'idle':
                            my_soldier.state = 'attacking'
                        my_soldier.attack(enemy)
                    else:
                        if my_soldier.state == "attacking":
                            my_soldier.state = "idle"

        self.my_soldier.update()
        self.my_soldier.draw(self.window)

    def load_enemy(self):
        for enemy in self.enemy:
            my_soldier = spritecollideany_smallratio(enemy, self.my_soldier)
            if my_soldier:
                if enemy.state == "walking":
                    enemy.state = "attacking"
                enemy.attack(my_soldier)
            else:
                if enemy.state == "attacking":
                    enemy.state = "walking"
            if not enemy.live:
                if enemy.state != "dying":
                    enemy.state = "dying"
                    self.coin.change(enemy.reward)
                    enemy.y = 0
        self.enemy.update()
        self.enemy.draw(self.window)

    def load_projectile(self):
        self.projectile.update(self.enemy)
        self.projectile.draw(self.window)

    def load_ornament(self):
        if not len(self.ornament):
            for i in range(4):
                self.ornament.add(Flag(i))

        self.ornament.update()
        self.ornament.draw(self.window)

    def set_my_soldier(self, pos):
        for card in self.cards:
            if card.button_down(pos):
                if self.choose == card.species:
                    self.choose = None
                else:
                    self.choose = card.species
            elif self.choose and map_point1[0] <= pos[0] < map_point2[0] and map_point1[1] <= pos[1] < map_point2[1]:
                species = self.choose()
                if self.coin.value + species.cost >= 0:
                    cell = self.map.get_cell(pos)
                    if cell.is_empty:
                        species.set((cell.center[0] + randint(-5, 5), cell.center[1] + randint(-5, 5)))
                        self.my_soldier.add(species)
                        self.coin.change(species.cost)
                        self.choose = None
                        cell.is_empty = False

    def wave(self):
        wave = self.waves[self.wave_num]
        for i in range(len(wave[0])):
            for k in range(wave[1][i]):
                enemy = wave[0][i]
                if enemy == 'infantry':
                    enemy = Infantry()
                    enemy.set((screen_width + randint(-50, 100), rows[randint(0, 3)] + randint(-5, 5)))
                elif enemy == 'barbarian':
                    enemy = Barbarian()
                    enemy.set((screen_width + randint(-50, 100), rows[randint(0, 3)] + randint(-5, 5)))
                self.enemy.add(enemy)

    def deal_wave(self):
        current_time = pygame.time.get_ticks()
        if self.wave_num == 0:
            if current_time - self.last_wave_time >= 1000 * self.time_interval[self.wave_num]:
                self.wave()
                self.wave_num += 1
                self.last_wave_time = current_time
        elif self.wave_num == 1:
            if current_time - self.last_wave_time >= 1000 * self.time_interval[self.wave_num]:
                self.wave()
                self.wave_num += 1
                self.last_wave_time = current_time
        elif self.wave_num == 2:
            if current_time - self.last_wave_time >= 1000 * self.time_interval[self.wave_num]:
                self.wave()
                self.wave_num += 1
                self.last_wave_time = current_time
        elif self.wave_num == 3:
            if current_time - self.last_wave_time >= 1000 * self.time_interval[self.wave_num]:
                self.wave()
                self.wave_num += 1
                self.last_wave_time = current_time


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

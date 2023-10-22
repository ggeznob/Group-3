import pygame
import sys
from random import randint, sample

from setting import *
from surface import Surface
from inventory import CoinDisplay
from utils import ImageButton, Card, Map, Image
from tower import Infantry, Archer, Shield, Fairy, King, Archmage, Manipulator, Miner
from enemy import Viking, Barbarian, Ogre, Elementals, Masker
from project import Flag, Campfire

pauseimg = pygame.transform.scale(pygame.image.load(pause_page), (screen_width, screen_height))
fightimg = pygame.transform.scale(pygame.image.load(fight), (screen_width, screen_height))


class Level1(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.stage_num = 1

        self.background = fightimg
        self.image = [Image(coin_box, self.window, coin_box_pos, coin_box_size[0], coin_box_size[1])]
        self.b_back = ImageButton(back_button, window, (screen_center[0], 450), 175, 70)
        self.b_continue = ImageButton(continue_button, window, (screen_center[0], 250), 250, 75)
        self.b_pause = ImageButton(pause_button, self.window, (110, 35), 180, 60)
        self.coin_box = CoinDisplay(self.window)

        self.tower = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.ornament = pygame.sprite.Group()
        self.my_projectile = pygame.sprite.Group()
        self.other_projectile = pygame.sprite.Group()
        self.kings = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()

        self.cards = [Card(miner_card, self.window, Miner, 1),
                      Card(infantry_card, self.window, Infantry, 2),
                      Card(archer_card, self.window, Archer, 3),
                      Card(shield_card, self.window, Shield, 4),
                      Card(fairy_card, self.window, Fairy, 5),
                      Card(archmage_card, self.window, Archmage, 6),
                      Card(manipulator_card, self.window, Manipulator, 7)]
        self.choose = None

        self.map = Map()
        self.waves = level1
        self.next_wave = 0
        self.last_wave_time = pygame.time.get_ticks()

        self.pause = False
        self.init_king()

    def draw_surface(self):
        super(Level1, self).draw_surface()
        if self.pause:
            self.b_back.draw()
            self.b_continue.draw()
        else:
            self.b_pause.draw()
            for image in self.image:
                image.draw()
            self.coin_box.display()

    # for getting events and update game
    def event_loop(self):
        clock = pygame.time.Clock()
        while self.running:

            self.draw_surface()

            mouse_pos = pygame.mouse.get_pos()
            if not self.pause:
                # self.check_game()
                self.show(mouse_pos)
                self.load_ornament()
                self.load_tower()
                self.load_enemy()
                self.load_projectile()
                self.deal_wave()
                self.load_coin()
                for card in self.cards:
                    card.draw()

            for event in pygame.event.get():
                # for quiting
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                    if not self.pause:
                        self.set_tower(pos)
                        self.clic_coin(pos)

                        if self.b_pause.button_down(pos):
                            self.pause = True
                            self.background = pauseimg

                    else:
                        if self.b_continue.button_down(pos):
                            self.pause = False
                            self.background = fightimg

                        elif self.b_back.button_down(pos):
                            self.upgrade = False
                            self.running = False

            pygame.display.flip()
            clock.tick(fps)

    def remove(self):
        super().remove()

    def load_tower(self):
        for my_soldier in self.tower:
            if not my_soldier.live:
                if my_soldier.state != "dying":
                    my_soldier.y = 0
                    my_soldier.state = "dying"
                    if my_soldier.name != 'KING':
                        self.map.get_cell(my_soldier.rect.center).is_empty = True

        self.tower.update(enemies=self.enemy, projectiles=self.my_projectile, towers=self.tower, coins=self.coin)
        self.tower.draw(self.window)

    def load_enemy(self):
        for enemy in self.enemy:
            if not enemy.live:
                if enemy.state != "dying":
                    enemy.y = 0
                    enemy.state = "dying"
                    self.coin_box.change(enemy.reward)
        self.enemy.update(self.tower, self.other_projectile)
        self.enemy.draw(self.window)

    def load_projectile(self):
        self.other_projectile.update(self.tower)
        self.other_projectile.draw(self.window)
        self.my_projectile.update(enemy_group=self.enemy, tower_group=self.tower)
        self.my_projectile.draw(self.window)

    def load_ornament(self):
        if not len(self.ornament):
            for i in range(6):
                flag = Flag(i)
                self.ornament.add(flag)
            for i in range(2):
                campfire = Campfire(i)
                self.ornament.add(campfire)

        self.ornament.update()
        self.ornament.draw(self.window)

    def load_coin(self):
        self.coin.update(self.coin_box)
        self.coin.draw(self.window)

    def clic_coin(self, pos):
        self.coin.update(self.coin_box, pos)

    def set_tower(self, pos):
        for card in self.cards:
            if card.button_down(pos):
                if self.choose == card:
                    self.choose = None
                else:
                    self.choose = card

        if self.choose and map_point1[0] <= pos[0] < map_point2[0] and map_point1[1] <= pos[1] < map_point2[1]:
            if self.choose.ready:
                species = self.choose.species()
                if self.coin_box.value + species.cost >= 0:
                    cell = self.map.get_cell(pos)
                    if cell.is_empty:
                        species.set((cell.center[0] + randint(-5, 5), cell.center[1] + randint(-5, 5)))
                        self.tower.add(species)
                        self.coin_box.change(species.cost)
                        cell.is_empty = False
                        self.choose.ready = False
                        self.choose.start_time = pygame.time.get_ticks()
                        self.choose = None

    def show(self, pos):
        if self.choose:
            if map_point1[0] <= pos[0] < map_point2[0] and map_point1[1] <= pos[1] < map_point2[1]:
                cell = self.map.get_cell(pos)
                if cell.is_empty:
                    rect = self.choose.pre_image.get_rect()
                    rect.center = cell.center
                    self.window.blit(self.choose.pre_image, rect)

    def init_king(self):
        if not len(self.kings):
            king_num = sample(range(0, 3), 3)
            for i in range(3):
                king = King(king_num[i])
                king.set((110, rows[i]))
                self.kings.add(king)
                self.tower.add(king)
            king = King(randint(0, 2))
            king.set((110, rows[3]))
            self.kings.add(king)
            self.tower.add(king)

    def check_game(self):
        if len(self.kings) < 4:
            self.upgrade = False
            self.running = False
        if not self.waves[self.next_wave]:
            if not len(self.enemy):
                self.upgrade = False
                self.running = False

    def wave(self):
        wave = self.waves[self.next_wave]
        for i in range(len(wave[0])):
            for k in range(wave[1][i]):
                row = rows[randint(0, 3)]
                enemy = wave[0][i]
                if enemy == VIKING:
                    enemy = Viking()
                    enemy.set((screen_width + randint(-50, 100), row + randint(-5, 5)))
                elif enemy == BARBARIAN:
                    enemy = Barbarian()
                    enemy.set((screen_width + randint(-50, 100), row + randint(-5, 5)))
                elif enemy == OGRE:
                    enemy = Ogre()
                    enemy.set((screen_width + randint(-50, 100), row + randint(-5, 5)))
                elif enemy == ELEMENTALS:
                    enemy = Elementals()
                    enemy.set((screen_width + randint(-50, 100), row + randint(-5, 5)))
                elif enemy == MASKER:
                    enemy = Masker()
                    enemy.set((screen_width + randint(-50, 100), row + randint(-5, 5)))
                self.enemy.add(enemy)

    def deal_wave(self):
        current_time = pygame.time.get_ticks()
        if self.waves[self.next_wave]:
            if current_time - self.last_wave_time >= 1000 * self.waves[self.next_wave][2]:
                self.wave()
                self.next_wave += 1
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

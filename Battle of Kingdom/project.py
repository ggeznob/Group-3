import pygame
import math

from utils import Button
from random import randint
from setting import *

coin_all_image = pygame.transform.scale(pygame.image.load(coin_image), (coin_size[0], coin_size[1] * 6))

projectile_image = {'arrow': pygame.transform.scale(pygame.image.load(arrow_image), (arrow_size[0], arrow_size[1])),
                    'shell': pygame.transform.scale(pygame.image.load(shell_image), (shell_size[0], shell_size[1])),
                    'ele_slash': pygame.transform.scale(pygame.image.load(elementals_slash),
                                                        (slash_size[0], slash_size[1])),
                    'fairy_spells': pygame.transform.scale(pygame.image.load(fairy_spells),
                                                           (spells_size[0], spells_size[1])),
                    'big_spells': pygame.transform.scale(pygame.image.load(big_spells),
                                                         (spells_size[0] * 1.5, spells_size[1] * 1.5)),
                    'vector_spells': pygame.transform.scale(pygame.image.load(vector_spells),
                                                            (spells_size[0], spells_size[1]))}

flags_image = [pygame.transform.scale(pygame.image.load(flags[0]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[1]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[2]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[3]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[4]), (flag_size[0] * 6, flag_size[1]))]
flag_x = [randint(424, 586), randint(606, 768), randint(788, 950), randint(1114, 1240), randint(566, 804),
          randint(1138, 1186)]
flag_y = [randint(148, 206), randint(100, 171), randint(163, 183)]

campfires_image = [pygame.transform.scale(pygame.image.load(campfires[0]), (campfire_size[0] * 6, campfire_size[1])),
                   pygame.transform.scale(pygame.image.load(campfires[1]),
                                          (campfire_size[0] * 6, campfire_size[1] / 2))]


class Coin(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, coin_size[0], coin_size[1]
        self.end_point = coin_box_pos
        self.dx = self.end_point[0] - self.rect_x
        self.dy = self.end_point[1] - self.rect_y
        self.distance = pygame.math.Vector2(self.dx, self.dy).length()
        self.speed = 0.02 * self.distance
        self.all_image = coin_all_image
        self.image = self.all_image.subsurface((0, 0, self.width, self.height))
        self.y = 0
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.direction = pygame.math.Vector2(self.dx, self.dy).normalize()
        self.move = self.direction * self.speed
        self.click = Button((self.rect_x, self.rect_y), coin_size[0], coin_size[1])
        self.clicked = False
        self.money = randint(25, 50)

    def update(self, coin, pos=None):
        if self.y < self.all_image.get_rect().h:
            if self.y % self.height == 0:
                self.image = self.all_image.subsurface((0, self.y, self.width, self.height))
            self.y += 10
        else:
            self.y = 0
            self.image = self.all_image.subsurface((self.y, 0, self.width, self.height))
        if pos:
            if self.click.button_down(pos):
                self.clicked = True
        if self.clicked:
            self.rect_x += self.move.x
            self.rect_y += self.move.y
            self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
            self.get(coin)

    def get(self, coin):
        if self.rect_x <= self.end_point[0] and self.rect_y <= self.end_point[1]:
            coin.change(self.money)
            self.kill()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, arrow_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, arrow_size[0], arrow_size[1]
        self.speed = 10
        self.image = projectile_image['arrow']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = arrow_damage

    def update(self, enemy_group, tower_group=None):
        self.rect_x += self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)

    def hit(self, enemy_group):
        target = collide(self, enemy_group, 0.5)
        if target:
            target.take_damage(self.damage)
            self.kill()


class OtherSlash(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, slash_damage, species):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, shell_size[0], slash_size[1]
        self.speed = 7
        if species == 'ELEMENTALS':
            self.image = projectile_image['ele_slash']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = slash_damage

    def update(self, enemy_group):
        self.rect_x -= self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)

    def hit(self, enemy_group):
        target = collide(self, enemy_group, 0.3)
        if target:
            target.take_damage(self.damage)
            self.kill()


class FairySpells(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, end_point, spells_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, shell_size[0], spells_size[1]
        self.speed = 5
        self.image = projectile_image['fairy_spells']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = spells_damage
        self.direction = pygame.math.Vector2(end_point[0] - self.rect_x, end_point[1] - self.rect_y).normalize()
        self.move = self.direction * self.speed

    def update(self, enemy_group=None, tower_group=None):
        self.rect_x += self.move.x
        self.rect_y += self.move.y
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(tower_group)

    def hit(self, tower_group):
        filtered_sprites = [sprite for sprite in tower_group if sprite.name != "FAIRY"]
        target = collide(self, filtered_sprites, 0.5)
        if target:
            target.take_damage(self.damage)
            self.kill()


class BigSpells(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, spells_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, spells_size[0] * 1.5, spells_size[1] * 1.5
        self.speed = 5
        self.image = projectile_image['big_spells']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = spells_damage

    def update(self, enemy_group, tower_group=None):
        self.rect_x += self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)

    def hit(self, enemy_group):
        target = collide(self, enemy_group, 0.5)
        if target:
            targets = collide_group(self, enemy_group, 1)
            for enemy in targets:
                enemy.take_damage(self.damage)
            self.kill()


class VectorSpells(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, arrow_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, spells_size[0], spells_size[1]
        self.speed = 8
        self.image = projectile_image['vector_spells']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = arrow_damage

    def update(self, enemy_group, tower_group=None):
        self.rect_x += self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemy_group)

    def hit(self, enemy_group):
        target = collide(self, enemy_group, 0.5)
        if target:
            target.rect_x += 15
            target.take_damage(self.damage)
            self.kill()


class Shell(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, end_x, shell_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, shell_size[0], shell_size[1]
        self.end_x = end_x
        self.distance = self.end_x - self.rect_x
        self.speed_x, self.h = 8, self.distance / 8
        self.gravity = 0.1
        self.speed_y = self.speed_x / 4
        self.image = projectile_image['shell']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = shell_damage

    def update(self, enemies):
        self.rect_x += self.speed_x
        self.rect_y = self.rect_x * self.rect_x * 2 / (self.distance * self.distance) * self.h
        angle = math.degrees(math.atan(self.rect_x * 2 / self.distance))
        self.image = pygame.transform.rotate(self.image, angle)
        if self.rect_x >= self.end_x:
            self.hit(enemies)

    def hit(self, enemies):
        target = collide_group(self, enemies, 2)
        if target:
            for enemy in target:
                enemy.take_damage(self.damage)
            self.kill()


class Flag(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.number = num
        if self.number == 5:
            self.all_image = flags_image[randint(0, 2)]
        else:
            self.all_image = flags_image[self.number]
        self.width, self.height = flag_size[0], flag_size[1]
        if self.number <= 4:
            if self.number == 4:
                self.rect = pygame.Rect(flag_x[self.number], flag_y[1], self.width, self.height)
            else:
                self.rect = pygame.Rect(flag_x[self.number], flag_y[0], self.width, self.height)
        else:
            self.rect = pygame.Rect(flag_x[self.number], flag_y[2], self.width, self.height)
        self.x = randint(0, 5) * self.width
        self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))

    def update(self):
        if self.x < self.all_image.get_rect().w:
            if self.x % self.width == 0:
                self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))
            self.x += 10
        else:
            self.x = 0
            self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))


class Campfire(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.number = num
        self.all_image = campfires_image[self.number]
        if self.number:
            self.width, self.height = campfire_size[0], campfire_size[1] / 2
        else:
            self.width, self.height = campfire_size[0], campfire_size[1]
        self.rect = pygame.Rect(campfire_x, campfire_y[self.number], self.width, self.height)
        self.x = 0
        self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))

    def update(self):
        if self.x < self.all_image.get_rect().w:
            if self.x % self.width == 0:
                self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))
            self.x += 5
        else:
            self.x = 0
            self.image = self.all_image.subsurface((self.x, 0, self.width, self.height))


def collide(sprite, sprite_group, extent):
    collide_circle_small_ratio = pygame.sprite.collide_circle_ratio(extent)
    for spr in sprite_group:
        if collide_circle_small_ratio(sprite, spr):
            return spr


def collide_group(sprite, sprite_group, extent):
    collide_circle_large_ratio = pygame.sprite.collide_circle_ratio(extent)
    target = []
    for spr in sprite_group:
        if collide_circle_large_ratio(sprite, spr):
            target.append(spr)
    return target

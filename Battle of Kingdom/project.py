import pygame
import math

from random import randint
from setting import *

project_image = {'arrow': pygame.transform.scale(pygame.image.load(arrow_image), (arrow_size[0], arrow_size[1])),
                 'shell': pygame.transform.scale(pygame.image.load(shell_image), (shell_size[0], shell_size[1]))}

flags_image = [pygame.transform.scale(pygame.image.load(flags[0]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[1]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[2]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[3]), (flag_size[0] * 6, flag_size[1])),
               pygame.transform.scale(pygame.image.load(flags[4]), (flag_size[0] * 6, flag_size[1]))]
flag_x = [randint(424, 586), randint(606, 768), randint(788, 950), randint(1134, 1260), randint(494, 668)]
flag_y = [randint(148, 206), randint(646, 712)]

campfires_image = [pygame.transform.scale(pygame.image.load(campfires[0]), (campfire_size[0], campfire_size[1] * 6)),
                   pygame.transform.scale(pygame.image.load(campfires[1]), (campfire_size[0], campfire_size[1] * 6))]


class Arrow(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, arrow_damage):
        super().__init__()
        self.rect_x, self.rect_y, self.width, self.height = start_x, start_y, arrow_size[0], arrow_size[1]
        self.speed = 10
        self.image = project_image['arrow']
        self.rect = self.image.get_rect()
        self.rect.center = (self.rect_x, self.rect_y)
        self.damage = arrow_damage

    def update(self, enemies):
        self.rect_x += self.speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))
        self.hit(enemies)

    def hit(self, enemies):
        target = spritecollideany_smallratio(self, enemies)
        if target:
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
        self.image = project_image['shell']
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
        target = groupcollide_largeratio(self, enemies)
        if target:
            for enemy in target:
                enemy.take_damage(self.damage)
            self.kill()


class Flag(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.number = num
        self.all_image = flags_image[self.number]
        self.width, self.height = flag_size[0], flag_size[1]
        if self.number <= 3:
            self.rect = pygame.Rect(flag_x[self.number], flag_y[0], self.width, self.height)
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


collide_circle_small_ratio = pygame.sprite.collide_circle_ratio(0.5)
collide_circle_large_ratio = pygame.sprite.collide_circle_ratio(2)


def spritecollideany_smallratio(sprite, sprite_group):
    for spr in sprite_group:
        if collide_circle_small_ratio(sprite, spr):
            return spr


def groupcollide_largeratio(sprite, sprite_group):
    target = []
    for spr in sprite_group:
        if collide_circle_large_ratio(sprite, spr):
            target.append(spr)
    return target

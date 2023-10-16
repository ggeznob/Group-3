import pygame

from setting import *


class Infantry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_image = pygame.transform.scale(pygame.image.load(infantry_attack), (100, 200))
        self.width = 100
        self.height = 100
        self.image = self.all_image.subsurface((0, 0, self.width, self.height))
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.y = 0
        self.rect_x = 0
        self.rect_y = 0
        self.cost = cost["infantry"]
        # self.HP =
        # self.attack =

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]

    def update(self):
        if self.y < self.all_image.get_rect().h:
            if self.y % self.width == 0:
                self.image = self.all_image.subsurface((0, self.y, self.width, self.height))
            self.y += 10
        else:
            self.y = 0
            self.image = self.all_image.subsurface((0, self.y, self.width, self.height))
        self.move()

    def move(self):
        self.rect_x += 1
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

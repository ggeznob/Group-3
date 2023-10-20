import pygame
from random import randint

from setting import *

walking_all_image = {enemy_type[0]: pygame.transform.scale(pygame.image.load(infantry_walking), (
    infantry_size[0], infantry_size[1] * num_image[enemy_type[0]]["walking"])),
                     enemy_type[1]: pygame.transform.scale(pygame.image.load(barbarian_walking), (
                         barbarian_size[0], barbarian_size[1] * num_image[enemy_type[1]]["walking"]))}

attack_all_image = {enemy_type[0]: pygame.transform.scale(pygame.image.load(infantry_attacking), (
    infantry_size[0], infantry_size[1] * num_image[enemy_type[0]]["attacking"])),
                    enemy_type[1]: pygame.transform.scale(pygame.image.load(barbarian_attacking), (
                        barbarian_size[0], barbarian_size[1] * num_image[enemy_type[1]]["attacking"]))}

dying_all_image = {enemy_type[0]: pygame.transform.scale(pygame.image.load(infantry_dying), (
    infantry_size[0], infantry_size[1] * num_image[enemy_type[0]]["dying"])),
                   enemy_type[1]: pygame.transform.scale(pygame.image.load(barbarian_dying), (
                       barbarian_size[0], barbarian_size[1] * num_image[enemy_type[1]]["dying"]))}


class Infantry(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, soldier_size[0] * 1.2, soldier_size[1] * 1.2
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.walking_all_image = walking_all_image['infantry']
        self.attacking_all_image = attack_all_image['infantry']
        self.dying_all_image = dying_all_image['infantry']
        self.y = randint(0, num_image["infantry"]["attacking"] - 1) * self.width
        self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))

        # value
        self.HP = HP_value["infantry"]
        self.damage = damage_value["infantry"]
        self.attack_speed = attack_interval["infantry"]
        self.move_speed = move_speed["infantry"]
        self.reward = reward_value["infantry"]
        self.state = "walking"
        self.live = True
        # other
        self.cell = None
        self.last_attack_time = 0

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]

    def update(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.kill()

    def move(self):
        self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000 * self.attack_speed:
            soldier.take_damage(self.damage)
            self.last_attack_time = pygame.time.get_ticks()


class Barbarian(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, soldier_size[0] * 1.2, soldier_size[1] * 1.2
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.walking_all_image = walking_all_image['barbarian']
        self.attacking_all_image = attack_all_image['barbarian']
        self.dying_all_image = dying_all_image['barbarian']
        self.y = randint(0, num_image["barbarian"]["attacking"] - 1) * self.width
        self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))

        # value
        self.HP = HP_value["barbarian"]
        self.damage = damage_value["barbarian"]
        self.attack_interval = attack_interval["barbarian"]
        self.move_speed = move_speed["barbarian"]
        self.reward = reward_value["barbarian"]
        self.state = "walking"
        self.live = True
        # other
        self.cell = None
        self.last_attack_time = 0

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]

    def update(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 30
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.kill()

    def move(self):
        self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000 * self.attack_interval:
            soldier.take_damage(self.damage)
            self.last_attack_time = pygame.time.get_ticks()

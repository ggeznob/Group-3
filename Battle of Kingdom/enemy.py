import pygame
from random import randint

from setting import *
from project import collide, OtherSlash

walking_all_image = {
    enemy_type[0]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[0]]),
                                          (enemy_size[enemy_type[0]][0],
                                           enemy_size[enemy_type[0]][1] * num_image[enemy_type[0]]["walking"])),

    enemy_type[1]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[1]]),
                                          (enemy_size[enemy_type[1]][0],
                                           enemy_size[enemy_type[1]][1] * num_image[enemy_type[1]]["walking"])),

    enemy_type[2]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[2]]),
                                          (enemy_size[enemy_type[2]][0],
                                           enemy_size[enemy_type[2]][1] * num_image[enemy_type[2]]["walking"])),

    enemy_type[3]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["walking"])),

    enemy_type[4]: pygame.transform.scale(pygame.image.load(walking_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["walking"]))}


attack_all_image = {
    enemy_type[0]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[0]]),
                                          (enemy_size[enemy_type[0]][0],
                                           enemy_size[enemy_type[0]][1] * num_image[enemy_type[0]]["attacking"])),

    enemy_type[1]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[1]]),
                                          (enemy_size[enemy_type[1]][0],
                                           enemy_size[enemy_type[1]][1] * num_image[enemy_type[1]]["attacking"])),

    enemy_type[2]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[2]]),
                                          (enemy_size[enemy_type[2]][0],
                                           enemy_size[enemy_type[2]][1] * num_image[enemy_type[2]]["attacking"])),

    enemy_type[3]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["attacking"])),

    enemy_type[4]: pygame.transform.scale(pygame.image.load(attacking_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["attacking"]))}


dying_all_image = {
    enemy_type[0]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[0]]),
                                          (enemy_size[enemy_type[0]][0],
                                           enemy_size[enemy_type[0]][1] * num_image[enemy_type[0]]["dying"])),

    enemy_type[1]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[1]]),
                                          (enemy_size[enemy_type[1]][0],
                                           enemy_size[enemy_type[1]][1] * num_image[enemy_type[1]]["dying"])),

    enemy_type[2]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[2]]),
                                          (enemy_size[enemy_type[2]][0],
                                           enemy_size[enemy_type[2]][1] * num_image[enemy_type[2]]["dying"])),

    enemy_type[3]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["dying"])),

    enemy_type[4]: pygame.transform.scale(pygame.image.load(dying_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["dying"]))}


ability_all_image = {
    enemy_type[3]: pygame.transform.scale(pygame.image.load(ability_images[enemy_type[3]]),
                                          (enemy_size[enemy_type[3]][0],
                                           enemy_size[enemy_type[3]][1] * num_image[enemy_type[3]]["run_attacking"])),
    enemy_type[4]: pygame.transform.scale(pygame.image.load(ability_images[enemy_type[4]]),
                                          (enemy_size[enemy_type[4]][0],
                                           enemy_size[enemy_type[4]][1] * num_image[enemy_type[4]]["sliding"]))
}


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, enemy_size[self.name][0], enemy_size[self.name][1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.walking_all_image = walking_all_image[self.name]
        self.attacking_all_image = attack_all_image[self.name]
        self.dying_all_image = dying_all_image[self.name]
        self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
        # value
        self.HP = HP_value[self.name]
        self.damage = damage_value[self.name]
        self.move_speed = move_speed[self.name]
        self.reward = reward_value[self.name]
        self.live = True
        self.state = "walking"
        # other
        self.last_attack_time = 0

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]


class Viking(Enemy):
    def __init__(self):
        self.name = 'VIKING'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size['VIKING'][1]
        super().__init__()

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.5)
        if opponent:
            if self.state == 'walking':
                self.state = 'attacking'
            if self.y == 1000:
                self.attack(opponent)
        else:
            if self.state == "attacking":
                self.state = "walking"
        self.update_image()

    def set(self, pos):
        super().set(pos)

    def move(self):
        if self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        soldier.take_damage(self.damage)


class Barbarian(Enemy):
    def __init__(self):
        self.name = 'BARBARIAN'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size['BARBARIAN'][1]
        super().__init__()

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 30
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.5)
        if opponent:
            if self.state == 'walking':
                self.state = 'attacking'
            if self.y == 1100:
                self.attack(opponent)
        else:
            if self.state == "attacking":
                self.state = "walking"
        self.update_image()

    def move(self):
        if self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def set(self, pos):
        super().set(pos)

    def take_damage(self, damage):
        super().take_damage(damage)

    def attack(self, soldier):
        soldier.take_damage(self.damage)


class Elementals(Enemy):
    def __init__(self):
        self.name = 'ELEMENTALS'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size[enemy_type[3]][1]
        super().__init__()
        self.ability_all_image = ability_all_image[self.name]

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "run_attacking":
            if self.y < self.ability_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles):
        if self.live:
            collide_opponent = collide(self, opponents, 0.5)
            if collide_opponent:
                if self.state != 'attacking':
                    self.state = 'attacking'
                if self.y == 700:
                    self.attack(collide_opponent)
            else:
                if self.spot(opponents):
                    if self.state != "run_attacking":
                        self.state = "run_attacking"
                    if self.y == 600:
                        self.run_attack(projectiles)
                else:
                    if self.state != 'walking':
                        self.state = 'walking'
        self.update_image()

    def set(self, pos):
        super().set(pos)

    def move(self):
        if self.state == 'run_attacking':
            self.rect_x -= (self.move_speed - 0.25)
        elif self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        soldier.take_damage(self.damage)

    def run_attack(self, projectiles):
        slash = OtherSlash(self.rect_x, self.rect_y, self.damage, self.name)
        projectiles.add(slash)

    def spot(self, opponent_group):
        if self.live:
            for enemy in opponent_group:
                if -15 <= self.rect_y - enemy.rect_y <= 15 and self.rect_x <= enemy.rect_x + attack_range[self.name]:
                    return True


class Masker(Enemy):
    def __init__(self):
        self.name = 'MASKER'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size[enemy_type[4]][1]
        super().__init__()
        self.ability_all_image = ability_all_image[self.name]
        self.state = 'sliding'

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "sliding":
            if self.y < self.ability_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.ability_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.5)
        if opponent:
            if self.state == 'sliding':
                self.attack(opponent)
                self.state = 'attacking'
            else:
                if self.state != 'attacking':
                    self.state = 'attacking'
                if self.y == 600:
                    self.attack(opponent)
        else:
            if self.state != 'sliding':
                if self.state != "walking":
                    self.state = "walking"
        self.update_image()

    def set(self, pos):
        super().set(pos)

    def move(self):
        if self.state == 'sliding':
            self.rect_x -= self.move_speed * 2
        elif self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        if self.state == 'sliding':
            soldier.take_damage(self.damage * 20)
        else:
            soldier.take_damage(self.damage)


class Ogre(Enemy):
    def __init__(self):
        self.name = 'OGRE'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * enemy_size[enemy_type[2]][1]
        super().__init__()

    def update_image(self):
        if self.state == "walking":
            if self.y < self.walking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 30
            else:
                self.y = 0
                self.image = self.walking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
            self.move()
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.height == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, opponents, projectiles=None):
        opponent = collide(self, opponents, 0.5)
        if opponent:
            if self.state == 'walking':
                self.state = 'attacking'
            if self.y == 1000:
                self.attack(opponent)
        else:
            if self.state == "attacking":
                self.state = "walking"
        self.update_image()

    def move(self):
        if self.state == 'walking':
            self.rect_x -= self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def set(self, pos):
        super().set(pos)

    def take_damage(self, damage):
        super().take_damage(damage)

    def attack(self, soldier):
        soldier.take_damage(self.damage)

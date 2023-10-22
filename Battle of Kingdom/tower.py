import pygame
from random import randint

from setting import *
from project import Arrow, Shell, FairySpells, BigSpells, VectorSpells, Coin
from project import collide, collide_group

idle_all_image = {
    tower_type[0]: pygame.transform.scale(pygame.image.load(idle_images[tower_type[0]]),
                                          (tower_size[tower_type[0]][0],
                                           tower_size[tower_type[0]][1] * num_image[tower_type[0]]["idle"])),

    tower_type[1]: pygame.transform.scale(pygame.image.load(idle_images[tower_type[1]]),
                                          (tower_size[tower_type[1]][0],
                                           tower_size[tower_type[1]][1] * num_image[tower_type[1]]["idle"])),

    tower_type[2]: pygame.transform.scale(pygame.image.load(idle_images[tower_type[2]]),
                                          (tower_size[tower_type[2]][0],
                                           tower_size[tower_type[2]][1] * num_image[tower_type[2]]["idle"])),

    tower_type[3]: pygame.transform.scale(pygame.image.load(idle_images[tower_type[3]]),
                                          (tower_size[tower_type[3]][0],
                                           tower_size[tower_type[3]][1] * num_image[tower_type[3]]["idle"])),

    tower_type[4]: pygame.transform.scale(pygame.image.load(idle_images[tower_type[4]]),
                                          (tower_size[tower_type[4]][0],
                                           tower_size[tower_type[4]][1] * num_image[tower_type[4]]["idle"])),

    tower_type[5]: pygame.transform.scale(pygame.image.load(idle_images[tower_type[5]]),
                                          (tower_size[tower_type[5]][0],
                                           tower_size[tower_type[5]][1] * num_image[tower_type[5]]["idle"])),

    tower_type[6]: pygame.transform.scale(pygame.image.load(idle_images[tower_type[6]]),
                                          (tower_size[tower_type[6]][0],
                                           tower_size[tower_type[6]][1] * num_image[tower_type[6]]["idle"]))}


attack_all_image = {
    tower_type[0]: pygame.transform.scale(pygame.image.load(attacking_images[tower_type[0]]),
                                          (enemy_size[enemy_type[0]][0],
                                           enemy_size[enemy_type[0]][1] * num_image[tower_type[0]]["attacking"])),

    tower_type[1]: pygame.transform.scale(pygame.image.load(attacking_images[tower_type[1]]),
                                          (tower_size[tower_type[1]][0],
                                           tower_size[tower_type[1]][1] * num_image[tower_type[1]]["shooting"])),

    tower_type[2]: pygame.transform.scale(pygame.image.load(attacking_images[tower_type[2]]),
                                          (tower_size[tower_type[2]][0],
                                           tower_size[tower_type[2]][1] * num_image[tower_type[2]]["attacking"])),

    tower_type[3]: pygame.transform.scale(pygame.image.load(attacking_images[tower_type[3]]),
                                          (tower_size[tower_type[3]][0],
                                           tower_size[tower_type[3]][1] * num_image[tower_type[3]]["attacking"])),

    tower_type[4]: pygame.transform.scale(pygame.image.load(attacking_images[tower_type[4]]),
                                          (tower_size[tower_type[4]][0],
                                           tower_size[tower_type[4]][1] * num_image[tower_type[4]]["attacking"])),

    tower_type[5]: pygame.transform.scale(pygame.image.load(attacking_images[tower_type[5]]),
                                          (tower_size[tower_type[5]][0],
                                           tower_size[tower_type[5]][1] * num_image[tower_type[5]]["attacking"])),

    tower_type[6]: pygame.transform.scale(pygame.image.load(attacking_images[tower_type[6]]),
                                          (tower_size[tower_type[6]][0],
                                           tower_size[tower_type[6]][1] * num_image[tower_type[6]]["attacking"]))}


dying_all_image = {
    tower_type[0]: pygame.transform.scale(pygame.image.load(dying_images[tower_type[0]]),
                                          (tower_size[tower_type[0]][0],
                                           tower_size[tower_type[0]][1] * num_image[tower_type[0]]["dying"])),

    tower_type[1]: pygame.transform.scale(pygame.image.load(dying_images[tower_type[1]]),
                                          (tower_size[tower_type[1]][0],
                                           tower_size[tower_type[1]][1] * num_image[tower_type[1]]["dying"])),

    tower_type[2]: pygame.transform.scale(pygame.image.load(dying_images[tower_type[2]]),
                                          (tower_size[tower_type[2]][0],
                                           tower_size[tower_type[2]][1] * num_image[tower_type[2]]["dying"])),

    tower_type[3]: pygame.transform.scale(pygame.image.load(dying_images[tower_type[3]]),
                                          (tower_size[tower_type[3]][0],
                                           tower_size[tower_type[3]][1] * num_image[tower_type[3]]["dying"])),

    tower_type[4]: pygame.transform.scale(pygame.image.load(dying_images[tower_type[4]]),
                                          (tower_size[tower_type[4]][0],
                                           tower_size[tower_type[4]][1] * num_image[tower_type[4]]["dying"])),

    tower_type[5]: pygame.transform.scale(pygame.image.load(dying_images[tower_type[5]]),
                                          (tower_size[tower_type[5]][0],
                                           tower_size[tower_type[5]][1] * num_image[tower_type[5]]["dying"])),

    tower_type[6]: pygame.transform.scale(pygame.image.load(dying_images[tower_type[6]]),
                                          (tower_size[tower_type[6]][0],
                                           tower_size[tower_type[6]][1] * num_image[tower_type[6]]["dying"]))}


kings_all_image = {'idle': [pygame.transform.scale(pygame.image.load(king_image[0]['idle']), (king_size[0],
                                                   king_size[1] * num_image['KING']['idle'])),
                            pygame.transform.scale(pygame.image.load(king_image[1]['idle']), (king_size[0],
                                                   king_size[1] * num_image['KING']['idle'])),
                            pygame.transform.scale(pygame.image.load(king_image[2]['idle']), (king_size[0],
                                                   king_size[1] * num_image['KING']['idle']))],
                   'attacking': [pygame.transform.scale(pygame.image.load(king_image[0]['attacking']), (king_size[0],
                                                        king_size[1] * num_image['KING']['attacking'])),
                                 pygame.transform.scale(pygame.image.load(king_image[1]['attacking']), (king_size[0],
                                                        king_size[1] * num_image['KING']['attacking'])),
                                 pygame.transform.scale(pygame.image.load(king_image[2]['attacking']), (king_size[0],
                                                        king_size[1] * num_image['KING']['attacking']))],
                   'dying': [pygame.transform.scale(pygame.image.load(king_image[0]['dying']), (king_size[0],
                                                    king_size[1] * num_image['KING']['dying'])),
                             pygame.transform.scale(pygame.image.load(king_image[1]['dying']), (king_size[0],
                                                    king_size[1] * (num_image['KING']['dying'] - 1))),
                             pygame.transform.scale(pygame.image.load(king_image[2]['dying']), (king_size[0],
                                                    king_size[1] * num_image['KING']['dying']))]}


class Tower(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, tower_size[self.name][0], tower_size[self.name][1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.idle_all_image = idle_all_image[self.name]
        self.attacking_all_image = attack_all_image[self.name]
        self.dying_all_image = dying_all_image[self.name]
        self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
        # value
        self.cost = cost_value[self.name]
        self.HP = HP_value[self.name]
        self.full_HP = self.HP
        self.damage = damage_value[self.name]
        self.live = True
        self.state = "idle"
        # other
        self.cell = None

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]


class Miner(Tower):
    def __init__(self):
        self.name = 'MINER'
        self.y = randint(0, num_image[self.name]["idle"] - 1) * tower_size[self.name][0]
        super().__init__()
        self.last_time = pygame.time.get_ticks()
        self.collection = 0
        self.mine_time = 1
        self.state = 'mining'

    def update_image(self):
        if self.state == "hurt":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.state = 'mining'
        elif self.state == "mining":
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
                self.kill()

    def update(self, enemies=None, projectiles=None, towers=None, coins=None):
        current_time = pygame.time.get_ticks()
        if self.state == 'hurt':
            self.collection = current_time - self.last_time
            self.last_time = pygame.time.get_ticks()
        elif self.state == 'mining':
            if current_time - self.last_time >= self.mine_time * 1000 + self.collection:
                coins.add(Coin(self.rect_x + randint(-50, 50), self.rect_y + randint(-50, 50)))
                self.last_time = pygame.time.get_ticks()
        self.update_image()

    def set(self, pos):
        super().set(pos)

    def take_damage(self, damage):
        self.HP += damage
        if damage < 0:
            if self.HP <= 0:
                self.live = False
            else:
                self.state = 'hurt'
                self.y = 0


class Infantry(Tower):
    def __init__(self):
        self.name = 'INFANTRY'
        self.y = randint(0, num_image[self.name]["idle"] - 1) * tower_size['INFANTRY'][0]
        super().__init__()

    def update_image(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
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
                self.kill()

    def update(self, enemies, projectiles=None, towers=None, coins=None):
        enemy = collide(self, enemies, 0.5)
        if enemy:
            if self.state == 'idle':
                self.state = 'attacking'
            if self.y == 700:
                self.attack(enemy)
        else:
            if self.state == "attacking":
                self.state = "idle"
        self.update_image()

    def set(self, pos):
        super().set(pos)

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        soldier.take_damage(self.damage)


class Archer(Tower):
    def __init__(self):
        self.name = 'ARCHER'
        self.y = randint(0, num_image[self.name]["idle"] - 1) * tower_size['ARCHER'][0]
        super().__init__()

    def update_image(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 10
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
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
                self.kill()

    def update(self, enemies, projectiles, towers=None, coins=None):
        if self.spot(enemies):
            if self.state == 'idle':
                self.state = 'attacking'
            if self.y == 10 * self.height:
                self.shoot(projectiles)
        else:
            if self.state == "attacking":
                self.state = "idle"
        self.update_image()

    def take_damage(self, damage):
        super().take_damage(damage)

    def set(self, pos):
        super().set(pos)

    def shoot(self, arrow_group):
        arrow = Arrow(self.rect_x + 8, self.rect_y + 10, self.damage)
        arrow_group.add(arrow)

    def spot(self, enemy_group):
        if self.live:
            for enemy in enemy_group:
                if -15 <= self.rect_y - enemy.rect_y <= 15 and self.rect_x <= enemy.rect_x - 15:
                    return True


class Shield(Tower):
    def __init__(self):
        self.name = 'SHIELD'
        self.y = randint(0, num_image[self.name]["attacking"] - 1) * tower_size['SHIELD'][0]
        super().__init__()

    def update_image(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
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
                self.kill()

    def update(self, enemies, projectiles, towers=None, coins=None):
        enemy = collide(self, enemies, 0.5)
        if enemy:
            if self.state == 'idle':
                self.state = 'attacking'
            if self.y == 700:
                self.attack(enemy)
        else:
            if self.state == "attacking":
                self.state = "idle"
        self.update_image()

    def set(self, pos):
        super().set(pos)

    def take_damage(self, damage):
        super().take_damage(damage)

    def attack(self, soldier):
        soldier.take_damage(self.damage)


class Fairy(Tower):
    def __init__(self):
        self.name = 'FAIRY'
        self.y = randint(0, num_image[self.name]["idle"] - 1) * tower_size[tower_type[3]][0]
        super().__init__()

    def update_image(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 10
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.state == "healing":
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
                self.kill()

    def update(self, enemies=None, projectiles=None, towers=None, coins=None):
        target = self.spot(towers)
        if target:
            if self.state == 'idle':
                self.state = 'healing'
            if self.y == 6 * self.height:
                self.heal(target, projectiles)
        else:
            if self.state == "healing":
                self.state = "idle"
        if self.live and self.y == 12 * self.height:
            self.HP += 4
        self.update_image()

    def take_damage(self, damage):
        super().take_damage(damage)

    def set(self, pos):
        super().set(pos)

    def heal(self, target, spells_group):
        spells = FairySpells(self.rect_x, self.rect_y, target.rect.center, self.damage)
        spells_group.add(spells)

    def spot(self, tower_group):
        towers = collide_group(self, tower_group, 1)
        lowest_hp = 1000
        target = None
        if self.live:
            for tower in towers:
                if tower.name != 'KING':
                    if tower.HP != tower.full_HP and tower.HP <= lowest_hp and tower.name != 'FAIRY':
                        lowest_hp = tower.HP
                        target = tower
        return target


class Archmage(Tower):
    def __init__(self):
        self.name = 'ARCHMAGE'
        self.y = randint(0, num_image[self.name]["idle"] - 1) * tower_size[tower_type[4]][0]
        super().__init__()

    def update_image(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 10
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.state == "attacking":
            if self.y < self.attacking_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 10
            else:
                self.y = 0
                self.image = self.attacking_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.kill()

    def update(self, enemies, projectiles, towers=None, coins=None):
        if self.spot(enemies):
            if self.state == 'idle':
                self.state = 'attacking'
            if self.y == 10 * self.height:
                self.attacking(projectiles)
        else:
            if self.state == "attacking":
                self.state = "idle"
        self.update_image()

    def take_damage(self, damage):
        super().take_damage(damage)

    def set(self, pos):
        super().set(pos)

    def attacking(self, arrow_group):
        spells = BigSpells(self.rect_x + 8, self.rect_y + 10, self.damage)
        arrow_group.add(spells)

    def spot(self, enemy_group):
        if self.live:
            for enemy in enemy_group:
                if -15 <= self.rect_y - enemy.rect_y <= 15 and enemy.rect_x - self.rect_x <= attack_range[self.name]:
                    return True


class Manipulator(Tower):
    def __init__(self):
        self.name = 'MANIPULATOR'
        self.y = randint(0, num_image[self.name]["idle"] - 1) * tower_size[tower_type[5]][0]
        super().__init__()

    def update_image(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 10
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
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
                self.kill()

    def update(self, enemies, projectiles, towers=None, coins=None):
        if self.spot(enemies):
            if self.state == 'idle':
                self.state = 'attacking'
            if self.y == 11 * self.height:
                self.shoot(projectiles)
        else:
            if self.state == "attacking":
                self.state = "idle"
        self.update_image()

    def take_damage(self, damage):
        super().take_damage(damage)

    def set(self, pos):
        super().set(pos)

    def shoot(self, arrow_group):
        spells = VectorSpells(self.rect_x + 8, self.rect_y + 10, self.damage)
        arrow_group.add(spells)

    def spot(self, enemy_group):
        if self.live:
            for enemy in enemy_group:
                if -15 <= self.rect_y - enemy.rect_y <= 15 and self.rect_x <= enemy.rect_x - 15:
                    return True


class King(pygame.sprite.Sprite):
    def __init__(self, num):
        super().__init__()
        self.name = 'KING'
        self.num = num
        self.y = randint(0, num_image[self.name]["idle"] - 1) * king_size[0]

        self.rect_x, self.rect_y, self.width, self.height = 0, 0, king_size[0], king_size[1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.idle_all_image = kings_all_image['idle'][self.num]
        self.attacking_all_image = kings_all_image['attacking'][self.num]
        self.dying_all_image = kings_all_image['dying'][self.num]
        self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))

        self.HP = HP_value[self.name]
        self.damage = damage_value[self.name]
        self.live = True
        self.state = "idle"

    def update_image(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
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
                self.kill()

    def update(self, enemies, projectiles=None, towers=None, coins=None):
        enemy = collide(self, enemies, 0.5)
        if enemy:
            if self.state == 'idle':
                self.state = 'attacking'
            if self.y == 1000:
                self.attack(enemy)
        else:
            if self.state == "attacking":
                self.state = "idle"
        self.update_image()

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        soldier.take_damage(self.damage)


class Mortar(Tower):
    def __init__(self):
        self.name = 'MORTAR'
        super().__init__()

    def update(self):
        if not self.live:
            self.kill()

    def take_damage(self, damage):
        super().take_damage(damage)

    def set(self, pos):
        super().set(pos)

    def shoot(self, projectiles, enemies):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > 1000 * self.attack_interval:
            min_distance = 1280
            for enemy in enemies:
                if enemy.rect_x - self.rect_x <= min_distance:
                    min_distance = enemy.rect_x - self.rect_x
            shell = Shell(self.rect_x, self.rect_y, min_distance + self.rect_x, self.damage)
            self.last_attack_time = current_time
            projectiles.add(shell)

    def spot(self, enemy_group):
        if self.live:
            for enemy in enemy_group:
                if -15 <= self.rect_y - enemy.rect_y <= 15 and self.rect_x <= enemy.rect_x - 15:
                    return True

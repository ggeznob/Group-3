import pygame
from random import randint

from setting import *
from project import Arrow, Shell

idle_all_image = {'archer': pygame.transform.scale(pygame.image.load(archer_idle),
                                                   (archer_size[0], archer_size[1] * num_image["archer"]["idle"])),
                  'shield': pygame.transform.scale(pygame.image.load(shield_idle),
                                                   (shield_size[0], shield_size[1] * num_image["shield"]["idle"]))}

attack_all_image = {'archer': pygame.transform.scale(pygame.image.load(archer_shooting),
                                                    (archer_size[0], archer_size[1] * num_image["archer"]["shooting"])),
                    'shield': pygame.transform.scale(pygame.image.load(shield_attacking),
                        (shield_size[0], shield_size[1] * num_image["shield"]["attacking"]))}

dying_all_image = {'archer': pygame.transform.scale(pygame.image.load(archer_dying),
                                                    (archer_size[0], archer_size[1] * num_image["archer"]["dying"])),
                   'shield': pygame.transform.scale(pygame.image.load(shield_dying),
                       (shield_size[0], shield_size[1] * num_image["shield"]["dying"]))}


class Archer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, archer_size[0], archer_size[1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.idle_all_image = idle_all_image['archer']
        self.shooting_all_image = attack_all_image['archer']
        self.dying_all_image = dying_all_image['archer']
        self.y = randint(0, num_image["archer"]["idle"] - 1) * self.width
        self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
        # value
        self.name = 'ARCHER'
        self.cost = cost_value["archer"]
        self.HP = HP_value["archer"]
        self.damage = damage_value["archer"]
        self.attack_interval = attack_interval["archer"]
        self.live = True
        self.state = "idle"
        # other
        self.last_attack_time = 0
        self.cell = None

    def update(self):
        if self.state == "idle":
            if self.y < self.idle_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 10
            else:
                self.y = 0
                self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.state == "shooting":
            if self.y < self.shooting_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.shooting_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.image = self.shooting_all_image.subsurface((0, self.y, self.width, self.height))
        elif self.state == "dying":
            if self.y < self.dying_all_image.get_rect().h:
                if self.y % self.width == 0:
                    self.image = self.dying_all_image.subsurface((0, self.y, self.width, self.height))
                self.y += 20
            else:
                self.y = 0
                self.kill()

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]

    def shoot(self, arrow_group):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > 1000 * self.attack_interval:
            arrow = Arrow(self.rect_x, self.rect_y, self.damage)
            self.last_attack_time = current_time
            arrow_group.add(arrow)

    def spot(self, enemy_group):
        if self.live:
            for enemy in enemy_group:
                if -15 <= self.rect_y - enemy.rect_y <= 15 and self.rect_x <= enemy.rect_x - 15:
                    return True


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, shield_size[0], shield_size[1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.idle_all_image = idle_all_image['shield']
        self.attacking_all_image = attack_all_image['shield']
        self.dying_all_image = dying_all_image['shield']
        self.y = randint(0, num_image["shield"]["attacking"] - 1) * self.width
        self.image = self.idle_all_image.subsurface((0, self.y, self.width, self.height))
        # value
        self.name = 'SHIELD'
        self.cost = cost_value["shield"]
        self.HP = HP_value["shield"]
        self.damage = damage_value["shield"]
        self.attack_interval = attack_interval["shield"]
        self.state = "idle"
        self.live = True
        # other
        self.cell = None
        self.last_attack_time = 0
        # self.card = Card(shield_card, self.window, Shield, 1)

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]

    def update(self):
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

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def attack(self, soldier):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= 1000 * self.attack_interval:
            soldier.take_damage(self.damage)
            self.last_attack_time = pygame.time.get_ticks()


class Mortar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # size
        self.rect_x, self.rect_y, self.width, self.height = 0, 0, soldier_size[0], soldier_size[1]
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # image
        self.image = pygame.transform.scale(pygame.image.load(mortar_image), (self.width, self.height))
        self.y = 0
        # value
        self.cost = cost_value["mortar"]
        self.HP = HP_value["archer"]
        self.damage = damage_value["archer"]
        self.attack_interval = attack_interval["archer"]
        self.live = True
        self.state = "idle"
        # other
        self.last_attack_time = 0
        self.cell = None

    def update(self):
        if not self.live:
            self.kill()

    def take_damage(self, damage):
        self.HP += damage
        if self.HP <= 0:
            self.live = False

    def set(self, pos):
        self.rect.center = pos
        self.rect_x = pos[0]
        self.rect_y = pos[1]

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


class Swordsman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_image = pygame.transform.scale(pygame.image.load(swordsman_attack), (100, 200))
        self.width = 100
        self.height = 100
        self.image = self.all_image.subsurface((0, 0, self.width, self.height))
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.y = 0
        self.rect_x = 0
        self.rect_y = 0
        self.cost = cost_value[""]
        self.HP = HP_value[""]
        self.damage = damage_value[""]
        self.move_speed = move_speed[""]
        self.attack_speed = attack_interval[""]
        self.last_attack_time = 0

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
        self.rect_x += self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.HP -= actual_damage
        if self.HP <= 0:
            self.kill()

    def attack_enemy_with_range(self, enemy):
        distance = ((enemy.rect_x - self.rect_x) ** 2 + (enemy.rect_y - self.rect_y) ** 2) ** 0.5
        if distance <= self.attack_range and self.can_attack():
            enemy.take_damage(self.attack)
            self.last_attack_time = pygame.time.get_ticks()

    def can_attack(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > (1000 / self.attack_speed):
            return True
        return False


class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_image = pygame.transform.scale(pygame.image.load(Cannon_attack), (100, 200))
        self.width = 100
        self.height = 100
        self.image = self.all_image.subsurface((0, 0, self.width, self.height))
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.y = 0
        self.rect_x = 0
        self.rect_y = 0
        self.HP = HP[""]
        self.attack = attack[""]
        self.defense = defense[""]
        self.move_speed = move_speed[""]
        self.attack_speed = attack_speed[""]
        self.attack_range = attack_range[""]
        self.blast_radius = 50
        self.last_attack_time = 0

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
        self.rect_x += self.move_speed
        self.rect = self.image.get_rect(center=(self.rect_x, self.rect_y))

    def blast_damage(self, enemy: "Infantry and Swordsman", enemy_sprites, projectile_position):
        for enemy in enemy_sprites:
            distance = ((enemy.rect_x - projectile_position[0] ** 2 + (
                    enemy.rect_y - projectile_position[1]) ** 2) ** 0.5)
            if distance <= self.blast_radius:
                enemy.take_damage(self.attack)

    def shoot_projectile(self, target):
        projectile = Projectile(self.rect_x, self.rect_y, target.rect_x, target.rect_y, "connonball")
        return projectile

    def fire_connon_at_closest_enemy(self, enemies: "Infantry and Swordsman"):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_attack_time > (1000 / self.attack_speed):

            target_enemy = None
            min_distance = float('inf')
            for enemy in enemies:
                distance = ((enemy.rect_x - self.rect_x) ** 2 + (enemy.rect_y - self.rect_y) ** 2) ** 0.5
                if distance < self.attack_range and distance < min_distance:
                    target_enemy = enemy
                    min_distance = distance

            if target_enemy:
                projectile = self.shoot_projectile(target_enemy)
                self.last_attack_time = current_time
                return projectile

        return None

    def check_impact(self, enemy: "Infantry and Swordsman", projectile, enemy_sprites):
        impacted_enemies = []

        if projectile.has_reach_target() or projectile.has_hit_ground():
            for enemy in enemy_sprites:
                distance = ((enemy.rect_x - projectile.target_x) ** 2 + (
                        enemy.rect_y - projectile.target_y) ** 2) ** 0.5
                if distance <= self.blast_radius:
                    impacted_enemies.append(enemy)

            for enemy in impacted_enemies:
                enemy.take_damage(self.attack)

            return impacted_enemies

        return []

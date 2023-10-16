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
        self.HP = HP["infantry"]
        self.attack = attack["infantry"]
        self.defense = defense["infantry"]
        self.move_speed = move_speed["infantry"]
        self.attack_speed = attack_speed["infantry"]
        self.attack_range = attack_range["infantry"]
        self.last_attack_time = 0

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
    

class Swordsman(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_image = pygame.transform.scale(pygame.image.load(Swordsman_attack), (100,200))
        self.width = 100
        self.height = 100
        self.image = self.all_image.subsurface((0, 0, self.width, self.height))
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.y = 0
        self.rect_x = 0
        self.rect_y = 0
        self.cost = cost[""]
        self.HP = HP[""]
        self.attack = attack[""]
        self.defense = defense[""]
        self.move_speed = move_speed[""]
        self.attack_speed = attack_speed[""]
        self.attack_range = attack_range[""]
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
    

class Projectile:
    def __init__(self, start_x, start_y, target_x, target_y, projectile_type):
        self.start_x = start_x
        self.start_y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.projectile_type = projectile_type

        if projectile_type == "cannonball":
            self.speed = 10
            self.arc_height = 100
        elif projectile_type == "arrow":
            self.speed = 20
            self.arc_height = 50
        
        self.current_x = start_x
        self.current_y = start_y
        self.distance_to_target = ((target_x - start_x) ** 2 + (target_y - start_y) ** 2) ** 0.5
        self.total_time = self.distance_to_target / self.speed
        self.elapsed_time = 0

    def update_position(self, delta_time):

        self.elapsed_time += delta_time

        t = self.elapsed_time / self.total_time

        self.current_x = self.start_x + t * (self.target_x - self.start_x)

        self.current_y = self.start_y - self.arc_height * (4 * t * (1 - t))

    def has_reach_target(self):
        return self.current_x >= self.target_x and self.current_y >= self.target_y
    
    def has_hit_ground(self):
        GROUND_Y = 500
        return self.current_y >= GROUND_Y

class Archer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_image = pygame.transform.scale(pygame.image.load(Archer_attack), (100,200))
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
    
    def shoot_arrow_at_closest_enemy(self, enemies: "Infantry and Swordsman"):
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
                arrow = Projectile(self.rect_x, self.rect_y, target_enemy.rect_x, target_enemy.rect_y, "arrow") 
                self.last_attack_time = current_time
                return arrow
            
        return None


class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_image = pygame.transform.scale(pygame.image.load(Cannon_attack), (100,200))
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
            distance = ((enemy.rect_x - projectile_position[0] ** 2 + (enemy.rect_y - projectile_position[1]) ** 2) ** 0.5)
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
                distance = ((enemy.rect_x - projectile.target_x) ** 2 + (enemy.rect_y - projectile.target_y) ** 2) ** 0.5
                if distance <= self.blast_radius:
                    impacted_enemies.append(enemy)

            for enemy in impacted_enemies:
                enemy.take_damage(self.attack)

            return impacted_enemies

        return []        
    

class ShieldBearer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.all_image = pygame.transform.scale(pygame.image.load(ShieldBearer_defense), (100,200))
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
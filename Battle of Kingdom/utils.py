# this module is used for code class

import pygame
import pygame.freetype
from setting import *


pre_images = {'INFANTRY': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[0]]),
                                     (tower_size[tower_type[0]][0]-21, tower_size[tower_type[0]][1])),
              'ARCHER': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[1]]),
                                     (tower_size[tower_type[1]][0]-21, tower_size[tower_type[1]][1])),
              'SHIELD': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[2]]),
                                     (tower_size[tower_type[2]][0]-35, tower_size[tower_type[2]][1]-22)),
              'FAIRY': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[3]]),
                                     (tower_size[tower_type[3]][0]-15, tower_size[tower_type[3]][1])),
              'ARCHMAGE': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[4]]),
                                     (tower_size[tower_type[5]][0]-15, tower_size[tower_type[4]][1])),
              'MANIPULATOR': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[5]]),
                                     (tower_size[tower_type[5]][0]-15, tower_size[tower_type[5]][1])),
              'MINER': pygame.transform.scale(pygame.image.load(pre_paths[tower_type[6]]),
                                     (tower_size[tower_type[6]][0]-10, tower_size[tower_type[6]][1]))}


class Text:
    def __init__(self, text, screen, path, foreground_color, center, size):
        self.text = text
        self.screen = screen
        self.font_path = path
        self.font = pygame.freetype.Font(self.font_path, size)
        self.foreground_color = foreground_color
        self.background_color = (0, 0, 0, 0)
        self.center = center
        self.size = size

        self.text_surface, _ = self.font.render(text, foreground_color, self.background_color)

        self.text_rect = self.text_surface.get_rect(center=center)

    def draw(self):
        self.screen.blit(self.text_surface, self.text_rect)

    def change(self, new_text):
        self.text = new_text
        self.text_surface, _ = self.font.render(new_text, self.foreground_color, self.background_color)
        self.text_rect = self.text_surface.get_rect(center=self.center)


class Image:
    def __init__(self, image, screen, center, width, height):
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.width, self.height = width, height
        self.center = center
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.center[0] - self.width // 2, self.center[1] - self.height // 2))


# define button class
class Button:
    # initialize class
    def __init__(self, pos, width, height):
        self.point1 = (pos[0] - (width + 10) / 2, pos[1] - (height + 10) / 2)
        self.point2 = (pos[0] + (width + 10) / 2, pos[1] + (height + 10) / 2)

    # to check whether mouse click button
    def button_down(self, pos):
        if self.point1[0] <= pos[0] <= self.point2[0] and self.point1[1] <= pos[1] <= self.point2[1]:
            return True


# a subclass of button class
class TextButton(Button):
    # initialize class
    def __init__(self, text, background, path, text_color, button_color, pos, width, height):
        super().__init__(pos, width, height)
        self.background = background
        self.button_color = button_color
        self.rect = pygame.Rect(self.point1[0], self.point1[1], self.point2[0] - self.point1[0],
                                self.point2[1] - self.point1[1])
        self.text = Text(text, background, path, text_color, pos, int(height * 0.75))

    def button_down(self, pos):
        return super().button_down(pos)

    # to draw button
    def draw(self):
        pygame.draw.rect(self.background, self.button_color, self.rect)
        pygame.draw.rect(self.background, (0, 0, 0), self.rect, 3)
        self.text.draw()


# also a subclass of button class
class ImageButton(Button):
    # initialize class
    def __init__(self, image, background, pos, width, height):
        super().__init__(pos, width, height)
        self.background = background
        self.img = pygame.transform.scale(pygame.image.load(image), (width, height))

    def button_down(self, pos):
        return super().button_down(pos)

    # to draw button
    def draw(self):
        self.background.blit(self.img, self.point1)


# define card class
class Card(ImageButton):
    def __init__(self, image, background, species, slot, width=card_size[0], height=card_size[1]):
        self.pos = (140 + slot * 150, 95)
        super().__init__(image, background, self.pos, width, height)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.pos

        self.slot = slot
        self.species = species
        self.name = Text(self.species().name, self.background, AGENCYB, (192, 192, 192),
                         (self.pos[0] - 5, self.pos[1] - 62), 20)
        self.cost = Text(str(-self.species().cost), self.background, AGENCYB, (0, 0, 0),
                         (self.pos[0] - 5, self.pos[1] + 56), 20)
        self.pre_image = pre_images[species().name]

        self.cd, self.ready = cd_value[self.species().name] * 1000, cd_init[self.species().name]
        self.cd_edge = pygame.Rect((self.pos[0] - self.width // 2 - 4, self.pos[1] + 75, self.width, 30))
        self.cd_blank = pygame.Rect((self.pos[0] - self.width // 2 - 4, self.pos[1] + 75, self.width, 30))
        self.cd_process = pygame.Rect((self.pos[0] - self.width // 2 - 4, self.pos[1] + 75, self.width, 30))
        self.process_fraction = 0
        self.READY = Text('READY', self.background, AGENCYB, (255, 255, 0), (self.pos[0], self.pos[1] + 90), 30)
        self.start_time = 0
        self.current_time = pygame.time.get_ticks()

    def button_down(self, pos):
        return super().button_down(pos)

    def draw(self):
        super().draw()
        self.cost.draw()
        self.name.draw()
        if self.process_fraction >= 1:
            self.ready = True
            self.process_fraction = 0
        if not self.ready:

            self.current_time = pygame.time.get_ticks()
            self.process_fraction = (self.current_time - self.start_time) / self.cd
            self.cd_process = pygame.Rect(
                (self.pos[0] - self.width // 2 - 4, self.pos[1] + 75, self.width * self.process_fraction, 30))
            pygame.draw.rect(self.background, (255, 255, 255), self.cd_blank)
            if self.process_fraction < 0:
                self.process_fraction = 0
            elif self.process_fraction > 1:
                self.process_fraction = 1
            pygame.draw.rect(self.background,
                             (255, int(255 * (1 - self.process_fraction)),
                              int(255 * (1 - self.process_fraction))),
                             self.cd_process)
            pygame.draw.rect(self.background, (0, 0, 0), self.cd_edge, 5)
        else:
            self.READY.draw()


class Map:
    def __init__(self):
        self.num_row = num_row
        self.num_column = num_column
        self.row = []
        self.data = []
        for row in range(1, self.num_row + 1):
            for column in range(1, self.num_column + 1):
                self.row.append(Cell(row, column))
            self.data.append(self.row)
            self.row = []

    def get_cell(self, pos):
        for row in self.data:
            for cel in row:
                if cel.in_range(pos):
                    return cel


class Cell:
    def __init__(self, row, col):
        self.range_x = (map_point1[0] + character_size[0] * (col - 1), map_point1[0] + character_size[0] * col)
        self.range_y = (map_point1[1] + character_size[1] * (row - 1), map_point1[1] + character_size[1] * row)
        self.center = ((self.range_x[0] + self.range_x[1]) / 2, (self.range_y[0] + self.range_y[1]) / 2)
        self.is_empty = True

    def in_range(self, pos):
        if self.range_x[0] <= pos[0] < self.range_x[1] and self.range_y[0] <= pos[1] < self.range_y[1]:
            return True
        else:
            return False

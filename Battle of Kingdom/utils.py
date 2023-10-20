# this module is used for code class

import pygame
import pygame.freetype
from setting import *


class Text:
    def __init__(self, text, screen, path, foreground_color, background_color, center, size):
        self.text = text
        self.screen = screen
        self.font_path = path
        self.font = pygame.freetype.Font(self.font_path, size)
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.center = center
        self.size = size

        self.text_surface, _ = self.font.render(text, foreground_color, background_color)

        self.text_rect = self.text_surface.get_rect(center=center)

    def draw(self):
        self.screen.blit(self.text_surface, self.text_rect)

    def change(self, new_text):
        self.text = new_text
        self.text_surface, _ = self.font.render(new_text, self.foreground_color, self.background_color)
        self.text_rect = self.text_surface.get_rect(center=self.center)


# define button class
class Button:
    # initialize class
    def __init__(self, background, pos, width, height):
        self.background = background
        self.point1 = (pos[0] - (width + 10) / 2, pos[1] - (height + 10) / 2)
        self.point2 = (pos[0] + (width + 10) / 2, pos[1] + (height + 10) / 2)

    # to check whether mouse click button
    def button_down(self, pos):
        if self.point1[0] <= pos[0] <= self.point2[0] and self.point1[1] <= pos[1] <= self.point2[1]:
            return True


# a subclass of button class
class TextButton(Button):
    # initialize class
    def __init__(self, text, background, font_path, text_color, button_color, pos, width, height):
        super().__init__(background, pos, width, height)
        self.button_color = button_color
        self.rect = pygame.Rect(self.point1[0], self.point1[1], self.point2[0] - self.point1[0],
                                self.point2[1] - self.point1[1])
        self.text = Text(text, background, font_path, text_color, button_color, pos, int(height * 0.75))

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
        super().__init__(background, pos, width, height)
        self.img = pygame.transform.scale(pygame.image.load(image), (width, height))

    def button_down(self, pos):
        return super().button_down(pos)

    # to draw button
    def draw(self):
        self.background.blit(self.img, self.point1)


# define card class
class Card(ImageButton):
    def __init__(self, image, background, species, slot, width=card_size[0], height=card_size[1]):
        self.pos = (-50 + slot * 160, 150)
        super().__init__(image, background, self.pos, width, height)
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.pos
        self.species = species
        self.name = Text(self.species().name, self.background, AGENCYB, (255, 0, 0), (0, 0, 0, 0),
                         (self.pos[0] - 5, self.pos[1] - 62), 20)
        self.cost = Text(str(-self.species().cost), self.background, AGENCYB, (255, 0, 0), (0, 0, 0, 0),
                         (self.pos[0] - 5, self.pos[1] + 54), 20)
        self.ready = False

    def button_down(self, pos):
        return super().button_down(pos)

    def draw(self):
        super().draw()
        self.cost.draw()
        self.name.draw()


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
        self.range_x = (map_point1[0] + soldier_size[0] * (col - 1), map_point1[0] + soldier_size[0] * col)
        self.range_y = (map_point1[1] + soldier_size[1] * (row - 1), map_point1[1] + soldier_size[1] * row)
        self.center = ((self.range_x[0] + self.range_x[1]) / 2, (self.range_y[0] + self.range_y[1]) / 2)
        self.is_empty = True

    def in_range(self, pos):
        if self.range_x[0] <= pos[0] < self.range_x[1] and self.range_y[0] <= pos[1] < self.range_y[1]:
            return True
        else:
            return False

# this module is used for code class

import pygame
import pygame.freetype


# define a text class to operate text
# class Text:
#     # initialize objects
#     def __init__(self, text, background, font_path, foreground_color, background_color, pos, size):
#         self.text = text
#         self.background = background
#         self.foreground_color = foreground_color
#         self.background_color = background_color
#         self.pos = pos
#         self.font = pygame.freetype.Font(font_path, size)
#
#         self.text_surface, _ = self.font.render(text, size=size)
#         self.rect = self.text_surface.get_rect(center=pos)
#
#     # to change text
#     def change_text(self, new_text):
#         # pygame.draw.rect(self.background, self.background_color, self.rect)
#         self.text_surface = self.font.render(new_text, True, self.foreground_color, self.background_color)
#         self.rect = self.text_surface.get_rect(center=self.pos)
#         self.background.blit(self.text, self.rect)
#
#     # to draw text
#     def draw(self):
#         self.background.blit(self.text_surface, self.rect)


class Text:
    def __init__(self, text, screen, font_path, foreground_color, background_color, center, size):
        self.text = text
        self.screen = screen
        self.font = pygame.freetype.Font(font_path, size)
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
    def __init__(self, image, background, pos, width, height, species):
        super().__init__(image, background, pos, width, height)
        self.species = species
        self.ready = False

    def button_down(self, pos):
        return super().button_down(pos)

    def draw(self):
        super().draw()

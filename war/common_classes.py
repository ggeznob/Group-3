# this module is used for code class

import pygame
import pygame.freetype


# define a text class to operate text
class Text:
    # initialize objects
    def __init__(self, text, background, font_path, fgcolor, bgcolor, pos, size):
        self.background = background
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.pos = pos

        self.font = pygame.font.Font(font_path, size)
        self.text = self.font.render(text, True, fgcolor, bgcolor)
        self.rect = self.text.get_rect()
        self.rect.center = self.pos

    # to change text
    def change_text(self, new_text):
        pygame.draw.rect(self.background, self.bgcolor, self.rect)
        self.text = self.font.render(new_text, True, self.fgcolor, self.bgcolor)
        self.background.blit(self.text, self.rect)

    # to draw text
    def draw(self):
        self.background.blit(self.text, self.rect)


# define button class
class Button:
    # initialize class
    def __init__(self, background, pos, height, width):
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
    def __init__(self, text, background, font_path, text_color, button_color, pos, height, width):
        super().__init__(background, pos, height, width)
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
    def __init__(self, image, background, pos, height, width):
        super().__init__(background, pos, height, width)
        self.img = pygame.transform.scale(pygame.image.load(image), (height, width))

    def button_down(self, pos):
        return super().button_down(pos)

    # to draw button
    def draw(self):
        self.background.blit(self.img, self.point1)

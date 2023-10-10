import pygame
import pygame.freetype

pygame.init()
pygame.display.set_caption("war")


class Text:
    def __init__(self, text, background, font_path, fgcolor, bgcolor, pos, size):
        self.background = background
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.pos = pos

        self.font = pygame.font.Font(font_path, size)
        self.text = self.font.render(text, True, fgcolor, bgcolor)
        self.rect = self.text.get_rect()
        self.rect.center = self.pos

    def changetext(self, newtext):
        pygame.draw.rect(self.background, self.bgcolor, self.rect)
        self.text = self.font.render(newtext, True, self.fgcolor, self.bgcolor)
        self.background.blit(self.text, self.rect)

    def draw(self):
        self.background.blit(self.text, self.rect)


class Button:
    def __init__(self, background, pos, height, width):
        self.background = background
        self.point1 = (pos[0] - (width + 10) / 2, pos[1] - (height + 10) / 2)
        self.point2 = (pos[0] + (width + 10) / 2, pos[1] + (height + 10) / 2)

    def buttondown(self, pos):
        if self.point1[0] <= pos[0] <= self.point2[0] and self.point1[1] <= pos[1] <= self.point2[1]:
            return True


class TextButton(Button):
    def __init__(self, text, background, font_path, text_color, button_color, pos, height, width):
        super().__init__(background, pos, height, width)
        self.button_color = button_color
        self.rect = pygame.Rect(self.point1[0], self.point1[1], self.point2[0] - self.point1[0],
                                self.point2[1] - self.point1[1])
        self.text = Text(text, background, font_path, text_color, button_color, pos, int(height * 0.75))

    def buttondown(self, pos):
        return super().buttondown(pos)

    def draw(self):
        pygame.draw.rect(self.background, self.button_color, self.rect)
        self.text.draw()


class ImageButton(Button):
    def __init__(self, image, background, pos, height, width):
        super().__init__(background, pos, height, width)
        self.img = pygame.transform.scale(pygame.image.load(image), (height, width))

    def buttondown(self, pos):
        return super().buttondown(pos)

    def draw(self):
        self.background.blit(self.img, self.point1)


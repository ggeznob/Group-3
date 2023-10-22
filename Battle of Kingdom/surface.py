import pygame
import sys

from utils import ImageButton
from setting import *

mainimg = pygame.transform.scale(pygame.image.load(main_page), (screen_width, screen_height))


# define a parent class for surface
class Surface:
    # set simple attributions
    def __init__(self, window):
        self.window = window
        self.upgrade = False
        self.running = True
        self.background = None

    # draw surface
    def draw_surface(self):
        self.window.blit(self.background, (0, 0))

    # remove this surface
    def remove(self):
        self.window.fill((0, 0, 0))


# code the main surface
class MainPage(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.background = mainimg
        # self.text1 = Text("Battle of Kingdom", window, ALGER, (255, 255, 255), (0, 0, 0, 0), (screen_center[0], 100),
        #                   80)
        self.text1 = ImageButton(title, window, (screen_center[0], 150), 500, 200)
        # set start button
        self.b_start = ImageButton(play_button, window, (screen_center[0], 385), 280, 100)
        # set quit button
        self.b_quit = ImageButton(quit_button, window, (screen_center[0], 515), 280, 80)
        self.stage_num = 0

    def draw_surface(self):
        super().draw_surface()
        # draw button and text
        self.b_quit.draw()
        self.b_start.draw()
        self.text1.draw()

    # for getting events and update game
    def event_loop(self):
        clock = pygame.time.Clock()
        while self.running:
            self.draw_surface()
            for event in pygame.event.get():
                # for quiting
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    # for quit button
                    if self.b_quit.button_down(pos):
                        self.running = False
                        pygame.quit()
                        sys.exit()
                    # for start button to turn to fight surface
                    elif self.b_start.button_down(pos):
                        self.upgrade = True
                        self.running = False

            pygame.display.flip()

            clock.tick(fps)

    def remove(self):
        super().remove()

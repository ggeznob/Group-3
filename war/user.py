import pygame
import sys

from common_classes import Text, ImageButton, TextButton
from setting import *

homeimg = pygame.image.load(Home)
homeimg = pygame.transform.scale(homeimg, (screen_width, screen_height))


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
class Home(Surface):
    def __init__(self, window):
        super().__init__(window)
        self.background = homeimg
        # set title
        self.text1 = Text("TITLE", window, ALGER, (255, 255, 255), (0, 0, 0, 0), (screen_center[0], 100), 100)
        # set start button
        self.b_start = ImageButton(play_button, window, (screen_center[0], 300), 250, 100)
        # set quit button
        self.b_quit = TextButton("QUIT", window, ebrima, (100, 100, 100), (200, 200, 200),
                                 (screen_center[0], 400), 150,
                                 60)
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


# for pause(unfinished)
def pause(window):
    # define setting window
    setting_rect = pygame.Rect(screen_center[0] - 120, screen_center[1] - 250, 240, 500)
    # set exit button and continue button in setting window
    b_exit = TextButton("EXIT", window, ebrima, (100, 100, 100), (200, 200, 200), (screen_center[0], 375), 150, 60)
    b_continue = TextButton("CONTINUE", window, ebrima, (100, 100, 100), (200, 200, 200), (screen_center[0], 225), 220,
                            60)
    # code and draw setting window
    pygame.draw.rect(window, (0, 255, 0), setting_rect)
    # draw buttons
    b_exit.draw()
    b_continue.draw()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            # for back home
            if b_exit.button_down(pos):
                back()
            # for closing window
            elif b_continue.button_down(pos):
                pause = False






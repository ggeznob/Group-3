import pygame
from main import *


def Home(running):
    text1 = Text("TITLE", window, ALGER, (255, 255, 255), 'purple', (screen_center[0], 100), 100)
    text1.draw()
    b_start = TextButton("START", window, ebrima, (100, 100, 100), (200, 200, 200), (screen_center[0], 300), 60, 150)
    b_quit = TextButton("QUIT", window, ebrima, (100, 100, 100), (200, 200, 200), (screen_center[0], 400), 60, 150)
    b_quit.draw()
    b_start.draw()

    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False

            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = e.pos
                if b_quit.buttondown(pos):
                    running = False
                elif b_start.buttondown(pos):
                    fighting(running)
                    return

        pygame.display.flip()

    pygame.quit()


def fighting(running):

    window.blit(fightimg, (0, 0))
    b_setting = ImageButton(setting, window, (30, 30), 40, 40)
    b_setting.draw()
    setting_rect = pygame.Rect(screen_center[0] - 120, screen_center[1] - 250, 240, 500)

    while running:
        events = pygame.event.get()

        for e in events:
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                pos = e.pos
                if b_setting.buttondown(pos):
                    pygame.draw.rect(window, (0, 255, 0), setting_rect)

        pygame.display.flip()

    pygame.quit()

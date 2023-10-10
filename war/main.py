import pygame
from normal import *
import surface

# get paths of fonts and images
font_path = './font/'
image_path = './img/'
ALGER = font_path + 'ALGER.TTF'
ebrima = font_path + 'ebrima.ttf'
Home = image_path + 'home.png'
fight = image_path + 'fighting.png'
setting = image_path + 'setting.png'

# create values
screen_size = (1280, 720)
screen_center = (screen_size[0] / 2, screen_size[1] / 2)

homeimg = pygame.image.load(Home)
homeimg = pygame.transform.scale(homeimg, screen_size)
fightimg = pygame.image.load(fight)
fightimg = pygame.transform.scale(fightimg, screen_size)

window = pygame.display.set_mode(screen_size)
window.blit(homeimg, (0, 0))


def main():
    pygame.init()
    running = True
    surface.Home(running)


if __name__ == '__main__':
    main()

import pygame, controls
from woman import Woman


def run():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Игра РСХБ")
    bg_color = (0, 0, 0)
    woman = Woman(screen)

    while True:

        controls.events()
        screen.fill(bg_color)
        woman.output()
        pygame.display.flip()

run()


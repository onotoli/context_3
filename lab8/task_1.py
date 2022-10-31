import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))

fill = (167, 23, 80)
screen.fill(fill)

WHITE = (255, 255, 255)
BLUE = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED = (255,   0,   0)
BLACK = (0, 0, 0)

circle(screen, WHITE, (300, 300), 200)
circle(screen, RED, (200, 250), 30)
circle(screen,RED, (400, 250), 30)
circle(screen, BLACK, (200, 250), 20)
circle(screen, BLACK, (400, 250), 20)
rect(screen, (255, 100, 100), (200, 400, 200, 30))
polygon(screen, (255, 134, 0), [(103, 157), (257, 249), (270, 232), (135, 124)])
polygon(screen, (255, 134, 0), [(357, 253), (457, 153), (430, 102), (345, 224)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
        if event.type == pygame.QUIT:
            finished = True


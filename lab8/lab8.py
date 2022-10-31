import pygame
from pygame.draw import *
pygame.init()
screen = pygame.display.set_mode((300, 200))
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

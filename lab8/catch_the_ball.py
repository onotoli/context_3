import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    '''рисует новый шарик '''
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    return(x, y, r)

def click(event):
    '''
    Выводит координаты круга
    '''
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

points = 0
counter = 0
while not finished:
    clock.tick(FPS)

    if counter == 180:
        screen.fill(BLACK)
        x0, y0, r = new_ball()
        pygame.display.update()
        counter = 0
        print(x0, y0, r)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y, x0, y0, r)
            if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
                print('+1')
                points += 1
    if event.type == pygame.QUIT:
        finished = True
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print('Click!')



    counter += 1

print(points)
pygame.quit()
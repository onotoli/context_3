import pygame
from pygame.draw import *
from random import randint

pygame.init()
screen_width = 1200
screen_heigt = 900
FPS = 60
screen = pygame.display.set_mode((screen_width, screen_heigt))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLOURS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

clock = pygame.time.Clock()

class Ball:
    '''
    Описывает шарик и действия над ним
    '''
    def __init__(self):
        '''
        Конструктор шарика
        Задаёт параметры шарика: значение радиуса, начальных координат его центра, скорости, цвета
        Параметры выбираются произвольно
        '''
        self.r = randint(30, 100)
        self.x = randint(100, screen_width - 100)
        self.y = randint(100, screen_width - 100)
        self.vx = randint(-6, 6)
        self.vy = randint(-6, 6)
        self.color = COLOURS[randint(0, 5)]
    def draw_the_ball(self):
        '''
        Рисует шарик на экране
        '''
        circle(screen, self.color, (self.x, self.y), self.r)
    def is_hit(self):
        '''
        Проверяет, попал ли игрок в шарик
        '''
        x, y = event.pos()
        if (x - self.x) ** 2 + (y - self.y) ** 2 <= self.r ** 2:
            return True
        else:
            return False
    def x_reflection(self):
        '''
        Меняет горизонтальную составляющую скорости шара на противоположную
        '''
        self.vx = - self.vx
    def y_reflection(self):
        '''
        Меняет вертикальную составляющую скорости шара на противоположную
        '''
        self.vy = - self.vy
    def reflection(self):
        '''
        Меняет скорость в случае столкновения шарика со стеной
        '''
        if self.x + self.r >= 1200 or self.x - self.r <= 0:
            self.x_reflection()
        if self.y + self.r >= 900 or self.y - self.r <= 0:
            self.y_reflection()
    def move(self):
        '''
        Равномерно двигает шар по экрану
        '''
        self.x += self.vx
        self.y += self.vy


#class Score:


finished = False
amount_of_balls = 10 #Количество шаров
balls = [0] * amount_of_balls #Список шаров
for i in range(amount_of_balls):
    balls[i] = Ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    for i in range(amount_of_balls):
        balls[i].draw_the_ball()
        balls[i].move()
        balls[i].reflection()


    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

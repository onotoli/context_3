import pygame
from pygame.draw import *
from random import randint

pygame.init()
FPS = 60
screen_width = 1200
screen_heigt = 900
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
        self.y = randint(100, screen_heigt - 100)
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
        if (event.pos[0] - self.x) ** 2 + (event.pos[1] - self.y) ** 2 <= self.r ** 2:
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
        if self.x + self.r >= screen_width or self.x - self.r <= 0:
            self.x_reflection()
        if self.y + self.r >= screen_heigt or self.y - self.r <= 0:
            self.y_reflection()

    def move(self):
        '''
        Равномерно двигает шар по экрану
        '''
        self.x += self.vx
        self.y += self.vy


def score_of_gamer():
    '''
    Выводит на экран количество набранных очков
    '''
    myfont = pygame.font.SysFont("monospace", 50)
    scoretext = myfont.render("Счет: " + str(balls_counter), 1, (255, 255, 255))
    screen.blit(scoretext, (10, 7))
    miss = myfont.render("Промахов: " + str(int(miss_counter)), 1, (255, 255, 255))
    screen.blit(miss, (10, 60))


def ball_wave():
    '''
    Выводит на экран порядковый номер волны шаров
    '''
    myfont = pygame.font.SysFont("monospace", 50)
    wavetext = myfont.render("Волна: " + str(wave), 1, (255, 255, 255))
    screen.blit(wavetext, (10, 110))


def stats():
    '''
    Выводит на экран статистику игрока по окончании игры
    '''
    myfont = pygame.font.SysFont("monospace", 50)
    wave_final = myfont.render(f'Пройденно волн: {str(wave)} ', 1, (255, 255, 255))
    screen.blit(wave_final, (270, 0.15 * screen_heigt))
    balls_final = myfont.render(
        f'Попаданий по шарам: {balls_counter}', 1,
        (255, 255, 255))
    screen.blit(balls_final, (270, 0.3 * screen_heigt))
    miss_final = myfont.render(
        f'Промахов: {int(miss_counter)} ', 1,
        (255, 255, 255))
    screen.blit(miss_final, (270, 0.45 * screen_heigt))
    accuracy = myfont.render(
        f'Точность: {str(balls_counter / (int(miss_counter) + balls_counter))[0:4]} ', 1,
        (255, 255, 255))
    screen.blit(accuracy, (270, 0.6 * screen_heigt))


finished = False
wave = 1
balls_counter = 0 # Счетчик попаданий
miss_counter = 0 # Счетчик промахов
amount_of_balls = 5  # Количество шаров
amount_of_balls_on_the_display = amount_of_balls  # Количество шариков на экране
balls = [0] * amount_of_balls  # Список шаров
live = [True] * amount_of_balls  # Список жизней шариков
for i in range(amount_of_balls):  # Присвоение параметров шарикам
    balls[i] = Ball()

while not finished:  # Основной цикл
    ball_wave()
    score_of_gamer()
    if 0 < amount_of_balls_on_the_display <= amount_of_balls:
        clock.tick(FPS)
        for i in range(amount_of_balls):  # Рисование живых шариков
            if live[i]:
                balls[i].draw_the_ball()
                balls[i].move()
                balls[i].reflection()

        for event in pygame.event.get(): # Выход из игры
            if event.type == pygame.QUIT:
                screen.fill(BLACK)
                stats()
                pygame.display.update()
                clock.tick(FPS / 150)
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN: # Удаление с экрана убитых шариков, ддобавление очков игроку
                for i in range(amount_of_balls):
                    if balls[i].is_hit() and live[i] == True:
                        live[i] = False
                        balls_counter += 1
                        amount_of_balls_on_the_display -= 1
                        miss = False
                        miss_counter += 0.2
                    else:
                        miss_counter += 0.2

    else: # Создание новой волны
        wave += 1
        amount_of_balls_on_the_display = amount_of_balls
        for i in range(amount_of_balls):
            balls[i] = Ball()
        live = [True] * amount_of_balls
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()

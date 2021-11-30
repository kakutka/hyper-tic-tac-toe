# модуль визуализации самой игры
import pygame
pygame.init()
pygame.font.init()
color = {'BLUE':(4, 217, 255), 'PINK':(254, 1, 154), 'GREEN':(57, 255, 20), 'WHITE':(255, 255, 255), 'BLACK':(0, 0, 0)}
text = pygame.font.Font(None, 36)
def draw_field():
    '''рисует поле 9 на 9 и рядом с ним маленькое 3 на 3.
Также рисует кнопку "правила" и удаляет старые рисунки
размер одной маленькой клетки 30*30
большое поле в центре, маленькое справа от него и на расстоянии 30 от его конца'''
    pass

def draw_zero(screen, mas):
    '''рисует нолик с центром в заданных координатах.
переменная mas - кортеж координат. размер нолика 26*26'''
    pygame.draw.circle(screen, color['GREEN'], mas, 13)
    #fff

def draw_cross(screen, mas):
    '''рисует крестик. размер крестика 26*26'''
    x0, y0 = mas[0]-13, mas[1]-13
    x1, y1 = mas[0]+13, mas[1]+13
    pygame.draw.line(screen, color['PINK'], (x0, y0), (x1, y1), 2)
    x0, y0 = mas[0]-13, mas[1]+13
    x1, y1 = mas[0]+13, mas[1]-13
    pygame.draw.line(screen, color['PINK'], (x0, y0), (x1, y1), 2)
    #fff

def draw_mass0(screen):
    for j in range(9):
            for i in range(9):
                if mass0[j][i]:
                    mas = mass0_in_mas(j, i)
                    if mass0[j][i] == 1:
                        draw_cross(screen, mas)
                    else:
                        draw_zero(screen, mas)

def draw_mass1(screen):
    for i in range(9):
            if mass1[i]:
                mas = mass1_in_mas(i)
                if mass1[i] == 1:
                    draw_cross(screen, mas)
                else:
                    draw_zero(screen, mas)

def draw_line0():
    '''рисует красные линии в тех квадратах, в которых кто-то выиграл,
использует для этого массив line0, в котором находятся под индексами
массивы с двумя кортежами координат: началом и концом отрезка'''
    pass

def draw_play_person(plper):
    if plper:
        pass # написать, что ходит второй игрок ноликом
    else:
        pass # вывести, что ходит первый крестиком
    
def draw_pobeda_zero():
    '''пишет, что победил второй игрок и игра закончена,
использует переменную pobeda_zero_text'''
    pass


def draw_pobeda_cross():
    '''пишет, что победил первый игрок и игра закончена,
использует для этого переменную pobeda_cross_text'''
    pass

def draw_you_win():
    '''пишет, что победил игрок, а бот проиграл. использует
переменную you_win_text'''
    pass

def draw_you_lose():
    '''пишет, что проиграл игрок, а бот победил. использует
переменную you_lose_text'''
    pass

def draw_your_play():
    '''Выводит текст, в котором говорится, что надо ходить. И чем ходить.
использует your_play_text'''
    pass















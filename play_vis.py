# модуль визуализации самой игры
import pygame
from model_two_person import mass0_in_mas
from model_two_person import mass1_in_mas
pygame.init()
pygame.font.init()
color = {'BLUE':(4, 217, 255), 'PINK':(254, 1, 154), 'GREEN':(57, 255, 20), 'WHITE':(255, 255, 255), 'BLACK':(0, 0, 0)}
text = pygame.font.Font(None, 36)
wall_box = [(340, 50),(480, 50),(480, 20),(340, 20)]
wall_text = text.render('правила', True, color['GREEN'])


def draw_field(screen):
    '''рисует поле 9 на 9 и рядом с ним маленькое 3 на 3.
Также рисует кнопку "правила" и удаляет старые рисунки
размер одной маленькой клетки 30*30
большое поле в центре, маленькое справа от него и на расстоянии 30 от его конца'''
    screen.fill(color['BLACK'])
    pygame.draw.polygon(screen, (25, 25, 25), wall_box)
    screen.blit(wall_text, (wall_box[3][0]+5, wall_box[3][1]+5))
    x, y = 65, 115
    x2, y2 = 65+270, 115+270
    for i in range(10):
        x1 = x + 30*i
        pygame.draw.line(screen, color['BLUE'], (x1, y),(x1, y2))
        y1 = y + 30*i
        pygame.draw.line(screen, color['BLUE'], (x, y1),(x2, y1))
        if i == 3 or i == 6:
            pygame.draw.line(screen, (255, 0, 0), (x1, y),(x1, y2))
            pygame.draw.line(screen, (255, 0, 0), (x, y1),(x2, y1))
    x, y = 365, 205
    x2, y2 = 365+90, 205+90
    for i in range(4):
        x1 = x + 30*i
        pygame.draw.line(screen, color['BLUE'], (x1, y),(x1, y2))
        y1 = y + 30*i
        pygame.draw.line(screen, color['BLUE'], (x, y1),(x2, y1))
    #ffff

def draw_s(screen, s):
    x, y = 65, 115
    s += 1
    if s == 1:
        pass
    if s == 2:
        x += 90
    if s == 3:
        x += 180
    if s == 4:
        y+=90
    if s==5:
        x+=90
        y+=90
    if s==6:
        x+=180
        y+=90
    if s==7:
        y+=180
    if s==8:
        x+=90
        y+=180
    if s==9:
        x+=180
        y+=180
    a = [(x, y), (x + 90, y), (x+90,y+90), (x, y+90)]
    pygame.draw.polygon(screen, (225, 225, 225), a, 3)


def draw_zero(screen, mas):
    '''рисует нолик с центром в заданных координатах.
переменная mas - кортеж координат. размер нолика 26*26'''
    pygame.draw.circle(screen, color['GREEN'], mas, 13, 4)
    #fff

def draw_cross(screen, mas):
    '''рисует крестик. размер крестика 26*26'''
    x0, y0 = mas[0]-13, mas[1]-13
    x1, y1 = mas[0]+13, mas[1]+13
    pygame.draw.line(screen, color['PINK'], (x0, y0), (x1, y1), 4)
    x0, y0 = mas[0]-13, mas[1]+13
    x1, y1 = mas[0]+13, mas[1]-13
    pygame.draw.line(screen, color['PINK'], (x0, y0), (x1, y1), 4)
    #fff

def draw_mass0(screen, mass0):
    for j in range(9):
            for i in range(9):
                if mass0[j][i]:
                    mas = mass0_in_mas(j, i)
                    if mass0[j][i] == 1:
                        draw_cross(screen, mas)
                    else:
                        draw_zero(screen, mas)

def draw_mass1(screen, mass1):
    for i in range(9):
            if mass1[i]:
                mas = mass1_in_mas(i)
                if mass1[i] == 1:
                    draw_cross(screen, mas)
                else:
                    draw_zero(screen, mas)

def draw_line0(screen, line0):
    for a in line0:
        if a != [(0, 0), (0, 0)]:
            pygame.draw.line(screen, (248,250,200), a[0], a[1], 6)
    '''рисует красные линии в тех квадратах, в которых кто-то выиграл,
использует для этого массив line0, в котором находятся под индексами
массивы с двумя кортежами координат: началом и концом отрезка'''


def draw_play_person(screen, plper):
    if plper:
        text1 = text.render('ходит второй игрок ноликом', True, color['GREEN'])
        screen.blit(text1, (55, 85))
    else:
        text1 = text.render('ходит первый игрок крестиком', True, color['PINK'])
        screen.blit(text1, (55, 85))
    
def draw_pobeda_zero(screen):
    '''пишет, что победил второй игрок и игра закончена,
использует переменную pobeda_zero_text'''
    pobeda_zero_text = text.render('Победил второй игрок.', True, color['WHITE'])
    screen.blit(pobeda_zero_text, (55, 55))
    pobeda_zero_text = text.render('Нолики торжествуют!', True, color['WHITE'])
    screen.blit(pobeda_zero_text, (55, 85))
    pass


def draw_pobeda_cross(screen):
    '''пишет, что победил первый игрок и игра закончена,
использует для этого переменную pobeda_cross_text'''
    pobeda_cross_text = text.render('Победил первый игрок.', True, color['WHITE'])
    screen.blit(pobeda_cross_text, (55, 55))
    pobeda_cross_text = text.render('Крестики торжествуют!', True, color['WHITE'])
    screen.blit(pobeda_cross_text, (55, 85))
    pass

def draw_you_win(screen):
    '''пишет, что победил игрок, а бот проиграл. использует
переменную you_win_text'''
    you_win_text = text.render('Поздравляю!', True, color['WHITE'])
    screen.blit(you_win_text, (55, 55))
    you_win_text = text.render('Ты смог победить меня!', True, color['WHITE'])
    screen.blit(you_win_text, (55, 85))
    pass

def draw_you_lose(screen):
    '''пишет, что проиграл игрок, а бот победил. использует
переменную you_lose_text'''
    you_lose_text = text.render('Как-нибудь', True, color['WHITE'])
    screen.blit(you_lose_text, (55, 25))
    you_lose_text = text.render('в следующий раз', True, color['WHITE'])
    screen.blit(you_lose_text, (55, 55))
    you_lose_text = text.render('тебе повезёт...', True, color['WHITE'])
    screen.blit(you_lose_text, (55, 85))
    pass

def draw_your_play(screen, play_person):
    '''Выводит текст, в котором говорится, что надо ходить. И чем ходить.
использует your_play_text'''
    your_play_text = text.render('Ваш ход.', True, color['WHITE'])
    screen.blit(your_play_text, (55, 55))
    your_play_text = text.render('Вы ходите '+["крестиками" if not play_person else "ноликами"][0], True, color['WHITE'])
    screen.blit(your_play_text, (55, 85))
    pass














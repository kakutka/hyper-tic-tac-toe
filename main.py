# основной файл запуска
import pygame
from random import randint
from inter_vis import *
from model_inter import *
from model_one_person import *
from model_two_person import *
from play_vis import *
from text import *
pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
# color - set type from inter_vis
play_box = [(),(),(),()]
wall_box = [(),(),(),()]
back_box = [(),(),(),()]
play_one_box = [(),(),(),()]
play_two_box = [(),(),(),()]
# переменные quit0, two, one принимают логические
# значения и после завершения цикла определяют дальнейшее поведение программы
quit0, two, one = 0, 0, 0
flag = True
while flag:
    priv_enter()
    # def from inter_vis
    # draw priv on display
    pygame.display.flip()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit0 = True
            flag = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if prov_box(event.pos, play_box):
                # def from inter_model
                # проверяет попадание мышки по кнопке
                flag1 = True
                while flag1:
                    play_enter()
                    # def from inter_vis
                    # draw play on display
                    pygame.display.flip()
                    clock.tick(30)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit0 = True
                            flag0 = False
                            flag1 = False
                            break
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if prov_box(event.pos, play_one_box):
                                one = True
                                flag1 = False
                                flag0 = False
                                break
                            if prov_box(event.pos, play_two_box):
                                two = True
                                flag1 = False
                                flag0 = False
                                break
                            if prov_box(event.pos, back_box):
                                flag1 = False
                                break
                if not flag1:
                    break
            if prov_box(event.pos, wall_box):
                flag1 = True
                while flag1:
                    wall_enter()
                    # def from inter_vis
                    # draw display with wall
                    pygame.display.flip()
                    clock.tick(30)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quit0 = True
                            flag0 = False
                            flag1 = False
                            break
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if prov_box(event.pos, back_box):
                                flag1 = False
                                break
                if not flag1:
                    break

if quit0:
    pygame.quit()

if two:
    quit0 = False
    flag = True # позволяет находиться в цикле, пока не потребуется завершить игру
    mass1 = [0 for i in range(9)] #главное поле 3*3
    mass0 = [mass1 for i in range(9)] #поле 9*9
    #крестику соотв 1, нолику - 2
    line0 = [[(0,0),(0,0)] for i in range(9)] # сюда вносятся координаты
    # отрезков, которые обозначают, кто на каком поле выиграл
    pobeda_zero = pobeda_cross = 0 #позволяет в конце вывести на экран победителя
    play_person = 0
    #счетчик определяет кто ходит: 0 - первый, 1 - второй
    while flag:
        draw_field() # рисует поля и кнопки
        draw_mass0() # заполняет поле 9*9
        draw_mass1() # заполняет поле 3*3
        draw_line0() # рисует линии в квадратах, где кто-то победил в поле 9*9
        draw_play_person(play_person) # пишет над полем, чья очередь ходить
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit0 = True
                flag = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if prov_field(event.pos): # проверяет попадание на поле 9*9
                    mas = event_mas(event.pos)
                    j, i = mas_in_mass0(mas) # коорд клетки в массиве,
                    # в которую нажали в игре
                    if play_person == 0:
                        mass0[j][i] = 1
                        play_person = 1
                    else:
                        mass0[j][i] = 2
                        play_person = 0
                if prov_box(event.pos, wall_box): # запускает цикл, где монжо
                    #прочитать правила и потом вернуться к игре
                    flag1 = True
                    while flag1:
                        wall_enter()
                        # def from inter_vis
                        # draw display with wall
                        pygame.display.flip()
                        clock.tick(30)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit0 = True
                                flag = False
                                flag1 = False
                                break
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if prov_box(event.pos, back_box):
                                    flag1 = False
                                    break
                    if not flag1:
                        break
        for j in range(9):
            # проверяет, есть ли в данном квадрате три
            #объекта в ряд и впервые ли это
            if prov_line_zero(mass0[j]) and line0[j] == [(0,0),(0,0)]:
                rest_line0(j) #вычисляет необходимые
                #коорд из mass0[j] и заполняет ими line0[j]
                mass1[j] = 2
            if prov_line_cross(mass0[j]) and line0[j] == [(0,0),(0,0)]:
                rest_line0(j)
                mass1[j] = 1
        if prov_line_zero(mass1):# проверяет, есть ли в главном квадрате три нуля в ряд
            pobeda_zero = 1
            break
        if prov_line_cross(mass1):
            pobeda_cross = 1
            break
    while flag: # выводит надпись, какой игрок победил
        draw_field()
        draw_mass0()
        draw_mass1()
        draw_line0()
        if pobeda_zero:
            draw_pobeda_zero()
        if pobeda_cross:
            draw_pobeda_cross()
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit0 = True
                flag = False
                break

    
    

if one:
    # Воистину! Предлагаю сие сделать Наиле. Хотя... Я сам.

    quit0 = False
    flag = True # позволяет находиться в цикле, пока не потребуется завершить игру
    mass1 = [0 for i in range(9)] #главное поле 3*3
    mass0 = [mass1 for i in range(9)] #поле 9*9
    #крестику соотв 1, нолику - 2
    line0 = [[(0,0),(0,0)] for i in range(9)] # сюда вносятся координаты
    # отрезков, которые обозначают, кто на каком поле выиграл
    pobeda_zero = pobeda_cross = 0 #позволяет в конце вывести на экран победителя
    play_person = randint(0, 1)
    #счетчик определяет кто ходит: 0 - первый, 1 - ход бота
    while flag:
        draw_field() 
        draw_mass0() 
        draw_mass1() 
        draw_line0() 
        draw_your_play() # выводит на экран то, что надо ходить; и в зависимости от
        # play_person это будут или крестики или нолики 
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit0 = True
                flag = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if prov_field(event.pos): 
                    mas = event_mas(event.pos)
                    j, i = mas_in_mass0(mas) # коорд клетки в массиве,
                    # в которую нажали в игре
                    if play_person == 0:
                        mass0[j][i] = 1
                        mass0 = bot_go(mass0, 2) # бот ходит на поле 9*9 ноликами
                    else:
                        mass0[j][i] = 2
                        mass0 = bot_go(mass0, 1) # бот ходит на поле 9*9 крестиками
                if prov_box(event.pos, wall_box):
                    flag1 = True
                    while flag1:
                        wall_enter()
                        pygame.display.flip()
                        clock.tick(30)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quit0 = True
                                flag = False
                                flag1 = False
                                break
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if prov_box(event.pos, back_box):
                                    flag1 = False
                                    break
                    if not flag1:
                        break
        for j in range(9):
            if prov_line_zero(mass0[j]) and line0[j] == [(0,0),(0,0)]:
                rest_line0(j) 
                mass1[j] = 2
            if prov_line_cross(mass0[j]) and line0[j] == [(0,0),(0,0)]:
                rest_line0(j)
                mass1[j] = 1
        if prov_line_zero(mass1):
            pobeda_zero = 1
            break
        if prov_line_cross(mass1):
            pobeda_cross = 1
            break
    while flag: 
        draw_field()
        draw_mass0()
        draw_mass1()
        draw_line0()
        if pobeda_zero:
            if play_person:
                draw_you_win() #говорит, что пользователь победил
            else:
                draw_you_lose() #проиграл
        if pobeda_cross:
            if play_person:
                draw_you_lose()
            else:
                draw_you_win()
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit0 = True
                flag = False
                break




if quit0:
    pygame.quit()







                
        
    
    

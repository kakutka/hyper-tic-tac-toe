## модель игры с ботом
from random import randint
from model_two_person import *


def prov2bot(mass0, k, j):
    if k == 1: #крестик
        for i in range(9):
            a = mass0[j][:]
            if a[i] == 0:
                a[i] = 1
                if prov_line_cross(a):
                    return(i)
                a[i] = 2
                if prov_line_zero(a):
                    return(i)
    if k == 2: #нолик
        for i in range(9):
            a = mass0[j][:]
            if a[i] == 0:
                a[i] = 2
                if prov_line_zero(a):
                    return(i)
                a[i] = 1
                if prov_line_cross(a):
                    return(i)
    return(17)


def prov_glav_desk(mass0, mass1, j):
    for i in range(9):
        if mass1[i] != 0 and mass0[j][i] == 0:
            return(i)
    return(17)


def heh(mass0, j):
    b = 1
    for i in range(9):
        b *= mass0[j][i]
    if b == 0:
        return True
    return False


def random_hod(mass0, j):
    i = randint(0, 8)
    for _ in range(9):
        if heh(mass0, j):
            while mass0[j][i] != 0:
                i = randint(0, 8)
            return(j, i)
        else:
            j = (j+1)%9
    return(j, i)


def bot_go(mass0, mass1, k, s):
    j = s[1]
    i = prov2bot(mass0, k, j)
    
    if i == 17:
        i = prov_glav_desk(mass0, mass1, j)
    if i == 17:
        j, i = random_hod(mass0, j)
    mass0[j][i] = k
    if not heh(mass0, i):
        i = -1
    return(mass0, i)
    '''в функцию подается массив - поле 9*9
и число к, которое дает понять, чем ходит бот.
если к=1, то бот ходит крестиками
если к=2, то бот ходит ноликами
бот делает ход в массиве mass0 и в нужную клетку ставит 1 или 2,
что соот крестику или нолику
потом возвращает новый массив с выполненным ходом'''
    '''чтобы лучше понять, как сделать эту функцию,
надо, вероятно, ознакомиться со всей программой.
Как-то так. кря-кря 128.'''





   


        

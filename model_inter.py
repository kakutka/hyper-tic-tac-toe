# модель интерфейса при начале игры

def prov_box(event, box):
    '''в функцию подают две переменные: event - координаты нажатия мышки
box - массив 4-х координат. Функция возвращает True в случае попадания мышкой
по прямоугольнику, иначе False'''
    x, y = event
    x1, y1 = box[0]
    x2, y2 = box[1]
    x3, y3 = box[2]
    x4, y4 = box[3]
    if x1 < x and x < x2 and y2 > y and y > y3:
        print(True)
        return True
    print(False)
    return False
    #функция написана полностью


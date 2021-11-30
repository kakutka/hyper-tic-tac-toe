# модуль визуализации интерфейса при запуске игры
# каждая функция сначала удаляет старые рисовки
import pygame
pygame.init()
pygame.font.init()
color = {'BLUE':(4, 217, 255), 'PINK':(254, 1, 154), 'GREEN':(57, 255, 20), 'WHITE':(255, 255, 255), 'BLACK':(0, 0, 0)}
text = pygame.font.Font(None, 36)
play_box = [(200, 250),(300, 250),(300, 220),(200, 220)]
wall_box = [(180, 330),(320, 330),(320, 300),(180, 300)]
play_text = text.render('играть', True, color['GREEN'])
wall_text = text.render('правила', True, color['GREEN'])
name_text = text.render('добро пожаловать в игру', True, color['WHITE'])
name1_text = text.render('"гипер-крестики-нолики"', True, color['WHITE'])
wall_long_text = 'туть правилаудут написаны чтобы дети читали их и слушали очень внимательно  а так всякую вигню нипшетдчь вьслыьлс овт мловат ьс лстмоврл лламгшврлст ьслотсмвос млопт ащташуо'
back_text = text.render('назад', True, color['PINK'])
play_one_text = text.render('играть с ботом', True, color['GREEN'])
play_two_text = text.render('играть вдвоём', True, color['GREEN'])
back_box = [(20, 50),(100, 50),(100, 20),(20, 20)]
play_one_box = [(120, 250),(310, 250),(310, 220),(120, 220)]
play_two_box = [(180, 330),(380, 330),(380, 300),(180, 300)]
def priv_enter(screen):
    ''' рисует на экране интерфейс начала игры.
Есть надпись с названием и какой-нибудь еще фразой.
Есть кнопки "играть" и "читать правила"
использует переменные play_text и wall_text для вывода текста играть и правила
Также использует переменные play_box и wall_box для рисовки
кнопок "играть" и "правила"
для вывода надписи использует переменную name_text
переменные с box это массивы кортежей координат'''
    screen.fill(color['BLACK'])
    pygame.draw.polygon(screen, (25, 25, 25), play_box)
    pygame.draw.polygon(screen, (25, 25, 25), wall_box)
    screen.blit(play_text, (play_box[3][0]+5, play_box[3][1]+5))
    screen.blit(wall_text, (wall_box[3][0]+5, wall_box[3][1]+5))
    screen.blit(name_text, (60, 70))
    screen.blit(name1_text, (80, 100))
    #функция написана

def play_enter(screen):
    '''рисует три кнопки: назад, играть вдвоем, играть с ботом
использует соответственно тексты back_text, play_one_text, play_two_text
и кнопки back_box, play_one_box, play_two_box'''
    screen.fill(color['BLACK'])
    pygame.draw.polygon(screen, (25, 25, 25), back_box)
    pygame.draw.polygon(screen, (25, 25, 25), play_one_box)
    pygame.draw.polygon(screen, (25, 25, 25), play_two_box)
    screen.blit(back_text, (back_box[3][0]+5, back_box[3][1]+5))
    screen.blit(play_one_text, (play_one_box[3][0]+5, play_one_box[3][1]+5))
    screen.blit(play_two_text, (play_two_box[3][0]+5, play_two_box[3][1]+5))
    #функция написана

def ren(text0, fize):
        s = text0.split()
        a = []
        k = 0
        b = ''
        for i in s:
            b += ' '+i
            k += 1
            if k == fize:
                k = 0
                c = text.render(b, True, color['BLUE'])
                a.append(c)
                b = ''
        return a
            


def wall_enter(screen):
    ''' выводит на экране кнопку "назад" и текст правил
для кнопки используются переменные back_text, back_box
для правил переменная wall_long_text_'''
    screen.fill(color['WHITE'])
    pygame.draw.polygon(screen, (215, 215, 215), back_box)
    screen.blit(back_text, (back_box[3][0]+5, back_box[3][1]+5))
    a = ren(wall_long_text, 4)
    x, y = 50, 150
    k = 0
    for c in a:
        k += 1
        x1 = x
        y1 = y + k*20
        screen.blit(c, (x1, y1))

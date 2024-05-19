import random

from tkinter import Tk, Canvas

# Размеры
WIDTH, HEIGHT = 800, 600
SEG_SIZE = 20

# Переменная отвечающая за состояние игры
IN_GAME = True


def create_block():

    """Создание поинта"""

    global BLOCK

    posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)

    posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)

    BLOCK = c.create_oval(posx, posy,
                          posx+SEG_SIZE, posy+SEG_SIZE,
                          fill="yellow")

def main():

    """Управление игровых процессом"""

    global IN_GAME

    if IN_GAME:
        s.move()
        head_coords = c.coords(s.segments[-1].instance) x1, y1, x2, y2 head_coords
        x1, y1, x2, y2 = head_coords

        # Проверка, нет ли столкновения с краями игрового поля
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False

        # Поедание поинтов
        elif head_coords == c.coords(BLOCK):
            s.add_segment()
            c.delete(BLOCK)
            create_block()

        # Самоедство
        else:
            for index in range(len(s.segments)-1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False

        root.after(100, main)

    # Если не в игре выводим сообщение о проигрыше
    else:
        set_state(restart_text, 'normal')
        set_state(game_over_text, 'normal')


class Segment(object):

   """Класс сегмента змейки"""

    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="white")
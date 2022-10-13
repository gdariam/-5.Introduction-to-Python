# Задача 10: Найти расстояние между двумя точками пространства

import os
def clear(): return os.system('cls')


clear()

ax = float(input("Введите координаты точки AX:"))
ay = float(input("Введите координаты точки AY:"))
bx = float(input("Введите координаты точки BX:"))
by = float(input("Введите координаты точки BY:"))


def destination(ax, ay, bx, by):
    destin = ((bx-ax)**2)+((by-ay)**2)
    return destin


print(destination(ax, ay, bx, by))

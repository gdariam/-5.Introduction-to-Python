# Задача 1: Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
import os


def clear(): return os.system('cls')


clear()

n = int(input("Введите количество чисел последовательности: "))


def getlist(n):
    return [random.randint(0, n) for i in range(n)]


mylist = getlist(n)


def sumlist(mylist):
    result = 0
    for i in range(len(mylist)):
        if i % 2 != 0:
            result += mylist[i]
    return result


print(f'{mylist} -> сумма элементов на нечетных позициях {sumlist(mylist)}')

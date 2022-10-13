# Задача 2: 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите количество чисел последовательности: "))


def getlist(n):
    return [random.randint(0, n) for i in range(n)]


my_list = getlist(n)


def product(my_list):
    result = []
    for i in range(0, len(my_list) // 2):
        resu = my_list[i] * my_list[ - 1 - i]
        result.append(resu)
    return result

new_list = product(my_list)

print(f'{my_list} => {new_list}')

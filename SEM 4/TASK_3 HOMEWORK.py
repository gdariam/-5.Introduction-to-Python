# Задача 3: Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random
import os


def clear(): return os.system('cls')


clear()

n = int(input("Введите количество чисел последовательности: "))


def getlist(n):
    return [random.randint(0, n) for i in range(n)]

list1 = getlist(n)

def number_sequence(list1):
    number_sequence_list = []
    for i in list1:
        if list1.count(i) == 1:
            number_sequence_list.append(i)
    return number_sequence_list

print(f"Cписок неповторяющихся элементов последовательности {list1} -> {number_sequence(list1)}")
# Задача 3 (Семинар 3): Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите количество чисел последовательности: "))


# def getlist(n):
#     return [random.uniform(0, n) for i in range(n)] # uniform возвращает псевдослучайные вещественные числа


list1 = [random.uniform(0, n) for i in range(n)]

list0 = [round(i % 1, 2) for i in list1]

# def getnewlist(list_n):
#     list0 = []
#     for i in list_n:
#         if isinstance(i, float):
#             rsult = round(i % 1, 2)
#             list0.append(rsult)
#     return list0

rslt = max(list0) - min(list0)

print(list1)
print(list0)
print(f'{list1} => {rslt}')

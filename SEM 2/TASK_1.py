# Задача 1: Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# - Для N = 5: 1, -3, 9, -27, 81

import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите число N: "))
result = "1, "
res = 1
for i in range(1, n):
    res *= (-3)
    result += str(res)
    result += ", "
print(result[0:(len(result)-2)])
# Задача 4: Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите целое число: "))

def binary_number(n):
    temp = n
    binary = ''
    while temp > 0:
        binary = str(temp % 2) + binary
        temp //= 2
    return binary

print(f'{n} -> {binary_number(n)}')
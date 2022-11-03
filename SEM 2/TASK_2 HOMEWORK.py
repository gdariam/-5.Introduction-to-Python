# Задача 2: Написать программу, получающую набор произведений чисел от 1 до N
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите целое число: "))


def product(n):
    result = []
    res = 1
    for i in range(1, n+1):
        res *= i
        result.append(res)
    print(result)

product(n)

# Задача 5: Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# (https://ru.wikipedia.org/wiki/Негафибоначчи)

import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите целое число: "))

def fib(n):
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def nfib(n):
    list_nfib = []
    for i in range(1, n + 1):
        fib_i = fib(i)
        list_nfib.append(fib_i)
        if i != 1:
            list_nfib.insert(0, (-1) ** (i) * fib_i)
    return list_nfib

print(nfib(n))
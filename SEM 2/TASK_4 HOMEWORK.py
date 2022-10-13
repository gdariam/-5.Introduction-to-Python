# Задача 4: Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

import random
import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите число: "))


def getlist(n):
    return [random.randint(-n, n) for i in range(n)]


def product(mylist, positions):
    res = 1
    maxindex = len(mylist)-1
    for i in positions:
        if i > maxindex:
            exit(print("Ваш список слишком короткий"))
        res *= mylist[i]
    return res


mylist = getlist(n)
positions = [1, 3, 4]

print(mylist)
print(f'Произведение элементов списка с индексами {positions} = {product(mylist, positions)}')

# Задача 1: Подсчитать сумму цифр в вещественном числе

import os
def clear(): return os.system('cls')


clear()

numberinput = input("Введите число: ")
number = numberinput.replace(".", "")

def sum(num):
    res = 0
    for i in num:
        res += int(i)
    return res

print(f'Сумма цифр числа {numberinput} = {sum(number)}')

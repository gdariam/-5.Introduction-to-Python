# Задача 1 (Семинар 2): Подсчитать сумму цифр в вещественном числе

from functools import reduce
import os
def clear(): return os.system('cls')


clear()

numberinput = input("Введите число: ")
number = numberinput.replace(".", "")

# def sum(num):
#     res = 0
#     for i in num:
#         res += int(i)
#     return res

list_number = [int(i) for i in number]
print(list_number)

sum = reduce(lambda a, x: a + x, list_number)

# print(f'Сумма цифр числа {numberinput} = {sum(number)}')

print(f'Сумма цифр числа {numberinput} = {sum}')

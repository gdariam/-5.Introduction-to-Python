# Задача 3 (Семинар 2): Задать список из n чисел последовательности (1 + 1/n)^n и вывести на экран их сумму

import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите количество чисел последовательности: "))


# def listsum(n):
#     result = []
#     mysum = 0
#     for i in range(1, n + 1):
#         res = (1 + (1/i))**i
#         mysum += res
#         result.append(res)
#     print(result)
#     print(f'Сумма чисел в последовательности {mysum}')

list1 = [(1 + (1/i))**i for i in range(1, n + 1)]
print(list1)

my_sum = sum(list1)
print(f'Сумма чисел в последовательности {my_sum}')

# listsum(n)
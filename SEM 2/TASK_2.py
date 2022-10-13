# Задача 2: Для натурального n создать список, состоящий из элементов последовательности 3n + 1
# Пример:
# - Для n = 6: [4, 7, 10, 13, 16, 19]

import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите число N: "))
result = []
for i in range(1, n + 1):
    res = 3*i + 1
    result.append(res)
print(result)
# print(*result) # * делает распаковку списка
# print(*result, sep=', ') # sep создает разделители для списка
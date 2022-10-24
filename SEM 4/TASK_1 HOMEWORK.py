# Задача 1: Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10**-1 <= d <= 10**-10

import math
import os
def clear(): return os.system('cls')


clear()

d = float(input("Введите число d (10**-1 <= d <= 10**-10): "))

count = 0
while d < 1:
    count += 1
    d = d * 10
print(f'Число с заданной точностью равно {round(math.pi, count)}')
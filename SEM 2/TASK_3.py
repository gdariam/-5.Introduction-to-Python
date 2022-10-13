# Задача 3: Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой

import os
def clear(): return os.system('cls')


clear()

first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
result = first_string.count(second_string)
print(f'Количество вхождений второй строки в первую: {result}')

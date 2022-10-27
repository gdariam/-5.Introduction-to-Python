# Задача 1: Напишите программу, удаляющую из текста все слова, содержащие "абв".

import os
def clear(): return os.system('cls')


clear()

str1 = input("Введите текст: ")
str2 = str1.replace('абв', '')
print(f'{str1} -> {str2}')
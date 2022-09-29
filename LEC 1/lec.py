# # типы данных и переменная
# # int, float, boolean, str, list, None

# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))

# s = 'hello world'
# print(s)  # вывод строки

# st = "hello 'world'"
# print(st)  # вывод строки для демонстрации вывода кавычек. Можно обрамлять двойными или одинарными в зависимости от того, какие кавычки нужно вывести в программу

# # интерполяция
# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)

# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print(list)
# print(col)

# Ввод и вывод данных
# print, input

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, '+', b, '=', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

# a = 1.31231
# b = 3
# c = round(a*b, 5)
# print(c)

# a = 3
# a += 5  # a=a*5
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 < 5 < 10
# print(a)

# Управляющие конструкции: if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# Управляющие конструкции: if, if-else
# username = input('Введите имя: ')
# if username == 'Маша':
# print('Ура, это же МАША!')
# elif username == 'Марина':
# print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
# print('Ильнар - топ)')
# else:
# print('Привет, ', username

# Управляющие конструкции: while
# while condition:
# # operator 1
# # operator 2
# # . . .
# # operator n
# Цикл позволяет выполнить блок операторов какое-
# то количество раз

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции: while-else
original = 23
inverted = 0
while original != 0:
    inverted = inverted * 10 + (original % 10)
    original //= 10
else:
    print('Пожалуй')
    print('хватит )')
print(inverted)
# Пожалуй
# хватит )
# 3
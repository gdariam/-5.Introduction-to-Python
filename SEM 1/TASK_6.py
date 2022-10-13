# Задача 6: Дано число, обозначающее день недели. Вывести его название
# и указать, является ли день выходным.

num = int(input("Введите номер дня недели: "))


# def weekday(number):
#     if number == 1:
#         print(f' {number} -> понедельник, рабочий день')
#     if number == 2:
#         print(f' {number} -> вторник, рабочий день')
#     if number == 3:
#         print(f' {number} -> среда, рабочий день')
#     if number == 4:
#         print(f' {number} -> четверг, рабочий день')
#     if number == 5:
#         print(f' {number} -> пятница, рабочий день')
#     if number == 6:
#         print(f' {number} -> суббота, выходной день')
#     if number == 7:
#         print(f' {number} -> воскресенье, выходной день')
#     if number > 7 or number < 0:
#         print(f' {number} -> такого дня недели не существует')

def weekday(number):
    week = ['понедельник', 'вторник', 'среда',
            'четверг', 'пятница', 'суббота', 'воскресенье']
    if number < 1 or number > 7:
        print(f' {number} -> такого дня недели не существует')
    elif number >= 6:
        print(f' {week[number-1]} -> выходной день')
    else:
        print(f' {week[number-1]} -> рабочий день')


weekday(num)

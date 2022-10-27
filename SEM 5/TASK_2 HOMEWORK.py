# Задача 2: Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


import random
import os
def clear(): return os.system('cls')


clear()


def input_num_candy(candy_qu):
    num = input("Введите количество конфет, которые вы забираете: ")
    if num.isdigit():
        num = int(num)
        if num > candy_qu:
            print(
                f'Нельзя взять больше конфет, чем осталось {candy_qu} или больше 28 штук')
            return input_num_candy(candy_qu)
        elif num > 28:
            print(
                'Вы хотите взять больше 28 конфет, это запрещено, возьмите другое количество')
            return input_num_candy(candy_qu)
        elif num == 0:
            print('Нужно взять хотя бы одну конфету')
            return input_num_candy(candy_qu)
        else:
            return num
    else:
        print("Введите целое число")
        return input_num_candy(candy_qu)


def bot_game(candy_qu):
    if candy_qu > 80:
        # если больше 80 конфет, бот берет рандомное количество
        res = random.randint(1, 29)
        return res
    elif candy_qu <= 28:
        res = candy_qu
        return res
    else:
        atemp = candy_qu // 28
        if atemp == 1:
            f = candy_qu  # если остается 1 попытка, это конфеты с 55 до 27; бот пытатется оставить 29 конфет, это получается
            temp = f
            while f >= 29:
                res = temp - 29
                f -= 1
                if res == 0:  # если получается 0, бот проиграл, берем 1 конфету
                    res += 1
            return res
        res = candy_qu - (atemp) * 28 + 1  # пытается оставить всегда 29 конфет
    return res


def main_game(bot=False):
    print("Здравствуйте!\nНачинаем игру с 2021 конфетой.\nДавайте представимся: ")
    player1_name = input("Введите имя первого игрока: ")
    if bot:
        player2_name = "Bot"
    else:
        player2_name = input("Введите имя второго игрока: ")
    print(f'\nИграет {player1_name} против {player2_name}')
    print(f'\nПравила игры: На столе лежит 2021 конфета.\nИграют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.')
    player1 = ''
    player2 = ''
    print(f'\nОпределяю, кто сделает первый ход')
    i = random.randint(1, 2)
    if i == 1:
        player1, player2 = player1_name, player2_name
    else:
        player1, player2 = player2_name, player1_name
    print(f'\nПо результатм жеребьевки первым ходит {player1}')

    candy_quant = 2021   # количество конфет
    allcandy_first = 0
    allcandy_second = 0
    last_player = 0  # запись последнего хода

    print(f'Всего конфет {candy_quant}')
    while candy_quant > 0:
        print(f'Ход игрока {player1}')
        if player1 == "Bot":
            first = int(bot_game(candy_quant))
        else:
            first = int(input_num_candy(candy_quant))
        allcandy_first += first
        candy_quant -= first
        last_player = 1
        print(f'Осталось {candy_quant} конфет')
        if candy_quant > 0:
            if player2 == "Bot":
                second = int(bot_game(candy_quant))
            else:
                second = int(input_num_candy(candy_quant))
            print(f'Ходит {player2}, взял {second} конфет')
            candy_quant -= second
            allcandy_second += second
            last_player = 0
        print(f'Осталось {candy_quant} конфет')

    print(f'В итоге: у {player1} {allcandy_first} конфет, у {player2} {allcandy_second} конфет')
    if last_player == 1:
        print(f'{player1} забрал конфеты последним, он выиграл и все конфеты переходят к нему')
    else:
        print(f'{player2} забрал конфеты последним, он выиграл и все конфеты переходят к нему')


bot_or_humans = input(
    'Будем играть с ботом? Введите "да", иначе играют 2 игрока: ')
if bot_or_humans.lower() == "да":
    main_game(True)
else:
    main_game()

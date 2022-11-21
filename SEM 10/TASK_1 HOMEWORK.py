# Задача 1: Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]
# Задача 1.1 (**): С помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)


from functools import wraps
import datetime
import time
import os
def clear(): return os.system('cls')


clear()


n = int(input('Введите значение n: '))


def decorator_cache(func):
    cache_dt = {}
    @wraps(func)
    def wrapper_cache(*args):
        if args not in cache_dt: # проверяем, был ли вызов функции с такими же аргументами
            cache_dt[args] = func(*args)
        return cache_dt[args]
    return wrapper_cache


def decorator_logger(func):
    @wraps(func)
    def wrapper_logger(*args, **kwargs):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\n'
        log_msg += f'Функция: {func.__name__}\n'
        log_msg += f'Параметры: {", ".join(map(str, args))}\n'
        start_time = time.time()
        res = func(*args, **kwargs)
        execution_time = round(time.time() - start_time, 6)
        log_msg += f'Время выполнения функции: {execution_time} с.\n'
        log_msg += f'Результат: {res}\n\n'
        print(log_msg)
        with open('hw1sem10_log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res
    return wrapper_logger


@decorator_cache
@decorator_logger
def seq(n):
    my_list = []
    for n in range(n):
        n = (1 + n) ** n
        my_list.append(n)
    return my_list


print(seq(n))

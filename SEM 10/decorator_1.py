from functools import wraps
import datetime


# def decorator(func):
#     print('decorator')
#     def wrapper(*args, **kwargs):
#         print('wrapper')
#         return func(*args, **kwargs)
#     print('end decorator')
#     return wrapper


# @decorator
# def area_room(x, y): # декорируемая функция
#     return x * y


# print(area_room(5, 4))

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        wraps docs
        :param args:
        :param kwargs:
        :return:
        """
        # a, b = args
        # res = 2 * (a + b)
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += f'Функция: {func.__name__}\t'
        log_msg += f"Параметры: {', '.join(map(str, args))}\t"
        res = func(*args, **kwargs)
        log_msg += f'результат: {res}\n'
        print(log_msg)
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        # print(f'Площадь комнаты: {res} м2')
        return res
    return wrapper


def html_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        log_msg = '<!DOCTYPE html><html><head><meta charset="UTF-8"><title><Title></title></head><body>'
        log_msg += f"<p>Комната {' на '.join(map(str, args))}\t"
        log_msg += f'Площадь комнаты: {res} м2</p></body></html>'

        with open('log_file.html', 'w', encoding='utf-8') as fp:
            fp.write(log_msg)
        # print(f'Площадь комнаты: {res} м2')
        return res
    return wrapper


@html_decorator
def area_room(x, y):  # декорируемая функция
    """
    Функция возвращает площадь комнаты
    :param x:
    :param y:
    :return:
    """
    return x * y


def main():
    print(area_room(5, 4))
    print(area_room.__doc__)
    # help(area_room(3, 5))


if __name__ == '__main__':
    main()

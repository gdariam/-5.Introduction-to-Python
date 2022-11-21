

def my_func(x, y):
    print(f'{x = }')
    print(f'{y = }')
    return x * y


# my_func(5, 3)
# print('', sep='***', end='\n\n')


# def my_func2(*arg, **kwargs):


def my_func2(x, y, *args,):
    print(f'{x = }')
    print(f'{y = }')
    other = args
    print(f'{other = }')


# my_func2(5, 4, 15, 35, 12)


# def my_func3(x, y, *args,):
#     print(f'{x = }')
#     print(f'{y = }')
#     other = args
#     print(f'{other = }')


# print('oiuyhnmk', 'werfds', '98765', sep='//', end='  ')


def my_func3(x, y, *, a, b, c): # *(или /) указывает, что мы разделяем позиционные параметры (x, y) от именованных (a, b, c)
    print(f'{x = }')
    print(f'{y = }')
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')


# f = '15'
# my_func3(5, f, a=4, b=8, c=10) # именованные параметры передаем без пробелов
# my_func3(5, f, b=8, a=4, c=f)
# (z: int = 12) # передаем значение параметра по умолчанию с пробелами


# def my_func4(*args, **kwargs):
#     a = args
#     b = kwargs # kwargs - keyword arguments = ключевые аргументы, т. е. словари
#     print(f'{a = }')
#     print(f'{b = }')


def my_func4(*args, **kwargs):
    a, b, *c = args
    d = kwargs # kwargs - keyword arguments = ключевые аргументы, т. е. словари
    print(f'{a = }')
    print(f'{b = }')
    print(f'{c = }')
    print(f'{d = }')


my_func4(1, 2, 3, 4, 5, z=12, x=15, v=14) # получаем кортеж и словарь
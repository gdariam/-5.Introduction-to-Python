# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# data.write('\nLINE 12\n')
# data.write('LINE 13\n')
# data.close()

# exit() # не выполнять следующий код
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# with open('file.txt', 'a') as data: # data.close() будет выполнен автоматически
#     data.write('line 1\n')
#     data.write('line 2\n')

# import hello as h
# print(h.f(1))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# Кортежи. Кортеж - это неизменяемый список
# a = (3, 1, 41, 4)
# print(a)
# print(a[-2])
# a[0] = 12  # невозможно присвоить этот элемент в кортеж

# Кортеж из одного элемента: a = (3,)

# for item in a:
#     print(item)

# Словари - неупорядоченные коллекции произвольных объектов с доступом по ключу

# dictionary = {} # пустой словарь
# dictionary = \
# {
# 'up': '↑', # up - ключ, ↑ - значение
# 'left': '←',
# 'down': '↓',
# 'right': '→'
# } # обратный слэш нужен, чтобы описывать с новой строки, если содержание слишком длинное
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# типы ключей могут отличаться

# for v in dictionary:
#     print(dictionary[v])

# Множества

# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
# .union(b) \
# .difference(a.intersection(b))
# # {1, 21, 3, 13}

# Неизменяемое множество
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# Списки
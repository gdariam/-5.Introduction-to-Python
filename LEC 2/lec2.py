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
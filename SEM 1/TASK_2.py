# Задача 2: Найти максимальное из 5 чисел

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# d = int(input('d = '))
# e = int(input('e = '))

a = [2, 33, 43, 132, 39]


def find_max_value(list):
    index = 0
    maxindex = len(list)-1
    max = list[0]
    while index <= maxindex:
        if list[index] > max:
            max = list[index]
        index += 1
    return max


print(find_max_value(a))

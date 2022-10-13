# Задача 5: Реализовать алгоритм перемешивания списка

import random
import os
def clear(): return os.system('cls')


clear()


def getlist():
    return [random.randint(-10, 10) for i in range(10)]


mylist = getlist()


def mixlist(array):
    newlist = mylist
    for i in range(len(newlist)):
        randindex = random.randint(0, len(newlist)-1)
        temp = newlist[i]
        newlist[i] = newlist[randindex]
        newlist[randindex] = temp
    return newlist


print(f'Список {mylist}')
print(f'Новый список после перемешивания {mixlist(mylist)}')

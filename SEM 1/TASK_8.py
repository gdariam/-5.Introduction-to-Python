# Задача 8: Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

def quater(x, y):
    text = None
    if x > 0 and y > 0:
        text = "Первая четверть"
    elif x > 0 and y < 0:
        text = "Вторая четверть"
    elif x < 0 and y < 0:
        text = "Третья четверть"
    elif x < 0 and y > 0:
        text = "Четвертая четверть"
    elif x == 0 and y == 0:
        text = "Пересечение осей"
    elif x == 0 and y != 0:
        text = "Ось X"
    elif x != 0 and y == 0:
        text = "Ось Y"
    return text


x = int(input("Введите X: "))
y = int(input("Введите Y: "))

print(quater(x, y))
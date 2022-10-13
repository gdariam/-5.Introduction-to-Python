# Задача 4: Показать первую цифру дробной части числа

num = float(input("Введите число: "))

round_num = int(num)
result = (num-round_num)*10

print(f' первая цифра дробной части {int(result)}')

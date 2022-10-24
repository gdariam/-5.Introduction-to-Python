# Задача 2: Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
def clear(): return os.system('cls')


clear()

n = int(input("Введите натуральное число: "))

def check_prime(n):
    for i in range(2, (n // 2 + 1)):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    if n < 2:
        return
    prime_numbers = []
    while n > 1:
        for i in range(2, (n + 1)):
            if n % i == 0:
                if check_prime(i):
                    prime_numbers.append(i)
                    n //= i
                    break
    return prime_numbers


print(f"Список простых множителей числа {n} -> {prime_factors(n)}")
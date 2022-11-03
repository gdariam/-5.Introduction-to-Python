from random import randint
lst = ['3', '5', '6', '4', '9']


def summ(x):
    return x + 2
# lambda x: x + 2


def func(x): return x + 2

# DRY - DON'T REPEAT YOURSELF


res = map(int, lst)
print(res)
res2 = map(lambda x: x * 2, res)
print(tuple(res2))


def more_five(x):
    if x > 5:
        return True


res = filter(more_five, res)
res = filter(lambda x: x > 5, res)
print(list(res))

# for i in 'строка':
#     print(i)

print(more_five(10))
print(more_five)

res_range = []
for i in range(10):
    res_range.append(randint(0, 10))

print(res_range)

rand_list = [randint(0, 10) for i in range(10)]
print(rand_list)
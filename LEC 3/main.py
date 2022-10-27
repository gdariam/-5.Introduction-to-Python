# def f(x):
#     x**2

# g = f

# print(type(f))
# print(f(1))
# print(g(1))

# def f(x):
#     return x**2

# print(f(2))

# def f(x):
#     return x**2

# g = f

# print(type(f))
# print(type(g))
# print(f(4))
# print(g(4))

# def calc1(x):
#     return x + 10

# print(calc1(10))

# def calc2(x):
#     return x * 10

# print(calc2(10))

# def math(op, x):
#     print(op(x))

# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x + y

# sum = lambda x, y: x + y


# def mult(x, y):
#     return x * y


# def calc(op, a, b):
#     print(op(a, b))
#     # return(op(a, b))


# calc(lambda x, y: x + y, 4, 5)


# List Comprehension
# list = []

# for i in range(1, 101):
#     # if(i % 2 == 0):
#     list.append(i)

# print(list)

# list = [i for i in range(1, 21) if i % 2 == 0]
# print(list)

# list = [(i, i) for i in range(1, 21) if i % 2 == 0] # список кортежей
# print(list)

# def f(x):
#     return x ** 3

# list = [f(i) for i in range(1, 21) if i % 2 == 0]
# print(list)

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

path = '/Users/Asus/Desktop/GB/files_for_lessons/python_lec3.txt'
f = open(path, 'r')
data = f.read() + ' '
f.close()

numbers = []

while data != '':
    space_pos = data.index(' ')
    numbers.append(int(data[:space_pos]))
    data = data[:space_pos + 1:]

out = []
for e in numbers:
    if not e % 2:
        out.append((e, e ** 2))
print(out)
# Задание №4
# ✔Напишите программу,
# которая вычисляет площадь круга и длину окружности по введённому диаметру.
# ✔Диаметр не превышает 1000 у.е.
# ✔Точность вычислений должна составлять не менее 42 знаков после запятой.

# Вариант 1 без точности в знаках:
# import math
#
# d = input('Введите диаметр не более 1000 ')
#
# while not d.isdigit() or int(d) > 1000 or int(d) < 1:
#     print('Число указанно не корректно')
#     d = input('Введите диаметр не более 1000 ')
#
# d = int(d)
# area = math.pi * (d / 2) ** 2
# length = math.pi * d
# print("Площадь круга = {:.42f}".format(length))
# print("Длина окружности = {:.42f}".format(area))

# Вариант 2 (correct):

import math
import decimal

decimal.getcontext().prec = 50

PI = decimal.Decimal(math.pi)

d = input('Введите диаметр не более 1000 ')

while not d.isdigit() or int(d) > 1000 or int(d) < 1:
    print('Число указанно не корректно')
    d = input('Введите диаметр не более 1000 ')

d = decimal.Decimal(d)
area = PI * (d / 2) ** 2
length = PI * d
print(f'Площадь круга = {area}')
print(f'Длина окружности = {length}')
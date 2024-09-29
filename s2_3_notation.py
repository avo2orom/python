# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает его
# двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
#
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

number: int = int(input('Введите число: '))
ZERO = 0
TWO = 2
EIGHT = 8

# num = number
# num2 = number
# res1: str = ''
# res2: str = ''
#
# while num > ZERO:
#   res1 = str(num % TWO) + res1
#   num //= TWO
#   res2 = str(num2 % EIGHT) + res2
#   num2 //= EIGHT
#
# print(res1, res2)
# print(bin(number), oct(number))

for div in (TWO, EIGHT):
  num = number
  res = ''

  while num > ZERO:
    res = str(num % div) + res
    num //= div

  print(res)



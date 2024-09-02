# Задание №7
# 📌 Пользователь вводит число от 1 до 999.
# Используя операции с числами сообщите что введено:
# цифра, двузначное число или трёхзначное число.
# 📌Для цифры верните её квадрат, например 5 - 25
# 📌 Для двузначного числа произведение цифр, например 30 - 0
# 📌 Для трёхзначного числа его зеркальное отображение, например 520 - 25
# 📌 Если число не из диапазона, запросите новое число
# 📌 Откажитесь от магических чисел
# 📌 В коде должны быть один input и один print

def numbers():
    LOWER_LIMINT = 1
    UPPER_LIMIT = 999
    ONE = 1
    NUM = 9
    TEN =10
    HUNDRES = 100


    number = LOWER_LIMINT - ONE

    while number < LOWER_LIMINT or number > UPPER_LIMIT:
        number = int(input(f'Введите число от {LOWER_LIMINT} до {UPPER_LIMIT}: '))

    if number < TEN:
        result = f'{number} - цифра и ее квадрат = {number*number}'

    elif number < HUNDRES:
        prod = (number // TEN) * (number % TEN)
        result =  f'{number} - двузначное число и произведение его цифр = {prod}'

    else:
        first = number // HUNDRES
        second = number % HUNDRES // TEN
        third = number % TEN
        mirror = third * HUNDRES + second * TEN + first
        result =  f'{number} - трехзначное число и его зеркальное отображение = {mirror}'

    print(result)



if __name__ == '__main__':
    numbers()
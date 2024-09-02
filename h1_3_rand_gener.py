# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

def random_generation():
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000

    from random import randint
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print(num)
    count = 10
    res = "К сожалению, ты не угадал!"


    while count > 0:
        number = int(input(f'Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
        if number < UPPER_LIMIT and number > LOWER_LIMIT:
            if number != num:
                if number < num:
                    print("Неверный номер! Нужно ввести число больше")
                    print(f'Осталось {count-1} попыток')
                else:
                    print("Неверный номер! Нужно ввести число меньше")
                    print(f'Осталось {count-1} попыток')
                count -= 1
            else:
                res = "Поздравляю, ты угадал!"
                break
        else:
            print("Номер не соответствует условию!")
            exit()

    print(f'{res} Было загадано число {num}')

if __name__ == '__main__':
    random_generation()
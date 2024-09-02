# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def simple_numbers():
    LOWER_LIMINT = 0
    UPPER_LIMIT = 100000
    ONE = 1

    const = 2
    number = LOWER_LIMINT - ONE

    while number < LOWER_LIMINT or number > UPPER_LIMIT:
        number = int(input(f'Введите число от {LOWER_LIMINT} до {UPPER_LIMIT}: '))
    #i = 1
    print(range(2,number))
    for i in range(2,number):
        res = number % i == 0
        print(i, res)
        if res:
            print('Это число не является простым')
            break

    if res == False:
        print('Это число является простым')

if __name__ == '__main__':
    simple_numbers()
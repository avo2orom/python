# Задание №9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def multiplication_table():
    LOWER_LIMINT = 2
    UPPER_LIMIT = 10
    COLUMNS = 4

    for seed_first_num in (LOWER_LIMINT, LOWER_LIMINT + COLUMNS):
        for second_num in range(LOWER_LIMINT, UPPER_LIMIT + 1):
            for first_num in range(seed_first_num, seed_first_num + COLUMNS):
                print(f'{first_num} X {second_num:>2} = {first_num * second_num:>2}' , end='\t')
            print()
        print()

if __name__ == '__main__':
    multiplication_table()
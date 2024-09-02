# Задание №8
# 📌 Нарисовать в консоли ёлку спросив у пользователя количество рядов.
# 📌 Пример результата:

def draw_christmas_tree():
    SPACE = ' '
    STAR = '*'
    ONE = 1

    rows = int(input('Сколько рядов у елки?: '))

    spaces = rows - ONE
    stars = ONE

    for _ in range(rows):
        print(SPACE * spaces + STAR * stars)
        stars += 2
        spaces -= 1

if __name__ == '__main__':
    draw_christmas_tree()


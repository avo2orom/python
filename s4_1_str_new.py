# Задание №1
# ✔Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔Строки нумеруются начиная с единицы.
# ✔Слова выводятся отсортированными согласно кодировки Unicode.
# ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова
# был один пробел между ним и номером строки

def user_input(text):
    words = sorted(text.split())
    max_length = len(max(words, key=len))

    for i, word in enumerate(words, start=1):
        print(f'{i}. {word:>{max_length}}')

input_text = input('Введите текст: ')
user_input(input_text)
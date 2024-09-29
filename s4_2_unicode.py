# Задание №2
# ✔Напишите функцию, которая принимает строку текста.
# ✔Сформируйте список с уникальными кодами Unicode
# каждого символа введённой строки отсортированный по убыванию.

def unique_unicode(text: str) -> list[int]:
    set_letters = sorted(set(text), reverse=True)
    return list(map(ord, set_letters))


text_out = input("Введите текст: ")
print(*unique_unicode(text_out))

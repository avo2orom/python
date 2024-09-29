# Задание №3
# ✔Функция получает на вход строку из двух чисел через пробел.
# ✔Сформируйте словарь, где ключом будет символ из Unicode, а значением —  целое число.
# ✔Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

def user_input_str(text: str) -> dict[str, int]:
    start, stop = sorted(map(int, text.split()))
    my_dict = {}

    for key in range(start, stop, + 1):
        my_dict[chr(key)] = key
    return my_dict

input_text = input("Введите 2 числа через пробел: ")
print(user_input_str(input_text))
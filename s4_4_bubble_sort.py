# Задание №4
# ✔Функция получает на вход список чисел.
# ✔Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# ✔Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

def bubble_sort(list_1: list[int]):
    for i in range(len(list_1) - 1):
        is_sorted = True
        for j in range(len(list_1) - 1):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
                is_sorted = False
        if is_sorted:
            return


new_list = [1, 5, 8, 56, 23, 1, 6, 101, 104,109]
print(new_list)
bubble_sort(new_list)
print(new_list)
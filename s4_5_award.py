# Задание №5
# ✔Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔Сумма рассчитывается как ставка умноженная на процент премии.

def salary(names: list[str], base_salary: list[int], percent: list[str]) -> dict[str, int]:
    my_dict = {}
    for name, bases, proc in zip(names, base_salary, percent):
        my_dict[name] = bases * float(proc[:-1]) / 100
    return my_dict

names_in = ['Ivan', 'Petr', 'Sergey']
base_salary_in = [100_000, 150_000, 200_000]
persent_in = ['10.25%', '5.6%', '7%']
print(salary(names_in, base_salary_in, persent_in))
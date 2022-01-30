"""
ЗАДАНИЕ № 3
Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    """ Возвращает сумму наибольших двух аргументов """
    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
        arg3 = float(arg3)
    except ValueError:
        print("Ошибка. Некорректные параметры")
    else:
        return sum(sorted([arg1, arg2, arg3])[1:])


a1 = input("Введите параметр № 1: ")
a2 = input("Введите параметр № 2: ")
a3 = input("Введите параметр № 3: ")
result = my_func(a1, a2, a3)
if result is not None:
    print(f"Сумма двух наибольших аргументов равна {result}")

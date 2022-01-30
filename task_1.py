"""
ЗАДАНИЕ № 1
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = ["hallo", 34, False, (2, 5, 6), {8, 9, 3}]

if type(my_list[0]) is str:
    print(f"Тип элемента '{my_list[0]}' - str")

if type(my_list[1]) is int:
    print(f"Тип элемента '{my_list[1]}' - int")

if type(my_list[2]) is bool:
    print(f"Тип элемента '{my_list[2]}' - bool")

if type(my_list[3]) is tuple:
    print(f"Тип элемента '{my_list[3]} - tuple")

if type(my_list[4]) is set:
    print(f"Тип элемента '{my_list[4]}' - set")

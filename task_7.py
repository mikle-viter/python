"""
ЗАДАНИЕ № 7
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""


def only_low_chars_and_lat(string_list):
    """ Проверяет, чтобы все элементы списка были строками только из маленьких латинских букв"""
    flag_error = False
    for string in string_list:
        if flag_error:
            break
        for char in string:
            if ord(char) < 97 or ord(char) > 122:
                flag_error = True
                break
    return not flag_error


def my_capitalise(string: str):
    """ Переводит первый символ строки в заглавный и возвращает строку"""
    return string.capitalize()


def int_func(string_list):  # Я ЭТУ ФУНКЦИЮ СЛЕГКА МОДЕРНИЗИРОВАЛ, ДУМАЮ ЭТО ЖЕ НЕ БУДЕТ СЧИТАТЬСЯ ОШИБКОЙ
    """  Вывод переданных аргументов с большой первой буквы """
    return ' '.join(map(my_capitalise, string_list)) if only_low_chars_and_lat(string_list) \
        else "Ошибка. Не все буквы в каждом слове являются маленькими и латинскими"


print(int_func(input("Введите строку из слов, разделённых пробелом (только из маленьких латинских букв): ").split()))

"""
ЗАДАНИЕ № 6
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""


def only_low_chars_and_lat(string):
    """ Проверяет, чтобы строка состояла только из маленьких латинских букв """
    flag_error = False
    for char in string:
        if ord(char) < 97 or ord(char) > 122:
            flag_error = True
            break
    return not flag_error


def int_func(string):
    """  Вывод переданных аргументов с большой первой буквы """
    if not only_low_chars_and_lat(string):
        return string + " -> " + "Ошибка. Не все буквы в слове являются маленькими и латинскими"
    else:
        return string + " -> " + string.capitalize()


print(int_func("a"))
print(int_func("aaa"))
print(int_func("ert"))
print(int_func("ert45"))
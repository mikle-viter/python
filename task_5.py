"""
ЗАДАНИЕ № 5
Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def my_sum(list_digits):
    """ Вычисление суммы переданного списка произвольной длины """
    try:
        for i in range(len(list_digits)):
            list_digits[i] = float(list_digits[i])
    except ValueError:
        print("Ошибка. Все значения входной строки должны быть числами, разделенными пробелами")
        return
    else:
        return sum(list_digits)


input_string = ""
accumulated_amount = 0.0
while True:
    input_string = input("Введите строку чисел, разделенных пробелами, или Q для выхода из программы: ").lower()
    if input_string == "q":
        break
    else:
        tmp_list = input_string.split()
        if 'q' in tmp_list:
            is_q = True
            tmp_list = tmp_list[0:tmp_list.index('q')]
        else:
            is_q = False
        current_amount = my_sum(tmp_list)
        if current_amount is not None:
            accumulated_amount += current_amount
        print(f"Накопленная сумма: {accumulated_amount}")
        if is_q:
            break

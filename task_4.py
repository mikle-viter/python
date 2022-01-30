"""
ЗАДАНИЕ № 4
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

while True:
    number_str = input("Введите целое положительное число: ")
    number = float(number_str)
    if (not number_str.isdigit()) or (number < 0.0) or (number % 1.0 > 0.0):    # по остатку от деления на 1.0
                                                                                # проверяю наличие дробной части
        print("Ошибка: вы не ввели целое положительное число.")
    else:
        number = int(number)
        length = len(number_str)
        i = 1
        max_digit = number_str[0]
        while i < length:
            current_digit = number_str[i]
            i += 1
            if current_digit > max_digit:
                max_digit = current_digit
        print(f"В числе {number_str} самое большое число - это {max_digit}")

    answer = input("\r\nВведите 1, если хотите попробовать еще раз и 0 для выхода из программы: ")
    if answer == "0":
        break

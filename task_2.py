""""
ЗАДАНИЕ № 2

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(ZeroDivisionError):
    """ Класс-исключение, обрабатывающий стуацию деления на ноль """
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


if __name__ == "__main__":
    inp_data = input("Введите два аргумента через пробел: делимое и делитель: ")
    try:
        inp_data = inp_data.split()
        dividend = float(inp_data[0])
        divisor = float(inp_data[1])
        if divisor == 0.0:
            raise MyZeroDivisionError("Ошибка деления на ноль")
    except ValueError:
        print("Неверный формат входных данных")
    except MyZeroDivisionError as err:
        print(err)
    else:
        print(round(dividend / divisor, 2))

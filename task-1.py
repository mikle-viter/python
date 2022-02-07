"""
ЗАДАНИЕ № 1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6          8    3    7    1
51    86        -1   64   -8
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    """ Класс 'Матрица'.
        Атрибуты:
            __list_of_list  - Список списков, хранящий значения ячеек матрицы
            __m             - Размер матрицы (число строк)
            __n             - Размер матрицы (число столбцов)
            __name          - Имя объекта
            correct         - Флаг, корректно ли произошла инициализация объекта.
            print_mess      - Флаг, выводить ли сообщение о созданиии/уничтожении объекта или ошибке
        Методы:
            __add__         - Перегруженный оператор сложения, А + В
            __del__         - Перегруженный деструктор
            __init__        - Перегруженный конструктор
            __str__         - Перегруженный оператор приведения к строковому типу, str(A)
            get_matrix_list - Возвращает список списков, то есть значения ячеек матрицы
            get_name        - Возвращает имя объекта
            get_size        - Возвращает размерность матрицы в виде списка [Число_строк х Число_столбцов]
    """

    def __init__(self, input_list, print_mess=False, input_name='Любовь'):
        """
        Конструктор объекта. Входные аргументы:
            input_list - список списков для инициализации матрицы
            print_mess - флаг, выводить ли сообщение о созданиии/уничтожении объекта или ошибке
            input_name - имя объекта класса "матрица"
        """
        try:
            self.__name = input_name
            self.print_mess = print_mess
            self.__list_of_list = input_list
            self.__m = len(self.__list_of_list)
            self.__n = len(self.__list_of_list[0])
            # Проверка одинаковой размерности всех вложенных списков
            if not all([len(lst) == len(input_list[0]) for lst in input_list]):
                raise Exception
            self.correct = "True"
        except Exception:
            if self.print_mess:
                print(f"Не могу инициализировать атрибуты объекта '{input_name}'.")
            self.correct = "False"
        else:
            if self.print_mess:
                print(f"Атрибуты объекта '{self.__name}' успешно инициализированы.")

    def __del__(self):
        """ Деструктор объекта """
        if self.print_mess:
            print(f"Объект '{self.__name}' удален")

    def __add__(self, other):
        """ Сложение матриц через оператор +, пример: A + B"""
        if (self.__m != other.__m) or (self.__n != other.__n):
            return None
        else:
            """ Применяется две функции map. 
                Внутренняя - складывает поэлементно вложенные списки с помощью lambda-функции сложения.
                Внешняя - применяет внутреннюю функцию map для каждого списка из списка-списков
                Также применяется две функции list для преобразования объекта класса map в объект класса list,
                так как класс Matrix хранит список-списков.
                Реализовал я это специально, а не банальным перебором во внешнем и вложенном цикле"""
            return Matrix(list(map(lambda x, y: list(map(lambda a, b: a + b, x, y)),
                                   self.__list_of_list, other.__list_of_list)))

            # Способ № 2 - через перебор циклами
            # result = list()
            # for i in range(self.__m):
            #     result.append(list())
            #     for j in range(self.__n):
            #         result[i].append(self.__list_of_list[i][j] + other.__list_of_list[i][j])
            # return Matrix(result)

    def __str__(self):
        """ Вывод матрицы на экран """
        new_line = "\n\t\t"
        ret_str = f"Объект '{self.__name}':{new_line}"
        for i in range(self.__m):
            for j in range(self.__n):
                ret_str += str(self.__list_of_list[i][j]) + " "
            if i < self.__m - 1:
                ret_str += new_line
        return ret_str

    def get_matrix_list(self):
        """ Возврат списка списков """
        return self.__list_of_list

    def get_name(self):
        """ Возврат имени объекта """
        return self.__name

    def get_size(self):
        """ Возврат размерности матрицы MxN """
        return [self.__m, self.__n]


if __name__ == "__main__":
    error_matrix = Matrix([[1, 2, 3, 4],
                           [1, 2]],
                          True, "Ошибочная матрица")
    neo = Matrix([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [1, 2, 3, 4],
                  [5, 6, 7, 8]],
                 input_name='Нео', print_mess=True)
    triniti = Matrix([[8, 7, 6, 5],
                      [4, 3, 2, 1],
                      [8, 7, 6, 5],
                      [4, 3, 2, 1]],
                     True, 'Тринити')
    if neo.correct and triniti.correct:
        print(neo)
        print(triniti)
        love = neo + triniti
        print("\nСюжет из фильма 'Матрица':")
        print(f"\t{neo.get_name()} + {triniti.get_name()} = {love.get_name()}\n{love}\n")

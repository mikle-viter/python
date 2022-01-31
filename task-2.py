"""
ЗАДАНИЕ № 2
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road():
    """ Класс Дорога. Значения длины и ширины передается конструктору. Есть метод изменения массы 1 м2.
        Осуществляет расчет массы асфальта на покрытие дороги (т) """
    __length = 0.0
    __width = 0.0
    __weight_m2 = 25.0

    def __init__(self, l, w):
        try:
            l = float(l)
            w = float(w)
            if l <= 0.0 or w <= 0.0:
                raise ValueError
        except ValueError:
            print("Некорректные параметры длины/ширины дороги. Они должны быть положительными вещественными числами")
        else:
            self.__length = l
            self.__width = w

    def change_weight_m2(self, new_weight):
        """ Метод изменения массы 1м2 асфальта толщиной 1 см """
        try:
            new_weight = float(new_weight)
            if new_weight <= 0.0:
                raise ValueError
        except ValueError:
            print("Ошибка. Масса 1 м2 асфальта должна быт положительным вещественным числом")
        else:
            self.__weight_m2 = new_weight

    def calc_weight(self, thikness=1, round_cnt=2):
        """ Метод расчета массы асфальта на покрытие дороги (т) """
        try:
            thikness = float(thikness)
            round_cnt = int(round_cnt)
            if thikness <= 0.0 or round_cnt < 0:
                raise ValueError
        except ValueError:
            return None
        else:
            return round((self.__length * self.__width * self.__weight_m2 * thikness) / 1000, round_cnt)


if __name__ == "__main__":
    my_width = 20
    my_length = 5000
    my_thikness = 5
    my_round_cnt = 0
    my_road = Road(my_length, my_width)
    my_weight = my_road.calc_weight(my_thikness, my_round_cnt)
    if my_weight is None:
        print("Ошибка входных параметров")
    else:
        print(f"Масса асфальта на покрытие дороги шириной {my_width} м, длиной {my_length} м, "
              f"толщиной {my_thikness} см составит: {my_weight} т")

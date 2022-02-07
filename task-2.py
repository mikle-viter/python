"""
ЗАДАНИЕ № 2
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class AbstractClothes:
    """Абстрактный класс 'Одежда' """

    __objects = []  # Список ссылок на все объекты-наследники класса Clothes

    def __init__(self, name):
        self.__name = name
        self.__objects.append(self)  # Добавление объекта в список одежды

    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def all_consumption(self):
        # Сумма значений всех методов consumption для всех созданных объектов
        return f"Вызов для объекта '{self.__class__.__name__}' с именем '{self.name}'. " \
            f"Общий расход ткани: {round(sum([obj.consumption for obj in self.__objects]), 2)} м2"


class Coat(AbstractClothes):
    """ Класс Пальто """
    def __init__(self, name, v):
        super().__init__(name)
        self.__V = v

    @property
    def consumption(self):
        return round(self.__V / 6.5 + 0.5, 2)

    @property
    def fabric_consumption(self):
        return f"Расход ткани на '{self.name}' размера {self.__V}: {self.consumption} м2"


class Costume(AbstractClothes):
    """ Класс Костюм """
    def __init__(self, name, h):
        super().__init__(name)
        self.__H = h

    @property
    def consumption(self):
        return round(2 * self.__H + 0.3, 2)

    @property
    def fabric_consumption(self):
        return f"Расход ткани на '{self.name}' роста {self.__H} м: {self.consumption} м2"


if __name__ == "__main__":
    my_clothes = [Coat("Пальто № 1", 52), Coat("Пальто № 2", 48), Costume("Костюм № 1", 1.9),
                  Costume("Костюм № 2", 1.6)]

    # Все объекты хранят списки ссылок на всю одежду, поэтому результаты вызова all_consumption будут одинаковы
    for cl in my_clothes:
        print(cl.fabric_consumption)
        print(cl.all_consumption)
        print()

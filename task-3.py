"""
ЗАДАНИЕ № 3
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker():
    """ Класс Рабочий. Атрибуты: имя, фамилия, должность, доход (оклад, премия).
        Методы: установка оклада, установка премии"""
    name = ''
    surname = ''
    position = ''
    __income = {"wage": 0.0, "bonus": 0.0}

    def __init__(self, n, s, p):
        self.name = n
        self.surname = s
        self.position = p

    def set_wage(self, w):
        """ Метод установки оклада """
        try:
            w = float(w)
            if w <= 0.0:
               raise ValueError
        except ValueError:
            print("Ошибка. Оклад должен быть положительным вещественным числом")
        else:
            self.__income.update({"wage": w})

    def set_bonus(self, b):
        """ Метод установки премии """
        try:
            b = float(b)
        except ValueError:
            print("Ошибка. Премия должна быть вещественным числом")
        else:
            self.__income.update({"bonus": b})

    def get_income(self):
        """ Метод получения словаря с доходом и премией"""
        return self.__income


class Position(Worker):
    """ Класс Должость. Методы: получение полного имени, получение дохода с учетом премии """

    def get_full_name(self):
        """ Метод получения полного имени сотрудника """
        return self.name + ' ' + self.surname

    def get_position(self):
        """ Метод получает должность сотрудника """
        return self.position

    def get_total_income(self):
        """ Метод получения дохода с учетом премии """
        income = self.get_income()
        return income["wage"] + income["bonus"]


user_1 = Position("Иван", "Добростроев", "Инженер")
user_1.set_wage(90000)
user_1.set_bonus(30000)
print(f"{user_1.get_full_name()} в должности {user_1.get_position()} получает {user_1.get_total_income()} руб.")

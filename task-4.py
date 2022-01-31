"""
ЗАДАНИЕ № 4
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""

#  В этот раз пишу без проверок на типы и комментариев, а то итак много кода для обзора получается

class Car():
    __speed = 0.0
    __color = ""
    __name = ""
    __is_police = False

    def __init__(self, color, name, is_police=False):
        self.__color, self.__name, self.__is_police = color, name, is_police

    def recolor(self, new_color):
        print(f"Цвет авто `{self.__name}` изменен с `{self.__color}` на `{new_color}`")
        self.__color = new_color

    def rename(self, new_name):
        print(f"Авто `{self.__name}` с цветом `{self.__color}` теперь будет называться `{new_name}`")
        self.__name = new_name

    def go(self, new_speed):
        self.__speed = new_speed
        print(f"Авто `{self.__name}` цвета `{self.__color}` поехало со скоростью {self.__speed} км/ч")

    def stop(self):
        self.__speed = 0.0
        print(f"Авто `{self.__name}` цвета `{self.__color}` остановилось")

    def turn(self, direction):
        print(f"Авто `{self.__name}` цвета `{self.__color}` повернуло в направлении `{direction}`")

    def get_speed(self):
        return self.__speed

    def show_speed(self):
        print(f"Текущая скорость авто `{self.__name}` цвета `{self.__color }` составляет {self.__speed} км/ч")

    def check_police(self):
        print(f"Авто `{self.__name}` цвета `{self.__color }` - это {'полиция' if self.__is_police else 'не полиция'}")


class TownCar(Car):
    __max_speed = 60

    def show_speed(self):
        curr_speed = self.get_speed()
        if curr_speed > 60.0:
            print(f"Городская машина превысила скорость. Максимальная 60 км/ч, а реальная {curr_speed} км/ч")


class SportCar(Car):
    pass


class WorkCar(Car):
    __max_speed = 40

    def show_speed(self):
        work_speed = self.get_speed()
        if work_speed > self.__max_speed:
            print(f"Рабочая машина движется с превышением скорости {work_speed} "
                  f"- {self.__max_speed} = {work_speed - self.__max_speed} км/ч")


class PoliceCar(Car):
    pass


if __name__ == "__main__":

    my_town_car = TownCar("красный", "жигули")
    my_sport_car = SportCar("серебристый", "ferrari")
    my_work_car = WorkCar("оранжевый", "мусоровоз")
    my_police_car = PoliceCar("белый", "huindai", True)

    my_town_car.go(50)
    my_town_car.turn("направо")
    my_town_car.stop()
    my_town_car.go(100)
    my_town_car.show_speed()

    print()
    my_sport_car.go(150)
    my_sport_car.stop()
    my_sport_car.recolor("зелёный")
    my_sport_car.check_police()

    print()
    my_work_car.go(35)
    my_work_car.show_speed()
    my_work_car.rename("машина для вывоза мусора")
    my_work_car.turn("направо")
    my_work_car.turn("налево")
    my_work_car.stop()
    my_work_car.go(50)
    my_work_car.show_speed()

    print()
    my_police_car.go(100)
    my_police_car.stop()
    my_police_car.rename("машина сотрудников ГИБДД")
    my_police_car.recolor("бежевый")
    my_police_car.show_speed()
    my_police_car.check_police()

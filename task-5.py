"""
ЗАДАНИЕ № 5
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery():
    __title = ""

    def __init__(self, name):
        self.__title = name

    def get_title(self):
        return self.__title

    def set_title(self, new_name):
        self.__title = new_name

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Ручкой {self.get_title()} рисовать тоже можно")


class Pencil(Stationery):
    def draw(self):
        print(f"Карандашом {self.get_title()}, особенно мягким, рисовать удобно")


class Handle(Stationery):
    def draw(self):
        print(f"Рисовать маркером {self.get_title()} можно, главное - не на стекле")


my_pen = Pen("Parker 567/56")
my_pencil = Pencil("Satin 45/f")
my_handle = Handle("Brend GH")

my_pen.draw()
my_pen.set_title("Parker 567")
my_pen.draw()

my_pencil.draw()

my_handle.draw()

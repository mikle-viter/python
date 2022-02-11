""""
ЗАДАНИЕ № 4

Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    """ Класс Склад """
    def __init__(self, name, address, area):
        self.equip = {}
        self.name = name
        self.address = address
        self.area = area


class Equipment:
    """ Класс Оргтехника """
    def __init__(self, **kwargs):
        self.inv_num = kwargs['inv_num']
        self.model = kwargs['model']
        self.brand = kwargs['brand']
        self.weight = kwargs['weight']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.depth = kwargs['depth']
        self.power = kwargs['power']


class Printer(Equipment):
    """ Класс Принтер """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = kwargs['p_type']
        self.color = kwargs['color']
        self.speed = kwargs['speed']
        self.resolution = kwargs['resolution']


class Scanner(Equipment):
    """ Класс Сканер """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.interface = kwargs['interface']
        self.sensor = kwargs['sensor']
        self.color_depth = kwargs['color_depth']
        self.resolution = kwargs['resolution']


class Xerox(Equipment):
    """ Класс Ксерокс """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.format = kwargs['format']
        self.speed = kwargs['speed']
        self.max_load = kwargs['max_load']


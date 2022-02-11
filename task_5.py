""""
ЗАДАНИЕ № 5

Продолжить работу над первым заданием.
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
"""


class Warehouse:
    """ Класс Склад """
    def __init__(self, name, address, area):
        self.equip = dict()   # {inv_num: [equipment_object_link, "department"]}
        self.name = name
        self.address = address
        self.area = area

    def __str__(self):
        return f"Склад '{self.name}' по адресу '{self.address}' площадью '{self.area}' м2"

    @property
    def warehouse_equipment(self):
        """ Получить информацию об оборудовании на складе """
        info = ""
        old_dep = ""
        num = 0
        for inv_num, obj_equip, depart in \
                sorted([(inv_num, equip[0], equip[1]) for inv_num, equip in self.equip.items()],
                                     key = lambda x: x[2]):   # Сортировка и группировка оборудования по отделам
            if depart != old_dep:
                num = 1
                old_dep = depart
                info += f"\n{depart}:"
            else:
                num += 1
            info += f"\n\t{num}) {obj_equip}"
        return info

    def take_to_warehouse(self, equipment_object_link, department):
        """ Принять оборудование на склад """
        self.equip.update({equipment_object_link.inv_num: [equipment_object_link, department]})
        equipment_object_link.status = 1   # На складе
        print(f"Оборудование '{equipment_object_link.brand}'"
              f" модели '{equipment_object_link.model}' принято на склад")

    def take_to_department(self, inv_num):
        """ Выдать оборудование со склада в соответствующее подразделение"""
        equipment_object_link = self.equip.get(inv_num, None)
        if equipment_object_link is None:
            print(f"Орудование по инвентарному номеру '{inv_num}' не найдено")
        else:
            print(f"Оборудование '{equipment_object_link[0].brand}"
                  f" {equipment_object_link[0].model}' выдано со склада "
                  f"в подразделение '{equipment_object_link[1]}'")
            # self.equip.pop(inv_num)
            equipment_object_link[0].status = 2  # В отделе


class Equipment:
    """ Класс Оргтехника """
    def __init__(self, params):
        self.inv_num = params['inv_num']
        self.model = params['model']
        self.brand = params['brand']
        self.weight = params['weight']
        self.width = params['width']
        self.height = params['height']
        self.depth = params['depth']
        self.power = params['power']
        self.status = 0   # Позиция не определена

    @staticmethod
    def status_to_str(status):
        if status == 1:
            return "на складе"
        elif status == 2:
            return "в отделе"
        else:
            return "не определен"

    def __str__(self):
        return f"Инв. №: {self.inv_num}, {self.brand} {self.model}, статус: {Equipment.status_to_str(self.status)}"

    def get_attribute(self, attr_name):
        return self.__getattribute__(attr_name)

    def set_attribute(self, attr_name, attr_value):
        return self.__setattr__(attr_name, attr_value)


class Printer(Equipment):
    """ Класс Принтер """
    def __init__(self, params):
        super().__init__(params)
        self.p_type = params['p_type']
        self.color = params['color']
        self.speed = params['speed']
        self.resolution = params['resolution']


class Scanner(Equipment):
    """ Класс Сканер """
    def __init__(self, params):
        super().__init__(params)
        self.interface = params['interface']
        self.sensor = params['sensor']
        self.color_depth = params['color_depth']
        self.resolution = params['resolution']


class Xerox(Equipment):
    """ Класс Ксерокс """
    def __init__(self, params):
        super().__init__(params)
        self.format = params['format']
        self.speed = params['speed']
        self.max_load = params['max_load']


class TestValues:
    test_data = [
        ("Printer", "Бухгалтерия", {"inv_num": "1000", "model": "Phaser 3020", "brand": "Xerox",
                    "weight": "2.1", "width": "0.52", "height": "0.4", "depth": "0.3", "power": "0.06",
                    "p_type": "лазерный", "color": "ч/б", "speed": "20", "resolution": "1200х1200"}),
        ("Printer", "Бухгалтерия", {"inv_num": "1001", "model": "ECOSYS P2335dn", "brand": "Kyocera",
                    "weight": "2.6", "width": "0.55", "height": "0.35", "depth": "0.31", "power": "0.065",
                    "p_type": "лазерный", "color": "ч/б", "speed": "25", "resolution": "1200х1200"}),
        ("Printer", "Отдел кадров", {"inv_num": "1002", "model": "HL-1202R", "brand": "Brother",
                    "weight": "2.4", "width": "0.53", "height": "0.38", "depth": "0.32", "power": "0.07",
                    "p_type": "лазерный", "color": "ч/б", "speed": "20", "resolution": "2400х600"}),
        ("Printer", "Юридический отдел", {"inv_num": "1003", "model": "Color Laser 150a", "brand": "HP",
                    "weight": "2.2", "width": "0.57", "height": "0.41", "depth": "0.32", "power": "0.075",
                    "p_type": "лазерный", "color": "ч/б", "speed": "25", "resolution": "600х600"}),
        ("Scanner", "Отдел продаж", {"inv_num": "1004", "model": "imageFORMULA DR-F120", "brand": "Canon ",
                    "weight": "1.7", "width": "0.62", "height": "0.32", "depth": "0.61", "power": "0.09",
                    "interface": "USB 2.0", "sensor": "CIS", "color_depth": "32", "resolution": "600x600"}),
        ("Scanner", "Секретариат", {"inv_num": "1005", "model": "P-215II", "brand": "Canon ",
                    "weight": "1.5", "width": "0.63", "height": "0.33", "depth": "0.61", "power": "0.08",
                    "interface": "USB 2.0", "sensor": "CIS", "color_depth": "32", "resolution": "600x600"}),
        ("Scanner", "Бухгалтерия", {"inv_num": "1006", "model": "Scanjet Pro 2000 s2", "brand": "HP",
                    "weight": "2.1", "width": "0.64", "height": "0.41", "depth": "0.69", "power": "0.085",
                    "interface": "USB 3.0", "sensor": "CIS", "color_depth": "48", "resolution": "600x600"}),
        ("Scanner", "Секретариат""Отдел МТО", {"inv_num": "1007", "model": "imageFORMULA DR-C225 II", "brand": "Canon ",
                    "weight": "2.3", "width": "0.65", "height": "0.39", "depth": "0.68", "power": "0.095",
                    "interface": "USB 2.0", "sensor": "CIS", "color_depth": "32", "resolution": "600x600"}),
        ("Xerox", "Отдел по работе с клиентами", {"inv_num": "1008", "model": "ECOSYS M2235dn", "brand": "Kyocera",
                    "weight": "2.9", "width": "0.66", "height": "0.34", "depth": "0.089", "power": "0.08",
                    "format": "ч/б", "speed": "35", "max_load": "30000"}),
        ("Xerox", "Отдел маркетинга", {"inv_num": "1009", "model": "DCP-L2500DR", "brand": "Brother",
                    "weight": "3.2", "width": "0.64", "height": "0.36", "depth": "0.078", "power": "0.078",
                    "format": "ч/б", "speed": "26", "max_load": "28000"}),
        ("Xerox", "Архив", {"inv_num": "1010", "model": "MFC-L2700DNR", "brand": "Brother",
                    "weight": "3.8", "width": "0.63", "height": "0.32", "depth": "0.087", "power": "0.067",
                    "format": "ч/б", "speed": "24", "max_load": "25000"}),
        ("Xerox", "Отдел МТО", {"inv_num": "1011", "model": "LaserJet Pro MFP M28w", "brand": "HP",
                    "weight": "3.5", "width": "0.61", "height": "0.33", "depth": "0.095", "power": "0.088",
                    "format": "ч/б", "speed": "18", "max_load": "20000"})
    ]


if __name__ == "__main__":
    pr1 = Printer(TestValues.test_data[0][2])
    pr2 = Printer(TestValues.test_data[1][2])
    pr3 = Printer(TestValues.test_data[2][2])
    pr4 = Printer(TestValues.test_data[3][2])

    sc1 = Scanner(TestValues.test_data[4][2])
    sc2 = Scanner(TestValues.test_data[5][2])
    sc3 = Scanner(TestValues.test_data[6][2])
    sc4 = Scanner(TestValues.test_data[7][2])

    xe1 = Xerox(TestValues.test_data[8][2])
    xe2 = Xerox(TestValues.test_data[9][2])
    xe3 = Xerox(TestValues.test_data[10][2])
    xe4 = Xerox(TestValues.test_data[11][2])

    # Принятие оборудования на склад с прикрпелением к соответствующим отделам
    wh1 = Warehouse("Склад № 1", "ул. Ленина 23/45", "200")

    wh1.take_to_warehouse(pr1, TestValues.test_data[0][1])
    wh1.take_to_warehouse(pr2, TestValues.test_data[1][1])
    wh1.take_to_warehouse(pr3, TestValues.test_data[2][1])
    wh1.take_to_warehouse(pr4, TestValues.test_data[3][1])

    wh1.take_to_warehouse(sc1, TestValues.test_data[4][1])
    wh1.take_to_warehouse(sc2, TestValues.test_data[5][1])
    wh1.take_to_warehouse(sc3, TestValues.test_data[6][1])
    wh1.take_to_warehouse(sc4, TestValues.test_data[7][1])

    wh1.take_to_warehouse(xe1, TestValues.test_data[8][1])
    wh1.take_to_warehouse(xe2, TestValues.test_data[9][1])
    wh1.take_to_warehouse(xe3, TestValues.test_data[10][1])
    wh1.take_to_warehouse(xe4, TestValues.test_data[11][1])

    # Вывод информации о складком оборудовании
    print()
    print(wh1)
    print(f"Состояние склада по отделам:{wh1.warehouse_equipment}")

    # Выдача оборудования в отделы
    print()
    print()
    wh1.take_to_department(pr2.inv_num)
    wh1.take_to_department(pr4.inv_num)
    wh1.take_to_department(sc1.inv_num)
    wh1.take_to_department(xe3.inv_num)
    wh1.take_to_department(xe4.inv_num)

    # Вывод информации о складком оборудовании
    print()
    print(wh1)
    print(f"Состояние склада по отделам:{wh1.warehouse_equipment}")

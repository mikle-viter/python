""""
ЗАДАНИЕ № 6

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

from task_5 import Warehouse, Equipment, Printer, Scanner, Xerox, TestValues  # Импорт ранее созданных классов


class NewEquipment(Equipment):
    """ Класс-наследник класса 'Equipment' с дополнительными атрибутами для автоматизированной обработки данных """
    base_attributes = [("Инвентарный номер", "inv_num", "", "is_natural"),
                       ("Бренд", "brand", "", "is_not_empty_str"),
                       ("Модель", "model", "", "is_not_empty_str"),
                       ("Вес", "weight", "кг", "is_float_above_zero"),
                       ("Ширина", "width", "м", "is_float_above_zero"),
                       ("Высота", "height", "м", "is_float_above_zero"),
                       ("Глубина", "depth", "м", "is_float_above_zero"),
                       ("Мощность", "power", "Вт", "is_float_above_zero")]


class NewPrinter(Printer):
    """ Класс-наследник класса 'Printer' с дополнительными атрибутами для автоматизированной обработки данных """
    custom_attributes = [("Тип печати", "p_type", "", "is_not_empty_str"),
                       ("Цвет печати", "color", "", "is_not_empty_str"),
                       ("Скорость печати", "speed", "стр/мин", "is_natural"),
                       ("Разрешение печати", "resolution", "dpi", "is_not_empty_str")]


class NewScanner(Scanner):
    """ Класс-наследник класса 'Scanner' с дополнительными атрибутами для автоматизированной обработки данных """
    custom_attributes = [("Интерфейс", "interface", "", "is_not_empty_str"),
                       ("Тип сенсора", "sensor", "", "is_not_empty_str"),
                       ("Глубина цвета", "color_depth", "бит", "is_natural"),
                       ("Разрешение сканирования", "resolution", "dpi", "is_not_empty_str")]


class NewXerox(Xerox):
    """ Класс-наследник класса 'Xerox' с дополнительными атрибутами для автоматизированной обработки данных """
    custom_attributes = [("Формат печати", "format", "", "is_not_empty_str"),
                       ("Скорость ксерокопирования", "speed", "стр/мин", "is_natural"),
                       ("Максимальная нагрузка", "max_load", "стр/мес", "is_natural")]


class NewWarehouse(Warehouse):
    """ Класс-наследник класса 'Warehouse' с дополнительным функционалом для автоматизированной обработки данных """

    class_dict = {"Printer": NewPrinter, "Scanner": NewScanner, "Xerox": NewXerox}  # Словарь классов оргтехники

    class WarehouseException(Exception):
        """ Собственный обработчик исключений """
        def __init__(self, txt):
            self.txt = txt

        def __str__(self):
            return self.txt

    def __init__(self, name, address, area):
        # Словарь функций автоматизированной проверки атрибутов объектов оргтехники
        self.check_func = {"is_natural": (self.is_natural, "должно быть натуральное число"),
                      "is_int": (self.is_int, "должно быть целове число"),
                      "is_float_above_zero": (self.is_float_above_zero, "должно быть вещественное число больше нуля"),
                      "is_not_empty_str": (self.is_not_empty_str, "должна быть непустая строка")}
        try:
            if not self.check_func['is_not_empty_str'][0](name):
                raise NewWarehouse.WarehouseException(self.check_func['is_not_empty_str'][1])
            if not self.check_func['is_not_empty_str'][0](address):
                raise NewWarehouse.WarehouseException(self.check_func['is_not_empty_str'][1])
            if not self.check_func['is_natural'][0](area):
                raise NewWarehouse.WarehouseException(self.check_func['is_natural'][1])
        except NewWarehouse.WarehouseException as err:
            print(err)
        else:
            super().__init__(name, address, area)

    def is_natural(self, digit):
        """ Проверяет, можно ли преобразовать аргумент в натуральное число """
        try:
            digit = int(digit)
            if digit < 1:
                raise ValueError
        except ValueError:
            return False
        else:
            return True

    def is_int(self, digit):
        """ Проверяет, можно ли преобразовать аргумент в целое число """
        try:
            digit = int(digit)
        except ValueError:
            return False
        else:
            return True

    def is_float_above_zero(self, digit):
        """ Проверяет, можно ли преобразовать аргумент в рациональное число """
        try:
            digit = float(digit)
            if digit <= 0.0:
                raise ValueError
        except ValueError:
            return False
        else:
            return True

    def is_not_empty_str(self, string):
        """ Проверяет на пустую строку """
        if len(str.strip(string)) == 0:
            return False
        else:
            return True

    def input_params(self, attributes):
        # Универсальный метод ввода параметров оборудования с проверкой на ошибки
        params = dict()
        for param in attributes:
            p_name = param[0]
            p_id = param[1]
            p_measure = param[2]
            p_func = param[3]
            # Цикл проверки ввода корректного значения атрибута
            while True:
                print(f"Введите '{p_name}{' (' + p_measure + ')' if p_measure else ''}': ", end='')
                p_val = input()
                if not self.check_func[p_func][0](p_val):
                    print(f"\tНеверный формат параметра '{p_name}': {self.check_func[p_func][1]}")
                else:
                    break
            # Добавление атрибута в словарь параметров
            params.update({p_id: p_val})
        return params

    def load_test_data(self, test_values):
        """ Автоматическое заполнение ИС тестовыми данными """
        if len(test_values) == 0:
            print("Данных нет. Загрузка невозможна")
        else:
            was_error = False
            all_cnt = 0
            cor_cnt = 0
            for row in test_values:
                try:
                    class_name = row[0]
                    department = row[1]
                    data_dict = row[2]
                    # Создание нового объекта оргтехники
                    new_obj = self.class_dict[class_name](data_dict)
                    # Прием оргтехники на склад
                    self.take_to_warehouse(new_obj, department)
                except Exception as e:
                    was_error = True
                    print(f"{e}. Не удалось корректно обработать данные '{row}'")
                else:
                    cor_cnt += 1
                finally:
                    all_cnt += 1
            if was_error:
                print(f"При обработке тестовых данных были ошибки. "
                      f"Загружено {round((cor_cnt / all_cnt)*100, 2)}% данных")
                return False
            else:
                print("\nВсе данные корректно загружены. Можно распечатать состояние склада, чтобы просмотреть их")
                return True

    def input_department(self):
        """ Ввод названия отдела """
        while True:
            dep = input("Введите отдел, за которым надо закрепить оборудование: ")
            if self.is_not_empty_str(dep):
                return dep
            else:
                print("Поле Отдел не может быть пустым")


    def del_by_inv_num(self):
        """ Удалить оборудование из ИС по его инвентарному номеру """
        dec = input("Вы вошли в режим удаления оргтехники из системы. Хотите продолжить? (да/нет): ")
        if dec.lower().strip() != "да":
            return
        else:
            inv_num = input("Введите инвентарный номер оборудования: ")
            equipment_object_link = self.equip.get(inv_num, None)
            if equipment_object_link is None:
                print(f"Орудование по инвентарному номеру '{inv_num}' не найдено")
            else:
                inf = str(equipment_object_link[0])
                print(f"Оборудование [{inf}] удалено из системы")
                self.equip.pop(inv_num)

    def del_all_in_department(self):
        """ Удалить оборудование из ИС для всего отдела по названию отдела """
        dec = input("Вы вошли в режим удаления всей оргтехники из системы, прикрпленной к отделу. "
                    "Хотите продолжить? (да/нет): ")
        if dec.lower().strip() != "да":
            return
        else:
            dep = input("Введите название отдела: ")
            del_cnt = 0
            del_inv_num_list = []
            for inv_num, equipment in self.equip.items():
                department = equipment[1]
                if department.lower() == dep.lower():
                    del_inv_num_list.append(inv_num)
            for inv_num in del_inv_num_list:
                equipment_object_link = self.equip.get(inv_num, None)
                inf = str(equipment_object_link[0])
                print(f"Оборудование [{inf}] удалено из системы")
                self.equip.pop(inv_num)
                del_cnt += 1
            if del_cnt == 0:
                print("Не было удалено ни одного устройства. "
                      "Возможно вы ввели несуществующий отдел или из него ранее уже были удалены все устройства.")
            else:
                print(f"Всего удалено {del_cnt} устройства из отдела {dep}")

    def start_dialog(self):
        """ Основная работа с пользователем """
        while True:
            op = input("\nВыберите операцию: "
              "\n\t1 - зарегистрировать новое оборудование и принять его на склад, "
              "\n\t2 - выдать оборудование со склада в отдел,"
              "\n\t3 - распечатать состояние склада"
              "\n\t4 - загрузить тестовые данные в систему"
              "\n\t5 - удалить оборудование из ИС по его инвентарному номеру"
              "\n\t6 - удалить все оборудование из отдела и ИС по названию отдела"
              "\n\t9 - выйти из программы\n")
            if op == "1":
                while True:
                    # Ввод оборудования
                    reg = input("Выберите тип оборудования:"
                                "\n\t1 - Принтер"
                                "\n\t2 - Сканер"
                                "\n\t3 - Ксерокс"
                                "\n\t9 - Выход в предыдущее меню\n")
                    parameters = dict()
                    # Ввод общих атрибутов
                    if reg in ("1", "2", "3"):
                        # Ввод отдела
                        department = self.input_department()
                        parameters.update(NewWarehouse.input_params(self, NewEquipment.base_attributes))
                        # Ввод уникальных атрибутов
                        if reg == "1":
                            parameters.update(NewWarehouse.input_params(self, NewPrinter.custom_attributes))
                            new_obj = NewPrinter(parameters)
                            self.take_to_warehouse(new_obj, department)
                        elif reg == "2":
                            parameters.update(NewWarehouse.input_params(self, NewScanner.custom_attributes))
                            new_obj = NewScanner(parameters)
                            self.take_to_warehouse(new_obj, department)
                        elif reg == "3":
                            parameters.update(NewWarehouse.input_params(self, NewXerox.custom_attributes))
                            new_obj = NewXerox(parameters)
                            self.take_to_warehouse(new_obj, department)
                    elif reg == "9":
                        break
                    else:
                        print("Неверная операция")
            elif op == "2":
                inv_num = input("Введите инвентарный номер оборудования: ")
                if not self.check_func['is_natural'][0](inv_num):
                    print(self.check_func['is_natural'][1])
                else:
                    self.take_to_department(inv_num)
            elif op == "3":
                print(self)
                data = self.warehouse_equipment
                print(f"Состояние склада по отделам:{data if data else ' склад пуст'}")
            elif op == "4":
                self.load_test_data(TestValues.test_data)
            elif op == "5":
                self.del_by_inv_num()
            elif op == "6":
                self.del_all_in_department()
            elif op == "9":
                break
            else:
                print("Неверная операция")


if __name__ == "__main__":
    new_wh = NewWarehouse("Новый склад", "Новый адрес", 400)
    new_wh.start_dialog()

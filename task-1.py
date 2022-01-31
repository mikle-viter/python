"""
ЗАДАНИЕ № 1
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд,
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time


class TrafficLight():
    """ Класс Светофор. Задает длительности горения трех цветов. Эмулирует работу циклов светофора """
    __states = [["Красный", 7], ["Желтый", 2], ["Зеленый", 5]]
    __color = 0  # Индекс начального цвета светофора: 0-красный, 1-желтый, 2-зеленый
    __cycles_to_stop = 1  # Число циклов отработки светофора

    def __init__(self, start_color=0):
        self.__color = start_color

    def __get_time(self):
        """  Возвращает текущее системное время """
        return time.strftime("%H:%M:%S", time.gmtime())

    def change_color_delay(self, color_index, new_delay):
        """  Изменяет задержку отображения цвета светофора """
        try:
            color_index = int(color_index)
            if color_index not in range(3):
                raise Exception
            else:
                self.__states[color_index][1] = int(new_delay)
        except Exception:
            print("Ошибка. Некорректный параметр задержки на красный цвет")

    def running(self, start_color=0, cycles=1):
        """ Запуск светофора. Задание индекса начального цвета и числа циклов отработки """
        try:
            start_color = int(start_color)
            if start_color not in range(3):
                raise Exception
            else:
                self.__color = start_color
            cycles = int(cycles)
            if cycles < 0:
                raise Exception
            else:
                self.__cycles_to_stop = cycles
        except Exception:
            print("Ошибка. Некорректные параметры: начальный цвет (0-красный, 1-желтый, 2-зеленый), "
                  "число циклов работы (натуральное число)")
        else:
            print(f"{self.__get_time()} Запуск светофора")
            cycles_cnt = self.__cycles_to_stop
            while cycles_cnt:
                cycles_cnt -= 1
                curr_color_ind = self.__color
                for i in range(3):
                    print(f"{self.__get_time()} "
                          f"Свет: {self.__states[curr_color_ind][0]}. "
                          f"Задержка {self.__states[curr_color_ind][1]} сек.")
                    time.sleep(self.__states[curr_color_ind][1])
                    curr_color_ind = (curr_color_ind + 1) % 3
            print(f"{self.__get_time()} Остановка светофора")


if __name__ == "__main__":
    traffic_light_1 = TrafficLight(1)           # Установка начального цвета по умолчанию - Желтый
    traffic_light_1.change_color_delay(2, 3)    # Установка длительности зеленого цвета 3 секунды
    traffic_light_1.running(2, 2)               # Запуск светофора с зеленого цвета, число циклов работы - 2

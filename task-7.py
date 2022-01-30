"""
ЗАДАНИЕ № 7
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

import json

file_source = "task-7-file-source.txt"  # Comma separated file
file_dest = "task-7-file-dest.txt"  # JSON-format file
with open(file_source, "r", encoding="utf-8") as file:
    stat = dict()
    average_profit = 0.0
    firms_success_cnt = 0
    for line in file:
        data = line.split(";") # Comma separated file
        try:
            firm_name = data[0]
            firm_form = data[1]
            firm_revenue = float(data[2])
            firm_costs = float(data[3])
        except Exception:
            print(f"Ошибка обработки строки {line}\tОна исключена из общей статистики")
        else:
            firm_result = firm_revenue - firm_costs
            stat[firm_name] = firm_result
            # Если фирма получила убытки, в расчёт средней прибыли её не включать
            if firm_result >= 0:
                firms_success_cnt += 1
                average_profit += firm_result
    average_profit = round(average_profit / firms_success_cnt, 2)
    json_obj = [stat, {"average_profit": average_profit}]
    with open(file_dest, "w", encoding="utf-8") as out_file:
        # Сериализация JSON-объекта в строку
        json_str = json.dumps(json_obj)
        print(f"Сериализация JSON-объекта в строку:\n\t{json_str}")
        out_file.write(json_str)

# Считывание файла
with open(file_dest, "r", encoding="utf-8") as in_file:
    line = in_file.readline()
    new_json = json.loads(line)
    print(f"Десериализация JSON-строки из файла в словарь:\n\t{new_json}")

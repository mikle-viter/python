"""
ЗАДАНИЕ № 6
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def update_stat(string):
    """ Добавляет в глобальный словарь общее число часов по предмету из строки string """
    data = string.split(":")
    subject = data[0]
    data = str(data[1]).strip().split()
    try:
        lects = int(data[0].split('(')[0])
    except Exception:
        lects = 0
    try:
        practs = int(data[1].split('(')[0])
    except Exception:
        practs = 0
    try:
        labs = int(data[2].split('(')[0])
    except Exception:
        labs = 0
    global stat_dict
    stat_dict[subject] = lects + practs + labs


source_file = "task-6-file.txt"
stat_dict = dict()
file = open(source_file,  "r", encoding="utf-8")
for line in file:
    update_stat(line)
file.close()
print(stat_dict)

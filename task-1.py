"""
ЗАДАНИЕ № 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

try:
    argv[1:] = [float(el) for el in argv[1:]]
except ValueError:
    print("Ошибка входных данных")
else:
    script_name, output_in_hours, rate_per_hour, bonus = argv
    employee_salary = (output_in_hours * rate_per_hour) + bonus
    print(f"Зарплата сотрудника: {employee_salary}")

"""
Примеры вызова:

D:\PyProjects\lesson-4>python task-1.py 23 200 500
Зарплата сотрудника: 5100.0

D:\PyProjects\lesson-4>python task-1.py 23 200 500e
Ошибка входных данных

D:\PyProjects\lesson-4>python task-1.py 23 2t00 500
Ошибка входных данных
"""

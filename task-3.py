"""
ЗАДАНИЕ № 3
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
"""

import os, sys, time


def get_fin_data(path_to_file, min_salary=20000):
    """ Считывает из файла path_to_file данные сотрудников и возвращает статистику:
     {ave_salary: значение_средней_зарплаты,
     list_salary_less: [Фамилия_сотрудника_с_зарплатой_менее_min_salary, значение_зарплаты]}
      Ошибочные строки из статистики исключаются.
      При некорректном пути к файлу возвращает False"""
    if not os.path.exists(path_to_file):
        sys.stderr.write("Ошибка. Такого файла не существует")
        return False
    else:
        with open(path_to_file, "r", encoding="utf-8") as file:
            cnt_employees = 0
            ave_salary = 0
            list_salary_less = []
            for line in file:
                line = line.rstrip("\n").replace(",", ".")
                try:
                    sirname, salary = line.split()
                    salary = float(salary)
                except BaseException:
                    print(f"Ошибка. Не могу обработать строку файла '{line}'. Она исключена из общей статистики")
                else:
                    cnt_employees += 1
                    ave_salary += salary
                    if salary < min_salary:
                        list_salary_less.append([sirname, salary])
            ave_salary = round(ave_salary / cnt_employees, 2)
            return {"ave_salary": ave_salary, "list_salary_less": list_salary_less}


def print_string_with_delay(string, delay=0.05):
    """ Печатает в стандартный поток вывода строку string посимвольно с задержкой вывода символа в delay секунд.
     При ошибке выводит сообщение и возвращает False"""
    try:
        for char in string:
            sys.stdout.write(char)
            time.sleep(delay)
    except Exception:
        sys.stderr.write("Неизвестная ошибка")
        return False
    else:
        return True


if __name__ == "__main__":
    fin_data = get_fin_data("task-3-file.txt")
    print_string_with_delay(f"Средняя зарплата: {fin_data['ave_salary']} руб.")
    print_string_with_delay("\nСотрудники, зарплата которых менее 20000 руб.:")
    if len(fin_data['list_salary_less']) == 0:
        print_string_with_delay("\nТакие сотрудники не обнаружены:")
    else:
        for employee in fin_data['list_salary_less']:
            print_string_with_delay(f"\n\t{employee[0]}: {employee[1]} руб.", 0.005)

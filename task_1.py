""""
ЗАДАНИЕ № 1

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    """ Класс Дата """
    __delimeters = [".", "/", "-"]  # Возможные разделители в дате (пробел учтен далее)
    __days_cnt = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31, 99: 29}

    def __init__(self, date):
        self.__date = date

    @classmethod
    def num_days_in_date(cls, d):
        # Подсчет числа дней от 0-го года по Христианскому календарю
        d = Date.date_validation(d)
        if d:
            day = d[0]
            month = d[1]
            year = d[2] - 1
            # Число лет без текущего года * 365 дней в году + число высокосных лет (+ 1 день в каждом высокосном году)
            # + сумма числа дней в месяцах этого года без текущего месяца + число дней в текущем месяце
            # + 1 день если текущий год высокосный
            return (365 * year) + (year // 4) + sum([cls.__days_cnt[m] for m in range(1, month)]) + \
                   day + (1 if (year + 1) % 4 == 0 else 0)
        else:
            return -1

    @classmethod
    def date_to_int(cls, d):
        # 12-02-2022 -> 12022022
        valid = Date.date_validation(d)
        if valid:
            return int(''.join([ch for ch in d if ord(ch) in range(48, 58)]))
        else:
            return -1

    @staticmethod
    def date_validation(d):
        try:
            d = str(d).strip()
            for delim in Date.__delimeters:
                d = d.replace(delim, " ")   # Приводим дату к единому формату разделителя - пробел
            d_parts = d.split()             # Разделяем дату на компоненты
            if len(d_parts) != 3:           # Если число компонент даты не равно 3, то ошибка
                raise Exception
            day = d_parts[0]                # День
            month = d_parts[1]              # Месяц
            year = d_parts[2]               # Год
            if (len(day) not in [1, 2]) or (len(month) not in [1, 2]) or (len(year) not in [2, 4]):
                raise Exception
            day = int(day)
            month = int(month)
            year = int(year)
            if year < 0:
                raise Exception
            if month < 1 or month > 12:
                raise Exception
            # Проверка дней в месяце с учетом февраля высокосного года
            if day < 1 or day > Date.__days_cnt[(99 if year % 4 == 0 else 2) if month == 2 else month]:
                raise Exception
        except Exception:
            return False
        else:
            return [day, month, year]


if __name__ == "__main__":
    # Проверка валидности и перевод в число, если валидна
    date_list = ["12.03.2021", "31.04.2022",  "30.04.2022","12 29 21", "15/12/1876", "1-2-21", "01-11-22", "10-01-2019"]
    for curr_date in date_list:
        print(f"Дата  {curr_date:<10}   ", end='')
        if Date.date_validation(curr_date):
            print(f"{'валидна':<10}", end='')
        else:
            print(f"{'не валидна':<10}", end='')
        print(f"  -->  {Date.date_to_int(curr_date):>10}  -->  {Date.num_days_in_date(curr_date)}")

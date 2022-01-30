"""
ЗАДАНИЕ № 5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

import random

file_name = "task-5-file.txt"
with open(file_name, "w+", encoding="utf-8") as file:
    file.write(' '.join([str(random.randint(1, 1000)) for i in range(100)]))
    file.seek(0, 0)  # Перевод курсора на начало файла
    try:
        print(f"Сумма чисел: {sum([int(el) for el in file.readline().split()])}")
    except Exception:
        print("Ошибка обработки данных")

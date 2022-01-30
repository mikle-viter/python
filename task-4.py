"""
ЗАДАНИЕ № 4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os, sys

source_path = "task-4-file-source.txt"
dest_path = "task-4-file-dest.txt"

if not os.path.exists(source_path):
    sys.stderr.write("Ошибка. Файл 'task-4-file-source.txt' не найден")
    sys.exit(-1)
else:
    dictionary = {"one": "Один", "two": "Два", "three": "Три", "four": "Четыре"}
    with open(source_path, "r", encoding="utf-8") as source_file, open(dest_path, "w", encoding="utf-8") as dest_file:
        for line in source_file:
            data = line.split()
            dest_file.write(dictionary[data[0].lower()] + ' ' + ' '.join(data[1:]) + "\n")

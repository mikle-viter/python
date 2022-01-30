"""
ЗАДАНИЕ № 1
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

import sys

file_name = input("Введите имя файла без расширения: ") + ".txt"
if file_name.strip(' ') == '':
    sys.stderr.write("Ошибка. Имя файла не должно быть пустым")
    sys.exit(-1)

print("Введите построчно данные для записи в файл:")
file = open("task-1-file.txt", "w+")
# Запиись файла
while True:
    string = input()
    if string == "":
        break
    file.write(string + "\n")
# Чтение файла
file.seek(0, 0)  # Курсор на начало файла
for line in file.readlines():
    print(line, end='')

file.close()

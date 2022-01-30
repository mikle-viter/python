"""
ЗАДАНИЕ № 2
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

def correct_char(char):
    """ Проверяет, является ли символ либо пробел, либо на латинице, либо на кириллице """
    ord_char = ord(char)
    if ord_char == 32 \
            or (ord_char > 64 and ord_char < 91) \
            or (ord_char > 96 and ord_char < 123) \
            or (ord_char >= 1040 and ord_char <= 1103)\
            or (ord_char == 1025) or (ord_char == 1105):
        return True
    else:
        return False


if __name__ == "__main__":  # Чтобы при импорте этого модуля не выполнялся скрипт ниже
    file_name = "task-2-file.txt"

    with open(file_name, "r", encoding="utf-8") as file:
        lines_cnt = 0
        words_stat = []
        for line in file:
            lines_cnt += 1
            line = line.rstrip("\n")
            line = "".join([ch for ch in line if correct_char(ch)])  # Очистка строки от ненужных символов
            words_stat.append(len(line.split()))
        print(f"Всего строк: {lines_cnt}")
        for i in range(len(words_stat)):
            print(f"\tВ строке № {i + 1}: {words_stat[i]} слов(а)")

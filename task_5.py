"""
ЗАДАНИЕ № 5
Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен
разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

rating_list = [8, 6, 6, 4, 1]

while True:
    user_input = input("Введите новый элемент рейтинга (натуральное число) или exit для выхода из программы: ")
    if user_input == "exit":
        break
    try:
        new_rating_element = int(user_input)
    except Exception:
        print("Введите только числовое значение без дробной части")
    else:
        if new_rating_element < 0:
            print("Вы не ввели натуральное число")
        else:
            print(f"Пользователь ввел число {new_rating_element}.", end='')
            inserted = False
            for i in range(len(rating_list)):
                if new_rating_element > rating_list[i]:
                    rating_list.insert(i, new_rating_element)
                    inserted = True
                    break
                elif new_rating_element == rating_list[i]:
                    rating_list.insert(i + 1, new_rating_element)
                    inserted = True
                    break
            if not inserted:
                rating_list.append(new_rating_element)
            print(f" Результат: {', '.join(map(str, rating_list))}")

"""
ЗАДАНИЕ № 2
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

while True:
    time_in_seconds = int(input("\r\nВведите время в секундах: "))

    hours = time_in_seconds // 3600
    new_seconds = time_in_seconds % 3600    # Остаток секунд
    minutes = new_seconds // 60
    seconds = new_seconds % 60              # Остаток секунд

    # Коррекция окончаний часов
    h_str = "часов"
    new_hours = hours % 10
    if hours == 1:
        h_str = "час"
    elif (hours >= 2) and (hours <= 4):
        h_str = "часа"
    elif ((hours >= 5) and (hours <= 20)) or ((hours >= 105) and (hours <= 120)):
        h_str = "часов"
    elif new_hours == 1:
        h_str = "час"
    elif (new_hours >= 2) and (new_hours <= 4):
        h_str = "часа"
    elif (new_hours >= 5) and (new_hours <= 21):
        h_str = "часов"

    # Коррекция окончаний минут
    m_str = "минут"
    new_minutes = minutes % 10
    if minutes == 1:
        m_str = "минута"
    elif (minutes >= 2) and (minutes <= 4):
        m_str = "минуты"
    elif ((minutes >= 5) and (minutes <= 20)) or ((minutes >= 105) and (minutes <= 120)):
        m_str = "минут"
    elif new_minutes == 1:
        m_str = "минута"
    elif (new_minutes >= 2) and (new_minutes <= 4):
        m_str = "минуты"
    elif (new_minutes >= 5) and (new_minutes <= 21):
        m_str = "минут"

    # Коррекция окончаний секунд
    s_str = "секунд"
    new_seconds = seconds % 10
    if seconds == 1:
        s_str = "секунда"
    elif (seconds >= 2) and (seconds <= 4):
        s_str = "секунды"
    elif ((seconds >= 5) and (seconds <= 20)) or ((seconds >= 105) and (seconds <= 120)):
        s_str = "секунд"
    elif new_seconds == 1:
        s_str = "секунда"
    elif (new_seconds >= 2) and (new_seconds <= 4):
        s_str = "секунды"
    elif (new_seconds >= 5) and (new_seconds <= 21):
        s_str = "секунд"

    # Вывод результата
    print(f"'{time_in_seconds}' секунд - это {hours} {h_str}, {minutes} {m_str} и {seconds} {s_str}")

    answer = input("\r\nВведите 1, если хотите попробовать еще раз и 0 для выхода из программы: ")
    if answer == "0":
        break

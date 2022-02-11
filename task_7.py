""""
ЗАДАНИЕ № 7

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexDigit:
    """ Класс Комплексное число """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} + {self.b}i"

    def __add__(self, other):
        return ComplexDigit(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexDigit(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        a1 = self.a
        b1 = self.b
        a2 = other.a
        b2 = other.b
        return ComplexDigit(a1 * a2 - b1 * b2, a1 * b2 + b1 * a2)

    def __eq__(self, other):
        if (self.a == other.a) and (self.b == other.b):
            return True
        else:
            return False


if __name__ == "__main__":
    c1 = ComplexDigit(3, 6)
    c2 = ComplexDigit(2, 3)
    c1_p_c2 = c1 + c2
    c1_s_c2 = c1 - c2
    c2_s_c1 = c2 - c1
    c1_m_c2 = c1 * c2
    c2_m_c1 = c2 * c1

    print(f"c1 = {c1}, c2 = {c2}")
    print(f"c1 + c2 = {c1_p_c2}")
    print(f"c1 - c2 = {c1_s_c2}")
    print(f"c2 - c1 = {c2_s_c1}")
    print(f"c1 * c2 = {c1_m_c2}")
    print(f"c2 * c1 = {c2_m_c1}")

    if c1_p_c2 == ComplexDigit(5, 9):
        print(f"Операция 'c1 + c2' корректна")
    else:
        print(f"Операция 'c1 + c2' корректна")

    if c1_s_c2 == ComplexDigit(1, 3):
        print(f"Операция 'c1 - c2' корректна")
    else:
        print(f"Операция 'c1 - c2' корректна")

    if c2_s_c1 == ComplexDigit(-1, -3):
        print(f"Операция 'c2 - c1' корректна")
    else:
        print(f"Операция 'c2 - c1' корректна")

    if c1_m_c2 == ComplexDigit(-12, 21):
        print(f"Операция 'c1 * c2' корректна")
    else:
        print(f"Операция 'c1 * c2' корректна")

    if c2_m_c1 == ComplexDigit(-12, 21):
        print(f"Операция 'c2 * c1' корректна")
    else:
        print(f"Операция 'c2 * c1' корректна")

    if ComplexDigit(1, -5) == ComplexDigit(1, -5):
        print(f"Два комплексных числа равны")
    else:
        print(f"Два комплексных числа не равны")

    if ComplexDigit(2, 5) == ComplexDigit(2, 6):
        print(f"Два комплексных числа равны")
    else:
        print(f"Два комплексных числа не равны")

# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры

# Операция ** не учитывает знак числа
from math import pow


def get_sum(start, degree):
    if degree == 0:
        return 0
    current = start / pow(-2, (degree - 1))
    return current + get_sum(start, degree - 1)


n = int(input('Введите колтчество n элементов ряда (натуральное число): '))
print(f'Сумма ряда: {get_sum(1, n)}')

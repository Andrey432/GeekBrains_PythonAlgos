# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться

from random import randint

ITEMS = 30
MIN_ITEM = -100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(ITEMS)]
print(array)
assert len(array) > 1, 'Требуется массив минимум с 2-мя элементами'


first_min_ind = second_min_ind = -1
first_min_val = second_min_val = float('inf')

for i, item in enumerate(array):
    if item < second_min_val:
        if item < first_min_val:
            first_min_val, item = item, first_min_val
            first_min_ind, i = i, first_min_ind
        # first всегда меньше second. Если first обновляется, то second заменяется на него
        # таким образом в переменных всегда лежит 2 наименьших встреченных значения
        second_min_val, item = item, second_min_val
        second_min_ind, i = i, second_min_ind

print(f"1-ый минимум: позиция {first_min_ind + 1} значение {first_min_val}")
print(f"2-ой минимум: позиция {second_min_ind + 1} значение {second_min_val}", sep='\n')

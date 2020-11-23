# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

from random import randint

ITEMS = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(ITEMS)]
print(array)
assert len(array) > 0, 'Пустой массив'


ind_min = ind_max = 0
val_min = val_max = array[0]

for i, value in enumerate(array):
    if value > val_max:
        ind_max = i
        val_max = value
    if value < val_min:
        ind_min = i
        val_min = value

array[ind_max], array[ind_min] = array[ind_min], array[ind_max]
print(array)

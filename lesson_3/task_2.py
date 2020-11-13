# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа

from random import randint

ITEMS = 30
MIN_ITEM = -100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(ITEMS)]
print(array)

even_nums_array = [i for i in range(len(array)) if not array[i] % 2]
print(even_nums_array)

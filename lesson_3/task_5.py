# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

from random import randint

ITEMS = 30
MIN_ITEM = -100
MAX_ITEM = 100
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(ITEMS)]
print(array)


max_ind, max_val = -1, float('-inf')

for i, item in enumerate(array):
    if max_val < item < 0:
        max_ind = i
        max_val = item

if max_ind == -1:
    print('В массиве отсутствуют отрицательные элементы')
else:
    print(f'Максимальный отрицательный элемент: позиция {max_ind + 1} значение: {max_val}')

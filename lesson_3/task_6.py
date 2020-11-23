# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

from random import randint

ITEMS = 30
MIN_ITEM = -100
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
    if i > 0:
        # Преффикс суммы, чтобы потом её снова не считать
        # Раз уж тема про алгоритмы :)
        # Преффикс пишется на исходном массиве, т.к. этот массив больше не используется
        array[i] += array[i - 1]


print(f"Максимум: позиция {ind_max + 1} значение {val_max}",
      f"Минимум: позиция {ind_min + 1} значение {val_min}", sep='\n')

print("Сумма в диапазоне (min, max): ", end='')

# min/max нельзя, поэтому if
if ind_min < ind_max:
    print(array[ind_max - 1] - array[ind_min])
elif ind_max < ind_min:
    print(array[ind_min - 1] - array[ind_max])
else:
    # Массивы длины 1 или из одного и того же элемента
    print(0)

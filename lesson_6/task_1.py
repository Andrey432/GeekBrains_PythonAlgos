# Задача с занятия 3, №6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

# оригинальный алгоритм
def find_1(array):
    mn = mx = 0
    mn_val = mx_val = array[0]
    prev_val = 0

    for i, value in enumerate(array):
        if value > mx_val:
            mx = i
            mx_val = value
        if value < mn_val:
            mn = i
            mn_val = value
        array[i] += prev_val
        prev_val = array[i]
    return array[max(mn, mx)] - array[min(mn, mx) - 1]


def find_2(array):
    mx = array.index(max(array))
    mn = array.index(min(array))
    return sum(array[min(mx, mn) + 1: max(mx, mn)])


def find_3(array):
    min_ind, min_val = 0, array[0]
    for i, value in enumerate(array):
        if min_val > value:
            min_ind = i
            min_val = value

    max_ind, max_val = 0, array[0]
    for i, value in enumerate(array):
        if max_val < value:
            max_ind = i
            max_val = value

    sm = 0
    for i in array[min(min_ind, max_ind) + 1: max(min_ind, max_ind)]:
        sm += i
    return sm

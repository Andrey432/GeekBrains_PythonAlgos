# Задача с занятия 3, №6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать

from random import randint
from timeit import timeit
import cProfile


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


def test_funcs(*funcs):
    n = 1
    for i in range(5):
        print('*' * 50)
        n *= 10
        for f in funcs:
            array = [randint(-100, 100) for _ in range(n)]
            print(f.__name__, end=": ")
            print(f"N={n} Time={timeit('f(array)', globals=locals(), number=100):.4f}")

    n = 1_000_000
    print(f'\nПроверка через cProfile. N={n}')
    for f in funcs:
        print(f.__name__)
        array = [randint(-100, 100) for _ in range(n)]
        cProfile.runctx('f(array)', globals(), locals())


if __name__ == '__main__':
    test_funcs(find_1, find_2, find_3)


#  **************************************************
#  find_1: N=10 Time=0.0005
#  find_2: N=10 Time=0.0003
#  find_3: N=10 Time=0.0004
#  **************************************************
#  find_1: N=100 Time=0.0028
#  find_2: N=100 Time=0.0012
#  find_3: N=100 Time=0.0024
#  **************************************************
#  find_1: N=1000 Time=0.0359
#  find_2: N=1000 Time=0.0065
#  find_3: N=1000 Time=0.0256
#  **************************************************
#  find_1: N=10000 Time=0.3653
#  find_2: N=10000 Time=0.0565
#  find_3: N=10000 Time=0.2398
#  **************************************************
#  find_1: N=100000 Time=3.7291
#  find_2: N=100000 Time=0.9504
#  find_3: N=100000 Time=2.4328
#
#  Проверка через cProfile. N=1000000
#  find_1
#           6 function calls in 0.328 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#          1    0.000    0.000    0.328    0.328 <string>:1(<module>)
#          1    0.328    0.328    0.328    0.328 task_1.py:11(find_1)
#          1    0.000    0.000    0.328    0.328 {built-in method builtins.exec}
#          1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#          1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#  find_2
#           11 function calls in 0.094 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#          1    0.000    0.000    0.093    0.093 <string>:1(<module>)
#          1    0.000    0.000    0.093    0.093 task_1.py:28(find_2)
#          1    0.000    0.000    0.094    0.094 {built-in method builtins.exec}
#          2    0.047    0.023    0.047    0.023 {built-in method builtins.max}
#          2    0.047    0.023    0.047    0.023 {built-in method builtins.min}
#          1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#          2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#
#
#  find_3
#           6 function calls in 0.241 seconds
#
#     Ordered by: standard name
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#          1    0.000    0.000    0.241    0.241 <string>:1(<module>)
#          1    0.241    0.241    0.241    0.241 task_1.py:34(find_3)
#          1    0.000    0.000    0.241    0.241 {built-in method builtins.exec}
#          1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#          1    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# У всех функций линейная зависимость
# Самой быстрой вышла функция 2, т.к. использует скомпилированные методы
# 3-я функция работает нормально, но вот почему 1-ая стабильно уступает ей на четверть - не могу понять
# Есть предположение, что из-за большего кол-ва обращений по индексу в массиве
# Но всё равно в 1-ой функции совершается 1 прогон по массиву, а в 3-ей - 2 + срез
# Или я 2-ой час не могу найти ошибку в алгоритме тестирования, или где-то закралась хлопотная подкопотная работа

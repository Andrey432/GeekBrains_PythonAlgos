import sys
from copy import copy


def _get_obj_memory_usage(obj, done):
    if hasattr(obj, '__call__') or hasattr(obj, '__loader__'):
        return 0

    total = sys.getsizeof(obj)
    done.add(id(obj))

    if hasattr(obj, '__iter__'):
        # В случае, если объект - словарь, то считаем только память значений,
        # т.к. ключи хранятся в виде хэша в самой структуре (по идее)

        for el in (obj.values() if isinstance(obj, dict) else obj):
            id_ = id(el)
            if id_ not in done:
                done.add(id_)
                total += _get_obj_memory_usage(el, done)

    return total


def calc_memory(namespace):
    total = 0
    done = set()

    for value, obj in namespace.items():
        # на случай, если в качестве namespace был передан словарь globals()
        if value.startswith('__') and value.endswith('__'):
            continue
        if hasattr(obj, '__call__') or hasattr(obj, '__loader__'):
            continue

        if id(obj) in done:
            msg = "repeated"
        else:
            mem = _get_obj_memory_usage(obj, done)
            msg = f"type '{type(obj).__name__}' {mem} bytes"
            total += mem

        print(f'{value}: {msg}')
    print(f'Total memory usage: {total} bytes')


def solution_1(sequence):
    # В одномерном массиве целых чисел определить два наименьших элемента.
    # Они могут быть как равны между собой (оба являться минимальными), так и различаться

    first_min_ind = second_min_ind = -1
    first_min_val = second_min_val = float('inf')

    for i, item in enumerate(sequence):
        if item < second_min_val:
            if item < first_min_val:
                first_min_val, item = item, first_min_val
                first_min_ind, i = i, first_min_ind
            second_min_val, item = item, second_min_val
            second_min_ind, i = i, second_min_ind
    calc_memory(locals())
    return first_min_ind, first_min_ind


def solution_2(sequence):
    sequence_c = copy(sequence)

    min_1 = sequence_c.index(min(sequence_c))
    sequence_c.pop(min_1)
    min_2 = sequence_c.index(min(sequence_c))

    calc_memory(locals())
    return min_1, min_2


def solution_3(sequence):
    sorted_seq = sorted(enumerate(sequence), key=lambda x: x[1])
    calc_memory(locals())
    return sorted_seq[0][0], sorted_seq[1][0]


if __name__ == '__main__':
    from random import randint

    ITEMS = 30
    MIN_ITEM = -100
    MAX_ITEM = 100

    array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(ITEMS)]
    funcs = (solution_1, solution_2, solution_3)

    print('Global namespace', end='\n\n')
    calc_memory(globals())
    print()

    for f in funcs:
        print('Function', f.__name__, end='\n\n')
        f(array)
        print()

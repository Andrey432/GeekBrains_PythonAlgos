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


# Global namespace
#
# ITEMS: type 'int' 28 bytes
# MIN_ITEM: type 'int' 28 bytes
# MAX_ITEM: type 'int' 28 bytes
# array: type 'list' 1152 bytes     <-- данная переменная будет далее передаваться в функции,
#                                       так что её размер можно в них не учитывать. Хотел написать класс,
#                                       чтобы избежать повторного замера таких переменных, но больно геморно вышло
# funcs: type 'tuple' 64 bytes
# Total memory usage: 1300 bytes
#
# Function solution_1
#
# sequence: type 'list' 1152 bytes
# first_min_ind: type 'int' 28 bytes
# second_min_ind: type 'int' 28 bytes
# first_min_val: repeated
# second_min_val: repeated
# i: repeated
# item: repeated
# Total memory usage: 1208 bytes
#
# Function solution_2
#
# sequence: type 'list' 1152 bytes
# sequence_c: type 'list' 296 bytes
# min_1: type 'int' 28 bytes
# min_2: type 'int' 28 bytes
# Total memory usage: 1504 bytes
#
# Function solution_3
#
# sequence: type 'list' 1152 bytes
# sorted_seq: type 'list' 2716 bytes
# Total memory usage: 3868 bytes
#
#
# 1-ая функция самая экономная, т.к. память расходуется только на несколько доп. int переменных
# 2-ая также относительно экономная, т.к. память в основном расходуется на создание списка,
# а хранящиеся в нём элементы идентичны элементам оригинальной коллекции
# 3-я функция очень прожорлива, т.к.:
# 1) Для каждого элемента создаётся tuple, который хранит его позицию
# 2) Создаётся список, который все эти tuple хранит

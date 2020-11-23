from collections import deque
from random import randint
from timeit import timeit


def _merge_sort_1(array, left, right, reverse, key):
    if left == right:
        return [array[left]]

    middle = (left + right) // 2
    a = _merge_sort_1(array, left, middle, reverse, key)
    b = _merge_sort_1(array, middle + 1, right, reverse, key)

    res = []
    a_ind, b_ind, mx_a, mx_b = 0, 0, len(a), len(b)

    while a_ind < mx_a and b_ind < mx_b:
        # is из-за того, что объекты True/False всегда в 1-ом экземпляре
        # И это работает, вроде как, немного быстрее обычного сравнения
        if (key(a[a_ind]) < key(b[b_ind])) is reverse:
            res.append(a[a_ind])
            a_ind += 1
        else:
            res.append(b[b_ind])
            b_ind += 1

    res.extend(i for i in (a[a_ind:] if a_ind < mx_a else b[b_ind:]))
    return res


def merge_sort_1(array, reverse=False, key=lambda x: x):
    return _merge_sort_1(array, 0, len(array) - 1, bool(reverse), key)


# Просто из интереса решил немного другим путём написать
# Пусть и меньше, чем я хотел, но в итоге 10-15% времени экономим :)
# Просто 1-ая функция немного затратнее по самим операциям, 2-ая функция выполняется питоном быстрее

def _merge_sort_2(array, left, right, reverse, key):
    if left == right:
        return deque((array[left],))

    middle = (left + right) // 2
    a = _merge_sort_2(array, left, middle, reverse, key)
    b = _merge_sort_2(array, middle + 1, right, reverse, key)

    res = deque()

    while a and b:
        if (key(a[0]) < key(b[0])) is reverse:
            res.append(a.popleft())
        else:
            res.append(b.popleft())

    res.extend(a if a else b)

    return res


def merge_sort_2(array, reverse=False, key=lambda x: x):
    return iter(_merge_sort_2(array, 0, len(array) - 1, bool(reverse), key))


def test_time(command, ncalls):
    print(f'{command=} time={timeit(command, globals=globals(), number=ncalls)}')


if __name__ == '__main__':
    arr = [1, 7, 6, 3, 9, 0, 2, 4, 5, 8]
    print(merge_sort_1(arr))
    print(arr)

    # a = [randint(-100, 100) for _ in range(100_000)]
    # test_time('merge_sort_1(a)', 1)
    # test_time('merge_sort_2(a)', 1)

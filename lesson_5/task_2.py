from collections import deque
from functools import reduce


def _hex2num(char):
    if char.isdigit():
        return int(char)
    return 10 + ord(char) - ord('a')


def _num2hex(num):
    if num < 10:
        return str(num)
    return chr(ord('a') + num - 10)


def _get_sum(a, b, add=0):
    sm = a + b + add
    return sm % 16, sm // 16


def _get_multi(a, b, add=0):
    ml = a * b + add
    return ml % 16, ml // 16


def hex_sum(first, second, del_nulls=True):
    res = deque()
    add = 0

    while first and second:
        a, b = first.pop(), second.pop()
        if type(a) is str:
            a = _hex2num(a.lower())
        if type(b) is str:
            b = _hex2num(b.lower())
        sm, add = _get_sum(a, b, add)
        res.appendleft(sm)

    greater_num = first if first else second

    while greater_num:
        num = greater_num.pop()
        if type(num) is str:
            num = _hex2num(num.lower())
        sm, add = _get_sum(num, add)
        res.appendleft(sm)
    if add:
        res.appendleft(1)

    if del_nulls:
        while res[0] == 0 and len(res) > 1:
            res.popleft()

    return res


def hex_multi(first, second):
    sums = []
    counter = 0

    for fnum in reversed(first):
        fnum = fnum.lower()
        res = deque([0 for _ in range(counter)])
        add = 0
        for snum in reversed(second):
            ml, add = _get_multi(_hex2num(fnum), _hex2num(snum.lower()), add)
            res.appendleft(ml)
        if add:
            res.appendleft(add)
        counter += 1
        sums.append(res)

    res = reduce(lambda a, b: hex_sum(a, b, False), sums)
    while res[0] == 0 and len(res) > 1:
        res.popleft()

    return res


if __name__ == '__main__':
    first_num, optype, second_num = input("Введите операцию (hex1 +* hex2): ").strip().split()

    if optype == '+':
        res = hex_sum(list(first_num), list(second_num))
    else:
        res = hex_multi(list(first_num), list(second_num))

    print(f'>>>', ''.join(_num2hex(i) for i in res))

def get_middle(array):
    done = set()
    mid = len(array) // 2

    for i in array:
        if i in done:
            continue

        done.add(i)
        smaller_nums_cnt = 0
        repeats_cnt = 0

        for j in array:
            if i > j:
                smaller_nums_cnt += 1
            elif i == j:
                repeats_cnt += 1
        if smaller_nums_cnt <= mid <= smaller_nums_cnt + repeats_cnt - 1:
            return i


def test(m, tests=100):
    from random import randint

    # [ok, wa]
    res = [0, 0]

    for i in range(tests):
        arr = [randint(0, 10) for _ in range(2 * m + 1)]
        ans = get_middle(arr)

        arr.sort()
        r_ans = arr[len(arr) // 2]

        msg = f'test {i + 1} {"OK" if ans == r_ans else "WA"}'
        res[ans == r_ans] += 1
        print(msg)

        if ans != r_ans:
            print(arr)
            print(f'expected {r_ans}, got {ans}')

    print(f'Total: OK {res[1]} WA {res[0]}')


if __name__ == '__main__':
    test(50)

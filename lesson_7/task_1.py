# оптимизация: в хвосте элементы уже будут стоять на своих местах и нам не нужно его проходить.
# Т.е. с каждым проходом идём на 1 элемент меньше


def bubble_sort(array):
    done = 0
    for _ in range(len(array)):
        for i in range(0, len(array) - done - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        done += 1


if __name__ == '__main__':
    arr = [1, 7, 6, 3, 9, 0, 2, 4, 5, 8]
    bubble_sort(arr)
    print(arr)

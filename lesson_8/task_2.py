from heapq import heappush, heappop, heapify
from collections import Counter, namedtuple


class Node(namedtuple('Node', 'priority letter left right')):
    # Избегаем последовательного сравнения всех элементов кортежа
    def __lt__(self, other):
        return self.priority < other.priority

# P.S. Такой подход с точки зрения ООП, наверное, не совсем корректный
# Но Node является классом для хранения временных данных и почти никакой логики в себе не несёт


def _encode_node(node, table, code):
    if node.letter is not None:
        if node.left or node.right:     # Проверка на случай, если дерево построилось неправильно
            raise ValueError('Incorrect node')
        table[node.letter] = code
    else:
        if node.left:
            _encode_node(node.left, table, code + '0')
        if node.right:
            _encode_node(node.right, table, code + '1')


def compression(text):
    if len(text) == 1:
        return '0', {text: '0'}

    heap = [Node(priority, letter, None, None) for letter, priority in Counter(text).items()]
    heapify(heap)

    while len(heap) > 1:
        first, second = heappop(heap), heappop(heap)
        node = Node(first.priority + second.priority, None, first, second)
        heappush(heap, node)

    letters_table = {}
    node = heappop(heap)
    _encode_node(node, letters_table, '')
    return ' '.join(letters_table[c] for c in text), letters_table


def _test(text_len):
    from random import randint
    from timeit import timeit

    print('Generate numbers...', end=' ')
    string = ''.join(chr(randint(ord('a'), ord('z'))) for _ in range(text_len))
    print('Done')

    func = compression
    print('Start compression')
    print(f'time: {timeit("func(string)", number=1, globals=locals())}')


if __name__ == '__main__':
    print(*compression('Hello, world!'), sep='\n', end='\n\n')
    print(*compression('beep boor beer!'), sep='\n', end='\n\n')

    # _test(1000000)  # Даже по скорости неплохо вышло. 1 000 000 - 0.25 сек на моём ноуте. Линейная зависимость

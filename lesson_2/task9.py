# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр


def get_sum(number):
    sm = 0
    while number > 0:
        sm += number % 10
        number //= 10
    return sm


n = int(input('Введите кол-во чисел: '))
mx = 0
number = None

for i in range(n):
    cur_num = int(input(f'Введите натуральное число №{i + 1}: '))
    sm = get_sum(cur_num)
    if sm > mx:
        mx = sm
        number = cur_num

if number is None:
    print('Числа отсутствуют')
else:
    print(f"Максимальная сумма: {mx}; число {number}")

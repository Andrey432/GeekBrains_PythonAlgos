# схемы https://drive.google.com/file/d/1N67n7QGRbLDNXA2pBlShOsU0MXz_PSJ9/view?usp=sharing

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

number = int(input('Введите натуральное число: '))
even = uneven = 0

while number > 0:
    if (number % 10) % 2:
        uneven += 1
    else:
        even += 1
    number //= 10

print(f'Кол-во чётных чисел: {even}',
      f'Кол-во нечётных чисел: {uneven}', sep='\n')
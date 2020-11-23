# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не
# более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное
# пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести правильный ответ


from random import randint


def game(number, attemts):
    if attemts == 0:
        print(f'Вы не угадали! Загаданное число: {number}')
        return
    print(f'Попыток осталось {attemts}')

    user_number = int(input("Введите ваше предположение: ").strip())
    if user_number == number:
        print('Поздравляем, вы угадали!')
        return

    print(f'Неправильно! Ваше число {"больше" if user_number > number else "меньше"}.')
    game(number, attemts - 1)


rnd_number = randint(0, 100)
attemts = 10

print('Программа загадала число от 0 до 100. Отгадайте же его!')
print('Вводите целые числа')
game(rnd_number, attemts)

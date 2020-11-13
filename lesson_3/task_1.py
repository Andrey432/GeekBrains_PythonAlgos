# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

START = 2
END = 99
VALUES_RANGE = (2, 10)

# Для конкретно этих данных можно взять только END // value
# но если START станет больше, то это выражение уже не будет работать
# немного универсальности)
for value in range(*VALUES_RANGE):
    print(f'{value} - {END // value - (START - 1) // value}')
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a, b, c = map(float, input("Введите 3 разных числа: ").split())

if min(a, c) < b < max(a, c):
    print(f"Число {b} среднее")
elif min(b, c) < a < max(b, c):
    print(f"Число {a} среднее")
else:
    print(f"Число {c} среднее")

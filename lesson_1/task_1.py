# схемы: https://drive.google.com/file/d/1l_pJRx-vZo7GTL0sXVIUyQ2NjyEXh-pG/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

a, b, c = map(int, input("Введите число, состоящее из 3-ёх цифр: "))
print(f"Сумма цифр: {a + b + c}", f"Произведение цифр: {a * b * c}", sep='\n')

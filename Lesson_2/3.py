"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = int(input('Введите число: '))


def reverse_num(number):
    i = str(number % 10)
    if number // 10 == 0:
        return i
    else:
        return i + reverse_num(number // 10)

print(reverse_num(number))


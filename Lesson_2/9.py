"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

number_stack = input('Введите числа через пробел: ')
maximum = 0
summary = 0
number_stack = number_stack.split()


def search(number, summ):
    if number == 0:
        return summ
    summ = summ + number % 10
    number = number // 10
    return search(number, summ)


for number in number_stack:
    number = int(number)
    if search(number, 0) > summary:
        summary = search(number, 0)
        maximum = number

print(f'В наибольшем по сумме цифр числе {maximum}  сумма его цифр - {summary}')

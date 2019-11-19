"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def elements_sum():
    summary = 0
    number = int(input("Введите число:"))
    for n in range(number):
        summary += 1 / (2 ** n) * (1 if n % 2 == 0 else -1)
    print(summary)


elements_sum()



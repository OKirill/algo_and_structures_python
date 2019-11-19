"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def eq(n):
    if n < 1:
        return 0
    else:
        return n + eq(n - 1)


num = int(input("Введите число: "))
if eq(num) == num * (num + 1) / 2:
    print("Условие выполняется")
else:
    print("Условие не выполняется")

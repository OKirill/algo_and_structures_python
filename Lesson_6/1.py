"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile
import random
import sys

number = int(input('Введите число: '))


@profile
def reverse_num(number):
    i = str(number % 10)
    if number // 10 == 0:
        return i
    else:
        return i + reverse_num(number // 10)
    print(reverse_num(number))


# print(reverse_num(number))

@profile
def elements_sum():
    summary = 0
    number = int(input("Введите число:"))
    for n in range(number):
        summary += 1 / (2 ** n) * (1 if n % 2 == 0 else -1)
    print(summary)


@profile
def function_1():
    b = []
    x = list(range(100000))
    for num in x:
        return b.append(num)


@profile
def function_2():
    b = []
    x = random.sample(range(100000), 1000)
    for num in x:
        if num % 2 == 0:
            return b.append(num)


def fact_iter_v1(n):
    if n == 0 or n == 1:
        return 1
    else:
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod


@profile
def fact_line_rec_proc(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_line_rec_proc(n - 1)


@profile
def fact_iter_v1(n):
    if n == 0 or n == 1:
        return 1
    else:
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod


if __name__ == '__main__':
    elements_sum()
    reverse_num(number)
    function_1()
    function_2()
    fact_iter_v1(20)
    fact_line_rec_proc(20)

"""Python 3.7.3 Windows 10 x64
Почему то везде используется одинаковое кол-во памяти, то ли из-за кол-ва процессов открытых, либо изначально выделяется какое то определенное кол-во с запасом
Line #    Mem usage    Increment   Line Contents
================================================
    30     14.3 MiB     14.3 MiB   @profile
    31                             def elements_sum():
    32     14.3 MiB      0.0 MiB       summary = 0
    33     14.3 MiB      0.0 MiB       number = int(input("Введите число:"))
    34     14.3 MiB      0.0 MiB       for n in range(number):
    35     14.3 MiB      0.0 MiB           summary += 1 / (2 ** n) * (1 if n % 2 == 0 else -1)
    36     14.3 MiB      0.0 MiB       print(summary)


Filename: D:/groupproject/algo/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    18     14.3 MiB     14.3 MiB   @profile
    19                             def reverse_num(number):
    20     14.3 MiB      0.0 MiB       i = str(number % 10)
    21     14.3 MiB      0.0 MiB       if number // 10 == 0:
    22     14.3 MiB      0.0 MiB           return i
    23                                 else:
    24                                     return i + reverse_num(number // 10)
    25                                 print(reverse_num(number))


Filename: D:/groupproject/algo/algo_and_structures_python/Lesson_6/1.py




Line #    Mem usage    Increment   Line Contents
================================================
    39     14.3 MiB     14.3 MiB   @profile
    40                             def function_1():
    41     14.3 MiB      0.0 MiB       b = []
    42     16.2 MiB      1.9 MiB       x = list(range(100000))
    43     16.2 MiB      0.0 MiB       for num in x:
    44     16.2 MiB      0.0 MiB           return b.append(num)


Filename: D:/groupproject/algo/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    47     14.8 MiB     14.8 MiB   @profile
    48                             def function_2():
    49     14.8 MiB      0.0 MiB       b = []
    50     14.4 MiB      0.0 MiB       x = random.sample(range(100000), 1000)
    51     14.4 MiB      0.0 MiB       for num in x:
    52     14.4 MiB      0.0 MiB           if num % 2 == 0:
    53     14.4 MiB      0.0 MiB               return b.append(num)


Filename: D:/groupproject/algo/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    74     14.4 MiB     14.4 MiB   @profile
    75                             def fact_iter_v1(n):
    76     14.4 MiB      0.0 MiB       if n == 0 or n == 1:
    77                                     return 1
    78                                 else:
    79     14.4 MiB      0.0 MiB           prod = 1
    80     14.4 MiB      0.0 MiB           for i in range(1, n + 1):
    81     14.4 MiB      0.0 MiB               prod *= i
    82     14.4 MiB      0.0 MiB           return prod


Filename: D:/groupproject/algo/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    66     14.4 MiB     14.4 MiB   @profile
    67                             def fact_line_rec_proc(n):
    68     14.4 MiB      0.0 MiB       if n == 0 or n == 1:
    69     14.4 MiB      0.0 MiB           return 1
    70                                 else:
    71                                     return n * fact_line_rec_proc(n - 1)


Filename: D:/groupproject/algo/algo_and_structures_python/Lesson_6/1.py
"""

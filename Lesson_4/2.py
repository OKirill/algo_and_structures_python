"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import timeit
import cProfile


def simple():
    n = int(input("Введите диапазон чисел:"))
    desire = int(input("Введите номер простого числа которое вы ищите:"))

    lst = []

    for i in range(2, n + 1):

        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    desire = lst[desire - 1]
    print(lst)
    print(f"Ваше число {desire}")


# simple()


def eratosfen():
    n = int(input("Введите диапазон чисел:"))
    desire = int(input("Введите номер простого числа которое вы ищите:"))
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    lst = (list(filter(lambda x: x != 0, numbers)))
    desire = lst[desire - 1]
    print(lst)
    print(print(f"Ваше число {desire}"))


# eratosfen()


print(timeit.timeit("simple()", setup="from __main__ import simple", number=1))
print(timeit.timeit("eratosfen()", setup="from __main__ import eratosfen", number=1))
cProfile.run("simple()")
cProfile.run("eratosfen()")

"""
При вводном диапазоне 1000 и числе под номером 5
Без решета: 5.3677638000000005
С рещетом: 6.9835752

При вводном диапазоне 10000 и числе под номером 123
Без решета: 8.980477400000002
С рещетом: 7.682048400000001

При вводном диапазоне 100000 и числе под номером 123
Без решета: 15.2321638
С рещетом: 13.4854729

Как видно на длинной дистанции и большем диапазоне алгоритм эратосфена начинает вырываться вперед, в то время как при небольшом диапазоне - наоборот.
Это далеко не самые оптимальые решения нахождения i-го числа и можно сделать их намного быстрее, но для эксперемента были выбраны специально "медлительные" способы решения
"""
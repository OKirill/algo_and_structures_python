"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import cProfile
import timeit
import random


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

                swapped = True


def selection_sort(nums):
    for i in range(len(nums)):

        lowest_value_index = i

        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j

        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]

        j = i - 1

        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]

        nums[j + 1] = item_to_insert


def main():
    r = random.sample(range(100000), 10000)

    bubble_sort(r)

    selection_sort(r)

    insertion_sort(r)


cProfile.run('main()')

number = int(input('Введите число: '))
user_input = number


def sort_numbers_r(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        n = number % 10
        number = number // 10
        if n % 2 == 0:
            even += 1
            return sort_numbers_r(number, even, odd)
        else:
            odd += 1
            return sort_numbers_r(number, even, odd)


def sort_numbers_c(number, even=0, odd=0):
    while number > 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        number = number // 10
    # print(f'В числе {user_input}: {even} четных  и {odd} нечетных чисел')


print(timeit.timeit("sort_numbers_r(number, 0, 0)", setup="from __main__ import sort_numbers_r, number"))
print(timeit.timeit("sort_numbers_c(number, 0, 0)", setup="from __main__ import sort_numbers_c, number"))

"""
Для числа 46876532 время обработки составило - 2.5510602999999996 - для рекурсии
1.4715314999999975 - для цикла
По профайлеру время обработки в диапоазоне 10000 из 100000
                                                пузырьковой сортировки: 16.093
                                                выборочной сортировки: 4.903
                                                вставочной сортировки: 0.002

Для рекурсии и цикла сложность составляет O(n)
для пузырьковой сортировки в худшем случае время составляет O(n²)
затраты времени на сортировку выборкой в среднем составляют O(n²), где n — количество элементов списка.
время сортировки вставками в среднем равно O(n²), где n — количество элементов списка.
Как видим самый медленный вариант - пузырьковая сортировка(совсем не годится для большого массива чисел)
потом идет сортировка выборкой а за ней сортировка вставкой
есть ещё сортировки пирамидальная, слиянием и быстрая(самый оптимальный вариант)
"""
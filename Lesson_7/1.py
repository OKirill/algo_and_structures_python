"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

quantity = 20
nums = [random.randint(-100, 100) for i in range(quantity)]
print(f'Исходный массив: {nums}')


def bubble_sort(nums):
    n = 1
    while n < len(nums):
        sorted = True
        for i in range(len(nums) - n):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                sorted = False
        if sorted:
            break
        n += 1
    print(f'Отсортированный по убыванию: {nums}')


bubble_sort(nums)

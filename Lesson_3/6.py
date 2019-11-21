"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import random

N = int(input("Укажите длину массива: "))
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(f"|{arr[i]:3d}|", end=' ')

arr_min = arr.index(min(arr))
arr_max = arr.index(max(arr))

summ = 0

if arr_min > arr_max:
    for i in range(arr_max + 1, arr_min):
        summ += arr[i]
else:
    for i in range(arr_min + 1, arr_max):
        summ += arr[i]

print(f'\nCумма элементов между минимальным {min(arr)} и максимальным элементами {max(arr)} равна {summ}.')
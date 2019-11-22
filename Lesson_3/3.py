# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random

N = int(input("Укажите длину массива: "))
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 100)
    print(f"|{arr[i]:3d}|", end=' ')

arr_min = arr.index(min(arr))
arr_max = arr.index(max(arr))
print(f'\n минимальный элемент - {min(arr)} под индексом: {arr_min + 1}\n'
      f'\n максимальный элемент - {max(arr)} под индексом: {arr_max + 1}\n')
arr[arr_min], arr[arr_max] = arr[arr_max], arr[arr_min]

for i in range(N):
    print(f"|{arr[i]:3d}|", end=' ')
print()

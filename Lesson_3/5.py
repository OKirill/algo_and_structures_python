# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import random

N = int(input("Укажите длину массива: "))
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(arr)

i = 0
index = -1
while i < N:
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index + 1, ':', arr[index])

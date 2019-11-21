# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random

M = int(input("Введите кол-во столбцов матрицы: "))
N = int(input("Введите кол-во строк матрицы: "))
arr = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random() * 1000)
        b.append(n)
        print(f"{n:5d}", end='')
    arr.append(b)
    print()

maximum = -1
for j in range(M):
    minimum = 1000
    for i in range(N):
        if arr[i][j] < minimum:
            minimum = arr[i][j]
    if minimum > maximum:
        maximum = minimum
print("Максимальный элемент среди минимальных: ", maximum)

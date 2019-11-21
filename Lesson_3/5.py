# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import random

N = int(input("Укажите длину массива: "))
ARR = []
for i in range(N):
    ARR.append(int(random() * 100) - 50)
print(ARR)

i = 0
index = -1
while i < N:
    if ARR[i] < 0 and index == -1:
        index = i
    elif ARR[i] < 0 and ARR[i] > ARR[index]:
        index = i
    i += 1

print(index + 1, ':', ARR[index])

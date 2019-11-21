# 4.	Определить, какое число в массиве встречается чаще всего.
from random import random

N = int(input("Укажите длину массива: "))
arr = [0] * N
for i in range(N):
    f = True
    arr[i] = int(random() * 10)
    print(f"|{arr[i]:3d}|", end=' ')


MNUMB = 0
MCOUNT = 0

for i in arr:
    if arr.count(i) > MCOUNT:
        MNUMB = i
        MCOUNT = arr.count(i)

print()

print(f"{MNUMB} встречается чаще всего - {MCOUNT} раз")

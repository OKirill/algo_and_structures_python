# 4.	Определить, какое число в массиве встречается чаще всего.
from random import random

N = int(input("Укажите длину массива: "))
ARR = [0] * N
for i in range(N):
    f = True
    ARR[i] = int(random() * 10)
    print(f"|{ARR[i]:3d}|", end=' ')


MNUMB = 0
MCOUNT = 0

for i in ARR:
    if ARR.count(i) > MCOUNT:
        MNUMB = i
        MCOUNT = ARR.count(i)

print()

print(f"{MNUMB} встречается чаще всего - {MCOUNT} раз")

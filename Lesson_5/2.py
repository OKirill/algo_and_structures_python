"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections


def get_result():
    hex_num = input('Введите два числа в шестнадцатеричном формате: ').split()
    numbers = collections.defaultdict(list)
    for num in hex_num:
        numbers[num] = list(num)
    tnum = 0
    mnum = 1
    for num in numbers.keys():
        num = int(num, 16)
        tnum += num
        mnum *= num
    tnum = list(hex(tnum))[2:]
    mnum = list(hex(mnum))[2:]
    return tnum, mnum


def main():
    tnum, mnum = get_result()
    print()
    print(f'Сумма чисел {tnum} \nПроизведение {mnum}'.upper())


main()

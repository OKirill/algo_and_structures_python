"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
number = int(input('Введите число: '))
user_input = number


def sort_numbers(number, even=0, odd=0):
    n = number % 10
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    if number // 10 == 0:
        print(f'В числе {user_input}: {even} четных  и {odd} нечетных чисел')
        return
    sort_numbers(int(number // 10), even, odd)


sort_numbers(number)

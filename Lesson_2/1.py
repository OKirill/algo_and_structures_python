"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
while True:
    CHOIСE = input(
        "Укажите операцию которую необходимо произвести над числами: '+', '-', '*', '/', для выхода введите - '0' ")
    if CHOIСE == "+" or CHOIСE == "-" or CHOIСE == "*" or CHOIСE == "/":
        NUM1 = int(input("Введите первое число: "))
        NUM2 = int(input("Введите второе число: "))
        if CHOIСE == "+":
            print(f"Сумма чисел равна {NUM1 + NUM2}")
        elif CHOIСE == "-":
            print(f"Разность чисел равна {NUM1 - NUM2}")
        elif CHOIСE == "*":
            print(f"Произведение чисел равно {NUM1 * NUM2}")
        elif CHOIСE == "/":
            if NUM2 == 0:
                print("Делить на 0 нельзя!")
            else:
                print(f"Частное чисел равно {NUM1 / NUM2}")
    elif CHOIСE == "0":
        break

    else:
        print("Введите правильный знак!")

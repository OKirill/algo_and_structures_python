# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

NUM1 = int(input("Введите первое число:"))
NUM2 = int(input("Введите второе число:"))
NUM3 = int(input("Введите третье число:"))

if ((NUM1 > NUM2) and (NUM1 < NUM3)) or ((NUM1 < NUM2) and (NUM1 > NUM3)):
    print(f"Среднее число {NUM1}")

elif ((NUM2 > NUM1) and (NUM2 < NUM3)) or ((NUM2 < NUM1) and (NUM2 > NUM3)):
    print(f"Среднее число {NUM2}")

elif ((NUM3 > NUM2) and (NUM3 < NUM1)) or ((NUM3 < NUM2) and (NUM3 > NUM1)):
    print(f"Среднее число {NUM3}")

else:
    print("Пожалуйста, введите разные числа!")

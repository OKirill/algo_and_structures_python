# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
MAIN_NUMBER = int(input("Введите любое трёхзначное число: "))

NUM3 = MAIN_NUMBER % 10
NUM2 = MAIN_NUMBER % 100 // 10
NUM1 = MAIN_NUMBER // 100

print(NUM1)
print(NUM2)
print(NUM3)

print(f"Сумма равна: {NUM1 + NUM2 + NUM3}")
print(f"Произведение равно: {NUM1 * NUM2 * NUM3}")


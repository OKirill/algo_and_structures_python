#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

LETTER1 = ord(input("Введите первую Букву: ").lower())
LETTER2 = ord(input("Введите вторую Букву: ").lower())

print(LETTER1 - 96)
print(LETTER2 - 96)

if LETTER1 > LETTER2:
    print(f"Букв между ними: {LETTER1 - LETTER2 - 1}")

else:
    print(f"Букв между ними: {LETTER2 - LETTER1 - 1}")
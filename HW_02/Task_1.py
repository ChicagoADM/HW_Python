"""
Напишите программу, которая получает целое число и возвращает его 
шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата. 
"""

num = int(input('Ввидите целое число: '))
intermediate = None
res = ""
hex_num = hex(num)
while num > 0:
    intermediate = num % 16
    if intermediate < 10:
        res += str(intermediate)
    elif intermediate == 10:
        res += "a"
    elif intermediate == 11:
        res += "b"
    elif intermediate == 12:
        res += "c"
    elif intermediate == 13:
        res += "d"
    elif intermediate == 14:
        res += "e"
    elif intermediate == 15:
        res += "f"
    num //= 16

print("Число в шестнадцатеричнм строковом представлении ", res[::-1])
print("Проверка hex: ", hex_num[2:])

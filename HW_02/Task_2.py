"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
import fractions

numerator1: str = str(input("Введите числитель первой дроби: "))
denominator1: str = str(input("Введите знаменатель первой дроби: "))
numerator2: str = str(input("Введите числитель второй дроби: "))
denominator2: str = str(input("Введите знаменатель второй дроби: "))
num1: int = int(numerator1)
num2: int = int(denominator1)
num3: int = int(numerator2)
num4: int = int(denominator2)


result1 = (num1 / num2 ) + (num3 / num4)
result2 = (num1 / num2 ) * (num3 / num4)
print("Cумму дробей: ", result1)
print("Произведение* дробей: ", result2)
print()
print("*" * 24)

firstfraction = fractions.Fraction(num1, num2)
denominator1fraction = fractions.Fraction(num3, num4)
result3 = firstfraction + denominator1fraction
result4 = firstfraction * denominator1fraction
print("Провервка кода модулем fractions")
print("Cумму дробей: ", result3)
print("Произведение* дробей: ", result4)

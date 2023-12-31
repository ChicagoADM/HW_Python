"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: «Число является простым, если делится нацело только на 
единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

flag = True
i = 2
number = int(input("Введите число от 1 до 100000: "))
if number < 0:
    print("Ограничение: отрицательное число")
elif number > 100000:
    print("Ограничение: число больше 100000 тысяч")
else:
    while i <= number ** 0.5:
        if number % i == 0:
            flag = False
            break
        i += 1
    if flag:
        print("Простое число")
    else:
        print("Составное число")
            

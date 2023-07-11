"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
import random
"""

random_num = random.randint(0, 1000)
num = None
attempts = 10
while attempts > 0:
    num = int(input(f"Угадай число от 0 до 1000 (У вас осталось {attempts} попыток): "))
    attempts -= 1
    if random_num > num:
        print(f"Загадоное число больше {num}")
    elif random_num < num:
        print(f"Загадоное число меньше {num}")
    else:
        print("Ура! Вы угадали")
        break
else:
    print("Вы не угадали, Получится в следующий ")

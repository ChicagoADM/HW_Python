# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from sys import argv
from modul_task_1 import my_date


print(my_date(argv[1]))
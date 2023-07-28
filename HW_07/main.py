
# Решить задачи, которые не успели решить на семинаре.
# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from pathlib import Path
from fill_numbers import fill_numbers
from name_gen import name_gen
from from_two_files import from_two_files
from make_files import make_files
from new_make_files import new_make_file
from group_rename import group_rename

if __name__ == '__main__':
    fill_numbers(20, 'numbers.txt')

    name_gen(10, 4, 7, Path('names.txt'))

    from_two_files(Path('numbers.txt'), Path('names.txt'), Path('result.txt'))

    make_files('bin', count=10)

    data = {
        'txt': 4,
        'zip': 3,
    }

    new_make_file(data)

    group_rename(4, 'bin', 'zip', [2, 4], "new")
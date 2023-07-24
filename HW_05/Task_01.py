# ✔Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

from typing import Tuple

FILE_1 = "C:\\Windows\\System32\\spool\\PRINTER\\Foto.jpg"
FILE_2 = "D:\\Folder\\New_folder\\main.py"
FILE_3 = "F:\\New_folder\\New_folder1\\Doc.docx"


def split_path(path: str) -> tuple[str, str, str]:
    path_only, _, file_name = path.rpartition('\\')
    file_name, _, file_ext = file_name.rpartition(".")
    return path_only, file_name, file_ext


def main():
    print(split_path(FILE_1))
    print(split_path(FILE_2))
    print(split_path(FILE_3))


main()
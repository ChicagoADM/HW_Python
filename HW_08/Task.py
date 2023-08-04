# 📌Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

import json
import os
import csv
import pickle
from os.path import join, getsize


def walk_in_directory(file_path):
    for root, dirs, files in os.walk(file_path):
        folder = root.split('\\')

        str_for_json = " ".join(files)
        to_json = {root: dirs, 'files': str_for_json, 'Size': sum(getsize(join(root, name)) for name in files) }
        with open('to_json.json', 'a') as f:
            json.dump(to_json, f, sort_keys=True, indent=2)

        
        with open('for_csv.csv', 'a', newline='') as csvfile:
            fieldnames = ['files', 'dirs']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'files': str_for_json, 'dirs': dirs})

       
        with open('data.pickle', 'wb') as f:
            pickle.dump(to_json, f)

        with open('data.pickle', 'rb') as f:
            ...
            data_new = pickle.load(f)
        print(data_new)


walk_in_directory(os.curdir)
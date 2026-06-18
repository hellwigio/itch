# Список файлов и папок
#
# Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
#
# Отдельно список папок
#
# Отдельно список файлов
#
# Пример запуска
#
# python script.py /home/user/documents
#
# Пример вывода
#
# Содержимое директории '/home/user/documents':
#
#
# Папки:
#
# - folder1
#
# - folder2
#
#
# Файлы:
#
# - file1.txt
#
# - file2.txt
#
# - notes.docx

import os
import sys

workdir = '.'


if len(sys.argv) > 1:
    workdir = sys.argv[1]

absolute_path = os.path.abspath(workdir)

folder_list = []
file_list = []

for root, dirs, files in os.walk(absolute_path):
    folder_list.append(root)

    for file in files:
        file_list.append(file)


print(f'Содержимое директории {absolute_path}:')

print("\n\nПапки:\n")

for f in folder_list:
    print(" - " + f)

print("\n\nФайлы:\n")

for f in file_list:
    print(" - " + f)

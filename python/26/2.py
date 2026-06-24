# Поиск и удаление файлов с указанным расширением
#
# Напишите программу, которая:
#
# Принимает путь к директории и расширение файлов через аргумент командной строки.
#
# Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
#
# Спрашивает у пользователя, хочет ли он удалить найденные файлы.
#
# Если пользователь подтверждает, удаляет их.
#
# Пример запуска:
#
# python script.py /home/user/PycharmProjects/project1 .log
#
# Пример вывода
#
# Найдены файлы с расширением '.log':
#
# - logs/error.log
#
# - logs/system.log
#
# - logs/backup/old.log
#
# - logs/backup/debug.log
#
#
# Вы хотите удалить эти файлы? (y/n): y
#
# Удаление завершено.
#

import os
import sys

if len(sys.argv) < 3:
    print("Usage: python script.py <workdir> <extension>")
    exit(1)

workdir = sys.argv[1]
extension = sys.argv[2]

absolute_path = os.path.abspath(workdir)

file_list = []

for root, dirs, files in os.walk(absolute_path):
    for file in files:
        if file.endswith(extension):
            file_list.append(root + "/" + file)

if len(file_list) == 0:
    print(f"Не найдено файлов с расширением {extension}.")
    exit(0)

choice = input(
    f"Найдено {len(file_list)} файлов с расширением {extension}, удалить? (y/n): "
).lower()

if choice == "y":
    for file in file_list:
        os.remove(file)

    print(f"Удаление завершено.")
else:
    print("Отмена.")

""" 02 Поиск и удаление дубликатов

Напишите программу, которая
- удаляет дублирующиеся строки из файла
- и сохраняет результат в новый файл.

Имя нового файла формируется как unique_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

"""
import os

def remove_duplicates(filename: str) -> None:
    if not os.path.isfile(filename):
        print(f"Ошибка: файл '{filename}', не найден.")
        return

    unique_lines = []
    with open(filename, 'r') as source:
        for line in source:
            if line not in unique_lines:
                unique_lines.append(line)

    with open(f'unique_{filename}', 'w') as output:
        for line in unique_lines:
            output.write(line)

    print(f'Дубликаты удалены. Уникальные строки сохранены в unique_{filename}.')



remove_duplicates("movies_to_watch.txt")
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

remove_duplicates("M")
# File not found: [Errno 2] No such file or directory: 'M'

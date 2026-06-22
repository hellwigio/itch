""" 01 Фильтрация по ключевому слову

Напишите программу, которая
- ищет в файле все строки, содержащие указанное пользователем слово,
- и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в <keyword>_<original_filename>.

"""
import os

def find_keyword(filename: str, keyword: str) -> None:
    if not os.path.isfile(filename):
        print(f'\nFile "{filename}" not found')
        return

    with open(f'{keyword}_{filename}', 'w') as output:
        with open(filename, 'r') as source:
             for line in source:
                if keyword in line:
                    output.write(line)

    print(f'Строки, содержащие \'{keyword}\', сохранены в {keyword}_{filename}.')


find_keyword('s', 'error')
# File not found: [Errno 2] No such file or directory: 's'

find_keyword('system_log.txt', 'error')
# Строки, содержащие 'error', сохранены в error_system_log.txt.

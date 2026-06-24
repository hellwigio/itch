"""11 Количество символов

Напишите программу, которая подсчитывает количество:
- букв;
- цифр;
- пробелов;
- остальных символов.

Пример вывода:
Строка: Python 3.12 is awesome!
Буквы: 15
Цифры: 3
Пробелы: 3
Остальные символы: 2
"""

text = "Python 3.12 is awesome!"
print("Строка:", text)

letters = 0
digits = 0
spaces = 0
others = 0

for i in text:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    elif i.isspace():
        spaces += 1
    else:
        others += 1

print("Буквы:", letters)
print("Цифры:", digits)
print("Пробелы:", spaces)
print("Остальные символы:", others)

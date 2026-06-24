"""06 Числа и слова

Напишите программу, которая
- обрабатывает строку, содержащую слова и целые числа, разделённые пробелами.

Программа должна преобразовать строку в список, где
- числа преобразуются в тип int,
- а остальные элементы остаются строками и начинаются с заглавной буквы.

text = "apple 42 banana 3 100 orange"

Пример вывода:
Изначальная строка: apple 42 banana 3 100 orange
Результат: ['Apple', 42, 'Banana', 3, 100, 'Orange']
"""

text = "apple 42 banana 3 100 orange"

print("Изначальная строка:", text)

words = text.split(" ")

result = []

for word in words:
    if word.isdigit():
        result += [int(word)]
    else:
        result += [word]

print("Результат:", result)

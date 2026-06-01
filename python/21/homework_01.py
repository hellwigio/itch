""" 01 Повторения букв

Реализуйте функцию, которая
- принимает текст
- и возвращает словарь с подсчётом количества каждой буквы, игнорируя регистр.

Данные:
text = "Programming is fun!"
Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""

from collections import Counter


def char_count(text):
    return Counter([s for s in text.lower() if s.isalpha()])


text = "Programming is fun!"
sample = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}


print(char_count(text))
print(char_count(text) == sample)

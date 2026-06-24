# Одно слово
#
# Напишите программу, которая обрабатывает список из строк и удаляет
# все строки, содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
#
# Данные:
#
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
#
# Пример вывода:
#
# Обработанный список: ['hello', 'world', 'simple']


words = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

i = 0
while i < len(words):
    if " " in words[i]:
        words.pop(i)
    else:
        words[i] = words[i].lower()
        i += 1

print("Обработанный список:", words)


# list comprehension

words = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

words[:] = [w.lower() for w in words if " " not in w]

print("Обработанный список:", words)

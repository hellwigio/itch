# Увеличение чисел
#
# Напишите программу, которая заменяет все числа в строке
# на их эквивалент, умноженный на 10.
#
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
#
# Пример вывода:
#
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."

print("Строка:", text)

result = []

NUMERIC = "1234567890."

for word in text.split():
    if "" == word.strip(NUMERIC) and word[0].isdigit():
        result += [str(float(word) * 10)]
    else:
        result += [word]

print("Результат:", " ".join(result))

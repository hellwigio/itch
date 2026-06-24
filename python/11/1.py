# Звёздочки вместо чисел
#
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
#
# text = "My number is 123-456-789"
#
# Пример вывода:
#
# Строка: My number is 123-456-789
#
# Результат: My number is ***-***-***

text = "My number is 123-456-789"

print("Строка:", text)

result = ""

for letter in text:
    if letter.isdigit():
        result += "*"
    else:
        result += letter

print("Результат:", result)

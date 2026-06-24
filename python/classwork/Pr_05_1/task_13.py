"""13 Все позиции подстроки
Напишите программу, которая
- ищет подстроку в строке
- и выводит все индексы начала вхождения подстроки.

ВАЖНО: программа должна быть регистро-независимой!

Пример вывода:
Строка: Banana bAnana baNAna
Подстрока: ban
Позиция: 0
Позиция: 7
Позиция: 14
"""

text = "Banana bAnana baNAna"
substring = "Ban"

print("Строка:", text)
print("Подстрока:", substring)

t = text.lower()
sub = substring.lower()

for i in range(len(t)):
    if t[i : i + len(sub)] == sub:
        print("Позиция:", i)

"""01 Проверка на подмножество

Напишите программу, которая
- проверяет, содержит ли первое множество все элементы второго множества.

Реализуйте решение несколькими способами.
(в том числе и способом, НЕ используящим возможности множеств).

Данные:
set1 = {1, 2, 3, 4}
set2 = {2, 3}
Пример вывода:
True
"""

set1 = {1, 2, 3, 4}
set2 = {2, 3}

# subset
print(set2.issubset(set1))

# intersection
print(set1.intersection(set2) == set2)

# difference in length
print(len(set1 - set2) == (len(set1) - len(set2)))


# cycle
for item in set2:
    if item not in set1:
        print(False)
        break
else:
    print(True)

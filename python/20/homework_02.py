""" 02 Фильтрация чисел по чётности

Напишите функцию filter_type, которая
- принимает первый аргумент ("even" или "odd")
- и произвольное количество чисел,
- возвращая только те, которые соответствуют фильтру.

Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр
"""

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0


def filter_numbers(filter_type, *numbers):
    if filter_type == "even":
        return list(filter(is_even, numbers))
    elif filter_type == "odd":
        return list(filter(is_odd, numbers))
    else:
        return "Некорректный фильтр"


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))   # [2, 4, 6]
print(filter_numbers("odd", 10, 15, 20, 25))      # [15, 25]
print(filter_numbers("prime", 2, 3, 5, 7))        # Некорректный фильтр

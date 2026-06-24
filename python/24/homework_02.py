"""02 Сумма вложенных чисел

Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.

Попробуйте решить в двух вариантах: tail и non-tail.

Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28
"""


def sum_digits_tail(items: list, acc: int = 0) -> int:
    if not items:
        return acc

    head, *tail = items

    if isinstance(head, list):
        return sum_digits_tail(head + tail, acc)

    return sum_digits_tail(tail, acc + head)


def sum_digits_non_tail(lst: list) -> int:
    if not lst:
        return 0

    head, *tail = lst
    if isinstance(head, list):
        return sum_digits_non_tail(head) + sum_digits_non_tail(tail)

    return head + sum_digits_non_tail(tail)


nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

print(sum_digits_tail(nested_numbers))  # 28
print(sum_digits_non_tail(nested_numbers))  # 28

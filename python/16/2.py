""" 02 Правильные скобки

Напишите программу, которая
- принимает строку, содержащую любые виды скобок
    — круглые (),
    — квадратные []
    — и фигурные {}.

Необходимо проверить, правильно ли они расставлены.
Скобки считаются правильно расставленными, если:
    Каждая открывающая скобка имеет соответствующую закрывающую.
    Скобки закрываются в правильном порядке.

Пример данных:
({[]}): True
({[}]): False
([]{}): True
: True
{[()()]}: True
([)]: False
{[)(()]}: False
({[): False
"""
from collections import deque

LEFT_BRACKETS = '([{'
RIGHT_BRACKETS = ')]}'

def check_brackets(string):
    stack = deque()

    for char in string:
        if char in LEFT_BRACKETS:
            stack.append(char)

        else:
            if not stack:
                return False

            i = RIGHT_BRACKETS.find(char)

            if i < 0:
                return False
            if stack.pop() != LEFT_BRACKETS[i]:
                return False

    return not stack


test_cases = [
    "({[]})",
    "({[}])",
    "([]{})",
    "",
    "{[()()]}",
    "([)]",
    "{[)(()]}",
    "({[)",
]

for test_case in test_cases:
    print(f"{test_case}: {check_brackets(test_case)}")



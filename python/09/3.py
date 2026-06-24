# Удаление всех повторяющихся символов
#
# Напишите программу, которая принимает строку и удаляет из неё
# все повторяющиеся символы, сохраняя только первые их вхождения.
#
# Пример вывода:
#
# Введите строку: Python programming
#
# Результат: Python prgami

inp = "Python programming"
result = ""

for s in inp:
    if s not in result:
        result += s

print("Результат: ", result)

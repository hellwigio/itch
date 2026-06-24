# Число в конце
#
# Напишите программу, которая создает новый список. В него необходимо
# добавить только те строки из исходного списка, в которых цифры находятся только в конце.
#
# Данные:
#
# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
#
# Пример вывода:
#
# Строки с цифрами только в конце: ['apple23', 'grape3']

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]

result = []

digits = "0123456789"

for value in strings:
    value_rstripped = value.rstrip(digits)

    if value.strip(digits) == value_rstripped:
        for digit in digits:
            if digit in value_rstripped:
                break
        else:
            result.append(value)


print(result)

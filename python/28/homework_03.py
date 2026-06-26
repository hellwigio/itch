""" 03 Комбинации одежды

Напишите функцию, которая
- принимает списки
    - типов одежды,
    - цветов
    - и размеров,
- а затем генерирует все возможные комбинации в формате "Clothe - Color - Size".

Данные:
clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L

"""

from itertools import product

def get_product(clothes, colors, sizes):
    for cloth, color, size in product(clothes, colors, sizes):
        print(f"{cloth} - {color} - {size}")


clothes = ["T-shirt", "Jeans", "Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

get_product(clothes, colors, sizes)

"""01 Выбор заказов

У вас есть список заказов.
Каждый заказ содержит название продукта и его цену.
Напишите функцию, которая:
- Отбирает заказы дороже 500.
- Создаёт список названий отобранных продуктов в алфавитном порядке.
- Возвращает итоговый список названий.

Данные:
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

Пример вывода:
['Chair', 'Laptop']

"""

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400},
]

sample = ["Chair", "Laptop"]


def select_expensive_orders(ords):
    filtered = filter(lambda i: i["price"] > 500, ords)

    products = [item["product"] for item in filtered]

    return sorted(products)


result = select_expensive_orders(orders)
print(result)
print(result == sample)

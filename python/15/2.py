# Обновление цен товаров
#
# Дан список товаров с ценами. Программа должна применить скидку
# к каждому товару и добавить в список элемент с новой ценой. 
# В конце вывести таблицу с новой ценой.
#
# Данные:
#
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
#
#
# Пример вывода:
#
# Введите скидку (в процентах): 17
#
# Товар          Старая цена    Новая цена
#
# Laptop            1200.00$       996.00$
#
# Mouse                25.00$         20.75$
#
# Keyboard           75.00$         62.25$
#
# Monitor            200.00$       166.00$
#

NAME, PRICE = 15, 13

line = "-" * (NAME + PRICE * 2)
row_template = f"{{:<{NAME}}}{{:>{PRICE}}}{{:>{PRICE}}}"
header_template = f"{line}\n{{:<{NAME}}}{{:>{PRICE}}}{{:>{PRICE}}}\n{line}"

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

percent = 17

for i, v in enumerate(products):
    v.append(v[1] * (1 - percent / 100))
    

print(header_template.format("Товар", "Старая цена", "Новая цена"))

for product, price, nprice in products:
    print(row_template.format(product.ljust(NAME, '.'), f"${price:.2f}", f"${nprice:.2f}"))

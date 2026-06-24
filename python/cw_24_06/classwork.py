from utils import print_result, db

import pymongo


collection = db.US_Adult_Income

# 1. Все пользователи, у которых age = 27
print_result(
    "1. Пользователи, у которых age = 27",
    collection.find({"age": 27}),
)


# 2. Пользователи из Mexico, у которых age = 27
print_result(
    "2. Пользователи из Mexico, у которых age = 27",
    collection.find({
        "age": 27,
        "native_country": " Mexico",
    }),
)


# 3. Все пользователи, но только поля age и native_country
print_result(
    "3. Только поля age и native_country",
    collection.find(
        {},
        {
            "age": 1,
            "native_country": 1,
        },
    ),
)


# 4. Только поля age и native_country, исключить _id
print_result(
    "4. Только поля age и native_country, без _id",
    collection.find(
        {},
        {
            "_id": 0,
            "age": 1,
            "native_country": 1,
        },
    ),
)


# 5. Сортировка по age по возрастанию
print_result(
    "5.1. Сортировка по age по возрастанию",
    collection.find(
        {},
        {
            "_id": 0,
            "age": 1,
            "native_country": 1,
            "education": 1,
            "hours_per_week": 1,
        },
    ).sort("age", pymongo.ASCENDING),
)


# 5. Сортировка по age по убыванию
print_result(
    "5.2. Сортировка по age по убыванию",
    collection.find(
        {},
        {
            "_id": 0,
            "age": 1,
            "native_country": 1,
            "education": 1,
            "hours_per_week": 1,
        },
    ).sort("age", pymongo.DESCENDING),
)


# 6. Возраст больше 18 и меньше 30
print_result(
    "6. Пользователи, у которых age > 18 и age < 30",
    collection.find({
        "age": {
            "$gt": 18,
            "$lt": 30,
        },
    }),
)


# 7. education не равен " Bachelors"
print_result(
    '7. Пользователи, у которых education != " Bachelors"',
    collection.find({
        "education": {
            "$ne": " Bachelors",
        },
    }),
)


# 8. Работает 45, 50 или 80 часов в неделю
print_result(
    "8. Пользователи, которые работают 45, 50 или 80 часов в неделю",
    collection.find({
        "hours_per_week": {
            "$in": [45, 50, 80],
        },
    }),
)


# 9. НЕ работает 45, 50 или 80 часов в неделю
print_result(
    "9. Пользователи, которые НЕ работают 45, 50 или 80 часов в неделю",
    collection.find({
        "hours_per_week": {
            "$nin": [45, 50, 80],
        },
    }),
)


# 10. native_country = United-States ИЛИ income = >50K
print_result(
    '10. Пользователи из United-States ИЛИ с income = ">50K"',
    collection.find({
        "$or": [
            {"native_country": " United-States"},
            {"income_bracket": " >50K"},
        ],
    }),
)

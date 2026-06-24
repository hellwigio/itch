from utils import print_result, db
import pymongo

customers = db.customers
adult_income = db.US_Adult_Income


# 1. Из коллекции customers выяснить, из какого города "Sven Ottlieb"
print_result(
    "1. Из коллекции customers выяснить, из какого города \"Sven Ottlieb\"", 
    customers.find(
        {"ContactName": "Sven Ottlieb"}, 
        {"_id": 0, "ContactName": 1, "City": 1}
    )
)


# 2. Из коллекции ich.US_Adult_Income найти возраст самого взрослого человека
oldest_person = adult_income.find_one(
    {},
    {"_id": 0, "age": 1},
    sort=[("age", pymongo.DESCENDING)],
)
print_result(
    "2. Из коллекции ich.US_Adult_Income найти возраст самого взрослого человека",
    oldest_person,
)


# 3. Из 2 задачи выясните, сколько человек имеют такой же возраст
max_age = oldest_person["age"]

same_age_count = adult_income.count_documents(
    {"age": max_age}
)

print_result(
    "3. Сколько человек имеют такой же возраст",
    [{"age": max_age, "count": same_age_count}],
)


# 4. Найти _id ObjectId документа, в котором education " IT-career-hub"
print_result(
    '4. Найти _id ObjectId документа, в котором education " IT-career-hub"',
    adult_income.find(
        {"education": " IT-career-hub"},
        {"_id": 1, "education": 1},
    ),
)


# 5. Выяснить количество людей в возрасте между 20 и 30 годами
count_20_30 = adult_income.count_documents(
    {
        "age": {
            "$gte": 20,
            "$lte": 30,
        }
    }
)

print_result(
    "5. Выяснить количество людей в возрасте между 20 и 30 годами",
    [{"count": count_20_30}],
)

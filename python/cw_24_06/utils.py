import os

from rich import print
from rich.pretty import pprint
import pymongo
from dotenv import load_dotenv


load_dotenv()

mongo_uri = os.getenv("MONGO_URI")

if not mongo_uri:
    raise RuntimeError("MONGO_URI is not set")

client = pymongo.MongoClient(mongo_uri)

db = client.ich
collection = db.US_Adult_Income

LIMIT = 10


def print_result(title: str, result) -> None:
    print("\n" + "=" * 100)
    print(title)
    print("=" * 100)

    if isinstance(result, pymongo.synchronous.cursor.Cursor):
        result = list(result.limit(LIMIT))

    pprint(result)


if __name__ == "__main__":
    print("UTILS")

import csv
import re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

def read_data(csv_file, db):
    with open(csv_file, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        mylist = list(reader)
    table_data = db.insert_many(mylist)
    return table_data


def find_cheapest(db):
    cheapest_ticket = db.find().sort("Цена")
    for price in cheapest_ticket:
    print(price)

def find_by_name(name, db):
    # regex = re.compile()
    find_name = db.find(name)
    for x in find_name:
        print(x)

if __name__ == '__main__':
    csv_file = 'artists.csv'
    db = client.admin.FIRST
    name = {"Исполнитель": "Семен Слепаков"}
    pass
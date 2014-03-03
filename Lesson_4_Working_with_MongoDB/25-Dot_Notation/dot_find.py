#!/usr/bin/env python
""" Your task is to write a query that will return all cars with width dimension greater than 2.5
Please modify only 'dot_query' function, as only that will be taken into account.

Your code will be run against a MongoDB instance that we have provided.
If you want to run this code locally on your machine,
you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.
"""


def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.examples
    return db


def dot_query():
    query = {}
    return query


if __name__ == "__main__":

    db = get_db()
    query = range_query()
    cars = db.cars.find(query)

    print "Found cars:", cars.count()
    import pprint
    pprint.pprint(cars[0])

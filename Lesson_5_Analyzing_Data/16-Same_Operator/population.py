#!/usr/bin/env python
"""
In an earlier exercise we looked at the cities dataset and asked which region in India contains 
the most cities. In this exercise, we'd like you to answer a related question regarding regions in 
India. What is the average city population for a region in India? Calculate your answer by first 
finding the average population of cities in each region and then by calculating the average of the 
regional averages.

Hint: If you want to accumulate using values from all input documents to a group stage, you may use 
a constant as the value of the "_id" field. For example, 
    { "$group" : "India Regional City Population Average",
      ... }

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation 
pipeline that can be passed to the MongoDB aggregate function. As in our examples in this lesson, 
the aggregation pipeline should be a list of one or more dictionary objects. 
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code 
locally on your machine, you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset used 
in examples in this lesson. If you attempt some of the same queries that we looked at in the lesson 
examples, your results will be different.
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [ ]
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result["result"]) == 1
    assert result["result"][0]["avg"] == 196025.97814809752
    import pprint
    pprint.pprint(result)

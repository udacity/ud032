#!/usr/bin/env python
"""
For this exercise, let's return to our cities infobox dataset. The question we would like you to answer
is as follows:  Which region in India contains the most cities?

As a starting point, use the solution for the example question we looked at -- "Who includes the most
user mentions in their tweets?"

One thing to note about the cities data is that the "isPartOf" field contains an array of regions or 
districts in which a given city is found. See the example document in Instructor Comments below.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation pipeline 
that can be passed to the MongoDB aggregate function. As in our examples in this lesson, the aggregation 
pipeline should be a list of one or more dictionary objects. Please review the lesson examples if you 
are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code 
locally on your machine, you have to install MongoDB, download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the dataset used in 
examples in this lesson. If you attempt some of the same queries that we looked at in the lesson 
examples, your results will be different.
"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = []
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    print "Printing the first result:"
    import pprint
    pprint.pprint(result["result"][0])
    assert result["result"][0]["_id"] == "Uttar Pradesh"
    assert result["result"][0]["count"] == 623



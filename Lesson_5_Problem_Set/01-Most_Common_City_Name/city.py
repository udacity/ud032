#!/usr/bin/env python
"""
Use an aggregation query to answer the following question. 

What is the most common city name in our cities collection?

Your first attempt probably identified None as the most frequently occurring city name. 
What that actually means is that there are a number of cities without a name field at all. 
It's strange that such documents would exist in this collection and, depending on your situation, 
might actually warrant further cleaning. 

To solve this problem the right way, we should really ignore cities that don't have a name specified. 
As a hint ask yourself what pipeline operator allows us to simply filter input? 
How do we test for the existence of a field?

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation pipeline 
that can be passed to the MongoDB aggregate function. As in our examples in this lesson, 
the aggregation pipeline should be a list of one or more dictionary objects. 
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. 
If you want to run this code locally on your machine, you have to install MongoDB, 
download and insert the dataset.
For instructions related to MongoDB setup and datasets please see Course Materials.

Please note that the dataset you are using here is a smaller version of the twitter dataset used in 
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
    pipeline = [ ]
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result["result"][0])
    assert len(result["result"]) == 1
    assert result["result"][0] == {'_id': 'Shahpur', 'count': 6}

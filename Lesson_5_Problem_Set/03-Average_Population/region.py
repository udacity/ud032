#!/usr/bin/env python
"""
Use an aggregation query to answer the following question. 

Extrapolating from an earlier exercise in this lesson, find the average regional city population 
for all countries in the cities collection. What were asking here is that you first calculate the 
average city population for each region in a country and then calculate the average of all the 
regional averages for a country. As a hint, _id fields in group stages need not be single values. 
They can also be compound keys (documents composed of multiple fields). You will use the same 
aggregation operator in more than one stage in writing this aggregation query. I encourage you to 
write it one stage at a time and test after writing each stage.

Please modify only the 'make_pipeline' function so that it creates and returns an aggregation 
pipeline that can be passed to the MongoDB aggregate function. As in our examples in this lesson, 
the aggregation pipeline should be a list of one or more dictionary objects. 
Please review the lesson examples if you are unsure of the syntax.

Your code will be run against a MongoDB instance that we have provided. If you want to run this code 
locally on your machine, you have to install MongoDB, download and insert the dataset.
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
    if len(result["result"]) < 150:
        pprint.pprint(result["result"])
    else:
        pprint.pprint(result["result"][:100])
    assert result["result"][0]["_id"] == 'Kuwait'
    assert result["result"][1]["avgRegionalPopulation"] == 363945.0
    assert result["result"][0] == {'_id': 'Kuwait', 'avgRegionalPopulation': 115945.66666666667}

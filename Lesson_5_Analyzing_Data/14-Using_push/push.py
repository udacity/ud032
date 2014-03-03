#!/usr/bin/env python
"""
$push is similar to $addToSet. The difference is that rather than accumulating only unique values 
it aggregates all values into an array.

Using an aggregation query, count the number of tweets for each user. In the same $group stage, 
use $push to accumulate all the tweet texts for each user. Limit your output to the 5 users
with the most tweets. 
Your result documents should include only the fields:
"_id" (screen name of user), 
"count" (number of tweets found for the user),
"tweet_texts" (a list of the tweet texts found for the user).  

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
    result = db.tweets.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('twitter')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    assert len(result["result"]) == 5
    assert result["result"][0]["count"] > result["result"][4]["count"]
    import pprint
    pprint.pprint(result)

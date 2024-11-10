#!/usr/bin/env python3
""" Insert document in Pyhton """


def insert_school(mongo_collection, **kwargs):
    """ insert document in a mango collection based on kwargs"""
    result = mongo_collection.insert_one(kwargs);
    return result.inserted_id;

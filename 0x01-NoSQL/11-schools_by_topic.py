#!/usr/bin/env python3
""" Where can I learn Pyhton? """


def schools_by_topic(mongo_collection, topic):
    """ return list of collection with specific topics """
    return list(mongo_collection.find({ "topics": topic }));

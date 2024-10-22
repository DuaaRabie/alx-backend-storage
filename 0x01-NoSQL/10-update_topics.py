#!/usr/bin/env python3
""" Change school topics"""


def update_topics(mongo_collection, name, topics):
    """ updaet topics """
    mongo_collection.update(
            { "name": name },
            { "$set": { "topics": topics } }
            );

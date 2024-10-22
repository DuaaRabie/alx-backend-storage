#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mango_collection):
    """ list all mango collection documents """
    return list(mango_collection.find());

# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""


class Photo(object):

    def __init__(self, id, orientation, tags: set):
        self.Id = id
        self.Orientation = orientation
        self.Tags = tags

    def __eq__(self, other):
        if isinstance(other, Photo):
            return other.Id == self.Id
        return NotImplemented

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "{}{}".format(self.Id, self.Orientation)

    def __iter__(self):
        return iter(self.Tags)


class Slide:

    def __init__(self, photos: list[Photo]):
        self.Photos = photos

    def __str__(self):
        return str(self.Photos)


## testing with inverted index.
def fill_index(index: dict[int, set], db: dict):
    # index =  {tag: list[photo]}
    # db = {photo: list[tags]}
    for id in db:
        add_to_index(id, db[id], index)


def add_to_index(id, tags, index):
    for t in tags:
        if t in index:
            index[t].append(id)
        else:
            index[t] = [id]

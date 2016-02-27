#!/usr/bin/env python
# coding: utf-8


class Completion(object):
    def __init__(self, surface, score):
        self.__surface = surface
        self.__score = score

    def __eq__(self, other):
        pass

    @property
    def surface(self):
        return self.__surface

    @property
    def score(self):
        return self.__score

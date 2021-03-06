#!/usr/bin/env python
# coding: utf-8


class Segment(object):
    def __init__(self, surface, headless, tailless):
        self.__surface = surface
        self.__headless = headless
        self.__tailless = tailless

    def __eq__(self, other):
        if type(self) is not type(other):
            return False

        return (
            self.is_tailless == other.is_tailless and
            self.is_headless == other.is_headless and
            self.surface == other.surface
        )

    def __repr__(self):
        return '<{} {}{!s}{}>'.format(
            type(self).__name__,
            '...' if self.is_headless else '',
            self.surface,
            '...' if self.is_tailless else '',
        )

    @property
    def surface(self):
        return self.__surface

    @property
    def is_headless(self):
        return self.__headless

    @property
    def is_tailless(self):
        return self.__tailless

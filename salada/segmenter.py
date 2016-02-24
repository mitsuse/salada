#!/usr/bin/env python
# coding: utf-8


class Default(object):
    def __init__(self):
        import re

        self.__pattern = re.compile('\s+')

    def segment(self, text):
        from salada import language

        sequence = self.__pattern.split(text)
        last_index = len(sequence) - 1

        segments = [
            language.Segment(
                s, i == 0, i == last_index,
            ) for i, s in enumerate(sequence)
        ]

        return segments

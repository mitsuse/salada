#!/usr/bin/env python
# coding: utf-8

from mprpc import RPCServer


class Service(RPCServer):
    '''
    `Service` is MessagePack-RPC service for K-best word completion
    '''

    def __init__(self, segmenter, completer):
        super(Service, self).__init__()

        self.__segmenter = segmenter
        self.__completer = completer

    def segment(self, text):
        '''
        `segment` the given `text` into words by using `segmenter`.
        '''
        return

    def complete(self, context, prefix):
        '''
        `complete` the next word starting with `prefix` by using `context`.
        '''
        return

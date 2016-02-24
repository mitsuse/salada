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

        from salada.rpc.response import encode_segment

        segments = self.__segmenter.segment(text)
        response = [encode_segment(s) for s in segments]

        return response

    def complete(self, context, prefix):
        '''
        `complete` the next word starting with `prefix` by using `context`.
        '''

        from salada.rpc.response import encode_completion

        completions = self.__completer.complete(context, prefix)
        response = [encode_completion(c) for c in completions]

        return response

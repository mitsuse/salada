#!/usr/bin/env python
# coding: utf-8

import mprpc as __mprpc


class Service(__mprpc.RPCServer):
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

        segments = self.__segmenter.segment(text)
        response = [encode_segment(s) for s in segments]

        return response

    def complete(self, context, prefix):
        '''
        `complete` the next word starting with `prefix` by using `context`.
        '''

        completions = self.__completer.complete(context, prefix)
        response = [encode_completion(c) for c in completions]

        return response


class Client(object):
    def __init__(self, port):
        self.__port = port

    def segment(self, text):
        from mprpc import RPCClient

        client = RPCClient('localhost', self.__port)
        response = client.call('segment', text)

        return [decode_segment(r) for r in response]

    def complete(self, context, prefix):
        from mprpc import RPCClient

        client = RPCClient('localhost', self.__port)
        response = client.call('complete', context, prefix)

        return [decode_completion(r) for r in response]


def encode_segment(segment):
    encoded = {
        'surface': segment.surface,
        'is_headless': segment.is_headless,
        'is_tailless': segment.is_tailless,
    }
    return encoded


def encode_completion(completion):
    encoded = {
        'candidate': completion.candidate,
        'score': completion.score,
    }
    return encoded


def decode_segment(segment):
    from salada import language
    return language.Segment(
        segment['surface'],
        segment['is_headless'],
        segment['is_tailless'],
    )


def decode_completion(segment):
    # TODO: Implement.
    pass


class DecodeError(object):
    def __init__(self):
        pass

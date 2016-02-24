#!/usr/bin/env python
# coding: utf-8


class MockSegmenter(object):
    def __init__(self, result):
        self.__result = result

    def segment(self, text):
        return self.__result


class TestService:
    def test_segment_text_by_using_the_given_segmenter(self):
        from salada import language
        from salada import rpc

        segments = [
            language.Segment('foo', True, False),
            language.Segment('bar', False, False),
            language.Segment('baz', False, True),
        ]
        service = rpc.Service(
            MockSegmenter(segments),
            None,
        )

        expectation = [
            {'surface': 'foo', 'is_headless': True, 'is_tailless': False},
            {'surface': 'bar', 'is_headless': False, 'is_tailless': False},
            {'surface': 'baz', 'is_headless': False, 'is_tailless': True},
        ]
        result = service.segment('')

        assert result == expectation

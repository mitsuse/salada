#!/usr/bin/env python
# coding: utf-8

from salada import language
from salada import segmenter


class TestDefault:
    def test_segment_text_by_sequence_of_spaces(self):
        text = '    foo \n \n\n   bar \t\n baz  '
        expectation = [
            language.Segment('', True, False),
            language.Segment('foo', False, False),
            language.Segment('bar', False, False),
            language.Segment('baz', False, False),
            language.Segment('', False, True),
        ]
        result = segmenter.Default().segment(text)
        assert result == expectation

    def test_regard_first_as_headless(self):
        text = 'foo \n \n\n   bar \t\n baz  '
        expectation = [
            language.Segment('foo', True, False),
            language.Segment('bar', False, False),
            language.Segment('baz', False, False),
            language.Segment('', False, True),
        ]
        result = segmenter.Default().segment(text)
        assert result == expectation

    def test_regard_last_as_tailless(self):
        text = '    foo \n \n\n   bar \t\n baz'
        expectation = [
            language.Segment('', True, False),
            language.Segment('foo', False, False),
            language.Segment('bar', False, False),
            language.Segment('baz', False, True),
        ]
        result = segmenter.Default().segment(text)
        assert result == expectation

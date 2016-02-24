#!/usr/bin/env python
# coding: utf-8

from salada import language
from salada import segmenter


def test_default_segment():
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


def test_default_segment_first_headless():
    text = 'foo \n \n\n   bar \t\n baz  '
    expectation = [
        language.Segment('foo', True, False),
        language.Segment('bar', False, False),
        language.Segment('baz', False, False),
        language.Segment('', False, True),
    ]
    result = segmenter.Default().segment(text)
    assert result == expectation


def test_default_segment_last_tailless():
    text = '    foo \n \n\n   bar \t\n baz'
    expectation = [
        language.Segment('', True, False),
        language.Segment('foo', False, False),
        language.Segment('bar', False, False),
        language.Segment('baz', False, True),
    ]
    result = segmenter.Default().segment(text)
    assert result == expectation

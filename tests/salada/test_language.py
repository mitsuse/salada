#!/usr/bin/env python
# coding: utf-8

from salada import language


def test_segument_equality():
    a = language.Segment('foo', True, False)
    b = language.Segment('foo', True, False)
    assert a == b and b == a


def test_segument_equality_different_surface():
    a = language.Segment('foo', True, False)
    b = language.Segment('bar', True, False)
    assert a != b and b != a


def test_segument_equality_different_head_status():
    a = language.Segment('foo', False, False)
    b = language.Segment('foo', True, False)
    assert a != b and b != a


def test_segument_equality_different_tail_status():
    a = language.Segment('foo', True, False)
    b = language.Segment('foo', True, True)
    assert a != b and b != a


def test_segument_equality_different_type():
    a = language.Segment('foo', True, False)
    b = 1
    assert a != b and b != a

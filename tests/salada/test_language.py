#!/usr/bin/env python
# coding: utf-8

from salada import language


class TestSegment:
    def equals_to_other_which_has_same_proporties(self):
        a = language.Segment('foo', True, False)
        b = language.Segment('foo', True, False)
        assert a == b and b == a

    def test_doesnt_equal_to_other_which_has_different_surface(self):
        a = language.Segment('foo', True, False)
        b = language.Segment('bar', True, False)
        assert a != b and b != a

    def test_doesnt_equal_to_other_which_is_headless_unexpectedly(self):
        a = language.Segment('foo', False, False)
        b = language.Segment('foo', True, False)
        assert a != b and b != a

    def test_doesnt_equal_to_other_which_is_tailless_unexpectedly(self):
        a = language.Segment('foo', True, False)
        b = language.Segment('foo', True, True)
        assert a != b and b != a

    def test_doesnt_equal_to_a_value_of_other_type(self):
        a = language.Segment('foo', True, False)
        b = 1
        assert a != b and b != a

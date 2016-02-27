#!/usr/bin/env python
# coding: utf-8

from salada import completer


class TestCompletion:
    def equals_to_other_which_has_same_proporties(self):
        a = completer.Completion('foo', 10)
        b = completer.Completion('foo', 10)
        assert a == b and b == a

    def test_doesnt_equal_to_other_which_has_different_surface(self):
        a = completer.Completion('foo', 10)
        b = completer.Completion('bar', 10)
        assert a != b and b != a

    def test_doesnt_equal_to_other_which_has_different_score(self):
        a = completer.Completion('foo', 20)
        b = completer.Completion('foo', 10)
        assert a != b and b != a

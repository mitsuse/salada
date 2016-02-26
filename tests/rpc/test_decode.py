#!/usr/bin/env python
# coding: utf-8


class TestDecodeSegment:
    def test_convert_a_dictionary_to_an_instance_of_segment(self):
        from salada import language
        from salada import rpc
        expectation = language.Segment('foo', True, False)
        result = rpc.decode_segment(rpc.encode_segment(expectation))
        assert result == expectation

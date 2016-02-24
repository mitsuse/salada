#!/usr/bin/env python
# coding: utf-8


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

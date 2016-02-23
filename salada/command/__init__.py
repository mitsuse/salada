#!/usr/bin/env python
# coding: utf-8

import click


@click.group()
def main():
    pass


@main.command()
def gather():
    '''Extract comments from the given source files.'''


@main.command()
def prepare():
    '''Segment strings into tokens'''


@main.command()
def build():
    '''Construct a prediction model and save it.'''


@main.command()
def serve():
    '''Launch a K-best word completion server.'''


@main.command()
def request():
    '''Predict next words with the given prefix.'''


if __name__ == '__main__':
    main()

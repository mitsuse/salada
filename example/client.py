#!/usr/bin/env python
# coding: utf-8

import click


@click.group()
def main():
    pass


@main.command()
def segment():
    '''Send request for word segmentation.'''


@main.command()
def complete():
    '''Send request for word completion.'''


if __name__ == '__main__':
    main()

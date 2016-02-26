#!/usr/bin/env python
# coding: utf-8

import click


@click.group()
def main():
    pass


@main.command()
@click.option(
    '--port', type=int,
    default=9000, show_default=True,
    help='The port number used by the server.',
)
@click.option(
    '--text', type=str, required=True,
    help='The input string to be segmented.',
)
def segment(port, text):
    '''Send request for word segmentation.'''

    from salada import rpc

    client = rpc.Client(port)
    print(client.segment(text))


@main.command()
def complete():
    '''Send request for word completion.'''


if __name__ == '__main__':
    main()

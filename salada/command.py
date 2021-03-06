#!/usr/bin/env python
# coding: utf-8

import click


@click.group()
def main():
    pass


@main.command()
def prepare():
    '''Segment strings into tokens'''


@main.command()
def build():
    '''Construct a prediction model and save it.'''


@main.command()
@click.option(
    '--port', type=int,
    default=9000, show_default=True,
    help='The port number to be used by the server.',
)
def serve(port):
    '''Launch a K-best word completion server.'''

    from gevent.server import StreamServer
    from salada import rpc
    from salada import segmenter

    service = rpc.Service(
        segmenter=segmenter.Default(),
        completer=None,
    )

    server = StreamServer(('localhost', port), service)
    server.serve_forever()


if __name__ == '__main__':
    main()

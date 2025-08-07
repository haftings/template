#! /usr/bin/env python3

'''A simple Hello World style program'''

import argparse
import sys
from typing import Sequence


def hello(name: str = 'World'):
    '''Say a greeting
    
    >>> hello()
    Hello, World!

    >>> hello('John Doe')
    Hello, John Doe!
    '''
    sys.stdout.write(f'Hello, {name}!\n')


def main(args: Sequence[str] | None = None):
    '''run script'''
    # parse arguments
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('name', nargs='?', default='World', help='who to greet')
    a = p.parse_args(args)
    # say hello
    hello(a.name)

if __name__ == '__main__':
    main()

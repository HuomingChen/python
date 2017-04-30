#!/usr/bin/env python
# -*- coding:utf-8 -*-

'module'

__author__ = 'test'

import sys


def test():
    args=sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('too many args')

if __name__ == '__main__':
    test()

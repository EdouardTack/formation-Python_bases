#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""Voir https://docs.python.org/3/howto/argparse.html"""

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="This script does something.")

    # parser.add_argument('who', help='Who are you ?')
    # parser.add_argument('many', type=int)
    # parser.add_argument('-v', '--verbose') # Will fail
    # parser.add_argument('-v', '--verbose', action='store_true')
    # parser.add_argument('-o', "--output",
    #                     help="Output file name")
    #
    args = parser.parse_args()

    # if args.verbose:
    #     print('lets do it')
    #
    # if args.output:
    #     print("output file: " + args.output)
    #
    # for i in range(args.many):
    #     print("Hello " + args.who)

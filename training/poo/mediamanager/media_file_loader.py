#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import re
import os

series_re = re.compile("-s([0-9]{2})e([0-9]{2})-")

series_full_name = "Silicon_Valley-s01e03-Articles_Of_Incorporation.avi"


def get_series_value_from_file(filename):
    """
    Returns an array of data for a series. The values are
    * Series name
    * Season number
    * episode number
    * episode title
    * File type

    :param filename:
    :return:
    """
    series_file_name, series_ext = os.path.splitext(filename)

    series_match = series_re.search(series_file_name)

    if series_match:
        return [series_file_name[:series_match.start()].replace('_', ' '),
                series_match.group(1),
                series_match.group(2),
                series_file_name[series_match.end():].replace('_', ' '),
                series_ext]


def open_file(filepath):
    if os.path.exists(filepath):
        media_file = open(filepath, 'r')
        media_data = [get_series_value_from_file(media[:-1]) for media in media_file]
        media_file.close()

        return media_data


if __name__ == '__main__':

    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to the file to parse", type=str, action="store")

    args = parser.parse_args()

    if args.file:
        for media in open_file(args.file):
            print(media)
    else:
        print(get_series_value_from_file(series_full_name))

# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

from util.get_dex_file import get_dex_file


def apk_to_dex_test():
    """
    extract the apk's dex file from apk directory
    then write into dex directory
    :return:
    """
    get_dex_file('apk', 'dex')

if __name__ == '__main__':
    apk_to_dex_test()

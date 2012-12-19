#!/usr/bin/env python2

import os
from urllib import urlretrieve
from lxml.html import parse

from lib import page

def download(number):
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'searches', '%d.html' % number)
    urlretrieve(page(number), filename = filename)

if __name__ == '__main__':
    page_number = page_number_arg()
    download(page_number)
    print('Downloaded page %d' % page_number)

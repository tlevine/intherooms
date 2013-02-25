#!/usr/bin/env python2

import os
from urllib import urlretrieve
from lxml.html import parse

import lib

def download(coords, number):
    dirname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'searches-usa', '%f,%f' % coords)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    filename = os.path.join(dirname, '%d.html' % number)
    urlretrieve(lib.page(coords, number), filename = filename)

    if len(parse(filename).xpath('//span[@class="current"][text()="%d"]' % number)) > 0:
        os.rename(filename, '.last.html')
        print('I stopped at page $page. If the script worked properly, this is because.')
        print('page %d was the last page. Check .last.html to make sure.' % (number - 1))
        return False

    else:
        print(('Downloaded (%f, %f), ' % coords) + 'page %d' % number)
        return True

if __name__ == '__main__':
    for coords in lib.choose_coords():
        number = 1
        while download(coords, number):
            number += 1

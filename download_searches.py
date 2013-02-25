#!/usr/bin/env python2

import os
from urllib import urlretrieve
from lxml.html import parse

from time import sleep
from random import normalvariate

import lib

def is_last(filename):
    html = parse(filename)
    if len(html.xpath('//span[@class="current"][text()="%d"]' % number)) == 0:
        return True
    if len(html.xpath('//div[@class="error-pane"][text()="No meetings found."]')) > 0:
        return True

    return False

def get_dirname(coords):
    return os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'searches-usa', '%f,%f' % coords)

def download(coords, number):
    filename = os.path.join(get_dirname(coords), '%d.html' % number)
    urlretrieve(lib.page(coords, number), filename = filename)

    if is_last(filename):
        os.rename(filename, '.last.html')
        print('When searching for (%f, %f),' % coords)
        print('I stopped at page %d. If the script worked properly, this is because' % number)
        print('page %d was the last page or there were no meetings for this search.' % (number - 1))
        print('Check .last.html to make sure.')
        return False

    else:
        print(('Downloaded (%f, %f), ' % coords) + 'page %d' % number)
        return True

if __name__ == '__main__':
    for coords in lib.choose_coords():
        dirname = get_dirname(coords)

        # Check if the search is done, or make a directory
        if os.path.isdir(dirname):
            if os.path.isfile(os.path.join(dirname, 'done')):
                continue
        else:
            os.makedirs(dirname)

        # Skip pages that are already finished.
        pages_so_far = set(os.listdir(dirname))
        number = 1
        while ('%d.html' % number) in pages_so_far:
            number += 1

        # Run the search.
        while download(coords, number):
            print lib.page(coords, number)
            number += 1
            sleep(normalvariate(1.17,0.2))

        # Mark as done.
        open(os.path.join(dirname, 'done'), 'w').write('')

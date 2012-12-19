#!/usr/bin/env python2

import os
from urllib import urlretrieve
from lxml.html import parse

def page(number):
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=11375&proximity=125&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=40.7209975&longitude=-73.8477874&process=1&page_city=Ridgewood&page_state=NY&page=1&results_per_page=25&page=%d' % number

def download(number):
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'searches', '%d.html' % number)
    urlretrieve(page(number), filename = filename)

if __name__ == '__main__':
    import sys
    page_number = int(sys.argv[1])
    if page_number < 0 or page_number > 400:
        raise ValueError('Page number should probably be between 0 and 400.')
    download(page_number)
    print('Downloaded page %d' % page_number)

#!/usr/bin/env python2
'General helpers'

def page_ny(number):
    # New York
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=11375&proximity=125&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=40.7209975&longitude=-73.8477874&process=1&page_city=Ridgewood&page_state=NY&page=1&results_per_page=25&page=%d' % number

def page(number):
    # San Francisco
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=94102&proximity=400&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=37.7786871&longitude=-122.4212424&process=1&page_city=Belmont&page_state=CA&page=1&results_per_page=25&page=' % number

def _id(url):
    'Convert a url into an id.'
    return int(url.split('/')[-1])

def page_number_arg():
    import sys
    page_number = int(sys.argv[1])
    if page_number < 0 or page_number > 400:
        raise ValueError('Page number should probably be between 0 and 400.')
    return page_number

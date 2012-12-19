#!/usr/bin/env python2
'General helpers'

def page(number):
    'The url for a page'
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=11375&proximity=125&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=40.7209975&longitude=-73.8477874&process=1&page_city=Ridgewood&page_state=NY&page=1&results_per_page=25&page=%d' % number

def page_number_arg():
    import sys
    page_number = int(sys.argv[1])
    if page_number < 0 or page_number > 400:
        raise ValueError('Page number should probably be between 0 and 400.')

#!/usr/bin/env python2
'General helpers'

def page_ny(number):
    # New York
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=11375&proximity=125&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=40.7209975&longitude=-73.8477874&process=1&page_city=Ridgewood&page_state=NY&page=1&results_per_page=25&page=%d' % number

def page(number):
    # San Francisco
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=94102&proximity=400&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=37.7786871&longitude=-122.4212424&process=1&page_city=Belmont&page_state=CA&page=1&results_per_page=25&page=%d' % number

def _id(url):
    'Convert a url into an id.'
    return int(url.split('/')[-1])

def page_number_arg():
    import sys
    page_number = int(sys.argv[1])
    if page_number < 0 or page_number > 400:
        raise ValueError('Page number should probably be between 0 and 400.')
    return page_number

def translate(coords, direction, R = 3961, d = 150)
    '''
    Move a longitude, latitude pair by 150 miles north, south, east or west.
    This only works for the northwest quarter of the planet.
    '''
    if direction not in 'NSEW':
        raise ValueError('direction must be one of "N", "S", "E" or "W".')

    lon1, lat1 = coords
    dx, dy = {
        'N': ( 0, 1),
        'S': ( 0,-1),
        'E': ( 1, 0),
        'W': (-1, 0)
    }[direction]

    dlon = d * dx / R
    dlat = d * dx / R

    return (lon1 + dlon, lat1 + dlat)

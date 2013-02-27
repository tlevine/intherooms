#!/usr/bin/env python2
'General helpers'
import re
import math

def page_ny(number):
    # New York
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=11375&proximity=125&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=40.7209975&longitude=-73.8477874&process=1&page_city=Ridgewood&page_state=NY&page=1&results_per_page=25&page=%d' % number

def page_sf(number):
    # San Francisco
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&zip=94102&proximity=400&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=37.7786871&longitude=-122.4212424&process=1&page_city=Belmont&page_state=CA&page=1&results_per_page=25&page=%d' % number

def page(coords, number):
    lon, lat = coords
    return 'http://meetings.intherooms.com/meetings/search?search=&fellowship=&proximity=150&day=&start_hour=1&start_min=00&start_am_pm=AM&end_hour=1&end_min=00&end_am_pm=AM&latitude=%f&longitude=%f&process=1&page_city=&page_state=&results_per_page=25&page=%d' % (lat, lon, number)

def _id(url):
    'Convert a url into an id.'
    return int(url.split('/')[-1])

def search_args():
    import sys
    dirname = sys.argv[1]
    lon, lat = map(float, dirname.split(','))
    page_number = int(sys.argv[2])

    if page_number < 0 or page_number > 400:
        raise ValueError('Page number should probably be between 0 and 400.')
    elif lon < -125 or lon > -60:
        raise ValueError('Longitude should probably be between -125 and -60.')
    elif lat < 20 or lat > 55:
        raise ValueError('Latitude should probably be between 20 and 55.')

    return dirname, page_number

def choose_coords():
    'Choose coordinates spanning the US that are about 150 miles apart.'
    d_lat = 2.16
    def d_lon(lat):
        if lat > 42:
            return 3
        elif lat > 30:
            return 2.5
        else:
            return 2.25

    lon_min = -122 # Seattle, WA
    lon_max =  -68 # Caribou, ME
    lat_min =   25 # Homestead, FL
    lat_max =   47 # Seattle, WA


    def lat(so_far = []):
        if so_far == []:
            return lat(so_far = [lat_min])
        elif so_far[-1] > lat_max:
            return so_far
        else:
            return lat(so_far = so_far + [round(so_far[-1] + d_lat, 2)])

    def lon(lat, so_far = []):
        if so_far == []:
            return lon(lat, so_far = [lon_min])
        elif so_far[-1] > lon_max:
            return so_far
        else:
            return lon(lat, so_far = so_far + [round(so_far[-1] + d_lon(lat), 2)])

    coords = []
    for _lat in lat():
        for _lon in lon(_lat):
            coords.append((_lon, _lat))

    return coords

PHONE = re.compile(r'.*1?[^0-9]?([0-9]{3})[^0-9]?([0-9]{3})[^0-9]?([0-9]{4}).*')
def meeting_description(row):
    if not row['Meeting Description']:
        return row

    # Number of colons
    ncolon = len(filter(lambda x: ':' in x, row['Meeting Description']))

    # Remove newlines
    desc = row['Meeting Description'].replace('\r', ' ').replace('\n', ' ')

    # Reset
    row['Details'] = row['Format'] = row['Language'] = row['Phone'] = ''

    phone = re.match(PHONE, desc)
    if phone:
        row['Phone'] = phone.group(1) + phone.group(2) + phone.group(3)
    elif len(filter(lambda c: c in '1234567890', desc)) >= 4:
        # Print it if it has four digits but wasn't matched.
        print row

    m3 = re.match(r'^Details: (.*)Format: (.*)Language: (.*)$', desc)
    m2 = re.match(r'^Details: (.*)(Format|Language): (.*)$', desc)
    m1 = re.match(r'^Details: (.*)$', desc)
    mweird = re.match(r'^Details: (.*)[fF]ormat:(.*)$', desc)
    if m3:
        row['Details'] = m3.group(1)
        row['Format'] = m3.group(2)
        row['Language'] = m3.group(3)
    elif m2:
        row['Details'] = m2.group(1)
        row[m2.group(2)] = m2.group(3)
    elif ncolon == 1 and m1:
        row['Details'] = m1.group(1)
    elif mweird:
        row['Details'] = mweird.group(1)
        row['Format'] = mweird.group(2)
    else:
        print desc
        assert False

    return row

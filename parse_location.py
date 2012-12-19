#!/usr/bin/env python2

import os
import re

import lxml.html
import dumptruck

from lib import _id

COORDS = re.compile(r'var startPoint = new google.maps.LatLng\(([0-9.]+), (-[0-9.]+)\);')

def coords(html_source):
    'Pick the latitude and longitude out of the text html source.'
    lng, lat= map(float, re.findall(COORDS, html_source)[0])
    return {
        "Longitude": lng,
        "Latitude": lat
    }

def description(html):
    return html.cssselect('#meeting-description address')[0].text_content()

def main():
    import sys
    if len(sys.argv) != 2:
        print("USAGE: %d [location page url]" % sys.argv[0])
        exit(1)

    url = sys.argv[1]

    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'locations', '%d.html' % _id(url))
    dt = dumptruck.DumpTruck(
        dbname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'intherooms.db'),
        adapt_and_convert = True
    )

    source = open(filename).read()
    html = lxml.html.parse(filename).getroot()

    data = {
        'Url': url,
    }
    data.update(coords(source))
    data['Meeting Description'] = description(html)
    print data

if __name__ == '__main__':
    main()

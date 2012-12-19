import os
import re

import lxml.html
import dumptruck

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
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'locations', _id(sys.argv[1]))

    dt = dumptruck.DumpTruck(
        dbname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'intherooms.db'),
        adapt_and_convert = True
    )

    source = open(filename).read()
    html = lxml.html.parse(filename).getroot()

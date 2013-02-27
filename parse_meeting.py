#!/usr/bin/env python2
import os
import dumptruck
import lxml.html

from lib import _id

def meeting_info(html):
    return html.cssselect('#meeting-description h3')[0].text_content()

def main():
    import sys
    url = sys.argv[1]
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'meetings', '%d.html' % _id(url))
    dt = dumptruck.DumpTruck(
        dbname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'intherooms.db'),
        adapt_and_convert = True
    )
    html = lxml.html.parse(filename).getroot()
    data = {
        'Url': url,
        'Meeting Description': meeting_info(html),
    }
    data = meeting_description(data)
    dt.insert(data, 'meeting_info')

if __name__ == '__main__':
    main()

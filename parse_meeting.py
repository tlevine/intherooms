#!/usr/bin/env python2
import os
import dumptruck
import lxml.html

from lib import _id, meeting_description

def meeting_info(html):
    h3s = html.cssselect('#meeting-description h3')
    if len(h3s) == 0:
        return ''
    else:
        return h3s[0].text_content()

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

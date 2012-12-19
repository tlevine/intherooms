import os
import dumptruck
import lxml.html

from lib import _id

def meeting_info(html):
    return html.cssselect('#meeting-description h3')[0].text_content()

def main():
    import sys
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'meetings', '%d.html' % _id(sys.argv[1]))
    dt = dumptruck.DumpTruck(
        dbname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'intherooms.db'),
        adapt_and_convert = True
    )
    html = lxml.html.parse(filename).getroot()
    data = meeting_info(html)
    dt.insert(data, 'meeting_info')

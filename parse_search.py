#!/usr/bin/env python2
from lxml.html import parse
import datetime

from lib import page, search_args

def is_valid_page(html):
    error_text = [error_pane.text_content() for error_pane in html.cssselect('.error-pane')]
    is_valid = [] == filter(None, error_text)
    return is_valid

def has_correct_page_number(html, page_number):
    observed_page_numbers = set(map(int, html.xpath('//span[@class="current"]/text()')))
    return observed_page_numbers == {page_number}

MANUAL_TIMES = [
    ('1:60 AM', '2:00 AM'),
    ('6:OO PM', '6:00 PM'),
]
def table_data(html):
    trs = html.cssselect('.all-meetings tr')
    tr_head = trs[0]
    trs_body = trs[1:]

    keys = map(unicode, tr_head.xpath('th/text()'))

    data = []
    for tr in trs_body:
        values = [td.text_content() for td in tr.cssselect('td')]
        values[2] = '\n'.join(tr.xpath('td[position()=3]/text()')).replace('  ', ' ')

        rowdata = dict(zip(keys, values))
        rowdata['Meeting Title Link'] = tr.xpath('td[position()=1]/a/@href')[0].replace('\n', '')
        rowdata['Location Link'] = tr.xpath('td[position()=2]/a/@href')[0].replace('\n', '')

        for orig, changed in MANUAL_TIMES:
            if rowdata['Time'] == orig:
                rowdata['Time'] = changed

        if 'unknown' == rowdata['Time']:
            rowdata['Time'] = ''
        elif ':' in rowdata['Time']:
            _t = rowdata['Time'].replace('Np', '00').replace('Mp', '00')
            rowdata['Time'] = datetime.datetime.strptime(
                _t, '%I:%M %p'
            ).strftime('%H:%M')
        else:
            rowdata['Time'] = datetime.datetime.strptime(
                rowdata['Time'] + ' pm', '%I%M %p'
            ).strftime('%H:%M')
        data.append(rowdata)
    return data

def main_json():
    import json
    url = page(*search_args())
    html = lxml.html.parse(url)
    data = table_data(html)
    print(json.dumps(data))

def main_sqlite():
    import os
    import dumptruck
    import lxml.html
    dt = dumptruck.DumpTruck(
        dbname = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'intherooms.db'),
        adapt_and_convert = True
    )
    dirname, n = search_args()
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'searches-usa', dirname, '%d.html' % n)
    html = lxml.html.parse(filename).getroot()
    data = table_data(html)
    for row in data:
        row['Search Longitude'], row['Search Latitude'] = dirname.split(',')
        row['Search Page'] = n
    dt.upsert(data, 'meeting_search')
    print('Parsed (%s) page %d' % (dirname, n))

if __name__ == '__main__':
    main_sqlite()

#!/usr/bin/env python2
from lxml.html import parse

from lib import page, page_number_arg

def is_valid_page(html):
    error_text = [error_pane.text_content() for error_pane in html.cssselect('.error-pane')]
    is_valid = [] == filter(None, error_text)
    return is_valid

def has_correct_page_number(html, page_number):
    observed_page_numbers = set(map(int, html.xpath('//span[@class="current"]/text()')))
    return observed_page_numbers == {page_number}

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
        rowdata['Meeting Title Link'] = tr.xpath('td[position()=1]/a/@href')[0]
        rowdata['Location Link'] = tr.xpath('td[position()=2]/a/@href')[0]
        data.append(rowdata)
    return data

def main_json():
    import json
    url = page(page_number_arg())
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
    n = page_number_arg()
    filename = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'searches', '%d.html' % n)
    html = lxml.html.parse(filename).getroot()
    data = table_data(html)
    dt.insert(data, 'meeting_search')
    print('Parsed page %d' % n)

if __name__ == '__main__':
    main_sqlite()

#!/usr/bin/env python2
from lxml.html import parse
from collections import OrderedDict

from lib import page_number, page_number_arg

def is_valid_page(html):
    error_text = [error_pane.text_content() for error_pane in html.cssselect('.error-pane')]
    is_valid = [] == filter(None, error_text)
    return is_valid

def has_correct_page_number(html, page_number):
    observed_page_numbers = set(map(int, html.xpath('//span[@class="current"]/text()')))
    return observed_page_numbers == {page_number}

def table_data(html):
    trs = html.cssselect('.all-meetings tr')
    tr_head = trs[1]
    trs_body = trs[1:]

    keys = tr_head.xpath('th/text()')

    data = []
    for tr in trs_body:
        values = [td.text_content for td in tr.cssselect('td')]
        rowdata = OrderedDict(zip(keys, values))
        rowdata['Meeting Title Link'] = tr.xpath('td[position()=1]/a/@href')
        rowdata['Location Link'] = tr.xpath('td[position()=2]/a/@href')
        data.append(rowdata)
    return data

if __name__ == '__main__':
    import json
    url = page(page_number_arg())
    html = lxml.html.parse(url)
    data = table_data(html)
    print(json.dumps(data))

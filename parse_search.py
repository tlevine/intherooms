#!/usr/bin/env python2
from lxml.html import parse

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

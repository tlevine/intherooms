#!/usr/bin/env python2
from lxml.html import parse

def is_valid_page(html):
    error_text = [error_pane.text_content() for error_pane in html.cssselect('.error-pane')]
    is_valid = [] == filter(None, error_text)
    return is_valid

def has_correct_page_number(html, page_number):
    observed_page_numbers = set(map(int, html.xpath('//span[@class="current"]/text()')))
    return observed_page_numbers == {page_number}

#!/usr/bin/env python2

import os
import csv

from lxml.html import parse
import nose.tools as n

from parse_search import is_valid_page, has_correct_page_number, table_data

FIXTURES = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'fixtures')

class TestParseSearch:
    def test_bad_page_should_be_identified(self):
        'A page that does not have results should be marked accordingly.'
        html = parse(os.path.join(FIXTURES, 'search-319.html')).getroot()
        n.assert_false(is_valid_page(html))
    def test_good_page_should_be_identified(self):
        'A page that does have results should be marked accordingly.'
        html = parse(os.path.join(FIXTURES, 'search-237.html')).getroot()
        n.assert_true(is_valid_page(html))
    def test_page_number_matcher_should_work(self):
        'We should be able to tell whether the page corresponds to a given page number.'
        html = parse(os.path.join(FIXTURES, 'search-237.html')).getroot()
        n.assert_true(has_correct_page_number(html, 237))
        n.assert_false(has_correct_page_number(html, 8))
    def test_data_should_match(self):
        'Automatically parsed data should match our manual parse.'
        html = parse(os.path.join(FIXTURES, 'search-237.html')).getroot()
        f = open(os.path.join(FIXTURES, 'search-237.csv'))

        expected = list(csv.DictReader(f))
        observed = table_data(html)

        if len(observed) == len(expected):
            # Pretty printing
            for o, e in zip(observed, expected):
                print o
                n.assert_dict_equal(o, e)
        else:
            # Ugly printing
            n.assert_list_equal(observed, expected)

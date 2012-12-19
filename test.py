import os
from lxml.html import parse
import nose.tools as n

from parse_search import is_valid_page, has_correct_page_number

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
        html = parse(os.path.join(FIXTURES, 'search-237.html')).getroot()
        n.assert_true(has_correct_page_number(html, 237))
        n.assert_false(has_correct_page_number(html, 8))

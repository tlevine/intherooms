import os
from lxml.html import parse
import nose.tools as n

from parse_search import is_valid_page

FIXTURES = os.path.join(os.environ['IN_THE_ROOMS_ROOT'], 'fixtures')

class TestParseSearch:
    def test_bad_page_should_be_identified(self):
        'A page that does not have results should be marked accordingly.'
        html = parse(os.path.join(FIXTURES, 'search-319.html'))
        n.assert_false(is_valid_page(html))
    def test_bad_page_should_be_identified(self):
        'A page that does have results should be marked accordingly.'
        html = parse(os.path.join(FIXTURES, 'search-237.html'))
        n.assert_true(is_valid_page(html))

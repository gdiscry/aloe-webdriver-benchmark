# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os.path
from urllib import pathname2url
from urlparse import urlunsplit

from features import USE_LETTUCE

if USE_LETTUCE:
    from lettuce import step
    from lettuce_webdriver.webdriver import visit
else:
    from aloe import step
    from aloe_webdriver import visit


@step('I am on the test page')
def on_test_page(self):
    test_page = os.path.join(
        os.path.dirname(os.path.normpath(__file__)),
        'test.html',
    )
    test_page_url = urlunsplit(('file', '', pathname2url(test_page), '', ''))
    visit(self, test_page_url)

# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

USE_LETTUCE = os.environ.get('LETTUCE', 0)
try:
    USE_LETTUCE = int(USE_LETTUCE)
except ValueError:
    USE_LETTUCE = 0

USE_FIREFOX = os.environ.get('FIREFOX', 0)
try:
    USE_FIREFOX = int(USE_FIREFOX)
except ValueError:
    USE_FIREFOX = 0

if USE_LETTUCE:
    import lettuce_webdriver.webdriver
else:
    import aloe_webdriver



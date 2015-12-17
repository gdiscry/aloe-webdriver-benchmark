# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from functools import partial
import logging
import os

from features import USE_LETTUCE

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger = logging.getLogger('selenium.webdriver.remote.remote_connection')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


if USE_LETTUCE:
    from lettuce.bin import main
    main()
else:
    from aloe import main
    main()

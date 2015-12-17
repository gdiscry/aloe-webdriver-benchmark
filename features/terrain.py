# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from selenium import webdriver

from features import USE_LETTUCE, USE_FIREFOX

if USE_LETTUCE:
    from lettuce import after, before, world
else:
    from aloe import after, before, world


if USE_FIREFOX:
    WebDriver = webdriver.Firefox
else:
    WebDriver = webdriver.PhantomJS


@before.all
def before_browser(*args, **kwargs):
    world.browser = WebDriver()


@after.all
def after_browser(*args, **kwargs):
    world.browser.quit()
    del world.browser

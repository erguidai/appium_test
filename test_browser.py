#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep


class TestBrowser:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['browserName'] = 'Browser'
        desired_caps['noReset'] = "true"

        # desired_caps['dontStopAppOnReset'] = "true"
        # desired_caps['skipDeviceInitialization'] = "true"
        # desired_caps['unicodeKeyboard'] = "true"
        # desired_caps['resetKeyboard'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)
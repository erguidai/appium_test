#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:7555'
desired_caps['appPackage'] = 'com.hnr.dxxw'
desired_caps['appActivity'] = '.WelcomeActivity'
desired_caps['noReset'] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
# driver.find_element_by_id()
driver.find_element_by_xpath(
    '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextSwitcher/android.widget.TextView').click()
time.sleep(5)
driver.find_element_by_xpath('')

driver.quit()

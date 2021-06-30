#!/usr/bin/env python
# -*- coding:utf-8 -*-

# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestGupiao:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.ss.android.caijing.stock'
        desired_caps['appActivity'] = 'com.ss.android.caijing.stock.main.MainActivity'
        desired_caps['noReset'] = "true"
        desired_caps['dontStopAppOnReset'] = "true"
        desired_caps['skipDeviceInitialization'] = "true"
        desired_caps['unicodeKeyboard'] = "true"
        desired_caps['resetKeyboard'] = "true"
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
        '''
        1.打开 海豚股票
        2.点击搜索输入框
        3.向搜索框输入”阿里巴巴“
        4.在搜索结果里面选择
        5.判断股价是否大于200
        '''

    @pytest.mark.parametrize('searchkey, type, price', [('alibaba', 'BABA', 200), ('xiaomi', '01810', 10)])
    def test_search(self, searchkey, type, price):
        print("搜索测试用例")
        self.driver.find_element_by_id('com.ss.android.caijing.stock:id/iv_search').click()
        self.driver.find_element_by_id('com.ss.android.caijing.stock:id/et_input').send_keys(f'{searchkey}')
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.ss.android.caijing.stock:id/recycler_view_auto_complete']/	android.widget.LinearLayout[1]").click()
        self.driver.find_element_by_xpath(
            f"//*[@resource-id='com.ss.android.caijing.stock:id/tv_stock_code' and @text='{type}']").click()
        now_price = float(self.driver.find_element_by_id("com.ss.android.caijing.stock:id/ivt_last_price").text)
        print(now_price)
        assert now_price > price

#!/usr/bin/env python
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

    def test_search(self):
        print("搜索测试用例")
        self.driver.find_element_by_id('com.ss.android.caijing.stock:id/iv_search').click()
        self.driver.find_element_by_id('com.ss.android.caijing.stock:id/et_input').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath(
            "//*[@resource-id='com.ss.android.caijing.stock:id/tv_search_suggestion' and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath(
            "//*[@resource-id='	com.ss.android.caijing.stock:id/tv_stock_name' and @text='阿里巴巴']").click()
        price = float(self.driver.find_element_by_id("com.ss.android.caijing.stock:id/ivt_last_price").text)
        print(price)
        assert price > 200

    def test_attr(self):
        '''
        打开首页搜索框
        判断搜索框的元素是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和他的宽高
        向搜索框输入：alibaba
        如果可见，打印“搜索成功”点击，如果不见打印“搜索失败”
        '''
        element = self.driver.find_element_by_id('com.ss.android.caijing.stock:id/iv_search')
        search = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search == True:
            element.click()
            self.driver.find_element_by_id('com.ss.android.caijing.stock:id/et_input').send_keys('阿里巴巴')
            alibaba_elemenet = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.ss.android.caijing.stock:id/tv_search_suggestion' and @text='阿里巴巴']")
            alibaba_elemenet.is_enabled()
            print(alibaba_elemenet.get_attribute("displayed"))
            if alibaba_elemenet.get_attribute("displayed") is True:
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        # self.driver.find_element_by_xpath(
        #     '//android.support.v7.app.ActionBar.Tab[@content-desc="资讯"]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView').click()
        self.driver.find_element_by_xpath("//*[@class='android.support.v7.app.ActionBar$Tab' and @content-desc='资讯']")
        action = TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()  # {'width': 810, 'height': 1440, 'x': 0, 'y': 0}
        width = window_rect['width']
        height = window_rect['height']
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)
        action.press(x=406, y=y_start).wait(200).move_to(x=406, y=y_end).release().perform()

        if __name__ == '__main__':
            pytest.main()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from appium import webdriver

# com.hnr.dxxw/.WelcomeActivity

desired_cap = {
    "platformName": "android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.hnr.dxxw",
    "appActivity": ".WelcomeActivity",
    "noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(10)
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.TextSwitcher/android.widget.TextView")
el2.click()
el3 = driver.find_element_by_id("com.hnr.dxxw:id/searchtext")
el3.send_keys("高考")
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[1]")
el4.click()


# 今日头条
# desired_cap = {
#     "platformName": "android",
#     "deviceName": "127.0.0.1:7555",
#     "appPackage": "com.ss.android.article.news",
#     "appActivity": ".activity.MainActivity",
#     "noReset": True
# }
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
# driver.implicitly_wait(10)
# el1 = driver.find_element_by_id("com.ss.android.article.news:id/vb")
# el1.click()
# el1.send_keys("腾讯")
# el2 = driver.find_element_by_accessibility_id("搜索")
# el2.click()
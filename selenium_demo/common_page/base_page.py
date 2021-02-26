# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/2/26 23:29
# @Author:汤易怀
# @File  :base_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import shelve
import time

import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from util import root_dir
from util.common_log import CommonLog


class BasePage:
    """
    po基类,用于被其他page继承
    """
    base_url = ""
    log = CommonLog("BasePage").add_handle()

    def __init__(self, driver: WebDriver = None):
        """
        初始化driver
        :param driver:
        """
        if driver is None:
            self.log.info("未传入driver，即将初始化一个driver")
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
        else:
            self.log.info("已传入driver，复用该driver")
            self.driver = driver
        if self.base_url != "":
            self.log.info("发现base_url，即将打开网页")
            self.driver.get(self.base_url)
            # 使用cookie打开浏览器
            with shelve.open("../mydbs/cookies") as db:
                # coo = self.driver.get_cookies()
                # print(coo)
                # db["cookies"] = coo
                cookies = db["cookies"]
            # print(cookies)
            for cookie in cookies:
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                    continue
                self.driver.add_cookie(cookie)
            self.driver.get(self.base_url)

    def __del__(self):
        """BasePage用完，回收对象driver"""
        pass
        # self.driver.quit()

    def find(self, locator, value, element=True):
        """
        控件操作的封装
        :param locator: 定位方式
        :param value: 定位值
        :param element: 是否使用find_element
        :return:
        """
        allure.attach.file(self.get_screenshot(), f"{locator}操作截图", attachment_type=1)
        if element:
            return self.driver.find_element(locator, value)
        else:
            return self.driver.find_elements(locator, value)

    def get_screenshot(self):
        """
        截图
        :return:
        """
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        picture_url = ""
        try:
            picture_url = self.driver.get_screenshot_as_file(f"{root_dir}/log/screenshot/{picture_time}.png")
            self.log.info(f"{picture_url}：截图成功！！！")
        except BaseException as msg:
            self.log.error(msg)
        return picture_url

    def wait_for_click(self, timeout, locator):
        """
        显示等待方法封装
        :param timeout: 显示等待时间
        :param locator: touple,定位器
        :return:
        """
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
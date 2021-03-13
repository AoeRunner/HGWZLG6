# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 11:32
# @Author:汤易怀
# @File  :base_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import os
import time
from typing import List, Dict

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from appium_demo import root_dir
from appium_demo.common.log_handle import CommonLog


class BasePage:
    """
    po基类，用于被其他page继承
    """
    log = CommonLog("BasePage").add_handle()
    _error_num = 0
    _max_num = 4
    _blacklist =[]

    def __init__(self, driver: WebDriver):
        """
        初始化appium webdriver
        :param driver:
        """
        self.driver = driver

    def not_find(self, locator):
        """
        定位元素不存在
        :return:
        """
        element = self.driver.find_elements(MobileBy.XPATH, locator)
        if len(element) == 0:
            self.log.info(f"元素不存在{locator}")
            allure.attach.file(self.get_screenshot(), f"{locator}操作截图", attachment_type=1)
            assert True
        else:
            self.log.info(f"元素存在{locator}")
            allure.attach.file(self.get_screenshot(), f"{locator}操作截图", attachment_type=1)
            assert False

    def find(self, locator):
        """
        定位元素，XPATH
        :param locator: 定位值
        :return:
        """
        try:
            element = self.driver.find_element(MobileBy.XPATH, locator)
            self.log.info(f"找到元素{locator}")
            allure.attach.file(self.get_screenshot(), f"{locator}操作截图", attachment_type=1)
            self._error_num = 0
            self.driver.implicitly_wait(10)
            return element
        except Exception as e:
            self.driver.implicitly_wait(2)
            # 设置查找次数
            if self._error_num > self._max_num:
                self._error_num = 0
                self.driver.implicitly_wait(10)
                raise e
            # 每次进except 一次都执行+1操作
            self._error_num += 1
            for ele in self._blacklist:
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(locator)
            raise e

    def find_click(self, locator):
        """
        元素点击
        :param locator: 定位值
        :return:
        """
        self.find(locator).click()

    def find_send(self, locator, text):
        """
        send输入
        :param locator: 定位值
        :param text: 输入值
        :return:
        """
        self.find(locator).send_keys(text)

    def swipe_click(self, text):
        """
        滑动点击
        :param text: 点击元素
        :return:
        """
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def get_screenshot(self):
        """
        截图
        :return:
        """
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        picture_url = ""
        try:
            picture_url = self.driver.get_screenshot_as_file(f"{root_dir}/appium_demo/log/screenshot/{picture_time}.png")
            self.log.info(f"{picture_url}：截图成功！！！")
        except BaseException as msg:
            self.log.error(msg)
        return picture_url

    def parse_action(self, path, fun_name, send_data: List = ""):
        """
        解析yaml文件并进行相应操作
        :param path: yamel文件位置
        :param fun_name: 方法名
        :param send_data: 输入值，默认为空，只有进行find_send输入时才会调用
        :return:
        """
        path = os.path.join(root_dir, "appium_demo", "pages", path)
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[fun_name]
        i = -1
        for step in steps:
            i += 1
            if step["action"] == "find":
                self.find(step["locator"])
            elif step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find_send":
                content: str = step["value"]
                content = content.replace("{value}", str(send_data[i]))
                self.find_send(step["locator"], content)
            elif step["action"] == "found_click":
                content: str = step["locator"]
                content = content.replace("{value}", str(send_data[i]))
                self.find_click(content)
            elif step["action"] == "swipe_click":
                self.swipe_click(step["locator"])
            elif step["action"] == "not_find":
                self.not_find(step["locator"])
            elif step["action"] == "not_found":
                content: str = step["locator"]
                content = content.replace("{value}", str(send_data[i]))
                self.not_find(content)

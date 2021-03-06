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
from typing import List, Dict

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

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(MobileBy.XPATH, locator)

    def find_click(self, locator):
        self.find(locator).click()

    def find_send(self, locator, text):
        self.find(locator).send_keys(text)

    def swipe_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path, fun_name, send_data: List = ""):
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
                l = step["locator"]
                v = step["value"]
                content = content.replace("{value}", str(send_data[i]))
                self.find_send(step["locator"], content)
            elif step["action"] == "swipe_click":
                self.swipe_click(step["locator"])

# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 11:41
# @Author:汤易怀
# @File  :app.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium import webdriver

from appium_demo.common import caps
from appium_demo.common.log_handle import CommonLog
from appium_demo.common.parser_handle import parse_handle
from appium_demo.pages.information_page import InformationPage


class App:
    log = CommonLog("App").add_handle()

    def __init__(self):
        self.driver = None
        self.caps_args = caps
        self.start()

    def start(self):
        """
        启动app，从命令行获取参数，后期接入jenkins后可由jenkins直接入参
        :return:
        """
        self.log.info("启动应用：com.tencent.wework")
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps_args)
        # 显式等待10s
        self.driver.implicitly_wait(10)

    def goto_main(self):
        self.log.info("进入消息界面")
        print(self.driver.page_source)
        return InformationPage(self.driver)

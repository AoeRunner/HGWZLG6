# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 12:24
# @Author:汤易怀
# @File  :test_base_case.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.app import App
from appium_demo.common.log_handle import CommonLog
from appium_demo.common.logcat_handle import logcat_handle


class TestBaseCase:
    log = CommonLog("TestBaseCase").add_handle()

    def setup_class(self):
        self.log.info("========setup_class===========")

    def setup(self):
        self.log.info("========setup=================")
        logcat_handle.start_write_logcat()
        self.app = App()

    def teardown(self):
        self.log.info("========teardown==============")
        logcat_handle.stop_write_logcat()
        pass

    def teardown_class(self):
        self.log.info("========teardown_class========")
        pass

    def generate_report(self):
        pass

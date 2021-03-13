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
from appium_demo.common.performance_handle import performance_handle


class TestBaseCase:
    """
    测试用例基类，用例被测试用例类继承
    """
    log = CommonLog("TestBaseCase").add_handle()

    def setup_class(self):
        """
        所有测试用例执行前的操作
        :return:
        """
        self.log.info("========setup_class===========")

    def setup(self):
        """
        单个用例执行钱的操作
        :return:
        """
        self.log.info("========setup=================")
        logcat_handle.start_write_logcat()
        performance_handle.start_preformance()
        self.app = App()

    def teardown(self):
        """
        单个测试用例执行后的操作
        :return:
        """
        self.log.info("========teardown==============")
        logcat_handle.stop_write_logcat()
        performance_handle.start_preformance()

    def teardown_class(self):
        """
        所有测试用例执行后的操作
        :return:
        """
        self.log.info("========teardown_class========")
        pass

    def generate_report(self):
        pass

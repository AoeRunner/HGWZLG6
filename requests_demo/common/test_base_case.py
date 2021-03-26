# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/27 0:30
# @Author:汤易怀
# @File  :test_base_case.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from util.common_log import CommonLog


class TestBaseCase:
    """
    测试用例基类，用例被测试用例类继承
    """
    log = CommonLog("TestBaseCase").add_handle()

    @classmethod
    def setup_class(cls):
        """
        所有测试用例执行前的操作
        :return:
        """
        cls.log.info("========setup_class===========")

    def setup(self):
        """
        单个用例执行钱的操作
        :return:
        """
        self.log.info("========setup=================")

    def teardown(self):
        """
        单个测试用例执行后的操作
        :return:
        """
        self.log.info("========teardown==============")

    @classmethod
    def teardown_class(cls):
        """
        所有测试用例执行后的操作
        :return:
        """
        cls.log.info("========teardown_class========")
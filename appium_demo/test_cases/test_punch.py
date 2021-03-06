# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 12:33
# @Author:汤易怀
# @File  :test_punch.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.test_base_case import TestBaseCase


class TestPunch(TestBaseCase):

    def test_punch_in_work(self):
        self.app.goto_main().goto_work_page().goto_punch_page().punch_in_work()

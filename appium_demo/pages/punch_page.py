# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 12:17
# @Author:汤易怀
# @File  :punch_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.base_page import BasePage


class PunchPage(BasePage):
    """
    打卡界面
    """

    def punch_in_work(self):
        self.log.info("开始上下班打卡")
        self.parse_action("punch_page.yaml", "punch_in_work")

    def punch_out_work(self):
        self.log.info("开始外出打卡")
        self.parse_action("punch_page.yaml", "punch_out_work")
# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 12:12
# @Author:汤易怀
# @File  :work_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.base_page import BasePage
from appium_demo.pages.punch_page import PunchPage


class WorkPage(BasePage):
    """
    工作台界面
    """

    def goto_punch_page(self):
        self.log.info("进入打卡界面")
        self.parse_action("work_page.yaml", "goto_punch_page")
        return PunchPage(self.driver)
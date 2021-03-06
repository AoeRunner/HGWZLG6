# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 17:46
# @Author:汤易怀
# @File  :add_member_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.base_page import BasePage
from appium_demo.pages.add_manually_page import AddManuallyPage


class AddMemberPage(BasePage):
    """
    添加成员界面
    """
    def goto_add_manually_page(self):
        self.log.info("进入手动添加界面")
        self.parse_action("add_member_page.yaml", "goto_add_manually_page")
        return AddManuallyPage(self.driver)
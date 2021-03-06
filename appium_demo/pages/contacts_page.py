# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 17:04
# @Author:汤易怀
# @File  :contacts_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.base_page import BasePage
from appium_demo.pages.add_member_page import AddMemberPage


class ContactsPage(BasePage):
    """
    通讯录界面
    """

    def goto_add_member_page(self):
        self.log.info("进入添加成员界面")
        self.parse_action("contacts_page.yaml", "goto_add_member_page")
        return AddMemberPage(self.driver)

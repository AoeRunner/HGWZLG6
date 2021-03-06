# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 12:07
# @Author:汤易怀
# @File  :information_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.base_page import BasePage
from appium_demo.pages.contacts_page import ContactsPage
from appium_demo.pages.work_page import WorkPage


class InformationPage(BasePage):
    """
    消息界面
    """

    def goto_work_page(self):
        self.log.info("进入工作台界面")
        self.parse_action("information_page.yaml", "goto_work_page")
        return WorkPage(self.driver)

    def goto_contacts_page(self):
        self.log.info("进入通讯录界面")
        self.parse_action("information_page.yaml", "goto_contacts_page")
        return ContactsPage(self.driver)

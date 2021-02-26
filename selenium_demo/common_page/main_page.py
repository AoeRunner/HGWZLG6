# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/2/27 0:17
# @Author:汤易怀
# @File  :main_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from selenium.webdriver.common.by import By

from selenium_demo.common_page.add_member_page import AddMemberPage
from selenium_demo.common_page.base_page import BasePage


class MainPage(BasePage):
    """
    首页
    """
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member_page(self):
        """
        跳转至添加成员界面
        :return:
        """
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)

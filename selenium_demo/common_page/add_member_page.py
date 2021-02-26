# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/2/27 0:15
# @Author:汤易怀
# @File  :add_member_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import allure
from selenium.webdriver.common.by import By

from selenium_demo.common_page.base_page import BasePage


@allure.feature("添加成员page")
class AddMemberPage(BasePage):
    """
    添加成员界面
    """

    @allure.story("添加成员方法")
    def add_member(self, username, account, phone_number):
        """
        添加成员
        :param username: 姓名
        :param account: 账号
        :param phone_number: 电话
        :return:
        """
        with allure.step(f"输入用户名{username}"):
            self.find(By.ID, "username").send_keys(username)
        with allure.step(f"输入账号{account}"):
            self.find(By.ID, "memberAdd_acctid").send_keys(account)
        with allure.step(f"输入手机号{phone_number}"):
            self.find(By.ID, "memberAdd_phone").send_keys(phone_number)
        with allure.step("点击保存"):
            self.find(By.LINK_TEXT, "保存").click()
        return self

    @allure.story("获取公司成员信息")
    def get_member_info(self):
        """
        获取公司成员
        :return:
        """
        with allure.step(f"获取姓名"):
            member_list = self.find(By.CSS_SELECTOR, ".member_colRight_memberTable_tr", element=False)
            return member_list

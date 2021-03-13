# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/2/27 0:58
# @Author:汤易怀
# @File  :test_member.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import pytest
import yaml

from selenium_demo.common_page.main_page import MainPage
from selenium_demo.test_case.test_base_case import TestBaseCase
from util import root_dir


class TestAddMember(TestBaseCase):
    """
    测试添加成员
    """

    @pytest.mark.parametrize(["username", "account", "phone_number"],
                             yaml.safe_load(open(f"{root_dir}/selenium_demo/yaml_data/case_data.yaml", encoding='UTF-8')))
    def test_add_member(self, username, account, phone_number):
        """
        测试添加
        :param username: 姓名
        :param account: 账号
        :param phone_number: 电话
        :return:
        """

        member_info = MainPage().goto_add_member_page().add_member(username, account, phone_number).get_member_info()
        assert username in member_info

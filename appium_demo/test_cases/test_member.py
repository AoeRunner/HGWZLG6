# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 19:48
# @Author:汤易怀
# @File  :test_member.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import os
import sys

import allure
import pytest
import yaml

from appium_demo.common.test_base_case import TestBaseCase
from util import root_dir

add_member_data_dir = os.path.join(root_dir, 'appium_demo', "data", "add_member_data.yaml")
delect_member_data_dir = os.path.join(root_dir, 'appium_demo', "data", "delect_member_data.yaml")


@allure.feature("通讯录用例")
class TestMember(TestBaseCase):

    @allure.feature("添加成员用例")
    @pytest.mark.parametrize(["send_data"], yaml.safe_load(open(add_member_data_dir, "r", encoding='UTF-8')))
    def test_add_member(self, send_data):
        self.app.goto_main().goto_contacts_page().goto_add_member_page().goto_add_manually_page().add_member(send_data)

    @allure.feature("删除成员用例")
    @pytest.mark.parametrize(["delect_data"], yaml.safe_load(open(delect_member_data_dir, "r", encoding='UTF-8')))
    def test_delect_member(self, delect_data):
        self.app.goto_main().goto_contacts_page().delete_member_page(delect_data)

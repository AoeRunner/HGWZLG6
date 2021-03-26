# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/27 0:28
# @Author:汤易怀
# @File  :test_address.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import os

import allure
import pytest
import yaml

from requests_demo.api.address_manage.member_manage_api import MemberManageApi
from requests_demo.common.base_handle import base_handle
from requests_demo.common.test_base_case import TestBaseCase
from util import root_dir

member_manage_api_dir = os.path.join(root_dir, 'requests_demo', "data", "test_address.yaml")


@allure.feature("通讯录管理接口测试模块")
class TestAddress(TestBaseCase):

    def setup(self):
        """
        实例化MemberManageApi类
        :return:
        """
        super().setup()
        self.member_manage_api = MemberManageApi()

    @allure.story("创建成员测试用例")
    @pytest.mark.parametrize(["user_id", "name", "mobile", "department"],
                             yaml.safe_load(open(member_manage_api_dir, "r", encoding='UTF-8'))["test_create_member"])
    def test_create_member(self, user_id, name, mobile, department):
        # 利用删除接口进行数据清理
        self.member_manage_api.delete_member(user_id)
        r = self.member_manage_api.create_member(user_id, name, mobile, department)
        base_handle.assert_result(r, errmsg="created")
        r = self.member_manage_api.get_member(user_id)
        base_handle.assert_result(r, name=user_id)

    @allure.story("读取成员测试用例")
    @pytest.mark.parametrize(["user_id", "name", "mobile", "department"],
                             yaml.safe_load(open(member_manage_api_dir, "r", encoding='UTF-8'))["test_get_member"])
    def test_get_member(self, user_id, name, mobile, department):
        self.address.create_member(user_id, name, mobile, department)
        r = self.address.get_member_information(self.user_id)
        base_handle.assert_result(r, errmsg="ok", name=name)

    @allure.story("更新成员测试用例")
    @pytest.mark.parametrize(["user_id", "name", "mobile", "department"],
                             yaml.safe_load(open(member_manage_api_dir, "r", encoding='UTF-8'))["test_delete_member"])
    def test_delete_member(self, user_id, name, mobile, department):
        self.address.create_member(user_id, name, mobile, department)
        r = self.address.delete_member(self.user_id)
        base_handle.assert_result(r, errmsg="deleted")
        r = self.address.get_member_information(self.user_id)
        base_handle.assert_result(r, errcode="60111")

    @allure.story("删除成员测试用例")
    @pytest.mark.parametrize(["user_id", "name", "mobile", "department"],
                             yaml.safe_load(open(member_manage_api_dir, "r", encoding='UTF-8'))["test_update"])
    def test_update(self, user_id, name, mobile, department):
        # 保证，成员一定是新添加的
        self.address.delete_member(user_id)
        self.address.create_member(user_id, name, mobile, department)
        new_name = self.name + "tmp"
        r = self.address.update_member(self.user_id, new_name, self.mobile)
        base_handle.assert_result(r, errmsg="updated")
        r = self.address.get_member_information(self.user_id)
        base_handle.assert_result(r, name=new_name)

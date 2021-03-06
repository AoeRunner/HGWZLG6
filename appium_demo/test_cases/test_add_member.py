# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 19:48
# @Author:汤易怀
# @File  :test_add_member.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import os
import sys
import pytest
import yaml

from appium_demo.common.test_base_case import TestBaseCase
from util import root_dir

data_dir = os.path.join(root_dir, 'appium_demo', "data", "case_data.yaml")


class TestAddMember(TestBaseCase):

    @pytest.mark.parametrize(["send_data"], yaml.safe_load(open(data_dir, "r", encoding='UTF-8')))
    def test_add_member(self, send_data):
        toast_text = self.app.goto_main().goto_contacts_page().goto_add_member_page().goto_add_manually_page().add_member(send_data)
        assert toast_text == "处理中"

# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 17:51
# @Author:汤易怀
# @File  :add_manually_page.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from typing import Dict, List

import pytest
import yaml

from appium_demo import root_dir
from appium_demo.common.base_page import BasePage


class AddManuallyPage(BasePage):
    """
    手动添加界面
    """

    def add_member(self, send_data):
        self.log.info("手动添加联系人")
        self.parse_action("add_manually_page.yaml", "add_member", send_data)

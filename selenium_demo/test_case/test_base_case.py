# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/2/27 1:00
# @Author:汤易怀
# @File  :test_base_case.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from util import root_dir
from util.common_log import CommonLog


class TestBaseCase:
    """
    测试基类
    """
    log = CommonLog("TestBase").add_handle()

    def setup(self):
        self.log.info("即将开始测试")

    def teardown(self):
        self.log.info("测试完成")

    def get_test_data(self, keys):
        """
        获取数据
        :return:
        """
        with open(f"{root_dir}/selenium_demo/yaml_data/case_data.yaml", encoding='UTF-8') as f:
            case_data = yaml.safe_load(f).get(keys)
            self.log.info(f"{keys}的值为：{case_data}")
        return case_data

    # @pytest.mark.parametrize(["username", "account", "phone_number"],
    #                          yaml.safe_load(open(f"{root_dir}/selenium_demo/yaml_data/case_data.yaml", encoding='UTF-8')))
    def test_hub_node(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        # capabilities['platform'] = "LINUX"  # 指定操作系统
        # capabilities['version'] = "10"  # 指定操作系统版本
        self.driver = webdriver.Remote(
            command_executor='http://106.75.190.11:5001/wd/hub',
            desired_capabilities=capabilities)
        self.driver.get("https://www.baidu.com/")
        sleep(10)
        self.driver.close()

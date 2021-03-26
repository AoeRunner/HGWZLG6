# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/27 1:55
# @Author:汤易怀
# @File  :request_runner.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import os
import time

import pytest

from appium_demo.common.cmd_handle import cmd_handle
from appium_demo.common.parser_handle import parse_handle
from util import root_dir
from util.common_log import CommonLog


class RequestRunner:
    """
    用例运行入口，jenkins执行入口，用于step节点中执行测试用例
    """
    log = CommonLog("RequestRunner").add_handle()

    def __init__(self, cases):
        """
        初始化cases
        :param cases: 运行用例
        """
        self.cases = cases

    def run(self):
        """
        运行测试用例并生成报告
        :return:
        """
        self.log.info(f"root_dir: {root_dir}")
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        allure_dir = os.path.join(root_dir, "request_demo", "report", time_stamp)
        if os.path.exists(allure_dir):
            os.makedirs(allure_dir)
        self.log.info(f"allure_dir: {allure_dir}")
        pytest.main([self.cases, "-vs", "--alluredir", f"{allure_dir}"])
        cmd = f"allure generate {allure_dir} -o {allure_dir}/html --clean"
        cmd_handle.cmd_start(cmd)


if __name__ == '__main__':
    # runner_args = parse_handle.runner_handle()
    # cases = runner_args.cases
    cases = r"test_cases\test_address.py"
    RequestRunner(cases).run()

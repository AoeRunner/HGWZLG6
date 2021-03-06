# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 14:18
# @Author:汤易怀
# @File  :app_runner.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import os
import subprocess
import sys
import time

import allure
import pytest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from appium_demo import root_dir
from appium_demo.common.log_handle import CommonLog
from appium_demo.common.parser_handle import parse_handle


class AppRunner:
    """
    用例运行入口
    """
    log = CommonLog("AppRunner").add_handle()

    def __init__(self, cases):
        """
        初始化cases
        :param cases: 运行用例
        """
        self.cases = cases

    def start_appium(self, host, port):
        """
        启动appium服务
        TODO: 以传参方式启动多个appium服务，并返回端口号，用于在CI持续集成中 远程分布式并发执行
        :return:
        """
        try:
            cmd = f"netstat –ano |findstr {port}"
            result = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
            if len(str(result)) == 0:
                cmd = f'start /b appium -a {host}  -p {port} --log {root_dir}/log/ '
                self.log.info(cmd)
                subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
                appium_server_url = f"http://{host}:{port}/wd/hub"
                self.log.info(appium_server_url)
            else:
                self.log.info(f"{port}:%d is used!")
        except Exception as e:
            self.log.error(e)

    def run(self):
        """
        运行测试用例并生成报告
        :return:
        """
        self.log.info(f"root_dir: {root_dir}")
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        allure_dir = os.path.join(root_dir, "appium_demo", "report", time_stamp)
        if os.path.exists(allure_dir):
            os.makedirs(allure_dir)
        self.log.info(f"allure_dir: {allure_dir}")
        pytest.main([self.cases, "-vs", "--alluredir", f"{allure_dir}"])
        os.system(f"allure generate {allure_dir} -o {allure_dir}/html --clean")


if __name__ == '__main__':
    # runner_args = parse_handle.runner_handle()
    # cases = runner_args.cases
    cases = r"test_cases\test_punch.py"
    AppRunner(cases).run()

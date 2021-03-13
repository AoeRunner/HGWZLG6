# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 11:41
# @Author:汤易怀
# @File  :app.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium import webdriver

from appium_demo.common.log_handle import CommonLog
from appium_demo.common.parser_handle import parse_handle
from appium_demo.pages.information_page import InformationPage


class App:
    """
    app启动入口
    """
    log = CommonLog("App").add_handle()

    def __init__(self):
        self.driver = None
        self.start()
        self.caps_args = None

    def get_caps_args(self):
        """
        获取配置项，从命令行获取参数，后期接入jenkins后可由jenkins直接入参
        :return:
        """
        self.log.info("获取配置项")
        caps_args = dict()
        caps_handle = parse_handle.caps_handle()
        caps_args["platformName"] = caps_handle.platformName
        caps_args["deviceName"] = caps_handle.deviceName
        caps_args["appPackage"] = caps_handle.appPackage
        caps_args["appActivity"] = caps_handle.appActivity
        # 不清空缓存启动app
        caps_args["noReset"] = caps_handle.noReset
        # 设置等待页面空闲状态的时间为0s
        caps_args['settings[waitForIdleTimeout]'] = caps_handle.waitForIdleTimeout
        return caps_args

    def start(self):
        """
        启动app, hose和 hub从命令行获取，用于并发启动多台设备
        :return:
        """
        remote_handle = parse_handle.remote_handle()
        app_host = remote_handle.host
        app_port = remote_handle.port
        self.log.info("启动应用：com.tencent.wework")
        self.log.info(f"host地址为：{app_host}")
        self.log.info(f"hub端口为：{app_port}")
        self.driver = webdriver.Remote(f"http://{app_host}:{app_port}/wd/hub", self.get_caps_args())
        # 显式等待10s
        self.driver.implicitly_wait(10)

    def goto_main(self):
        """
        进入消息界面
        :return:
        """
        self.log.info("进入消息界面")
        print(self.driver.page_source)
        return InformationPage(self.driver)

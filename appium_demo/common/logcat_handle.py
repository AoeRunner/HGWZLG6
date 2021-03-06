# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 17:19
# @Author:汤易怀
# @File  :logcat_handle.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from appium_demo.common.log_handle import CommonLog


class LogcatHandle:
    """
    安卓日志写入，以线程方式写入，和用例并行执行
    """
    log = CommonLog("LogcatHandle").add_handle()

    def __init__(self):
        pass

    def start_write_logcat(self):
        """
        统计安卓日志
        TODO
        :return:
        """
        self.log.info("开始打印安卓日志，adb logcat -v")

    def stop_write_logcat(self):
        """
        结束统计
        TODO
        :return:
        """
        self.log.info("结束统计安卓日志")


logcat_handle = LogcatHandle()

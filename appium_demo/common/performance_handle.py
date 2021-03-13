# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/13 15:32
# @Author:汤易怀
# @File  :performance_handle.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import time

from appium_demo.common import thread_run
from appium_demo.common.cmd_handle import cmd_handle
from appium_demo.common.log_handle import CommonLog
from util import root_dir


class PerformanceHandle:
    """
    性能采集服务
    """
    log = CommonLog("TestBaseCase").add_handle()

    def __init__(self):
        self.time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.start = False

    def start_preformance(self):
        """
        开始采集数据，cpu，内存，帧率FPS，电量，流量
        :return:
        """
        self.start = True

    def stop_preformance(self):
        """
        停止采集
        :return:
        """
        self.start = False

    @thread_run
    def get_performance_data(self):
        """
        获取性能数据
        :return:
        """
        while self.start:
            performance_data = f"{self.get_cpu_data()} {self.get_mem_data()} {self.get_fps_data()} "
            with open(f"{root_dir}/appium_demo/performance_data/{self.time_stamp}.txt", mode='w') as db:
                db.write(performance_data)

    def get_cpu_data(self):
        """
        获取cpu数据
        :return:
        """
        self.log.info("获取cpu数据")
        return cmd_handle.cmd_adb_shell_start("top -m 10 -n 1 -s cpu")

    def get_mem_data(self, package_name="com.tencent.wework"):
        """
        获取内存数据
        :return:f
        """
        self.log.info("获取内存数据")
        return cmd_handle.cmd_adb_shell_start(f"dumpsys meminfo {package_name}")

    def get_fps_data(self):
        """
        获取帧率数据
        :return:
        """
        self.log.info("获取帧率数据")
        return cmd_handle.cmd_adb_shell_start("dumpsys SurfaceFlinger")

    def get_quantity_data(self):
        """
        获取电量数据
        :return:
        """
        self.log.info("获取电量数据")
        pass

    def get_flow_data(self):
        """
        获取流量数据
        :return:
        """
        self.log.info("获取流量数据")
        pass


performance_handle = PerformanceHandle()

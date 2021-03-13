# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/13 15:04
# @Author:汤易怀
# @File  :cmd_handle.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import subprocess

from appium_demo.common.log_handle import CommonLog


class CmdHandle:
    """
    cmd命令执行工具
    """
    log = CommonLog("CmdHandle").add_handle()

    def __init__(self):
        pass

    def cmd_start(self, cmd):
        """
        cmd命令基础方法
        :param cmd:
        :return:
        """
        self.log.info(f"cmd : {cmd}")
        sub_process = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)
        cmd_result = sub_process.stdin.read()
        return cmd_result

    def cmd_adb_start(self, cmd, device=None):
        """
        adb命令方法
        :param cmd:
        :param device: 设备devices
        :return:
        """
        if device is not None:
            cmd = f"adb -s {device} {cmd}"
        else:
            cmd = f"adb {cmd}"
        self.log.info(f"cmd_adb : {cmd}")
        return self.cmd_start(cmd)

    def cmd_adb_shell_start(self, cmd, device=None):
        """
        adb shell命令方法
        :param cmd:
        :param device: 设备devices
        :return:
        """
        self.log.info(f"cmd_adb : {cmd}")
        cmd = f"shell {cmd}"
        return self.cmd_adb_start(cmd, device=device)


cmd_handle = CmdHandle()

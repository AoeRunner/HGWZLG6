# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/29 23:03
# @Author:汤易怀
# @File  :calc_lator.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from util.common_log import CommonLog


class CalcuLater:
    """
    计算器类
    """
    log = CommonLog("CalcuLater").add_handle()

    def add(self, a, b):
        self.log.info(f"开始计算加法: {a} + {b}")
        result = a + b
        self.log.info(f"计算结果为: {result}")
        return result

    def sub(self, a, b):
        self.log.info(f"开始计算加法: {a} - {b}")
        result = a - b
        self.log.info(f"计算结果为: {result}")
        return result

    def mul(self, a, b):
        self.log.info(f"开始计算加法: {a} * {b}")
        result = a * b
        self.log.info(f"计算结果为: {result}")
        return result

    def div(self, a, b):
        self.log.info(f"开始计算加法: {a} / {b}")
        result = a / b
        self.log.info(f"计算结果为: {result}")
        return result

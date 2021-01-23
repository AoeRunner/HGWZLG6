# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/23 16:24
# @Author:汤易怀
# @File  :money.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from util.common_log import CommonLog


class Money:
    """
    存工资
    """

    log = CommonLog("Money").add_handle()

    def __init__(self):
        self.save_money = 88

    def spend_money(self, spends):
        """
        消费功能
        :param spends: 消费金额
        :return:
        """
        self.save_money -= spends
        self.log.info(f"本次消费{spends}$")
        return self.save_money

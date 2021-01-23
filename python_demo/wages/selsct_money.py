# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/23 16:36
# @Author:汤易怀
# @File  :selsct_money.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from python_demo.wages.money import Money


class SelectMoney(Money):
    """
    查询工资
    """

    def select_money(self):
        self.log.info(f"测试开发小马哥当前余额：{self.save_money}$")
        return self.save_money

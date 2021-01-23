# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/23 16:26
# @Author:汤易怀
# @File  :send_money.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from python_demo.wages.selsct_money import SelectMoney


class SendMoney(SelectMoney):
    """
    发工资
    """

    def __init__(self, monthly_salary=15000):
        """
        初始化余额和月薪
        :param balance: 余额
        :param monthly_salary: 月薪
        """
        super(SendMoney, self).__init__()
        self.monthly_salary = monthly_salary

    def send_money(self):
        """
        发工资方法
        :return: 返回当前余额
        """
        self.log.info(f"测试开发小马哥月薪：{self.monthly_salary}$, 即将开始发工资, 请注意查收短信")
        self.save_money += self.monthly_salary
        return self.save_money

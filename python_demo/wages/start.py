# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/23 16:34
# @Author:汤易怀
# @File  :start.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from python_demo.wages.selsct_money import SelectMoney
from python_demo.wages.send_money import SendMoney
from util.common_log import CommonLog


def start():
    log = CommonLog("start").add_handle()
    # 先查询一次工资
    select_money = SelectMoney()
    money = select_money.select_money()
    # 如果工资太少，该程序员快饿死了，发一次工资给他
    send_money = SendMoney()
    if money < 100:
        log.info("工资太少，测试开发小马哥快饿死了，发一次工资给他")
        send_money.send_money()
    # 再次查询工资
    send_money.select_money()
    log.info("测试开发小马哥工作结果突出，再发一个月的年终奖给他")
    money = send_money.send_money()
    send_money.select_money()
    # 有钱了，给女朋友买个包
    if money > 20000:
        log.info("测试开发小马哥有钱了，给女朋友买个包")
        send_money.spend_money(30000)
    send_money.select_money()


if __name__ == '__main__':
    start()

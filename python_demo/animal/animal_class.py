# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/22 20:57
# @Author:汤易怀
# @File  :animal_class.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from util.common_log import CommonLog


class AnimalClass:
    """
    比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    创建子类【猫】，继承【动物类】，
    重写父类的__init__方法，继承父类的属性，
    添加一个新的属性，毛发 = 短毛，
    添加一个新的方法， 会捉老鼠，
    重写父类的【会叫】的方法，改成【喵喵叫】
    """
    log = CommonLog("AnimalClass").add_handle()

    def __init__(self, name="旺财", colour="黄色", age="2岁", gender="公"):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender

    def animal_run(self):
        self.log.info(f"{self.name}正在跑")

    def animal_call(self):
        self.log.info(f"{self.name}正在叫, 汪汪汪")

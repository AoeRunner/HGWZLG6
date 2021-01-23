# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/23 0:14
# @Author:汤易怀
# @File  :kitten_class.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
from python_demo.animal.animal_class import AnimalClass


class Kitten(AnimalClass):
    """
    机器猫
    """
    def __init__(self, name="哆啦A梦", colour="蓝色", age="2岁", gender="公"):
        super().__init__(name, colour, age, gender)
        self.hair = "没有头发"

    def animal_call(self):
        self.log.info(f"{self.name}正在喊, 大雄！！！快做作业，大雄~~做好死的觉悟了吧！")

    def catching_mice(self):
        self.log.info(f"{self.name}非常害怕老鼠, 抓老鼠是不可能抓老鼠的，这辈子都不可能抓老鼠的")


if __name__ == '__main__':
    Doraemon = Kitten()
    Doraemon.animal_call()
    Doraemon.catching_mice()

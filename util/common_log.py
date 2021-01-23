# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/22 22:47
# @Author:汤易怀
# @File  :common_log.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import logging
import time


class CommonLog(object):
    """
        封装后的logging
    """

    def __init__(self, name="common_log", level: logging = logging.DEBUG):
        """
        实例化logging
        :param name: 该日志名称
        :param level: 该日志级别
        """
        self.name = name
        self.level = level
        self.formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s %(filename)s %(module)s %(funcName)s %(lineno)d %(message)s")

    def create_logger(self):
        """
        创建一个logger，并设置日志级别
        :return:
        """
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        return logger

    def create_handle(self):
        """
        创建所需要的handel，并指定输出格式
        :return:
        """
        time_stamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file_write = logging.FileHandler(f"./log/{time_stamp}.log", encoding="utf-8")
        file_write.setFormatter(self.formatter)
        file_print = logging.StreamHandler()
        file_print.setFormatter(self.formatter)
        return file_write, file_print

    def add_handle(self):
        """
        为handle添加日志处理器
        :return:
        """
        logger = self.create_logger()
        logger.addHandler(self.create_handle()[0])
        logger.addHandler(self.create_handle()[1])
        return logger


if __name__ == '__main__':
    log = CommonLog("sss").add_handle()
    log.info("这是第一次输出")
    log.info("这是第二次输出")

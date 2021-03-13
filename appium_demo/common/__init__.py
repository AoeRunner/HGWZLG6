# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 11:32
# @Author:汤易怀
# @File  :__init__.py.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import threading


def thread_run(func):
    """
    线程方法，用于将普通方法转换成线程执行
    :param func:
    :return:
    """

    def thread_fun(*args, **kwargs):
        thread_tts = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread_tts.start()
        thread_tts.join()

    return thread_fun

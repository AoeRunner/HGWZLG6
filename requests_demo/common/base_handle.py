# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/27 1:14
# @Author:汤易怀
# @File  :base_handle.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import json
import re

from util.common_log import CommonLog


class BaseHandle:
    """
    基础方法，封装基本方法的使用
    """
    log = CommonLog("BaseHandle").add_handle()

    def assert_result(self, result, **kwargs):
        """
        对result进行解析
        :param result:
        :param kwargs:
        :return:
        """
        for k, v in kwargs.items():
            if type(v) == dict:
                for k1, v1 in v.items():
                    value1 = result[k][k1]
                    if type(value1) == str:
                        value1 = re.sub(r'(\\u[a-zA-Z0-9]{4})',
                                       lambda x: x.group(1).encode("utf-8").decode("unicode-escape"), value1)
                    assert value1 == v1, f"预期结果{k1}={v1}, 实际结果{k1}={value1}"
            else:
                value = result[k]
                if type(value) == str:
                    value = re.sub(r'(\\u[a-zA-Z0-9]{4})',
                                   lambda x: x.group(1).encode("utf-8").decode("unicode-escape"), value)
                assert value == v, f"预期结果{k}={v}, 实际结果{k}={value}"


base_handle = BaseHandle()

# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/30 0:02
# @Author:汤易怀
# @File  :conftest.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import pytest
import yaml

from pytest_demo.page_code.calculator import CalcuLater
from util import root_dir
from util.common_log import CommonLog

log = CommonLog("conftest").add_handle()

with open(f"{root_dir}/pytest_demo/yaml_data/calc.yaml") as f:
    datas = yaml.safe_load(f)


@pytest.fixture(scope="module")
def get_calc():
    """
    实例化计算器类，并返回一个实例
    :return:
    """
    log.info("实例化计算器")
    calc = CalcuLater()
    return calc


@pytest.fixture(params=datas["add"]["add_data"], ids=datas["add"]["add_name"])
def get_add_data(request):
    """
    获取加法数据，并返回
    :param request:
    :return:
    """
    data = request.param
    log.info(f"已获取到加法数据：{data},即将开始计算")
    yield data
    log.info("结束计算")


@pytest.fixture(params=datas["sub"]["sub_data"], ids=datas["sub"]["sub_name"])
def get_sub_data(request):
    """
    获取剑法数据，并返回
    :param request:
    :return:
    """
    data = request.param
    log.info(f"已获取到剑法数据：{data},即将开始计算")
    yield data
    log.info("结束计算")


@pytest.fixture(params=datas["mul"]["mul_data"], ids=datas["mul"]["mul_name"])
def get_mul_data(request):
    """
    获取乘法数据，并返回
    :param request:
    :return:
    """
    data = request.param
    log.info(f"已获取到乘法数据：{data},即将开始计算")
    yield data
    log.info("结束计算")


@pytest.fixture(params=datas["div"]["div_data"], ids=datas["div"]["div_name"])
def get_div_data(request):
    """
    获取除法数据，并返回
    :param request:
    :return:
    """
    data = request.param
    log.info(f"已获取到除法数据：{data},即将开始计算")
    yield data
    log.info("结束计算")


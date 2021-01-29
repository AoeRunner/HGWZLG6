# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/1/29 23:54
# @Author:汤易怀
# @File  :test_calc.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import allure
import pytest


@allure.feature("测试计算器")
class TestCalc:

    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add_data):
        """
        加法用例
        :param get_calc: 实例化加法
        :param get_add_data: 测试数据
        :return:
        """
        with allure.step("计算两个数的相加和"):
            result = get_calc.add(get_add_data[0], get_add_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_add_data[2]

    @allure.story("测试除法")
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div_data):
        """
        除法用例
        :param get_calc: 实例化除法
        :param get_div_data: 测试数据
        :return:
        """
        with allure.step("计算两个数的相除商"):
            result = get_calc.div(get_div_data[0], get_div_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_div_data[2]

    @allure.story("测试剑法")
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub_data):
        """
        剑法用例
        :param get_calc: 实例化剑法
        :param get_sub_data: 测试数据
        :return:
        """
        with allure.step("计算两个数的相减差"):
            result = get_calc.sub(get_sub_data[0], get_sub_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_data[2]

    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_mul_data):
        """
        乘法用例
        :param get_calc: 实例化乘法
        :param get_mul_data: 测试数据
        :return:
        """
        with allure.step("计算两个数的乘法积"):
            result = get_calc.mul(get_mul_data[0], get_mul_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_data[2]

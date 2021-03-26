# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/26 23:04
# @Author:汤易怀
# @File  :base_api.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import allure
import requests

from util.common_log import CommonLog


class BaseApi:
    """
    api基类，用于被各模块接口继承
    """
    log = CommonLog("BaseApi").add_handle()

    def __init__(self):
        """
        初始化基础url,并实例化Session()
        """
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin/"
        self.s = requests.Session()

    @allure.step("调用接口凭证")
    def get_token(self, corp_secret, corp_id="ww252669c57684666d"):
        """
        请求方式： GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        注：此处标注大写的单词ID和SECRET，为需要替换的变量，根据实际获取值更新。其它接口也采用相同的标注，不再说明。

        :param corp_id: 企业ID，获取方式参考：术语说明-corp_id
        :param corp_secret: 应用的凭证密钥，获取方式参考：术语说明-secret：
        :return:
        """
        return requests.get(f"{self.base_url}gettoken?corpid={corp_id}&corpsecret={corp_secret}")

    def send(self, method, *args, **kwargs):
        """
        发送请求
        :param method: 请求方法
        :param args: 元组
        :param kwargs: 字典
        :return:
        """
        if method == 1:
            self.log.info("即将发起GET请求")
            return self.s.request("GET", *args, **kwargs)
        elif method == 2:
            self.log.info("即将发起POST请求")
            return self.s.request("POST", *args, **kwargs)
        elif method == 3:
            self.log.info("即将发起PUT请求")
            return self.s.request("PUT", *args, **kwargs)
        elif method == 4:
            self.log.info("即将发起DEFLECT请求")
            return self.s.request("DEFLECT", *args, **kwargs)

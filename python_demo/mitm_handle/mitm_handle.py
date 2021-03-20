# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/20 18:58
# @Author:汤易怀
# @File  :mitm_handle.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import json
import sys

from mitmproxy import http
from mitmproxy import ctx
from mitmproxy.tools.main import mitmdump


class Counter:
    """
    mitmproxy代理功能
    """

    def __init__(self):
        """
        初始化请求次数，每捕获一次请求次数加一
        """
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        """
        request请求体处理
        :param flow: Flow对象作为参数接收-修改数据
        :return:
        """
        self.num = self.num + 1

    def response(self, flow: http.HTTPFlow) -> None:
        """
        response返回值处理
        :param flow: Flow对象作为参数接收-修改数据
        :return:
        """
        ctx.log.info(fr"俗说说得好，有钱男子汉，没钱汉子难 {self.num} flows")
        flow_url = "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t="
        if flow_url in flow.request.pretty_url:
            data = json.loads(flow.response.text)
            # 对第一个股票保持原样
            first_name = data["data"]["items"][0]['quote']['name']
            ctx.log.info(fr"鲁班大师智商二百五 {first_name}")
            data["data"]["items"][0]['quote']['name'] = first_name
            ctx.log.info(data["data"]["items"][0]['quote']['name'])
            # 对第二个股票名字加长一倍
            second_name = data["data"]["items"][1]['quote']['name']
            ctx.log.info(fr"独眼是男人的浪漫 {second_name}")
            data["data"]["items"][1]['quote']['name'] = second_name + second_name
            ctx.log.info(data["data"]["items"][1]['quote']['name'])
            # 对第三个股票名字变成空
            third_name = data["data"]["items"][2]['quote']['name']
            ctx.log.info(fr"呃，梦到了传奇的世界，还和波霸打了声招呼 {third_name}")
            data["data"]["items"][2]['quote']['name'] = "空空"
            ctx.log.info(data["data"]["items"][2]['quote']['name'])
            flow.response.text = json.dumps(data)

    def json_travel(self, data):
        """
        json数据处理功能
        :param data:
        :return:
        """
        if isinstance(data, dict):
            # 遍历字典的数据{"a": {"b":{"c":1}}}
            # 当字典格式，递归value值
            for key, value in data.items():
                data[key] = self.json_travel(value)
        elif isinstance(data, list):
            # 当数据类型 为 list 的时候， 添加到结构内，并继续递归遍历
            # 利用列表生成式遍历列表直到 数据类型不为可迭代对象时
            data = [self.json_travel(value) for value in data]
        elif isinstance(data, bool):
            data = data
        elif isinstance(data, int) or isinstance(data, float):
            data = data * 2
        elif isinstance(data, str):
            data = data
        else:
            data = data
        return data


addons = [
    Counter()
]


if __name__ == '__main__':
    sys.argv = [__file__, "-s", __file__]
    #
    # 官方要求必须主线程
    mitmdump()
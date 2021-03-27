# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/26 23:20
# @Author:汤易怀
# @File  :member_manage_api.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
import allure
import requests

from requests_demo.common.base_api import BaseApi


class MemberManageApi(BaseApi):
    """
    成员管理接口
    """

    def __init__(self):
        """
        继承基类的构造方法，并附加通讯录管理token
        """
        super().__init__()
        self.s.params = {"access_token": self.get_token("YGxrFgR57hKqLnI1a2_i8AVBLcIP9sdGWzg8fd-gpYQ")}

    @allure.step("调用创建成员接口")
    def create_member(self, user_id, name, mobile, department):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN

        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节。只能由数字、字母和“_-@.”
                        四种字符组成，且第一个字符必须是数字或字母
        :param name: 成员名称。长度为1~64个utf8字符
        :param mobile: 手机号码。企业内必须唯一，mobile/email二者不能同时为空
        :param department: 成员所属部门id列表,不超过100个
        :return:
        """
        create_url = f"{self.base_url}user/create"
        return self.send(2, create_url, userid=user_id, name=name, mobile=mobile, department=department)

    @allure.step("调用读取成员接口")
    def get_member(self, user_id):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID

        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :return:
        """
        get_url = f"{self.base_url}user/get"
        return self.send(1, get_url, userid=user_id)

    @allure.step("调用更新成员接口")
    def update_member(self, user_id, name, mobile):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN

        :param user_id: 成员UserID。对应管理端的帐号，企业内必须唯一。不区分大小写，长度为1~64个字节
        :param name: 成员名称。长度为1~64个utf8字符
        :param mobile: 手机号码。企业内必须唯一。若成员已激活企业微信，则需成员自行修改（此情况下该参数被忽略，但不会报错）
        :return:
        """
        update_url = f"{self.base_url}user/update"
        return self.send(2, update_url, userid=user_id, name=name, mobile=mobile)

    @allure.step("调用删除成员接口")
    def delete_member(self, user_id):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID

        :param user_id: 成员UserID。对应管理端的帐号
        :return:
        """
        delete_url = f"{self.base_url}user/delete"
        return self.send(1, delete_url, userid=user_id)

    @allure.step("调用批量删除成员接口")
    def batch_delete_member(self, userid_list):
        """
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token=ACCESS_TOKEN

        :param userid_list: 成员UserID列表。对应管理端的帐号。最多支持200个。若存在无效UserID，直接返回错误
        :return:
        """
        batch_delete_url = f"{self.base_url}user/batchdelete"
        return self.send(1, batch_delete_url, useridlist=userid_list)


member_manage_api = MemberManageApi()

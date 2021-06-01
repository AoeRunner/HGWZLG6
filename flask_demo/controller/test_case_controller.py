# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/24 22:32
# @Author:tyh
# @File  :test_case_controller.py
# @Phone :13926528314
# ================================================
from flask import request
from flask_restful import Resource

from flask_demo import db, api
from flask_demo.model.test_case_model import TestCaseModel


class TestCaseController(Resource):
    def get(self):
        s = TestCaseModel.query.all()
        print(s)
        result = []
        for comment in s:
            l=comment.to_json()
            result.append(l)
        print(result)
        return {"msg": "ok", "data":result}

    def post(self):
        print(request.json)
        testcase = TestCaseModel(**request.json)
        print(testcase)
        db.session.add(testcase)
        db.session.commit()
        return {"msg": "ok"}


api.add_resource(TestCaseController, "/testcase")

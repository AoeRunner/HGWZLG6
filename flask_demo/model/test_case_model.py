# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/24 22:25
# @Author:tyh
# @File  :test_case_model.py
# @Phone :13926528314
# ================================================
from flask_demo import db


class TestCaseModel(db.Model):
    def to_json(self):
        dict = self.__dict__

        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    __tablename__ = "test_case"
    # The message will not show: Unresolved attribute reference 'Column' for class 'SQLAlchemy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    desc = db.Column(db.String(20), unique=True, nullable=False)
    step = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<TestCase %r>' % self.name
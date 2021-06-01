# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/4/14 22:49
# @Author:tyh
# @File  :server.py
# @Phone :13926528314
# ================================================
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@106.75.190.11:3307/test_case?charset=utf8mb4'
app.config['JSON_AS_ASCII'] = False
api = Api(app)
db = SQLAlchemy(app)

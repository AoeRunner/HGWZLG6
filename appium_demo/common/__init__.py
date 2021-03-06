# ！/usr/bin/env python
# -*- coding = utf-8 -*-
# ================================================
# @Time  :2021/3/6 11:32
# @Author:汤易怀
# @File  :__init__.py.py
# @IDE   :PyCharm
# @Phone :13926528314,微信同号
# ================================================
caps = dict()
caps["platformName"] = "Android"
caps["deviceName"] = "wework"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.LaunchSplashActivity"
# 不清空缓存启动app
caps["noReset"] = "true"
# 设置等待页面空闲状态的时间为0s
caps['settings[waitForIdleTimeout]'] = 0
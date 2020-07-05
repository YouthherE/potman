# 1 导包
import os
import unittest

import HTMLTestRunner_PY3

from ihrm.script.test_ihrm_login import TestIHRMLogin

import time

# os.path.dirname(os.path.abspath(__file__)) 可以定位到当前项目的目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2 创建测试套件
suite = unittest.TestSuite()
# 3 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 4 定义测试报告的目录和报告名称
report_path = BASE_DIR + "/report/login-{}.html".format(time.strftime('%Y%m%d %H%M%S'))
# 5 使用HTMLTestRunner_PY3生成测试报告
with open(report_path, mode='wb') as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="ihrm登录接口功能测试",
                                               description="这是一个更加美观的报告，前提是连上互联网")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite)
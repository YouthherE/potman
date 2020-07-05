# 1.导包
from BeautifulReport import BeautifulReport
import os
import time
import unittest

# 2.组织测试套件
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
suite = unittest.TestLoader().discover(BASE_DIR + "/script", "test*.py")
# 3.定义测试报告文件名
report_file = "{}-report.html".format(time.strftime("%Y%m%d%H%M%S"))
# 4.使用BeautifulReport来批量运行测试用例并且生成测试报告
BeautifulReport(suite).report(filename=report_file, description="webAutoTest", log_path=BASE_DIR + "/report")

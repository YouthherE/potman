# 导入Unittest和requests模块
import unittest, requests
from parameterized import parameterized
# 创建测试类
from utils import read_login_data
class TestIHRMLogin(unittest.TestCase):
    # 初始化unittest
    def setUp(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"
    def tearDown(self):
        pass
    @parameterized.expand(read_login_data())
    # 编写测试函数
    def test01_login(self,case_name,request_body, message):
        # 发要送的请求体数据
        data = request_body
        # 发送请求并接收结果
        response = requests.post(url=self.login_url, json=data)
        # 打印结果
        print(response.json())
        # 断言
        self.assertIn(message, response.json().get('message'))

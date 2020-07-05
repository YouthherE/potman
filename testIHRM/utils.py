# 读取登录数据
import json
import os


def read_login_data():
    # 定义要登录的数据文件地址
    login_data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/login_data.json"
    # 打开这个文件，然后使用json加载文件流，加载成json格式
    with open(login_data_path, mode='r', encoding='utf-8') as f:
        # 使用json加载文件流
        jsonData = json.load(f)
        # 定义临时存放数据的空列表
        result_list = list()
        # 使用for循环遍历jsonData，取出登录的数据
        for login_data in jsonData:  # type:dict
            result_list.append(tuple(login_data.values()))
    print(result_list)
    return result_list


if __name__ == '__main__':
    read_login_data()

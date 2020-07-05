# 导包
import logging

from ihrm import utils
# 初始化
utils.init_logging()


if __name__ == '__main__':
    logging.info("日志会不会打印")
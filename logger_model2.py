# 模块按日期打印日志，并删除过期的日志
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler
import re
import time

def log_init():
    filename = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    log_fmt = '%(asctime)s\tFile \"%(filename)s\",line %(lineno)s\t%(levelname)s: %(message)s'
    formatter = logging.Formatter(log_fmt)
    log_file_handler = TimedRotatingFileHandler(logname="/Users/xiaoweiyu/PycharmProjects/Python-Selenium-UIAutomator/log/"+filename+".log",
                                                when="D", interval=1, backupCount=7)
    log_file_handler.suffix = "%Y-%m-%d_%H-%M.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    log = logging.getLogger()
    log.addHandler(log_file_handler)

if __name__ == '__main':
    log_init()
    # 程序运行
    #removeHandler 要放在程序运用打印日志的后面
    # log.removeHandler(log_file_handler)()


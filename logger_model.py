import logging
#开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Logger():
    def __init__(self, logname, loglevel, logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            Level	Numeric value
            CRITICAL	50
            ERROR	    40
            WARNING	    30
            INFO	    20
            DEBUG	    10
            NOTSET	    0
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = {
                    1:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(thread)d'),
                    2:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(thread)d'),
                    3:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(thread)d')
                     }
        # formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger

# 再通过以下方式调用，便是一个简单的日志系统了
logger = Logger(logname='/Users/xiaoweiyu/PycharmProjects/Python-Selenium-UIAutomator/log/log.txt',
                loglevel=1, logger="fox").getlog()





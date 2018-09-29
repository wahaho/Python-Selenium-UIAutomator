import logging

# 创建一个logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
# 1、不同级别日志信息
# formatter = {
#             1:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(thread)d'),
#             2:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(thread)d'),
#             3:logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(thread)d')
#              }

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

# 记录一条日志    Logger.setLevel(lvl)  级别高低顺序：NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
logger.info('foorbar')
# logger.debug('debug')
# logger.info("foobar")
# logger.warning("foobar")
# logger.error("foobar")
# logger.critical("foobar")

# Logger.addHandler(hdlr)
# StreamHandler: 输出到控制台
# FileHandler:   输出到文件
# BaseRotatingHandler 可以按时间写入到不同的日志中。比如将日志按天写入不同的日期结尾的文件文件。
# SocketHandler 用TCP网络连接写LOG
# DatagramHandler 用UDP网络连接写LOG
# SMTPHandler 把LOG写成EMAIL邮寄出去
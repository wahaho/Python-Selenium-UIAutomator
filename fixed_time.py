import datetime
import time

def doSth():
    print('test')
    # 假装做这件事情需要2秒钟
    time.sleep(2)

def main(h=17, m=46):
    '''h表示设定的小时，m为设定的分钟'''
    while True:
        # 判断是否达到设定时间，例如0:00
        while True:
            now = datetime.datetime.now()
            print('现在时间为:',now.ctime())
            # 到达设定时间，结束内循环
            if now.hour==h and now.minute==m:
                break
            # 不到时间就等30秒之后再次检测
            time.sleep(30)
        # 做正事，一天做一次
        doSth()

main()
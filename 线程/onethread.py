import _thread
from time import sleep, ctime


loops = [4, 2]

def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    print('start:', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('all end:', ctime())

if __name__ == '__main__':
    main()


# 4 秒，是最长的循环 的运行时间与其它的代码的时间总和。


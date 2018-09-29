#coding=utf-8
from selenium import webdriver
import time
#访问百度
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
#将页面滚动条拖到底部
js="var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
#将滚动条移动到页面的顶部
js="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)
#将页面滚动条移动到页面任意位置，改变等于号后的数值即可
js="var q=document.documentElement.scrollTop=50"
driver.execute_script(js)
time.sleep(9)
'''
#若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作
js="var q=document.getElementById('id').scrollTop=100000"
driver.execute_script(js)
time.sleep(3)
'''
from selenium import webdriver
import time

browser=webdriver.Chrome()
first_url="http://www.baidu.com"
browser.get(first_url)
print ("open the first url is %s"%first_url)
time.sleep(3)
second_url="http://news.baidu.com"
print("open the second url is %s"%second_url)
browser.get(second_url)
time.sleep(3)

print("back to the first_url %s"%first_url)
browser.back()
time.sleep(2)

print ("forwar to the second_url %s"%first_url)
browser.forward()
time.sleep(2)

print("设置浏览器高320，宽480显示")
browser.set_window_size(1400,1100)
time.sleep(2)

# print("浏览器最大化")
# browser.maximize_window()

title=browser.title
print (title)

browser.find_element_by_link_text("贴吧").click
time.sleep(3)

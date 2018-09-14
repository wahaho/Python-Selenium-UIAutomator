# 模块化 登录,退出功能。
from selenium import webdriver
import time

# 用户登录
def login_(driver):
    user = '***'
    pw = '***'

    driver.find_element_by_css_selector(".login-button.js-kmf-login.hollow-button").click()
    inputuser = driver.find_element_by_id("LoginPopupName")
    inputuser.send_keys(user)
    inputpw = driver.find_element_by_id("LoginPopupPassword")
    inputpw.send_keys(pw)
    driver.find_element_by_id("LoginSubmit").click()
    time.sleep(1)

# 用户退出
def logout_(driver):
    driver.find_element_by_css_selector(".user-avatar.has-submenu.asidecol").click()
    time.sleep(2)

    now_handle = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != now_handle:
            print(handle)
            driver.switch_to_window(handle)
            time.sleep(1)
        else:
            driver.find_element_by_link_text("退出登录").click()
        time.sleep(1)


.


# 实现用户登录、打开、退出
from selenium import webdriver
import time

class loginout_user():

    driver = webdriver.Chrome()
    driver.get("https://toefl.kmf.com")

    # 用户登录
    def login_(self,user='***',pw='***'):
        self.user = user
        self.pw = pw

        self.driver.find_element_by_css_selector(".login-button.js-kmf-login.hollow-button").click()
        inputuser = self.driver.find_element_by_id("LoginPopupName")
        inputuser.send_keys(user)
        inputpw = self.driver.find_element_by_id("LoginPopupPassword")
        inputpw.send_keys(pw)
        self.driver.find_element_by_id("LoginSubmit").click()
        time.sleep(1)

    #打卡
    def punch_card(self):
        try:
            self.driver.find_element_by_css_selector(".punch-detail-pannel.showone")
            a = True
        except:
            a = False
        if a == True:
            self.driver.find_element_by_class_name("punch-btn").click()
            time.sleep(2)
            self.driver.find_element_by_class_name("punch-save").click()
            print("打卡成功")
            time.sleep(2)
        elif a == False:
            print("该账户今日已经打卡了")

    # 用户退出
    def logout_(self):
        self.driver.find_element_by_css_selector(".user-avatar.has-submenu.asidecol").click()
        time.sleep(2)

        now_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                print(handle)
                self.driver.switch_to_window(handle)
                time.sleep(1)
            else:
                self.driver.find_element_by_link_text("退出登录").click()
            time.sleep(1)

if __name__ == '__main__':
    loginout_user().login_()
    loginout_user().punch_card()
    time.sleep(2)
    loginout_user().logout_()
    time.sleep(2)
    loginout_user.driver.close()


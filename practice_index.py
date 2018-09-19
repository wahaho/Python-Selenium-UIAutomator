from selenium import webdriver
import time
import action

driver = webdriver.Chrome()
driver.get("https://toefl.kmf.com")
time.sleep(2)

def login():
    action.login_(driver)

# 点击练习模块进入列表页
def practice_list():
    # 进入听力列表页
    driver.find_element_by_class_name("hasnav").click()
    driver.find_element_by_css_selector(".ctrl-subjects-icons.listen").click()
    driver.find_element_by_css_selector(".subject-infos.half").click()
    time.sleep(1)
    # 进入阅读列表页
    driver.find_element_by_class_name("hasnav").click()
    driver.find_element_by_css_selector(".ctrl-subjects-icons.read").click()
    driver.find_element_by_xpath("//a[@href='/read/ets/order']").click()
    time.sleep(1)
    # 进入口语列表页
    driver.find_element_by_class_name("hasnav").click()
    driver.find_element_by_css_selector(".ctrl-subjects-icons.spoken").click()
    driver.find_element_by_css_selector(".subject-infos.half.sub-info").click()
    time.sleep(1)
    # 进入写作列表页
    driver.find_element_by_class_name("hasnav").click()
    driver.find_element_by_css_selector(".ctrl-subjects-icons.write").click()
    driver.find_element_by_xpath("//a[@href='/write/ets/order']").click()



def logout():
    action.logout_(driver)

if __name__ == '__main__':
    login()
    practice_list()
    logout()
    time.sleep(1)
    # 关闭浏览器
    driver.close()

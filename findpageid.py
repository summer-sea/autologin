import time
from selenium import webdriver

def login(username,password):

    #设置要登录的地址
    url ='http://localhost:8080/jctest/'

    driver = webdriver.Firefox()
    driver.get(url)


    #抓取的是页面的元素的id
    #查找用户名的输入框
    name_input =driver.find_element_by_id('login_input_name')
    #查找输入密码的输入框
    pass_input =driver.find_element_by_id('txtPassword')
    #查找到登录的按钮
    login_button = driver.find_element_by_id('login_button')

    name_input.clear()
    name_input.send_keys(username)
    time.sleep(0.2)
    pass_input.clear()
    pass_input.send_keys(password)  # 填写密码
    time.sleep(0.2)
    login_button.click() #点击登录

    time.sleep(0.2)
   # print (driver.get_cookie())

    time.sleep(2)
    print(driver.title)
    #driver.close()


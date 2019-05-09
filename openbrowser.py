import webbrowser
#webbrowser.open("http://www.baidu.com")
#new=1新的浏览器窗口会打开，new=2新的浏览器tab会被打开
#webbrowser.open('http://www.baidu.com',new =0,autoraise=True)



#使用selenium
from selenium import webdriver
url ='http://www.baidu.com'
driver = webdriver.Firefox()
driver.get(url)
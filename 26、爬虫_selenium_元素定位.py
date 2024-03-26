from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.common.by import By
path= '/usr/local/bin/chromedriver'
browser=webdriver.Chrome(path)
url='https://www.baidu.com'
browser.get(url)

#元素定位

#根据id来找到对象
button1=browser.find_element(By.ID,'su')  #百度一下四个字的id是su
print(button1)

#根据标签属性的属性值来获取对象
button2=browser.find_element(By.NAME,"wd")  #查询框的name
print(button2)

#根据xpath语句来获取对象
button3=browser.find_element(By.XPATH,'//input[@id="su"]')
print(button3)

#根据标签的名字来获取对象
button4=browser.find_element(By.TAG_NAME,'input')
print(button4)

#适用bs的语法来获取对象
button5=browser.find_element(By.CSS_SELECTOR,'#su')
print(button5)

#
button6=browser.find_element(By.LINK_TEXT,'新闻')
print(button6)

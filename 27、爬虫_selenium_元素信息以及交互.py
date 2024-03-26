from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service(path= 'chromedriver.exe')
options = webdriver.ChromeOptions()

broswer=webdriver.Chrome(service=service, options=options)
url='http://www.baidu.com/'
broswer.get(url)

input=broswer.find_element(By.ID,"su")
#1、获取标签的属性
print(input.get_attribute('class'))#得到id是su的，属性是class对应的值 ——bg s_btn

#2、获取标签的名字
print(input.tag_name) #获取标签名  ——input

#3、获取元素文本
#获取> <中间的部分
a=broswer.find_element(By.LINK_TEXT,"新闻")
print(a.text) #获取元素文本 ——新闻

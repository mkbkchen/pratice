from selenium import webdriver
from selenium.webdriver.common.by import By
path= 'phantomjs.exe'
broswer=webdriver.PhantomJS(path)

url='https://www.baidu.com/'
broswer.get(url)
#看一下照片
broswer.save_screenshot('baidu.png')
import time
time.sleep(2)

input=broswer.find_element(By.ID,"kw")
input.send_keys("周杰伦")

time.sleep(2)

broswer.save_screenshot('周杰伦.png')



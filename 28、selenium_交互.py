from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service=Service(path= 'chromedriver.exe')
options = webdriver.ChromeOptions()

broswer=webdriver.Chrome(service=service, options=options)
#创建浏览器对象
# path= '/usr/local/bin/chromedriver'
# broswer=webdriver.Chrome(path)

#获取浏览器
url='https://www.baidu.com/'
broswer.get(url)

import time
time.sleep(2)

#1、获取文本框的对象
input=broswer.find_element(By.ID,"kw")

#在文本框中输入周杰伦
input.send_keys('周杰伦')

time.sleep(2)

#2、获取百度一下的按钮
button=broswer.find_element(By.ID,"su")
#点击按钮
button.click()

time.sleep(2)

#3、滑倒底部
js_bottom='document.documentElement.scrollTop=1000000'
broswer.execute_script(js_bottom)

time.sleep(2)

#4、获取下一页的按钮
next=broswer.find_element(By.XPATH,'//div/a[@class="n"]')

#点击下一页的按钮
next.click()

time.sleep(2)

#5、回到上一页
broswer.back()
time.sleep(2)

#6、回去
broswer.forward()
time.sleep(2)

#7、退出
broswer.quit()

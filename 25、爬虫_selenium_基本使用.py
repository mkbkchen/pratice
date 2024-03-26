#(1)导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(path='chromedriver.exe')
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=service, options=options)
# ...


#（2）创建浏览器操作对象

#（3）访问网址
url='https://www.jd.com/'

browser.get(url)
content=browser.page_source  #page_source获取网页源码
print(content)
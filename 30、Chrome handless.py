from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#封装的方法
def share_broswer():
    chrome_options = Options()
    chrome_options.add_argument('-headless')
    chrome_options.add_argument('--disable-gpu')

    # path是chrome浏览器的文件路径
    # path=r'/Applications/Google Chrome.app'
    # chrome_options.binary_location=path

    broswer = webdriver.Chrome(options=chrome_options)
    return broswer

broswer=share_broswer()
url='https://www.baidu.com/'
broswer.get(url)
broswer.save_screenshot('baidu1.png')



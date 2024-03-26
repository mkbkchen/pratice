#(1)获取网页的源码

#（2）解析——解析服务器响应的文件 etree.HTML

#(3)打印

import urllib.request
from lxml import etree

url='https://www.baidu.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
request=urllib.request.Request(url=url,headers=headers)
resopnse=urllib.request.urlopen(request)
content=resopnse.read().decode('utf-8')
#print(content)

#解析服务器响应的文件，获取想要的数据   xpath返回值是一个列表类型数据,写个[0]得到第一个
tree=etree.parse(content)
# 用ctrl+shift+x可以调出黑框
list=tree.xpath('//input[@id="su"]/@value')[0]
print(list)
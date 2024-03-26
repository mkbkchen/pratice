import urllib.request

url='http://www.baidu.com/'

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(url)

#一个类型和六个方法

#1、response 是—— HTTPResponse的类型
print(type(response))

# 2按照一个字节一个字节去读 —— read
content=response.read()
# print(content)

#返回多少个字节
content=response.read(5)
# print(content)

#按照一行一行去读，只能读取一行 —— readline
content=response.readline()
# print(content)

#一行一行读，读取所有行 —— readlines
content=response.readlines()
# print(content)

#返回状态码  如果是200就证明我们的逻辑没有错 —— getcode
print(response.getcode())

#返回的是url地址 —— geturl
print(response.geturl())

#获取的是一个状态信息
print(response.getheaders())

#一个类型 HTTPResponse
#6个方法 read readline readlines getcode geturl getheaders
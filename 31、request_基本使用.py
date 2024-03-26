import requests
url='http://www.baidu.com'
response=requests.get(url=url)
#一、一个类型
print(type(response))#<class 'requests.models.Response'>
#二、六个属性
#设置响应的编码格式
response.encoding='utf-8'

#以字符串的形式返回网页源码
print(response.text)

#返回一个url地址
print(response.url)

#返回二进制的数据
print(response.content)

#返回响应的状态码
print(response.status_code)

#返回是是响应头
print(response.headers)



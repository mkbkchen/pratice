
#需求 获取  https://www.baidu.com/s?wd=周杰伦 的网页源码
import urllib.request
import urllib.parse

url='https://www.baidu.com/s?wd='
#1、请求对象的定制，为了解决反爬的第一种手段 UA
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64010 ; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'}

#将周杰伦三个字变成unicode编码
name=urllib.parse.quote('周杰伦')
url=url+name
print(url)

request=urllib.request.Request(url=url,headers=headers)

#模拟浏览器向服务器发送请求
response=urllib.request.urlopen(request)

content=response.read().decode('utf-8')

print(content)
